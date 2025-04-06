import hashlib
from random import randrange
from sympy import isprime

def generate_keys_rsa(bits=512):
    def get_prime():
        while True:
            p = randrange(2**(bits-1), 2**bits)
            if isprime(p):
                return p
    p = get_prime()
    q = get_prime()
    n = p * q
    phi = (p-1)*(q-1)

    e = 65537
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def rsa_sign(message, priv_key):
    d, n = priv_key
    hashed = int.from_bytes(hashlib.sha512(message.encode()).digest(), 'big')
    return pow(hashed, d, n)

def rsa_verify(message, signature, pub_key):
    e, n = pub_key
    hashed = int.from_bytes(hashlib.sha512(message.encode()).digest(), 'big')
    return hashed == pow(signature, e, n)

# Usage
pub, priv = generate_keys_rsa()
msg = "hello world"
sig = rsa_sign(msg, priv)
print("RSA Verified:", rsa_verify(msg, sig, pub))
