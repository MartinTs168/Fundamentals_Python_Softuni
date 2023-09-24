number = float(input())
message = ""
if number == 0:
    message = "zero"
elif 0 > number:
    message = "negative"
    if number > -1:
        message = "small negative"
    elif number < -1000000:
        message = "large negative"
else:
    message = "positive"
    if number < 1:
        message = "small positive"
    elif number > 1000000:
        message = "large positive"
print(message)