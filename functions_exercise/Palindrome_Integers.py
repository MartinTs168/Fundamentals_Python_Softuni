def palindrome_check(number):
    if number == number[::-1]:
        return True
    return False


list_of_numbers = input().split(', ')
for number in list_of_numbers:
    is_palindrome = palindrome_check(number)
    print(is_palindrome)
