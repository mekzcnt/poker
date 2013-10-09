class Card(object):
    """Represents a standard playing card."""

    suit_names = ['C', 'D', 'H', 'S']
    rank_names = [None, 'A', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns readable string"""
        return '%s%s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        """Comparing cards"""
        t1 = self.suit, self.rank
        t2 = other.suit, other,rank
        return cmp(t1, t2)

class Deck(object):
    """Represents a deck of card."""

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        """ remove cards from a deck"""
        return self.cards.pop()

    def add_card(self, card):
        """ add a card from a deck"""
        self.cards.append(card)

    def shuffle(self):
        """ shuffle a deck for any card"""
        random.shuffle(self.cards)
    
    
