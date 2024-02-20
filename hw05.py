# Input
# The input consists of two parameters:
# - n: an integer representing the total number of distinct cards;
# - game: a list of pairs following the format $(integer, string)$ with at least $n$ pairs. The integer number in each pair represents the card value in the range from 1 to $n$. The string represents whether the card is discarded, \texttt{"discard"}, or returned to the deck, \texttt{"keep"}, after each draw.
# Output
# Your output must be a list of strings. Each string can be one of the possible values:
# - "higher": if the next card is more likely to have a higher value than a lower value.
# - "lower": if the next card is more likely to have a lower value than a higher value.
# - "impossible": when the previous cases don't apply.

def answer(n, game):
    deck = list(range(1, n)) # create a list of every card in the deck
    for i in range(len(game)): # iterate through all the tuples
        draw = game[i][0] # card drawn
        ix = deck.index(draw) # index of card drawn
        comp = 1 # to compensate depending on if card is replaced or not
        if game[i][1] == "discard":
            deck.pop(ix) # remove card from deck
            comp = 0 # no need for compensation
        lwr = ix # no. of cards lower than the draw
        hghr = len(deck) - comp - ix # no. of cards higher than the draw

        # return statements
        if lwr > hghr:
            return "lower"
        elif lwr < hghr:
          return "higher"
        else:
            return "impossible"
