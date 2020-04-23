# Caesar cipher encryption and decryption function
def caesar_cipher_decrypt(crypt, shift):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    crypt = list(crypt.lower())
    shift = int(shift)
    result = ""
    k = 0
    while(k < len(crypt)):       
        letter = crypt[k]
        for l in range(len(alphabet)):
            match = alphabet[l]
            if letter == match:
                pos = l + shift
                if pos >= 26:
                    pos = pos - 26
                replacement = alphabet[pos]
                result = result + replacement
                break
        else:
            result = result + letter
        k = k + 1
    return result

def caesar_cipher_encrypt(plain, shift):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    plain = list(plain.lower())
    shift = int(shift)
    result = ""
    k = 0
    while(k < len(plain)):
        letter = plain[k]
        for l in range(len(alphabet)):
            match = alphabet[l]
            if letter == match:
                pos = l - shift
                if pos < 0:
                    pos = 26 + pos
                replacement = alphabet[pos]
                result = result + replacement
                break
        else:
            result = result + letter
        k = k + 1
    return result

if __name__ == "__main__":
    print("A Caesar encryption program.")
    choice = input("Do you want to [d]ecrypt or [e]ncrypt? ")
    if choice == 'd':
        print("Decryption chosen. Enter message to decrypt and the key.")
        text = input("Message (string): ")
        shift = input("Shift (integer): ")
        print("The encrypted text:\n", str(caesar_cipher_decrypt(text, shift)))
    elif choice == 'e':
        print("Encryption chosen. Enter message to encrypt and the key.")
        text = input("Message (string): ")
        shift = input("Shift (integer): ")
        print("The encrypted text:\n", str(caesar_cipher_encrypt(text, shift)))
    else:
        print("Invalid option. Exiting.")
    exit()