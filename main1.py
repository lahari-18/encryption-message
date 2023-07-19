import random
import string

#creating a string of characters
#1st method
#chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#2nd method
chars = " " + string.punctuation + string.digits + string .ascii_letters
#print(chars)
chars= list(chars)


#creating a key which is going to shuffle eventually
key= chars.copy()
#shuffling the key
random.shuffle(key)


#print(f"chars:{chars}")
#print(f"key:{key}")

#ENCRYPTION

plain_text=input("enter a message to encrypt:")
cipher_text=""

for letter in plain_text:
    index =chars.index(letter)
    cipher_text+= key[index]

print(f"original_message:{plain_text}")
print(f"encrypted_message:{cipher_text}")


#DECRYPTION

cipher_text=input("enter a message to encrypt:")
plain_text=""

for letter in cipher_text: #refer to the key
    index =key.index(letter) #then appending the character to the plain text
    plain_text+= chars[index]

print(f"encrypted_message:{cipher_text}")
print(f"original_message:{plain_text}")