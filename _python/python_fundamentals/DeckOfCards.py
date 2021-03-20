class Card:
    def __init__(self, val, type):
        self.value = val
        self.type = type

    def show(self):
        print(self.value, " of ", self.type)


class Deck:
    def __init__(self, name):
        self.deck=[]
        self.name = name
        suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
        values = ["Ace", 1,2,3,4,5,6,7,8,9,10,"Jack", "Queen", "King"]

        for suit in suits:
            for val in values:
                self.deck.append(Card(val, suit))

    def show(self):
        print("\n", "*"*30, self.name, "*"*30)
        for card in self.deck:
            card.show()

d=Deck("Deck1")
d.show()
