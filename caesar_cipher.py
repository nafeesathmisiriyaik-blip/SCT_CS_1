def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


while True:
    print("\n===== Caesar Cipher Tool =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        message = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        print("Encrypted Message:", caesar_cipher(message, shift, "encrypt"))

    elif choice == "2":
        message = input("Enter encrypted message: ")
        shift = int(input("Enter shift value: "))
        print("Decrypted Message:", caesar_cipher(message, shift, "decrypt"))

    elif choice == "3":
        print("Thank you for using Caesar Cipher Tool.")
        break

    else:
        print("Invalid choice. Try again.")