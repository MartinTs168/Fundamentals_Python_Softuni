phonebook = {}
while True:
    contact_info = input()
    if len(contact_info.split('-')) < 2:
        break
    name = contact_info.split('-')[0]
    number = contact_info.split('-')[1]
    phonebook[name] = number
n = int(contact_info)
for _ in range(n):
    name = input()
    if name in phonebook.keys():
        number = phonebook.pop(name)
        print(f"{name} -> {number}")
    else:
        print(f"Contact {name} does not exist.")