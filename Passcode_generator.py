import random
import string 

def generate_passcode(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Start with letters and optionally add digits and special characters
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars
    
    pwd = ""
    meets_criteria = False 
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in digits:
            has_number = True
        if new_char in special_chars:
            has_special = True 

        # Ensure criteria are met
        meets_criteria = True
        if numbers:
            meets_criteria = meets_criteria and has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd 

# User input
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

# Generate and display the password
pwd = generate_passcode(min_length, has_number, has_special)
print("The generated password is:", pwd)
