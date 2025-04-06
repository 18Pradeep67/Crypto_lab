def caesar_cipher(text,shift,encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result+=chr((ord(char)-base+shift)%26 + base)
        else:
            result+=char
    return result

if __name__ == "__main__":
    print(caesar_cipher("Qsroic H Pyjjc",4,False)) 
    