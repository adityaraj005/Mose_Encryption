# Morse Code Encryptor/Decryptor

## Project Overview
A Python script to encrypt text into Morse code and decrypt Morse code back into readable text. This project supports letters, numbers, and some common punctuation marks, making it a simple but effective tool for basic encryption and decryption tasks.

## Features
- **Encryption**: Convert plain text to Morse code.
- **Decryption**: Convert Morse code back to plain text.

## How It Works
The script uses a dictionary to map each character to its corresponding Morse code equivalent. It then provides two main functions:
- `encrypt(text)`: Converts text into Morse code.
- `decrypt(text)`: Converts Morse code into readable text.

## Example Usage

### Encrypting Text
```bash
Do you want to Encrypt your message or Decrypt your message? (Encrypt: 0 / Decrypt: 1): 0
Enter the String/Text for Encryption: Hello World
Your Output: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### Decrypting Morse Code
```bash
Do you want to Encrypt your message or Decrypt your message? (Encrypt: 0 / Decrypt: 1): 1
Enter the Text for Decryption: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Your Output: HELLO WORLD
