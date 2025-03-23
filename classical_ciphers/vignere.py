def vignere_encrypt(text, key):
    return ''.join(chr((ord(t) - ord('a') + ord(k) - ord('a')) % 26 + ord('a')) for t, k in zip(text, key))

def vignere_decrypt(text, key):
    return ''.join(chr((ord(t) - ord('a') - (ord(k) - ord('a'))) % 26 + ord('a')) for t, k in zip(text, key))

if __name__ == "__main__":
    text = "cryptolabmat"
    key = "allthebest"
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    print("Key:", key)

    encrypted_text = vignere_encrypt(text, key)
    print("Encrypted:", encrypted_text)

    decrypted_text = vignere_decrypt(encrypted_text, key)
    print("Decrypted:", decrypted_text)
