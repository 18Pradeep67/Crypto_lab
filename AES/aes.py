from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)  # Using CBC mode
    iv = cipher.iv  # Initialization Vector
    encrypted_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return iv + encrypted_text  # Prepend IV for decryption

def aes_decrypt(encrypted_text, key):
    iv = encrypted_text[:AES.block_size]  # Extract IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text[AES.block_size:]), AES.block_size)
    return decrypted_text.decode()

key = os.urandom(16)  # AES key must be 16, 24, or 32 bytes (128, 192, or 256-bit)
message = "HELLO AES"

enc = aes_encrypt(message, key)
dec = aes_decrypt(enc, key)

print("Encrypted:", enc.hex())
print("Decrypted:", dec)
