# Returns a positive floating point between 0 and 1 that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction
WEIGHT = 1

#Current algorithm is very conservative, and does not challenge snakes it knows it can be.

def run(data, direction):
	#In the event we will run into a snake head to head, return None if the Snake is larger or equal to us. Return 0 if smaller.
    ourSnake = [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]
    ourHead = ourSnake["coords"][0][:]
    ourSize = len(ourSnake["coords"])
    otherSnakeHeads = [tuple(x["coords"][0]) for x in data["snakes"] if x["id"] != data["our-snake-id"]]
    otherSnakes = [x for x in data["snakes"] if x["id"] != data["our-snake-id"]]
    for snake in otherSnakes:
        if snake["id"] is not data["our-snake-id"]:
            theirHead = snake["coords"][0]
            checkSquares = []
            if calculateMoves(ourHead, theirHead) <= 2:
                if direction is "north":
                    potentialHead = [ourHead[0], ourHead[1]-1]
                    checkSquares.append(tuple([potentialHead[0] - 1, potentialHead[1]])) #west
                    checkSquares.append(tuple([potentialHead[0] + 1, potentialHead[1]])) #east
                    checkSquares.append(tuple([potentialHead[0], potentialHead[1] - 1]))  #north
                    #checkSquares.append(tuple([potentialHead[0], potentialHead[1] + 1]))  #south
                elif direction is "east":
                    potentialHead = [ourHead[0] + 1, ourHead[1]]
                    #checkSquares.append(tuple([potentialHead[0] - 1, potentialHead[1]])) #west
                    checkSquares.append(tuple([potentialHead[0] + 1, potentialHead[1]])) #east
                    checkSquares.append(tuple([potentialHead[0], potentialHead[1] - 1]))  #north
                    checkSquares.append(tuple([potentialHead[0], potentialHead[1] + 1]))  #south
                elif direction is "south":
                    potentialHead = [ourHead[0], ourHead[1] + 1]
                    checkSquares.append(tuple([potentialHead[0] - 1, potentialHead[1]])) #west
                    checkSquares.append(tuple([potentialHead[0] + 1, potentialHead[1]])) #east
                    #checkSquares.append(tuple([potentialHead[0], potentialHead[1] - 1]))  #north
                    checkSquares.append(tuple([potentialHead[0], potentialHead[1] + 1]))  #south
                else:
                    potentialHead = [ourHead[0] - 1, ourHead[1]]
                    checkSquares.append(tuple([potentialHead[0] - 1, potentialHead[1]])) #west
                    #checkSquares.append([tuple(potentialHead[0] + 1, potentialHead[1])]) #east
                    checkSquares.append(tuple([potentialHead[0], potentialHead[1] - 1]))  #north
                    checkSquares.append(tuple([potentialHead[0], potentialHead[1] + 1]))  #south
                checkSquares.append(tuple(potentialHead))
                if (len(set(checkSquares).intersection(otherSnakeHeads)) > 0 and len(snake["coords"]) >= ourSize):
                    return None
                else:
                    return 1    

    		#When were at a crossroads, check the size of the snake.
    return 1

def calculateMoves(head,point):
    return abs(head[0] - point[0]) + abs(head[1] - point[1])

if __name__ == '__main__':
    print run({"width": 17, "height":17, "food":[[3,1]],"snakes": [{"id":"9a6b2c23-9485-4d7b-b459-d0a8689e10d8","coords":[[3,1]]},{"id":"9a6b2c23-9485-4d7b-b459-d0a8689e10d7","coords":[[2,2]]},{"id":"9a6b2c23-9485-4d7b-b459-d0a8689e10d6","coords":[[0,4]]}], "our-snake-id":"9a6b2c23-9485-4d7b-b459-d0a8689e10d8"},"west")