from Crypto.Hash import MD5
def md5_hash(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    h = MD5.new()
    h.update(data)
    return h.hexdigest()
print(md5_hash("Ore wa monkeydluffy"))