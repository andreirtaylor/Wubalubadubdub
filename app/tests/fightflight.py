WEIGHT  = 15

# Returns a positive floating point between 0 and 1 that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction
def run(data, direction):
    moves = {"north": 0.5, "south": 0.5, "east": 0.5, "west": 0.5}

    oursnake = [s for s in data["snakes"] if s["id"] == data["our-snake-id"]][0]
    othersnakes = [s for s in data["snakes"] if s["id"] != data["our-snake-id"]]

    for snake in othersnakes:
        xDist = snake["coords"][0][0] - oursnake["coords"][0][0]
        yDist = snake["coords"][0][1] - oursnake["coords"][0][1]
        xMove = float(xDist)/data["width"]
        yMove = float(yDist)/data["height"]

        moveRatio = 0.5/len(othersnakes)

        if len(snake["coords"]) < len(oursnake["coords"]):
            # We're bigger! Eat em.
            attackRatio = 1
            moves["east"]  +=  moveRatio * attackRatio * xMove;
            moves["west"]  -=  moveRatio * attackRatio * xMove;

            moves["south"] +=  moveRatio * attackRatio * yMove;
            moves["north"] -=  moveRatio * attackRatio * yMove;
        elif len(snake["coords"]) > len(oursnake["coords"]):
            # We're smaller! Run!
            runRatio = 0.5
            moves["east"]  +=  -1 * moveRatio * runRatio * xMove;
            moves["west"]  -=  -1 * moveRatio *  runRatio * xMove;

            moves["south"] +=  -1 * moveRatio * runRatio * yMove;
            moves["north"] -=  -1 * moveRatio *  runRatio * yMove;

            continue

    return moves[direction]



