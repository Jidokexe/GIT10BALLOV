import random

class Suit:
    def __init__(self, name):
        self.name = name

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def to_text(self):
        for card in self.cards:
            print(f"{card.value} of {card.suit.name}")

    def shuffle(self):
        random.shuffle(self.cards)

class Suits:
    def __init__(self):
        self.suits = [Suit("Serdechki"), Suit("Bubenchiki"), Suit("Kakoytoclever"), Suit("Pikitocheniye")]

class DeckBuilder:
    @staticmethod
    def build_deck(num_cards):
        deck = Deck()
        suits = Suits().suits
        for i in range(num_cards // 4):
            for suit in suits:
                for value in range(1, num_cards//4 + 1):
                    deck.add_card(Card(value, suit))
        return deck

deck36 = DeckBuilder.build_deck(36)
deck52 = DeckBuilder.build_deck(52)

print("Deck of 36 cards:")
deck36.to_text()
print("\nDeck of 52 cards:")
deck52.to_text()

deck36.shuffle()
deck52.shuffle()

print("\nDeck of 36 cards after shuffling:")
deck36.to_text()
print("\nDeck of 52 cards after shuffling:")
deck52.to_text()

