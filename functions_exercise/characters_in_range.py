def characters_between(a,b):
    for i in range(ord(a) + 1,ord(b)):
        print(chr(i),end=" ")


character1 = input()
character2 = input()
characters_between(character1, character2)