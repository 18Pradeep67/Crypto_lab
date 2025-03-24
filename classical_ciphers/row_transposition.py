import math
def row_trans_encrypt(text,key):
    key_order = sorted(range(len(key)), key = lambda k:key[k])
    cols = len(key)
    rows = math.ceil(len(text)/cols)
    grid = [text[i * cols:(i + 1) * cols].ljust(cols, 'X') for i in range(rows)]
    return ''.join(grid[row][col] for col in key_order for row in range(rows))
def decrypted_text(cipher,key):
    key_order = sorted(range(len(key)), key = lambda k:key[k])
    cols, rows = len(key), math.ceil(len(cipher)/len(key))
    grid = [['']*cols for _ in range(rows)]
    idx=0
    for i in key_order:
        for j in range(rows):
            if idx<len(cipher):
                grid[j][i]=cipher[idx]
                idx+=1
    return ''.join(''.join(row) for row in grid).rstrip('X')

if __name__ == "__main__":
    encrypted_text = row_trans_encrypt("Cryptomatlabexam","3142")
    print(encrypted_text)
    print(decrypted_text(encrypted_text,"3142"))