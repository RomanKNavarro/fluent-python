# A deck sequence of cards
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])           # The Card tuple subclass represents the format used for each individual card

class FrenchDeck:
   ranks = [str(n) for n in range(2, 11)] + list('JQKA')          
   suits = 'spades diamonds clubs hearts'.split()                 # the ranks and suits lists are defined

   def __init__(self):
      self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
                                                                  # defines the self._cards list, containing all 52 card names, formatted with Card class


   def __len__(self):
      return len(self._cards)                                     # returns len of list

   def __getitem__(self, position):
      return self._cards[position]                                # returns any card from list given the position
                                        





suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
   rank_value = FrenchDeck.ranks.index(card.rank)
   return rank_value * len(suit_values) + suit_values[card.suit] 
3142
