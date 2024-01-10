def is_ticket_valid(ticket):
    if len(ticket) == 20:
        return True
    return False


def is_ticket_winning(ticket):
    winning_symbols = ['@', '#', '$', '^']
    if is_ticket_valid(ticket):
        middle = 10
        left_side = ticket[0:middle]
        left_symbol = ''
        left_counter = 0
        right_side = ticket[middle:20]
        right_symbol = ''
        right_counter = 0
        winning_symbol = ''
        for symbol in left_side:
            if symbol in winning_symbols:
                if symbol != left_symbol and left_counter < 6:
                    left_counter = 1
                elif symbol == left_symbol:
                    left_counter += 1
                    winning_symbol = symbol
            left_symbol = symbol
        for symbol in right_side:
            if symbol in winning_symbols:
                if symbol != right_symbol and right_counter < 6:
                    right_counter = 1
                elif symbol == right_symbol:
                    right_counter += 1
            right_symbol = symbol
        if left_counter == 10 and right_counter == 10:
            return f'ticket "{ticket}" - {left_counter}{winning_symbol} Jackpot!'
        elif left_counter >= 6 and right_counter >= 6:
            return f'ticket "{ticket}" - {min(right_counter, left_counter)}{winning_symbol}'
        return f'ticket "{ticket}" - no match'
    else:
        return "invalid ticket"


lottery_tickets = [ticket.strip() for ticket in input().split(', ')]
for current_ticket in lottery_tickets:
    print(is_ticket_winning(current_ticket))
