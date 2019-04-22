from myModules.hand import Hand


class Player:
    bet = 0

    def __init__(self, name, chips=0):
        self.name = name
        self.hand = Hand()
        self.chips = chips

    def __str__(self):
        return f"{self.name}'s Chips : {self.chips}\n{self.name}'s bet : {self.bet}"

    def take_bet(self):
        while True:
            try:
                self.bet = int(input('Enter your bet : '))
            except:
                print("Un-valid bet, please enter a number")
            else:
                if self.bet <= 0:
                    print('Bet amount must be greater than 0')
                elif self.chips - self.bet > 0:
                    print(f"Your bet is : {self.bet}")
                    break
                else:
                    print('Bet amount can not exceed the available chips')

    def win_bet(self):
        self.chips += 2 * self.bet
        self.bet = 0

    def lose_bet(self):
        self.chips -= self.bet
        self.bet = 0

    def hit(self, card):
        self.hand.add_card(card)


if __name__ == '__main__':
    player = Player()
    player.chips = 100
    print(player)
    player.take_bet()
    print(player.hand)
