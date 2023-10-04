def calculate(a: int, b: int, operator: str) -> int:
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)


operator = input()
num1 = int(input())
num2 = int(input())
result = calculate(num1, num2, operator)
print(result)