# Eric and Noah, two avid dart players and close friends, were always on the lookout for new challenges to test their skills. One rainy afternoon, while they were brainstorming over a cup of coffee, Eric proposed a unique challenge - the Darts Challenge.
# In this challenge, they would use their knowledge of geometry and probability along with their dart-throwing prowess to solve a complex problem involving intersecting rectangles and dart throws within a confined space.
# The challenge was set: within a 10x10 dartboard, they needed to identify the intersection area of two randomly positioned rectangles. Moreover, they had to determine the probability of hitting this intersection area when throwing a dart randomly within the board.

# To make things more interesting, Eric and Noah decided to ask you to write a Python function to solve the problem.

# INPUT:
# Eight integer numbers, 0 <= X1, Y1, X2, T2, X3, Y3, X4, Y4 <= 10, such that:
# (X1, Y1) is the bottom-left coordinate of the first rectangle;
# (X2, Y2) is the top-right coordinate of the  first rectangle;
# (X3, Y3) is the bottom-left coordinate of the second rectangle;
# (X4, Y4) is the top-right coordinate of the second rectangle;

# OUTPUT
# The probability of hitting the intersection area if a dart is thrown randomly within the 10x10 region.
# Your answer should be expressed as float number within the interval [0.0,1.0]
def answer(x1,y1,x2,y2,x3,y3,x4,y4):
    # check if rectangles intersect
    if x1 > x4 or x3 > x2 or y1 > y4 or y3 > y2:
        return 0

    p1 = max(x1, x3) #find left x coordinate
    p2 = min(x2, x4) # find right x coordinate
    q1 = max(y1, y3) # find bottom y coordinate
    q2 = min(y2, y4) # find top y coordinate

    area = (q2-q1)*(p2-p1) # calculate area

    probability = area/100 # put over total area
    return probability