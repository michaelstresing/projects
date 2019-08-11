import random


class Card:

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return f"The {self.number} of {self.suit}"

    def show(self):
        print(self.__repr__())


class Deck:

    def __init__(self):
        self.cards = []
        self.getdeck()

    def getdeck(self):

        for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for number in range(1,14):
                self.cards.append(Card(suit, number))

#    print("Deck done!")

    def show(self):

        for card in self.cards:
            card.show()


    def shuffle(self):

        for
