import socket
import ast

q = 353
alpha = 3
priv_key = 107

def generate_key(key):
    return pow(key,priv_key,q)

def darth():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind(("localhost",3000))
        s.listen()
        print("[Darth] Waiting for Alice...")

        alice_conn, addr = s.accept()
        with alice_conn:
            alice_pub_key = ast.literal_eval(alice_conn.recv(1024).decode())
            print("[Darth] Intercepted Alice's public key: ",alice_pub_key)
            
            darth_public_key = generate_key(alpha)
            alice_conn.sendall(str(darth_public_key).encode())
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as bs:
                bs.connect(("localhost",6060))
                bs.sendall(str(darth_public_key).encode())
                bob_pub_key = ast.literal_eval(bs.recv(1024).decode())
                print("[Darth] Intercepted Bob's public key: ",bob_pub_key)

                alice_shared_key = generate_key(alice_pub_key)
                bob_shared_key = generate_key(bob_pub_key)

                print("[Darth] Shared key with Alice: ",alice_shared_key)
                print("[Darth] Shared key with Bob: ",bob_shared_key)
if __name__ == "__main__":
    darth()