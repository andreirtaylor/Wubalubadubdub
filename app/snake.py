import os
import tests

def get_move(data):
    moves = {key: 1 for key in ["north", "south", "east", "west"]}
    for direction in moves:
        for test in tests.get():
            score = test.run(None, direction)
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

