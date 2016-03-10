import os
import random as _random
import tests

# Might be useful to print out the current weights and tests
# tests.print_tests()

def get_move(data):
    directions = ["north", "south", "east", "west"]
    moves = {key: 1 for key in directions}
    for test in tests.get():
        testMoves = {}
        for direction in directions:
            ## The test.run score is either a positive floating point number
            ## between 0 and 1 or None
            ## If the score is a number it is added to the
            ## overall score for that direction

            ## if the score is None then stop processing that direction
            ## and set the direction to zero as you do not want to go in that direction
            if moves[direction] == 0: continue
            testMoves[direction] = test.run(data, direction)
            if testMoves[direction] == None: moves[direction] = 0
            else: moves[direction] += test.WEIGHT * float(testMoves[direction])
        print "{0} ({1}): {2}".format(os.path.basename(test.__file__), test.WEIGHT, testMoves)
    print "Total: {0}".format(moves)
    return max(moves, key=moves.get)

def taunt(data):
    taunts = [
                  "Oh man oh geese Rick!",
                  "WUBBA LUBBA DUB DUBS!!!",
                  "Yo! What's up my glip glops?",
                  "I'm tiny Rick!",
                  "Time to get schwifty in here",
                  "Can you assimilate a giraffe?",
                  "It's time to get your beak wet tonight playa!"
             ]

    return taunts[int(_random.random() * len(taunts))]

def head(bottle):
    return '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

def color():
    return "#F9FD72"
    # r = lambda: _random.randint(0,255)
    # return '#%02X%02X%02X' % (r(),r(),r())
