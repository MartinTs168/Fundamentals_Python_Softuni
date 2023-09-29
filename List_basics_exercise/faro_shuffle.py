deck = input().split(" ")
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    middle_of_deck = len(deck)//2
    deck_1 = deck[0:middle_of_deck]
    deck_2 = deck[middle_of_deck:]
    shuffled_deck = []
    for card_index in range(len(deck_1)):
        shuffled_deck.append(deck_1[card_index])
        shuffled_deck.append(deck_2[card_index])
    deck = shuffled_deck
print(deck)
