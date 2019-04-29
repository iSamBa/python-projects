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
    player_balance = 300
    while True:
        dealer = Player('Dealer')
        player = Player('Player')
        player.chips = player_balance
        deck = Deck()
        deck.shuffle()
        print('Player, please take a bet\n')
        player.take_bet()
        print('Dealing 2 cards to the dealer\n')
        dealer.hit(deck.deal())
        dealer.hit(deck.deal())
        print('Dealing 2 cards to the player\n')
        player.hit(deck.deal())
        player.hit(deck.deal())

        print(f"Dealer's hand :\t| {dealer.hand.cards[0]} \t| --- HIDDEN --- \t|")
        print(f"Player's hand :\t| {player.hand.cards[0]} \t| {player.hand.cards[1]} \t|")

        player_value = player.hand.calculate_hand_value()
        print(f"\nYour current hand value is : {player_value}")

        while player_value < 21:
            answer = input("\nDo you want to hit (Y/N) ? : ")
            if answer.upper() == 'Y':
                player.hit(deck.deal())
                print(f"Player's hand : {player.hand}")
                player_value = player.hand.calculate_hand_value()
                continue
            elif answer.upper() == 'N':
                player_value = player.hand.calculate_hand_value()
                print(f"Your current hand value is : {player_value}")
                break

        if player.hand.calculate_hand_value() > 21:
            player_value = player.hand.calculate_hand_value()
            #  print(f"Player hand : {player.hand}")
            print('\n>> You lost ! <<\n')
            print(f"Your current hand value is : {player_value}")
            player_balance = player.lose_bet()

        else:

            if dealer.hand.calculate_hand_value() <= 17:
                dealer.hit(deck.deal())

            dealer_value = dealer.hand.calculate_hand_value()

            if dealer_value > 21 or dealer_value <= player_value < 21:
                print('\n>> You won ! <<\n')
                print(f"Your current hand value is : {player_value}")
                print(f"Dealer's current hand value is : {dealer_value}\n\n")
                player_balance = player.win_bet()

        print('Current balance : \n' + str(player))

        answer = input('\nContinue Y/N : ').upper()
        if answer == 'Y':
            continue
        elif answer == 'N':
            break
