from myModules.deck import Deck
from myModules.player import Player


def init_chips():
    while True:
        try:
            chips = int(input("Enter player's chips : "))
        except:
            print("Un-valid number, please enter a number")
        else:
            if chips <= 0:
                print('chips amount must be greater than 0')
            else:
                return chips


if __name__ == '__main__':
    dealer = Player('Dealer')
    print('\nWelcome to the Black Jack game\n')
    player = Player('Player')
    print('A player instance has been created\n')
    player.chips = init_chips()
    while True:
        deck = Deck()
        print('Player, please take a bet\n')
        player.take_bet()
        print('Dealing 2 cards to the dealer\n')
        dealer.hit(deck.deal())
        dealer.hit(deck.deal())
        print('Dealing 2 cards to the player\n')
        player.hit(deck.deal())
        player.hit(deck.deal())

        print(f"Dealer's hand : {dealer.hand.cards[0]} | --- HIDDEN --- |")
        print(f"Player's hand : {player.hand.cards[0]} | {player.hand.cards[1]} |")

        player_value = player.hand.calculate_hand_value()
        print(f"Your current hand value is : {player_value}")

        while player_value <= 21:
            answer = input("Do you want to hit (Y/N) ? : ")
            if answer.upper() == 'Y':
                player.hit(deck.deal())
                print(f"Player's hand : {player.hand}")
                player_value = player.hand.calculate_hand_value()
                continue
            elif answer.upper() == 'N':
                print(f"Your current hand value is : {player_value}")
                break
            else:
                continue

        if player.hand.calculate_hand_value() > 21:
            player_value = player.hand.calculate_hand_value()
            #        print(f"Player hand : {player.hand}")
            print('You lost !')
            print(f"Your current hand value is : {player_value}")
            player.lose_bet()

        if dealer.hand.calculate_hand_value() <= 17:
            dealer.hit(deck.deal())

        dealer_value = dealer.hand.calculate_hand_value()

        if dealer_value > 21 or dealer_value <= player_value <= 21:
            print('You won !')
            print(f"Your current hand value is : {player_value}")
            print(f"Dealer's current hand value is : {dealer_value}")
            player.win_bet()

        print(player)
        answer = input('Continue Y/N').upper()
        if answer == 'Y':
            continue
        elif answer == 'N':
            break
