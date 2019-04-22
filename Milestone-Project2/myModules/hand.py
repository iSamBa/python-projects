from myModules.card import Card

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        current_hand = ''
        for card in self.cards:
            current_hand += f' | {card}'
        return f'{current_hand} |\n'

    def add_card(self, card):
        self.cards.append(card)

    def calculate_hand_value(self):
        self.value = 0
        if 'Ace' in map(lambda card: card.rank, self.cards):
            for card in self.cards:
                if not card.rank == 'Ace':
                    self.value += values[card.rank]
            for card in self.cards:
                if card.rank == 'Ace':
                    if self.value <= 10:
                        self.value += 11
                    else:
                        self.value += 1
        else:
            for card_value in map(lambda card: card.rank, self.cards):
                self.value += values[card_value]
        return self.value


if __name__ == '__main__':
    my_hand = Hand()
    cards = [Card("Hearts", 'Five'), Card('Clubs', 'Queen'), Card('Diamonds', 'Queen')]

    for card in cards:
        my_hand.add_card(card)

    print(my_hand.hand_value())
