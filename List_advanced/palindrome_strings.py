def get_palindrome_and_occurrence(list,string_to_search):
    palindrome_list = [x for x in list if x == x[::-1]]
    count_of_string = palindrome_list.count(string_to_search)
    return palindrome_list, count_of_string


text = input().split()
string_to_search = input()
palindrome_text, occurrences = get_palindrome_and_occurrence(text, string_to_search)
print(palindrome_text)
print(f"Found palindrome {occurrences} times")

