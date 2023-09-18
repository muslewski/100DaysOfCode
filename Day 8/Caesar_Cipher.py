import art

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def encrypt(text, shift):
    shifted_text = ""
    for letter in text:
        if letter.isupper():
            number = alphabet.index(letter.lower())
            shift_number = number + shift
            shifted_text += alphabet[shift_number % len(alphabet)].upper()
        elif letter not in alphabet:
            shifted_text += letter
        else:
            number = alphabet.index(letter)
            shift_number = number + shift
            shifted_text += alphabet[shift_number % len(alphabet)]

    with open('encrypto.txt', 'a') as f:
        f.write(f'Normal text:\n{text}\n\n')
        f.write(f'Encrypted text:\n{shifted_text}\n\n')

    print("\n\033[32m" + shifted_text)


def decrypt(text, shift):
    shifted_text = ""
    for letter in text:
        if letter.isupper():
            number = alphabet.index(letter.lower())
            shift_number = number - shift
            shifted_text += alphabet[shift_number % len(alphabet)].upper()
        elif letter not in alphabet:
            shifted_text += letter
        else:
            number = alphabet.index(letter)
            shift_number = number - shift
            shifted_text += alphabet[shift_number % len(alphabet)]

    with open('decrypto.txt', 'a') as f:
        f.write(f'Normal text:\n{text}\n\n')
        f.write(f'Decrypted text:\n{shifted_text}\n\n')

    print("\n\033[32m" + shifted_text)


print(art.logo)

should_continue = True
while should_continue:
    direction = input("\nChoose 'encrypt' or 'decrypt': ")
    text = input("\nType your message:\n")
    shift = int(input("\nType the shift number: "))

    if direction == "encrypt":
        encrypt(text, shift)
    elif direction == "decrypt":
        decrypt(text, shift)

    result = input("\n\033[0mContinue? 'yes' or 'no': ")
    if result == 'no':
        should_continue = False
        print("\nGoodbye")
