import socket
import random
import ast

q = 353
alpha = 3
priv_key = random.randint(1,q-1)

def generate_key(pub_key):
    return pow(pub_key,priv_key,q)

def bob():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost",6060))
        s.listen()
        print("[Bob] Waiting for a connection....")
        conn, addr = s.accept()
        with conn:
            fake_alice_pub_key = ast.literal_eval(conn.recv(1024).decode())
            print("[Bob] Received public key: ",fake_alice_pub_key)

            pub_key = generate_key(alpha)
            print("[Bob] Sending public key ",pub_key)
            conn.sendall(str(pub_key).encode())

            shared_key = generate_key(fake_alice_pub_key)
            print("[Bob] Shared key established: ",shared_key)
if __name__ == "__main__":
    bob()
