import secrets
import string

def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure that the generated password has a mix of characters
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            break
    
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)
