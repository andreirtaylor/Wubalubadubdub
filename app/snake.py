import os
import tests

# Might be useful to print out the current weights and tests
# tests.print_tests()

def get_move(data):
    moves = {key: 1 for key in ["north", "south", "east", "west"]}
    for direction in moves:
        for test in tests.get():
            ## The test.run score is either a positive floating point number 
            ## between 0 and 1 or None
            ## If the score is a number it is added to the
            ## overall score for that direction

            ## if the score is None then stop processing that direction
            ## and set the direction to zero as you do not want to go in that direction
            score = test.run(data, direction)
            if not score:
                moves[direction] = 0
                break
            moves[direction] += test.WEIGHT * score 
    print moves
    return max(moves, key=moves.get)

def taunt(data):
    return "Tauting alll the shit"

def head(bottle):
    return '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

def color():
    return "#1447D4"

