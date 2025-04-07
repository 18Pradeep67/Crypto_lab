from random import randint
from math import gcd
import hashlib

def modinv(a, m):
    return pow(a, -1, m)
def generate_keys_dsa():
    q = 59399
    p = 2 * q + 1
    h = 2
    g = pow(h, (p-1)//q, p)
    x = randint(1, q - 1)
    y = pow(g, x, p)
    return (p, q, g, y), x

def dsa_sign(message, priv_key, params):
    p, q, g, _ = params
    x = priv_key
    H = int.from_bytes(hashlib.sha512(message.encode()).digest(), 'big') % q
    while True:
        k = randint(2, q - 1)
        if gcd(k, q) == 1:
            break
    r = pow(g, k, p) % q
    k_inv = modinv(k, q)
    s = (k_inv * (H + x * r)) % q
    return r, s

def dsa_verify(message, signature, params):
    p, q, g, y = params
    r, s = signature
    H = int.from_bytes(hashlib.sha512(message.encode()).digest(), 'big') % q
    w = modinv(s, q)
    u1 = (H * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r

# Usage
params, x = generate_keys_dsa()
msg = "hello world"
sig = dsa_sign(msg, x, params)
print("DSA Verified:", dsa_verify(msg, sig, params))
