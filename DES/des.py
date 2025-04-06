from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def des_decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(encrypted_text), DES.block_size)
    return decrypted_text.decode()

key = b'8bytekey'  # DES key must be exactly 8 bytes
message = "HELLO DES"

enc = des_encrypt(message, key)
dec = des_decrypt(enc, key)

print("Encrypted:", enc.hex())
print("Decrypted:", dec)
