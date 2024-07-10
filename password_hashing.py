from argon2 import PasswordHasher
from argon2.low_level import Type
import json
import secrets
import string

# Initialize Argon2 password hasher
ph = PasswordHasher(hash_len=16, type=Type.ID)

# Function to generate a random salt
def generate_salt():
    alphabet = string.ascii_letters + string.digits
    salt = ''.join(secrets.choice(alphabet) for _ in range(16))  # Generate a 16-character salt
    return salt

# Function to load users from users.json
def load_users():
    with open('users.json', 'r') as file:
        users = json.load(file)
    return users

# Function to hash passwords with salt and save to hashed_passwords.json
def hash_passwords():
    users = load_users()
    hashed_passwords = {}

    for username, password in users.items():
        salt = generate_salt()
        salted_password = password + salt  # Concatenate password and salt
        hashed_password = ph.hash(salted_password)
        combined = hashed_password + salt  # Combine hashed password and salt
        hashed_passwords[username] = combined

    with open('hashed_passwords.json', 'w') as file:
        json.dump(hashed_passwords, file, indent=4)

    print("Saved hashed passwords with salt to hashed_passwords.json")

# Main function to execute password hashing
if __name__ == "__main__":
    hash_passwords()
