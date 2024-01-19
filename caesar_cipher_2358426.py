import os.path

def welcome():
    print("Welcome to the Caesar Cipher. This program encrypts and decrypts text with the Caesar Cipher.")

def entry_message():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid mode\n")
        
    message = input(f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: ").upper()
    
    while True:
        try:
            key = int(input("What is the key number (0-25): "))
            if 0 <= key <= 25:
                break
            else:
                print("Invalid key\n")
        except ValueError:
            print("Invalid key\n")

    return mode, message, key


def encrypt(message, key):
    cipher = ""
    for char in message:
        if char.isalpha():           
            cipher += chr((ord(char.upper()) + key - 65) % 26 + 65)
        else:
            cipher += char
    return cipher


def decrypt(cipher, key):
    message = ""
    for char in cipher:
        if char.isalpha():          
            message += chr((ord(char.upper()) - key - 65) % 26 + 65)
        else:
            message += char
    return message

def message_or_file():
    while True:
        choice = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if choice in ['c', 'f']:
            break
        else:
            print("Invalid choice\n")
    return choice

def write_messages(messages, filename):
    with open(filename, 'w') as file:
        for message in messages:
            file.write(message + "\n")
    print("Messages written to file:", filename)

def read_messages(filename):
    with open(filename, 'r') as file:
        messages = [line.strip().upper() for line in file]
    return messages

def main():
    welcome()

    while True:            
        choice = message_or_file()

        if choice == 'c':
            mode, message, key = entry_message()
            if mode == 'e':
                print(encrypt(message, key))
            elif mode == 'd':
                print(decrypt(message, key))
            else:
                print("Invalid mode")
        elif choice == 'f':
            filename = input("Please enter the name of the input file: ")
            if not os.path.isfile(filename):
                print("File not found")
                continue

            mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
            if mode not in ['e', 'd']:
                print("Invalid mode")
                continue

            while True:
                try:
                    key = int(input("What is the key number (0-25): "))
                    if 0 <= key <= 25:
                        break
                    else:
                        print("Invalid key\n")
                except ValueError:
                    print("Invalid key\n")

            output_filename = input("Please enter the name of the output file: ")

            messages = read_messages(filename)
            if mode == 'e':
                encrypted_messages = [encrypt(message, key) for message in messages]
                write_messages(encrypted_messages, output_filename)
            else:
                decrypted_messages = [decrypt(message, key) for message in messages]
                write_messages(decrypted_messages, output_filename)

        while True:
            repeat = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
            if repeat == 'y':
                break
            elif repeat == 'n':
                print("thanks for using This program encrypts and decrypts text with the Caesar Cipher.]")
                return
            else:
                print("Invalid choice\n")

if __name__ == '__main__':
    main()
