import socket
import random
import math
import ast

def modinv(a, m):
    if math.gcd(a, m) != 1:
        raise ValueError("Inverse doesn't exist")
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = m // a
        m, a = a, m % a
        x0, x1 = x1, x0 - q * x1
    return x1 + m0 if x1 < 0 else x1

def generate_elgamal_keys():
    q = 257
    alpha = 3
    xa = random.randint(2,q-2)
    ya = pow(alpha,xa,q)
    return (q,alpha,ya), (xa,q)

def decrypt(cipher, priv_key):
    xa,q = priv_key
    c1, c2 = cipher
    K = pow(c1,xa,q)
    s_inv = modinv(K,q)
    decrypted_text = []
    for i in c2:
        m = i*s_inv % q
        decrypted_text.append(m)
    decrypted_message = "".join(chr(i) for i in decrypted_text)
    return decrypted_message

def server():
    pub_key, priv_key = generate_elgamal_keys()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1",5202))
        s.listen()
        print("\n[SERVER] Listening on port 5202...") 
        conn, addr = s.accept()
        with conn:
            print("\n[SERVER] connected by", addr)
            conn.sendall(str(pub_key).encode())

            cipher = ast.literal_eval(conn.recv(1024).decode())
            print("[SERVER] Received Encrypted ElGamal:", cipher)

            dec_elg = decrypt(cipher,priv_key)
            print("[SERVER] Decrypted ElGamal message:", dec_elg)
if __name__ =="__main__":
    server() 

