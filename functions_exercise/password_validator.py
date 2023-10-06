def password_check(password: str) -> list:
    list_of_errors = []
    if not 6 <= len(password) <= 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        list_of_errors.append('Password must consist only of letters and digits')
    digits_counter = 0
    for character in password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


current_password = input()
errors_in_password = password_check(current_password)
if len(errors_in_password) == 0:
    print("Password is valid")
else:
    print(f"\n".join(errors_in_password))
