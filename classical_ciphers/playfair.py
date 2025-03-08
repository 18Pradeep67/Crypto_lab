def generate_key_table(key):
    key = key.upper().replace("J", "I").replace(" ", "")
    key += "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    used = set()
    key_matrix = []

    for c in key:
        if c not in used:
            used.add(c)
            key_matrix.append(c)

    return [key_matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(key_table, char):
    for i in range(5):
        for j in range(5):
            if key_table[i][j] == char:
                return i, j
    return -1, -1

def playfair_cipher(text, key, encrypt=True):
    key_table = generate_key_table(key)
    text = text.upper().replace("J", "I").replace(" ", "")

    text_pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text) and text[i] != text[i + 1]:
            b = text[i + 1]
            i += 2
        else:
            b = 'X'
            i += 1
        text_pairs.append((a, b))
    print(text_pairs)

    result = ""
    for a, b in text_pairs:
        r1, c1 = find_position(key_table, a)
        r2, c2 = find_position(key_table, b)

        if r1 == r2:  
            shift = 1 if encrypt else -1
            result += key_table[r1][(c1 + shift) % 5] + key_table[r2][(c2 + shift) % 5]
        elif c1 == c2:  
            shift = 1 if encrypt else -1
            result += key_table[(r1 + shift) % 5][c1] + key_table[(r2 + shift) % 5][c2]
        else:  
            result += key_table[r1][c2] + key_table[r2][c1]

    if not encrypt:
        cleaned_text = ""
        for i in range(len(result)):
            if result[i] == 'X' and (i == len(result) - 1 or result[i-1] == result[i+1]):
                continue
            cleaned_text += result[i]
        return cleaned_text

    return result

text = input("Enter text: ")
key = input("Enter key: ")
encrypted = playfair_cipher(text, key, encrypt=True)
print("Encrypted:", encrypted)
decrypted = playfair_cipher(encrypted, key, encrypt=False)
print("Decrypted:", decrypted)
