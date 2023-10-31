import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if _name_ == "_main_":
    password_length = int(input("Enter the desired password length: "))
    
    if password_length < 1:
        print("Password length should be at least 1.")
    else:
        password = generate_password(password_length)
        print("Generated Password: ", password)
