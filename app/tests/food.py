WEIGHT  = 10

import math

# Returns a positive floating point between 0 and 1 that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction
def run(data, direction):
    head = [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]["coords"][0]
    myWeight = 0
    numFood = 0
    if "gold" in data: things = data["food"] + data["gold"]
    else: things = data["food"]
    for food in things:
        if foodInDirectionOfHead(head,food,direction):
            numFood += 1
            myWeight += 1/float(calculateMoves(head,food, data["height"],data["width"]))
    #moves = {"north": 0.1, "south": 0.20, "east": 0.3, "west": 0.4}
    if numFood is 0:
        return 0
    else:
        return myWeight / (math.log(numFood + 1) * 2)
    return myWeight


def calculateMoves(head,point,height,width):
    return abs(head[0] - point[0]) + abs(head[1] - point[1])

def foodInDirectionOfHead(head,point, direction):
    if direction == "north":
        if head[1] - point[1] > 0:
            return True
        else:
            return False
    elif direction == "west":
        if head[0] - point[0] > 0:
            return True
        else:
            return False
    elif direction == "south":
        if point[1] - head[1] > 0:
            return True
        else:
            return False
    else:
        if point[0] - head[0] > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print run({"width": 17, "height":17, "food":[[2,1]],"snakes": [{"id":"9a6b2c23-9485-4d7b-b459-d0a8689e10d8","coords":[[3,1]]}], "our-snake-id":"9a6b2c23-9485-4d7b-b459-d0a8689e10d8"},"west")