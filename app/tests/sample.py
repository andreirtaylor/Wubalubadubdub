WEIGHT  = 10

# Returns a positive floating point between 0 and 1 that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction
def run(data, direction):
    moves = {"north": 0.1, "south": 0.20, "east": 0.3, "west": 0.4}
    return moves[direction]
