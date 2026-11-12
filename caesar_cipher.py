# =========================================
# PROJECT: CAESAR CIPHER ENCRYPTION SYSTEM
# STUDENT NAME: Christabel Owusu
# INDEX NUMBER: 10353422
# PROGRAMMING LANGUAGE: Python
# ALGORITHM USED: Caesar Cipher
# =========================================
print("Welcome to the Caeser Cipher Program!")
print("=== Caesar Cipher Program ===")

message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))

print("Your message is:", message)
print("The shift value is:", shift)

print("=== Caesar Cipher Program ===")

def encrypt(message, shift):
    encrypted_text = ""

    for letter in message:
        if letter.isalpha():
            start = ord('A') if letter.isupper() else ord('a')

            new_letter = chr((ord(letter) - start + shift) % 26 + start)

            encrypted_text += new_letter
        else:
            encrypted_text += letter

    return encrypted_text


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)

print("Encrypted message:", encrypted)
def decrypt(message, shift):
    return encrypt(message, -shift)
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted message:", decrypted)


print("================================")
print("       CAESAR CIPHER SYSTEM")
print("================================")


def encrypt(message, shift):
    encrypted_text = ""

    for letter in message:
        if letter.isalpha():
            start = ord('A') if letter.isupper() else ord('a')

            new_letter = chr(
                (ord(letter) - start + shift) % 26 + start
            )

            encrypted_text += new_letter
        else:
            encrypted_text += letter

    return encrypted_text


def decrypt(message, shift):
    return encrypt(message, -shift)


while True:
    print("\n1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        message = input("Enter message: ")
        shift = int(input("Enter shift value: "))

        result = encrypt(message, shift)
        print("Encrypted message:", result)

    elif choice == "2":
        message = input("Enter encrypted message: ")
        shift = int(input("Enter shift value: "))

        result = decrypt(message, shift)
        print("Decrypted message:", result)

    elif choice == "3":
        print("Thank you for using Caesar Cipher!")
        break

    else:
        print("Invalid choice. Please try again.")
