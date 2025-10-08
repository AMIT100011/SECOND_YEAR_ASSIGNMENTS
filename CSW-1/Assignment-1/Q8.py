def validate_password(password):
    errors = []  # to store rule violations

    # Rule 1: Minimum length 8
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    # Rule 2: At least one uppercase letter
    if not any(ch.isupper() for ch in password):
        errors.append("Password must contain at least one uppercase letter (A–Z).")

    # Rule 3: At least one lowercase letter
    if not any(ch.islower() for ch in password):
        errors.append("Password must contain at least one lowercase letter (a–z).")

    # Rule 4: At least one digit
    if not any(ch.isdigit() for ch in password):
        errors.append("Password must contain at least one digit (0–9).")

    # Rule 5: At least one special character (!@#$%)
    special_chars = "!@#$%"
    if not any(ch in special_chars for ch in password):
        errors.append("Password must contain at least one special character (!@#$%).")

    # Rule 6: No whitespace
    if any(ch.isspace() for ch in password):
        errors.append("Password must not contain any spaces.")

    # Final check
    if len(errors) == 0:
        return True, []
    else:
        return False, errors


# Main program
password = input("Enter your password: ")

is_valid, error_list = validate_password(password)

if is_valid:
    print("\n Password is valid and secure.")
else:
    print("\n Password is invalid. Please fix the following issues:")
    for err in error_list:
        print(f"- {err}")
