import hashlib

def sha512_hash(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    hash_obj = hashlib.sha512()
    hash_obj.update(data)
    return hash_obj.hexdigest()

# Example
text = "hello world"
hashed = sha512_hash(text)
print("SHA-512 Hash:", hashed)
