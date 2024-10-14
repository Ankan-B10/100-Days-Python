# Coding:
import random
import string

def random_chars(n=3):
    return ''.join(random.choices(string.ascii_letters, k=n))

def encode_word(word):
    if len(word) >= 3:
        word = word[1:] + word[0]  
        return random_chars() + word + random_chars()  
    else:
        return word[::-1]  
def decode_word(word):
    if len(word) < 3:
        return word[::-1]  
    else:
        word = word[3:-3]  
        return word[-1] + word[:-1] 
def encode_message(message):
    return ' '.join(encode_word(word) for word in message.split())

def decode_message(encoded_message):
    return ' '.join(decode_word(word) for word in encoded_message.split())

message = input("Enter a message to encode: ")
encoded_message = encode_message(message)
print(f"Encoded message: {encoded_message}")

decoded_message = decode_message(encoded_message)
print(f"Decoded message: {decoded_message}")
