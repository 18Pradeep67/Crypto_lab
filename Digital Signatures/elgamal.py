from random import randint
from math import gcd
import hashlib

def modinv(a, m):
    return pow(a, -1, m)

def generate_keys_elgamal():
    p = 30803
    g = 2
    x = randint(2, p - 2)
    y = pow(g, x, p)
    return (p, g, y), x

def elgamal_sign(message, priv_key, params):
    p, g, _ = params
    x = priv_key
    H = int.from_bytes(hashlib.sha512(message.encode()).digest(), 'big') % (p - 1)
    while True:
        k = randint(2, p - 2)
        if gcd(k, p - 1) == 1:
            break
    r = pow(g, k, p)
    s = (modinv(k, p - 1) * (H - x * r)) % (p - 1)
    return r, s

def elgamal_verify(message, signature, pub_key, params):
    p, g, y = params
    r, s = signature
    H = int.from_bytes(hashlib.sha512(message.encode()).digest(), 'big') % (p - 1)
    lhs = (pow(y, r, p) * pow(r, s, p)) % p
    rhs = pow(g, H, p)
    return lhs == rhs

# Usage
params, x = generate_keys_elgamal()
msg = "hello world"
sig = elgamal_sign(msg, x, params)
print("ElGamal Verified:", elgamal_verify(msg, sig, params[2], params))
