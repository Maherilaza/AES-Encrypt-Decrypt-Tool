import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def generate_aes_key():
    key = get_random_bytes(16)
    with open("KEY/AES-C.KEY", "wb") as key_file:
        key_file.write(key)


def encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(input_file, "rb") as file_in, open(output_file, "wb") as file_out:
        data = file_in.read()
        ciphertext, tag = cipher.encrypt_and_digest(data)
        file_out.write(cipher.nonce)
        file_out.write(tag)
        file_out.write(ciphertext)

try:
    def delete_past_file():
        rm = os.remove("AES-EF/PAST_FILE_HERE")
    delete_past_file()

except:
    pass

import os

def encrypt_directory(directory, key):
    output_dir = "AES-EF"
    os.makedirs(output_dir, exist_ok=True)
    for root, _, files in os.walk(directory):
        for file in files:
            if file == "PAST_FILE_HERE":
                continue
            input_path = os.path.join(root, file)
            output_path = os.path.join(output_dir, file + ".enc")
            encrypt_file(input_path, output_path, key)
            os.remove(input_path)


def main():
    generate_aes_key()

    print("Choose an option:")
    print("1. Specify the path of the file/directory to encrypt")
    print("2. Use the default directory (AES-EF)")
    choice = input("Your choice: ")

    key = None
    with open("KEY/AES-C.KEY", "rb") as key_file:
        key = key_file.read()

    if choice == "1":
        path = input("Enter the path of the file/directory to encrypt: ")
        if os.path.isfile(path):
            encrypt_file(path, path + ".enc", key)
            print("File encrypted successfully.")
        elif os.path.isdir(path):
            encrypt_directory(path, key)
            print("Directory encrypted successfully.")
        else:
            print("The specified path is neither a file nor a directory.")
    elif choice == "2":
        encrypt_directory("AES-EF", key)
        print("Default directory (AES-EF) encrypted successfully.")
    else:
        print("Invalid choice.")
#Create past file

with open("AES-EF\PAST_FILE_HERE", "w") as f:
    f.write("You are in past here and you understand what I mean!")

if __name__ == "__main__":
    main()
