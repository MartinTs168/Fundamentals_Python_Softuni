def loading(number: int) -> str:
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    number_of_percentage_symbol = number // 10
    return f"{number}% [{'%' * number_of_percentage_symbol}{'.' * (10 - number_of_percentage_symbol)}]\nStill loading..."


percent = int(input())
print(loading(percent))
