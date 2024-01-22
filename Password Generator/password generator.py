# Project: Password Genrator
# The program is a function that takes in parameters namely: length, nums, special_chars, uppercase, lowercase
# These parametrs play a role in defining how the password should be randomized, by defining the length, how many numbers you want, how many special characters, how many uppercase characters and lowecase you may require.

# Importing Python modules strings and secret allow us to access the alphabet and generate randomized outputs whilst maintaining security. 

import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
    
if __name__ == '__main__': 
    new_password = generate_password()
    print('Generated password:', new_password)