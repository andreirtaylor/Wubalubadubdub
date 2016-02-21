# Returns a positive floating point between 0 and 1 that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction
WEIGHT = 1

def run(data, direction):
	#In the event we will run into a snake head to head, return None if the Snake is larger or equal to us. Return 0 if smaller.
	ourSnake = [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]
    ourHead = ourSnake["coords"][0][:]
    ourSize = len(ourSnake["coords"])
    for snake in data["snakes"]:
    	theirHead = snake["coords"][0]
    	if calculateMoves(ourHead, theirHead) == 2 and len(snake) >= ourSize:
    		return None
    		#When were at a crossroads, check the size of the snake.
    return 1

def calculateMoves(head,point,height,width):
    return abs(head[0] - point[0]) + abs(head[1] - point[1]) 