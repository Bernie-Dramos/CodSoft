# Call necessary libraries
import random
import string

# Function for password generation and choice between length, numbers and characters
def gen_pass(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
        
    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False
    
    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
            
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
            
        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special
            
    return pwd

# Request User parameters for password
min_length = int(input("Minimum length for password? "))
has_number = input("Do you want numbers in it? (Y/N) ").lower() == "y"
has_special = input("Do you want special characters in it? (Y/N) ").lower() == "y"
  
# Set the password parameters
pwd = gen_pass(min_length, has_number, has_special)

# Display Generated password
print("Your generated password is: ", pwd)