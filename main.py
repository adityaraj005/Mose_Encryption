MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'
                   }


def encrypt(text):
    encrypted_text = ""
    for alphabet in text:
        if alphabet != " ":
            encrypted_text += MORSE_CODE_DICT[alphabet] + " "
        else:
            encrypted_text += " "
    return encrypted_text


def decrypt(text):
    text += " "
    my_text = ""
    decrypted_text = ""
    space_count = 0

    for letter in text:
        if letter != " ":
            space_count = 1
            my_text += letter

        else:
            space_count += 1
            if space_count == 1:         # This if statement is created to add space at front because if person added
                decrypted_text += " "    # spaces before typing the actual text so the code will add space and do not
                space_count = 0          # generate any error

            elif space_count == 3:
                decrypted_text += " "

            else:
                decrypted_text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(my_text)]
                my_text = ""

    return decrypted_text


choice = input("Do you Encrypt your message or Decrypt your message? (Encrypt: 0 / Decrypt: 1): ")

if choice == '0':
    input_text = input("Enter the String/Text for Encryption: ")
    encrypted = encrypt(input_text.upper())
    print(f"Your Output: {encrypted}")

elif choice == '1':
    input_text = input("Enter the Text for Decryption: ")
    decrypted = decrypt(input_text)
    print(f"Your Output: {decrypted}")

else:
    print("Please make right choice (for Encryption: 0, for Decryption: 1)")

