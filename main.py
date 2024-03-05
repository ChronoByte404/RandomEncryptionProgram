import random
import os
import sys

class REP:
    def __init__(self):
        self.length = 256

    def create_new_key(self, key_name):
        new_key = ''.join([str(random.randint(0, 9)) for _ in range(self.length)])
        print(f"Finished key: {new_key}")
        
        with open(f"./keys/{key_name}.key", "w+") as file:
            file.write(new_key)

    def encrypt_key(self, key_name):
        print("Place all the files you wish to encrypt within the 'target' folder and the key within the 'keys' folder.")
        with open(f"./keys/{key_name}.key", "r") as file:
            key = int(file.read())
        
        for filename in os.listdir("./target"):
            with open(f"./target/{filename}", "rb") as f:
                data = f.read()
                encrypted_data = bytes([(byte + key) % 256 for byte in data])  # Use modular arithmetic for encryption
            
            with open(f"./target/{filename}.encrypted", "wb+") as f:
                f.write(encrypted_data)

    def decrypt_key(self, key_name):
        print("Place all the files you wish to decrypt within the 'target' folder and the key within the 'keys' folder.")
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
    mode = sys.argv[1]

    if mode == "newkey":
        key_name = sys.argv[2]
        rep_instance.create_new_key(key_name)
    elif mode == "encrypt":
        key_name = sys.argv[2]
        rep_instance.encrypt_key(key_name)
    elif mode == "decrypt":
        key_name = sys.argv[2]
        rep_instance.decrypt_key(key_name)
    else:
        print("Invalid mode. Please use 'newkey', 'encrypt', or 'decrypt'.")
