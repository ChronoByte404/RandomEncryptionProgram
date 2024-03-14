import random
import os

class REP:
    def __init__(self):
        self.length = 256

    def create_new_key(self):
        key_name = input("Enter the name for the key: ")
        multiplier = int(input("Enter the multiplier: "))
        
        ascii_values = [ord(char) for char in key_name]
        multiplied_values = [value * multiplier for value in ascii_values]
        new_key = ''.join([str(value % 10) for value in multiplied_values])  # Ensure each digit is within 0-9
        print(f"Finished key: {new_key}")
        
        with open(f"./keys/{key_name}.key", "w+") as file:
            file.write(new_key)

    def encrypt_key(self):
        print("Place all the files you wish to encrypt within the 'target' folder and the key within the 'keys' folder.")
        key_name = input("Enter the name of the key: ")
        with open(f"./keys/{key_name}.key", "r") as file:
            key = int(file.read())
        
        for filename in os.listdir("./target"):
            with open(f"./target/{filename}", "rb") as f:
                data = f.read()
                encrypted_data = bytes([(byte + key) % 256 for byte in data])  # Use modular arithmetic for encryption
            
            with open(f"./target/{filename}.encrypted", "wb+") as f:
                f.write(encrypted_data)

    def decrypt_key(self):
        print("Place all the files you wish to decrypt within the 'target' folder and the key within the 'keys' folder.")
        key_name = input("Enter the name of the key: ")
        with open(f"./keys/{key_name}.key", "r") as file:
            key = int(file.read())
        
        for filename in os.listdir("./target"):
            if filename.endswith(".encrypted"):
                with open(f"./target/{filename}", "rb") as f:
                    data = f.read()
                    decrypted_data = bytes([(byte - key) % 256 for byte in data])  # Use modular arithmetic for decryption
                
                with open(f"./target/{filename[:-10]}", "wb+") as f:  # Remove '.encrypted' suffix
                    f.write(decrypted_data)

if __name__ == "__main__":
    rep_instance = REP()
    
    print("Choose an option:")
    print("1. Create New Key")
    print("2. Encrypt")
    print("3. Decrypt")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        rep_instance.create_new_key()
    elif choice == 2:
        rep_instance.encrypt_key()
    elif choice == 3:
        rep_instance.decrypt_key()
    else:
        print("Invalid choice.")
