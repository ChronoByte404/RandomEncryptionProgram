# Encryption Program

This Python script allows you to encrypt and decrypt files using a simple encryption algorithm.

## Features
- **Key Generation:** Generate a new encryption key.
- **Encryption:** Encrypt files using the generated key.
- **Decryption:** Decrypt files using the generated key.

## Prerequisites
- Python 3.x
- `os` module
- `random` module

## Usage
1. Clone or download the repository to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Use the following command to run the script:

```bash
python3 encryption_program.py [mode] [key_name]
```

Replace `[mode]` with one of the following:
- `newkey`: Generate a new encryption key.
- `encrypt`: Encrypt files using an existing key.
- `decrypt`: Decrypt files using an existing key.

Replace `[key_name]` with the name of the key (without the `.key` extension).

## Key Management
- Keys are stored in the `keys` folder within the same directory as the script.
- Encrypted files are stored in the `target` folder within the same directory as the script.
- Decrypted files will overwrite the original files in the `target` folder.

## Example Usage

### Generate a New Key

```bash
python3 main.py newkey my_key
```

### Encrypt Files

```bash
python3 main.py encrypt my_key
```

### Decrypt Files

```bash
python3 main.py decrypt my_key
```

## Notes
- Make sure to keep your encryption key secure.
- Always remember to back up your files before encryption.
- Save your generated key (placed in the keys folder) to an EXTREMELY safe space. Once it's lost, it will be unrecoverable for the next 256 billion years or so.
