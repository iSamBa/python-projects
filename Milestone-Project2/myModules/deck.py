import random

from myModules.card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:

    def __init__(self, deck=[]):
        self.deck = deck
        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit, rank))

    def __str__(self):
        return f'This deck contain {len(self.deck)} card\n{self.deck}\n'

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal(self):
        self.shuffle()
        return self.deck.pop()


if __name__ == '__main__':
    my_deck = Deck()
    print(my_deck)

    my_deck.shuffle()
    print(my_deck)
