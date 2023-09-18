import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def generate_aes_key():
    key = get_random_bytes(16)
    with open("AES-C", "wb") as key_file:
        key_file.write(key)


def encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(input_file, "rb") as file_in, open(output_file, "wb") as file_out:
        data = file_in.read()
        ciphertext, tag = cipher.encrypt_and_digest(data)
        file_out.write(cipher.nonce)
        file_out.write(tag)
        file_out.write(ciphertext)


def encrypt_directory(directory, key):
    output_dir = "AES-EF"
    os.makedirs(output_dir, exist_ok=True)
    for root, _, files in os.walk(directory):
        for file in files:
            input_path = os.path.join(root, file)
            output_path = os.path.join(output_dir, file + ".enc")
            encrypt_file(input_path, output_path, key)


def main():
    generate_aes_key()

    print("Choisissez l'option :")
    print("1. Spécifier le chemin du fichier/dossier à crypter")
    print("2. Utiliser le dossier par défaut (AES-EF)")
    choice = input("Votre choix : ")

    key = None
    with open("AES-C", "rb") as key_file:
        key = key_file.read()

    if choice == "1":
        path = input("Entrez le chemin du fichier/dossier à crypter : ")
        if os.path.isfile(path):
            encrypt_file(path, path + ".enc", key)
            print("Fichier crypté avec succès.")
        elif os.path.isdir(path):
            encrypt_directory(path, key)
            print("Dossier crypté avec succès.")
        else:
            print("Le chemin spécifié n'est ni un fichier ni un dossier.")
    elif choice == "2":
        encrypt_directory("AES-EF", key)
        print("Dossier par défaut (AES-EF) crypté avec succès.")
    else:
        print("Choix invalide.")


if __name__ == "__main__":
    main()
