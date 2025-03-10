import random
import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(a_list):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(a_list) == 21 and len(a_list) == 2:
        return 0
    elif sum(a_list) > 21 and 11 in a_list:
        a_list.remove(11)
        a_list.append(1)
    return sum(a_list)


def compare(u_score, c_score):
    if u_score > 21 and c_score > 21:
        return "We both are over. You Lose"
    elif u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "I have a Blackjack. You Lose"
    elif u_score == 0:
        return "You Win with a Blackjack!"
    elif u_score > 21:
        return "You are over. You lose"
    elif c_score > 21:
        return "I am over. You Win!"
    elif u_score > c_score:
        return "You Win!"
    else:
        return "You Lose"


def play_game():
    print(art.logo)
    c_cards = []
    u_cards = []
    game_over = False
    ur_score = 0
    co_score = 0
    for _ in range(2):
        c_cards.append(deal_card())
        u_cards.append(deal_card())
    while not game_over:
        co_score = calculate_score(c_cards)
        ur_score = calculate_score(u_cards)
        print(f" Your cards: {u_cards}, your score {ur_score}")
        print(f" Dealer top card: {c_cards[0]}")
        if co_score == 0 or ur_score == 0 or ur_score > 21:
            game_over = True
        else:
            user_dec = input("Type 'y' for a hit, 'n' for stay: ")
            if user_dec == 'y':
                u_cards.append(deal_card())
            else:
                game_over = True

    while co_score != 0 and co_score < 17:
        c_cards.append(deal_card())
        co_score = calculate_score(c_cards)

    print(f"Your final hand is {u_cards}, your score is {ur_score}")
    print(f"Dealer's final hand is {c_cards}, your score is {co_score}")
    print(compare(ur_score, co_score))

    while input("Wanna play again, type 'y' or 'n'") == "y":
        play_game()


play_game()
