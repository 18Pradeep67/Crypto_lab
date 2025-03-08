import socket

q = 353
alpha = 3
darth_priv_key = 99 

def generate_key(pub_key):
    return pow(pub_key, darth_priv_key, q)

def darth():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as alice_sock:
        alice_sock.bind(("localhost", 5555))
        alice_sock.listen()
        print("[Darth] Waiting for Alice...")
        alice_conn, _ = alice_sock.accept()

        with alice_conn:
            alice_pub_key = int(alice_conn.recv(1024).decode()) 
            print(f"[Darth] Intercepted Alice's public key: {alice_pub_key}")

            fake_darth_pub_for_alice = pow(alpha, darth_priv_key, q)
            alice_conn.sendall(str(fake_darth_pub_for_alice).encode()) 

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as bob_sock:
                bob_sock.connect(("localhost", 6666)) 

                bob_sock.sendall(str(fake_darth_pub_for_alice).encode()) 
                bob_pub_key = int(bob_sock.recv(1024).decode()) 
                print(f"[Darth] Intercepted Bob's public key: {bob_pub_key}")

                fake_darth_pub_for_bob = pow(alpha, darth_priv_key, q)
                alice_conn.sendall(str(fake_darth_pub_for_bob).encode())  

                alice_shared_key = generate_key(alice_pub_key)
                bob_shared_key = generate_key(bob_pub_key)

                print(f"[Darth] Shared key with Alice: {alice_shared_key}")
                print(f"[Darth] Shared key with Bob: {bob_shared_key}")

if __name__ == "__main__":
    darth()
