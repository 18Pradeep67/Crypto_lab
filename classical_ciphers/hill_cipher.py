import numpy as np

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text]

def numbers_to_text(num):
    return ''.join(chr(n + ord('A')) for n in num)

def mod_matrix_inverse(matrix, mod):
    det = int(round(np.linalg.det(matrix)))  # Determinant of the matrix
    det_inv = pow(det, -1, mod)  # Modular inverse of determinant
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod  # Adjugate matrix
    return (det_inv * adjugate) % mod  # Modular inverse matrix

def hill_encrypt(plain_text, key_matrix):
    plain_text = plain_text.upper().replace(" ", "")
    if len(plain_text) % 2 == 1:
        plain_text += 'X'  # Padding for even length

    text_nums = text_to_numbers(plain_text)
    cipher_nums = []

    for i in range(0, len(text_nums), 2):
        pair = np.dot(key_matrix, text_nums[i:i+2]) % 26
        cipher_nums.extend(pair)

    return numbers_to_text(cipher_nums)

def hill_decrypt(cipher_text, key_matrix):
    cipher_nums = text_to_numbers(cipher_text)
    key_inv = mod_matrix_inverse(key_matrix, 26)  # Compute modular inverse matrix
    plain_nums = []

    for i in range(0, len(cipher_nums), 2):
        pair = np.dot(key_inv, cipher_nums[i:i+2]) % 26
        plain_nums.extend(pair)

    return numbers_to_text(plain_nums)

if __name__ == "__main__":
    key_matrix = np.array([[3, 5], [2, 3]])
    text = "CRYPTOMATLABEXAM"
    cipher = hill_encrypt(text, key_matrix)
    print("Encrypted:", cipher)
    print("Decrypted:", hill_decrypt(cipher, key_matrix))
