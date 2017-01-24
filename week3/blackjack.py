from random import randint

def deal(score):
    card = randint(1, 13)

    if card == 1: # Ace
        return 1 if score > 10 else 11
    else:
        return min(card, 10)

def print_update(player_score, computer_score):
    print('You have:', player_score, '| Computer has:', computer_score)

def check_bust(score):
    return score > 21

def player_decision():
    decision = input('Would you like to "hit" or "stay"?: ')

    if decision != 'hit' and decision != 'stay':
        print('Invalid decision! Exiting...')
        exit(0)

    return decision

def computer_decision(score, player_score):
    if player_score > score:
        return 'hit'
    else:
        return 'stay'

def process_decision(score, decision):
    if decision == 'hit':
        return deal(score)
    elif decision == 'stay':
        return 0
    else:
        print('Invalid decision! Exiting...')
        exit(0)

def main():
    # Deal two cards to the player
    player_score = deal(0)
    player_score += deal(player_score)

    # Deal two cards to the computer
    computer_score = deal(0)
    computer_score += deal(computer_score)

    print_update(player_score, computer_score)

    # Process player's turn
    player_score += process_decision(player_score, player_decision())
    print_update(player_score, computer_score)

    if check_bust(player_score):
        print('You bust! Computer wins!')
        exit(0)

    # Process computer's turn
    decision = computer_decision(computer_score, player_score)
    print('Computer decision:', decision)
    computer_score += process_decision(computer_score, decision)
    print_update(player_score, computer_score)

    if check_bust(computer_score):
        print('Computer busts! You win!')
        exit(0)

    # Determine winner if no one has busted
    if player_score > computer_score:
        print('You win!')
    elif computer_score > player_score:
        print('Computer has won!')
    else:
        print('It\'s a tie!')

if __name__ == '__main__':
    main()