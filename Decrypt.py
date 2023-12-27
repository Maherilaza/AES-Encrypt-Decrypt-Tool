import os
from Crypto.Cipher import AES

def decrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as file_in, open(output_file, "wb") as file_out:
        nonce = file_in.read(16)
        tag = file_in.read(16)
        ciphertext = file_in.read()
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        file_out.write(plaintext)

def decrypt_directory(input_directory, key):
    output_dir = "AES-DF"
    os.makedirs(output_dir, exist_ok=True)
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".enc"):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, file[:-4])
                decrypt_file(input_path, output_path, key)
                print(f"Decrypted file: {output_path}")

def main():
    try:
        key = None
        with open("KEY/AES-C.KEY", "rb") as key_file:
            key = key_file.read()

        decrypt_directory("AES-EF", key)
        print("Default directory (AES-EF) decrypted successfully.")
    except:
        print("Please put the correct AES-C key in the main folder.")
        print("No key, no file.")

if __name__ == "__main__":
    main()
