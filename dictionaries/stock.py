elements = input().split()
stock = {}
for i in range(0,len(elements),2):
    key = elements[i]
    value = elements[i+1]
    stock[key] = int(value)
searching_for = input().split()
for element in searching_for:
    if element in stock:
        print(f"We have {stock[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")