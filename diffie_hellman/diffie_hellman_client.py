import socket
import random
import math
import ast

q = 353
alpha = 3
priv_key = random.randint(1,q-1)

def generate_key(pub_key):
    key = pow(pub_key,priv_key,q)
    return key

def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost",5555))

        pu_key = ast.literal_eval(s.recv(1024).decode())
        print(f"Received public key from server is: {pu_key}")

        client_pub_key = pow(alpha,priv_key,q)
        print(f"Sending server's public key... {client_pub_key}")
        s.sendall(str(client_pub_key).encode())

        print(f"Exchanged key is: {generate_key(pu_key)}")
if __name__ == "__main__":
    client()

