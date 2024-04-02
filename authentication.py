import re

def validate_password(password, username, last_three_passwords):
    
    if len(password) < 10:
        return False, "Password must be at least 10 characters long."

    if not (any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in '@#$%&*!' for c in password)):
        return False, "Password must contain at least 2 uppercase letters, 2 lowercase letters, 2 digits, and 2 special characters."

    if re.search(r'(\w)\1\1\1', password):
        return False, "Password should not contain more than 3 repeating characters in a row."

    if username and re.search(username, password):
        return False, "Password should not contain the username."

    if password in last_three_passwords:
        return False, "Password cannot be the same as any of the last three passwords."

    return True, "Password is valid."


def main():
    username = input("Enter username: ")
    last_three_passwords = []  

    while True:
        password = input("Enter new password: ")
        is_valid, message = validate_password(password, username, last_three_passwords)
        if is_valid:
            print("Password set successfully!")
            last_three_passwords.append(password)
            if len(last_three_passwords) > 3:
                last_three_passwords.pop(0)
            break
        else:
            print("Password validation failed:", message)


if __name__ == "__main__":
    main()
