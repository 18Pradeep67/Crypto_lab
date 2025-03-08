import socket
import random

q = 353  
alpha = 3  
priv_key = random.randint(1, q-1) 

def generate_key(pub_key):
    return pow(pub_key, priv_key, q)

def alice():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 5555))  

        alice_pub_key = pow(alpha, priv_key, q)
        print(f"[Alice] Sending public key: {alice_pub_key}")
        s.sendall(str(alice_pub_key).encode()) 

        fake_bob_pub_key = int(s.recv(1024).decode())  
        print(f"[Alice] Received public key: {fake_bob_pub_key}")

        shared_key = generate_key(fake_bob_pub_key) 
        print(f"[Alice] Shared key established: {shared_key}")

if __name__ == "__main__":
    alice()
