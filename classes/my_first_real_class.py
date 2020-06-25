"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

import random


class Card:
    """Represents a standard playing card.
    Attributes:
      naipe: integer 0-3
      rank: integer 1-13
    """

    naipe_names = ["Paus", "Ouros", "Copas", "Espadas"]
    rank_names = [None, "As", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Valete", "Rainha", "Rei"]

    def __init__(self, naipe=0, rank=2):
        self.naipe = naipe
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '{} de {}'.format(Card.rank_names[self.rank],
                                Card.naipe_names[self.naipe])

    def __eq__(self, other):
        # Eu estou informando para o objeto, para a classe, como fazer comparação dessas coisas
        """Checks whether self and other have the same rank and naipe.

        returns: boolean
        """
        return self.naipe == other.naipe and self.rank == other.rank

    def __lt__(self, other):
        # lt = larger than = maior que
        """Compares this card to other, first by naipe, then rank.

        returns: boolean
        """
        t1 = self.naipe, self.rank
        t2 = other.naipe, other.rank
        return t1 < t2


class Deck:
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """

    def __init__(self):
        """Initializes the Deck with 52 cards.
        """
        self.cards = []
        for naipe in range(4):
            for rank in range(1, 14):
                card = Card(naipe, rank)
                self.cards.append(card)

    def __str__(self):
        """Returns a string representation of the deck.
        """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck.

        card: Card
        """
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there.

        card: Card
        """
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    #
    alan = Hand('Alan')
    godoy = Hand('Godoy')
    #
    deck.move_cards(alan, 3)
    deck.move_cards(godoy, 3)
    # hand.sort()
    # print(hand)
