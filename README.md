# AES Encryption and Decryption

This Python script allows you to encrypt and decrypt files using the AES encryption algorithm. The code utilizes the pycryptodome library to implement AES encryption.

## Requirement
```shell
python3 -r requirement.txt
```

## Encryption

To encrypt a file or a folder, run the 'Encrypt.py' script. You will have the option to specify the path of the file/folder to encrypt or to use the default folder "AES-EF". The decryption key will be automatically generated in the "AES-C" file each time the script is used.
```shell
python3 Encrypt.py
````

## Decryption
To decrypt an encrypted file, run the "Decrypt.py" script. You can choose to use the key stored in "AES-C" or specify a location for the decryption key. The decrypted files will be placed in the "AES-DF" folder.

### File Structure
* Encrypt.py: AES encryption script.
* Decrypt.py: AES decryption script.
* AES-C: Fichier contenant la clé de déchiffrement générée automatiquement.
* KEY/AES-EF.KEY: File containing the automatically generated decryption key.
* AES-DF: Default folder for encrypting files.
* AES-DF: Folder where decrypted files are stored.

#### Warning :
Make sure to securely keep the decryption key ("AES-C" file) as it is required to decrypt the files.
