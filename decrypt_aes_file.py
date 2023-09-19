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
                print(f"Fichier déchiffré : {output_path}")

def main():
    try:
        key = None
        with open("AES-C", "rb") as key_file:
            key = key_file.read()

        decrypt_directory("AES-EF", key)
        print("Dossier par défaut (AES-EF) déchiffré avec succès.")
    except:
        print(("Veuillez mettre la bonne clé AES-C dans le dossier principal."))
        print(("Pas de clé pas de fichier "))

if __name__ == "__main__":
    main()
