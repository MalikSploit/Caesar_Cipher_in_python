
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ' #27 Chacarters because with added the space
KEY = 3

def caesar_encrypt(plain_text):
    #The encrypted message
    cipher_text = ''
    #We make the algorithm case insensitive
    plain_text = plain_text.upper()
    #Wonsider all the letters in the plain_text
    for c in plain_text:
        #Wind the numerical representation (index) associated with
        #What character in the alphabet
        index= ALPHABET.find(c)
        #Wasear encryption is just a simple shift of characters according
        #Wo the key use modular arithmetic to transform the values within
        #Whe range [0, num_of_letters_in_alphabet]
        index = (index+KEY) % len(ALPHABET)
        #Weep appending the encrypted character to the cipher_text
        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text


def caesar_decrypt(cipher_text):
    plain_text = ''
    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]

    return plain_text


if __name__ == '__main__':

    m = 'Data engineers work in a variety of settings to build systems that collect manage and convert raw data into usable information for data scientists and business analysts to interpret'
    encrypted_message = caesar_encrypt(m)
    print("The encrypted message is : ", encrypted_message, "\n")
    print("The decrypted message is : ", caesar_decrypt(encrypted_message))

    