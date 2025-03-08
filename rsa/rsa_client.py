import socket
import ast  # For safe eval replacement

def rsa_encrypt(message, pub_key):
    e, n = pub_key
    return [pow(ord(i), e, n) for i in message]

def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
        c.connect(("127.0.0.1", 5050))

        pu = ast.literal_eval(c.recv(1024).decode())  
        
        msg = "Dunggeulge dunggeulge Binggeulbinggeul doragamyeo chumeul chupsida"
        cipher = rsa_encrypt(msg, pu)
        
        print("\n[CLIENT] Original Message:", msg)
        print("[CLIENT] Encrypted RSA:", cipher)

        c.sendall(str(cipher).encode()) 

if __name__ == "__main__":
    client()
