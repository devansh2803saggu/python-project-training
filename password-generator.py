import random
import string

def generate_password(length=12):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return ""

    # Characters sets
    letters = string.ascii_letters   # a-zA-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # special characters like !@#$%

    # Ensure password has at least one letter, digit, and symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length with random choices from all sets
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)

    # Shuffle to avoid predictable sequences
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter desired password length (minimum 4): "))
    pwd = generate_password(length)
    if pwd:
        print(f"Generated password: {pwd}")
