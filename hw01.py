import math

# Cléo Thor
# thor@bu.edu

# Annie, Steve, and Can have to choose a place for lunch, but they can't agree on one
# option. As great CS237 CA's they came up with this idea: let each of the three roll 
# a fair six-sided die, and the one with the highest amount of points will be the winner,
# and will take the other two to their favorite restaurant.

# Steve throws a die and gets S points, Can gets C points. It is Annie's turn. But she 
# doesn't hurry. She wants to know for sure the probability of choosing her favorite 
# restaurant.

# It is known that Can and Steve are true gentlemen, that's why if they have the same 
# amount of points with Annie, they will let Annie win.

# Finish the implementation of the function in hw01.py and return a string with the 
# probability of Annie winning in the form of an irreducible fraction in format A/B, 
# where A — the numerator, and B — the denominator. If the required probability equals 
# to zero, output 0/1. If the required probability equals to 1, output 1/1. 

# input: Two natural numbers C and S — the results of Can's and Steve's die rolls.
def answer(C, S):
    # output: A string with the probability of Annie winning in the form of an 
    # irreducible fraction in format A/B, where A — the numerator, and B — the 
    # denominator.
    possible = 6
    highest = max(C, S)
    highest = 7 - highest
    x = math.gcd(highest, possible)
    highest /= x
    possible /= x
    toReturn = str(int(highest)) + "/" + str(int(possible))
    return toReturn
