alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(para_text, para_shift):
    for char_t in list(text):
        for char_a in alphabet:
            if char_t == char_a:
                new_text = alphabet.index(char_t) + shift
                encrypt_text = str(alphabet[new_text])
                print(encrypt_text)
                break

encrypt(text, shift)
