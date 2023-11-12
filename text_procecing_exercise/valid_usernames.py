def username_is_valid(username):
    if length_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        return True
    return False


def length_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def characters_are_valid(username):
    for character in username:
        if not (character.isalnum() or character == '_' or character == '-'):
            return False
    return True


def no_redundant_symbols(username):
    if " " in username:
        return False
    return True


usernames = input().split(', ')
for current_username in usernames:
    if username_is_valid(current_username):
        print(current_username)
