import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length >= 4:
                return length
            else:
                print("Password length should be at least 4 characters!")
        except ValueError:
            print("Please enter a valid number!")

def get_character_options():
    print("\nSelect character types to include:")
    print("1. Lowercase letters (a-z)")
    print("2. Uppercase letters (A-Z)")
    print("3. Numbers (0-9)")
    print("4. Special symbols (!@#$%^&*)")
    
    choices = input("\nEnter your choices (e.g., 1234 for all): ")
    
    char_pool = ""
    
    if '1' in choices:
        char_pool += string.ascii_lowercase
    if '2' in choices:
        char_pool += string.ascii_uppercase
    if '3' in choices:
        char_pool += string.digits
    if '4' in choices:
        char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not char_pool:
        print("No valid option selected! Using all character types.")
        char_pool = string.ascii_letters + string.digits + "!@#$%^&*"
    
    return char_pool

def generate_password(length, char_pool):
    password = ""
    for i in range(length):
        password += random.choice(char_pool)
    return password

def check_password_strength(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    strength = 0
    if has_lower:
        strength += 1
    if has_upper:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    
    if len(password) >= 12:
        strength += 1
    
    if strength <= 2:
        return "Weak"
    elif strength <= 3:
        return "Medium"
    else:
        return "Strong"

def main():
    print("=" * 50)
    print("       SIMPLE PASSWORD GENERATOR")
    print("=" * 50)
    
    while True:
        try:
            # Get password requirements
            length = get_password_length()
            char_pool = get_character_options()
            
            # Generate password
            password = generate_password(length, char_pool)
            strength = check_password_strength(password)
            
            # Display result
            print("\n" + "=" * 50)
            print("Generated Password:", password)
            print("Password Strength:", strength)
            print("=" * 50)
            
            # Ask for another password
            again = input("\nGenerate another password? (y/n): ").lower()
            if again != 'y':
                print("Thank you for using Password Generator!")
                break
                
        except KeyboardInterrupt:
            print("\n\nProgram terminated by user!")
            break
        except Exception as e:
            print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()