import string
def create_cipher(key):
    alphabet = string.ascii_lowercase
    cipher = dict(zip(alphabet, key))
    return cipher
def encrypt(plain_text, key):
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates
    cipher = create_cipher(key)
    
    # Encrypt the message
    encrypted_text = ""
    for char in plain_text:
        if char.lower() in string.ascii_lowercase:
            if char.isupper():
                encrypted_text += cipher[char.lower()].upper()
            else:
                encrypted_text += cipher[char]
        else:
            encrypted_text += char 

    return encrypted_text
def decrypt(encrypted_text, key):
    key = ''.join(sorted(set(key), key=key.index)) 
    cipher = create_cipher(key)
    reverse_cipher = {v: k for k, v in cipher.items()}  # Reverse the dictionary for decryption
    decrypted_text = ""
    for char in encrypted_text:
        if char.lower() in string.ascii_lowercase:
            if char.isupper():
                decrypted_text += reverse_cipher[char.lower()].upper()
            else:
                decrypted_text += reverse_cipher[char]
        else:
            decrypted_text += char  

    return decrypted_text
key = "qazwsxrdctfvgbyhnujmikolp" 
plain_text = "Hello, World! This is a substitution cipher."
encrypted = encrypt(plain_text, key)
decrypted = decrypt(encrypted, key)

print("Original Text: ", plain_text)
print("Encrypted Text: ", encrypted)
print("Decrypted Text: ", decrypted)
