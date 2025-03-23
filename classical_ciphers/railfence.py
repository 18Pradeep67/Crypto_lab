def rail_fence_encrypt(text, rails):
    fence = [''] * rails
    i, step = 0, 1
    for char in text:
        fence[i] += char
        if i == 0: step = 1
        elif i == rails - 1: step = -1
        i += step
        print(fence)
    return ''.join(fence)
def rail_fence_decrypt(cipher, rails):
    fence = [[''] * len(cipher) for _ in range(rails)]
    i, step, idx = 0, 1, 0
    for _ in cipher:
        fence[i][idx] = '*'
        if i == 0: step = 1
        elif i == rails - 1: step = -1
        i += step
        idx += 1
    for i in range(rails):
        print(fence[i])
    print("\n")
    idx = 0
    for r in range(len(fence)):
        for c in range(len(cipher)):
            if fence[r][c]=='*' and idx<len(cipher):
                fence[r][c] = cipher[idx]
                idx += 1
    for i in range(rails):
        print(fence[i])
    res = ''
    i, step, idx = 0,1,0
    for _ in cipher:
        res+=fence[i][idx]
        if i==0:step=1
        elif i==rails-1:step=-1
        i+=step
        idx+=1
    return res

if __name__ == "__main__":
    encrypted_text = rail_fence_encrypt("Pradeep",3)
    print(encrypted_text)
    print("\n")
    print(rail_fence_decrypt(encrypted_text,3))