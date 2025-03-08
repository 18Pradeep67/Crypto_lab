import socket
import random 
import ast

q = 353
alpha = 3
priv_key = random.randint(1,q-1)

def generate_key(pub_key):
    return pow(pub_key,priv_key,q)

def alice():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost",3000))
        pub_key = generate_key(alpha)
        print("[Alice] Sending public key ",pub_key)
        s.sendall(str(pub_key).encode())

        fake_bob_public_key = ast.literal_eval(s.recv(1024).decode())
        print("[Alice] Received bob's public key: ",fake_bob_public_key)
        fake_shared_key = generate_key(fake_bob_public_key)

        print(f"[Alice] Shared key established: {fake_shared_key}")
if __name__ == "__main__":
    alice()
        
