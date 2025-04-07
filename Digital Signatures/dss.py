import hashlib
import random

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def modinv(a, m):
    # Extended Euclidean Algorithm for modular inverse
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def sha1_hash(message):
    return int(hashlib.sha1(message.encode()).hexdigest(), 16)

# Parameters (p, q, g) setup
q = 59399  # 160-bit prime in real use
p = 2 * q + 1
while not is_prime(p):
    q += 2
    p = 2 * q + 1

h = 2
g = pow(h, (p - 1) // q, p)
while g <= 1:
    h += 1
    g = pow(h, (p - 1) // q, p)

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# Key generation
x = random.randint(1, q - 1)  # Private key
y = pow(g, x, p)              # Public key

# Signing
def sign(message):
    m = sha1_hash(message) % q
    k = random.randint(1, q - 1)
    r = pow(g, k, p) % q
    k_inv = modinv(k, q)
    s = (k_inv * (m + x * r)) % q
    return r, s

# Verification
def verify(message, r, s):
    if not (0 < r < q and 0 < s < q):
        return False
    m = sha1_hash(message) % q
    w = modinv(s, q)
    u1 = (m * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p)) % p % q
    return v == r

# Demo
msg = "forged message"
r, s = sign(msg)
print("Signature (r, s):", r, s)
print("Verification result:", verify(msg, r, s))
