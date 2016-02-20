WEIGHT  = 1

# Returns a integer that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction
def run(data, direction):
    print direction
    moves = {key: sum([ord(x) for x in key]) for key in ["north", "south", "east", "west"]}
    print moves[direction]
    return moves[direction]
