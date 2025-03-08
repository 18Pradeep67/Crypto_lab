import socket
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

def generate_rsa_keys():
    p, q = 53, 29
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 31
    d = modinv(e, phi)
    return (e, n), (d, n)

def rsa_decrypt(cipher, pr_key):
    d, n = pr_key
    return ''.join(chr(pow(i, d, n)) for i in cipher)

def server():
    pu, pr = generate_rsa_keys()
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 5050))
        s.listen()
        print("\n[SERVER] Listening on port 5050...")

        conn, addr = s.accept()
        with conn:
            print("\n[SERVER] Connected by", addr)
            
            conn.sendall(str(pu).encode())  

            cipher = ast.literal_eval(conn.recv(1024).decode()) 
            print("\n[SERVER] Received Encrypted RSA:", cipher)

            dec_rsa = rsa_decrypt(cipher, pr)
            print("\n[SERVER] Decrypted RSA message:", dec_rsa)

if __name__ == "__main__":
    server()
