# AES-E-D
# Chiffrement et Déchiffrement AES

Ce script Python vous permet de chiffrer et de déchiffrer des fichiers en utilisant l'algorithme de chiffrement AES (Advanced Encryption Standard). Le code utilise la bibliothèque `pycryptodome` pour implémenter le chiffrement AES.

## Configuration

Assurez-vous d'installer la bibliothèque `pycryptodome` en utilisant `pip install pycryptodome` avant d'exécuter le code.

## Chiffrement

Pour chiffrer un fichier ou un dossier, exécutez le script main.py`. Vous aurez le choix de spécifier le chemin du fichier/dossier à chiffrer ou d'utiliser le dossier par défaut "AES-EF". La clé de déchiffrement sera générée automatiquement dans le fichier "AES-C" à chaque utilisation.

```shell
python3 main.py
````

## Déchiffrement
Pour déchiffrer un fichier chiffré, exécutez le script decrypt_aes_file.py. Vous aurez le choix entre utiliser la clé stockée dans "AES-C" ou spécifier un emplacement pour la clé de déchiffrement. Les fichiers déchiffrés seront placés dans le dossier "AES-DF".

### Structure des fichiers
* main.py: Script de chiffrement AES.
* decrypt_aes_file.py: Script de déchiffrement AES.
* AES-C: Fichier contenant la clé de déchiffrement générée automatiquement.
* AES-EF: Dossier par défaut pour le chiffrement des fichiers.
* AES-DF: Dossier où les fichiers déchiffrés sont stockés.

#### Avertissement
Assurez-vous de conserver en sécurité la clé de déchiffrement (fichier "AES-C"), car elle est nécessaire pour déchiffrer les fichiers.
