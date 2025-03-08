import socket
import random

q = 353
alpha = 3
priv_key = random.randint(1, q-1)  

def generate_key(pub_key):
    return pow(pub_key, priv_key, q)

def bob():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 6666))  
        s.listen()
        print("[Bob] Waiting for connection...")
        conn, addr = s.accept()

        with conn:
            print("[Bob] Connected to Darth (thinking it's Alice)")

            fake_alice_pub_key = int(conn.recv(1024).decode())  
            print(f"[Bob] Received public key: {fake_alice_pub_key}")

            bob_pub_key = pow(alpha, priv_key, q) 
            print(f"[Bob] Sending public key: {bob_pub_key}")
            conn.sendall(str(bob_pub_key).encode())  

            shared_key = generate_key(fake_alice_pub_key) 
            print(f"[Bob] Shared key established: {shared_key}")

if __name__ == "__main__":
    bob()
