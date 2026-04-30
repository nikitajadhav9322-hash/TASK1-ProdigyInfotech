def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)

print("=== Caesar Cipher Program ===")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").lower()

if choice == 'e':
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)

elif choice == 'd':
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice! Please select 'e' or 'd'.")