import socket
import random
import math
import ast

def encrypt(message, pub_key): 
    p, g, y = pub_key 
    k = 5 
    
    c1 = pow(g, k, p) 
    c2 = [] 
    
    for char in message: 
        m = ord(char) 
        c = (m * pow(y, k, p)) % p 
        c2.append(c) 
    
    return c1, c2

def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 5202))

        pub_key = ast.literal_eval(s.recv(1024).decode())

        msg = "Gyeong-su, YOU!!, OUT!! LESSSSSSSGOOOO"
        pt = [ord(i) for i in msg]  # Original ASCII values
        print(f"[CLIENT] Plaintext ASCII values: {pt}")

        enc_msg = encrypt(msg, pub_key)
        print(f"[CLIENT] Encrypted message: {enc_msg}")

        s.sendall(str(enc_msg).encode())
if __name__ == "__main__":
    client()