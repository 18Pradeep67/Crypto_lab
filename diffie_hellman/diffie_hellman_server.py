import socket
import math
import random
import ast

q = 353
alpha = 3
priv_key = random.randint(1,q-1)

def generate_key(pub_key):
    key = pow(pub_key,priv_key,q)
    return key

def server():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind(("localhost",5555))
        s.listen()
        print(f"Server listening on port 5555...")

        conn, addr = s.accept()
        with conn:
            serv_pub_key = pow(alpha,priv_key,q)
            print(f"Sending server's public key... {serv_pub_key}")
            conn.sendall(str(serv_pub_key).encode())

            pu_key = ast.literal_eval(conn.recv(1024).decode())
            print(f"Received public key from server is: {pu_key}")

            print(f"Exchanged key is: {generate_key(pu_key)}")
if __name__ == "__main__":
    server()
