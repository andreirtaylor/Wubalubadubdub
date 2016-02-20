WEIGHT  = 1

# Returns a positive integer that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction
def run(data, direction):
    print direction
    moves = {"north": 1, "south": 20, "east": 3, "west": 4}
    print moves[direction]
    return moves[direction]
