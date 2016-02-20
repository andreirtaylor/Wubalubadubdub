WEIGHT  = 10

# Returns a positive floating point between 0 and 1 that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction
def run(data, direction):
    head = [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]["coords"][0]
    myweight = 0
    for food in data["food"]:
    	if foodInDirectionOfHead(head,food,direction):
    		myweight += 1 / float(calculateMoves(head,food)) 
    #moves = {"north": 0.1, "south": 0.20, "east": 0.3, "west": 0.4}
    return myweight
    

def calculateMoves(head,point):
    return abs(head[0] - point[0]) + abs(head[1] - point[0])

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
    print run({"food":[[0,3],[3,2],[2,2]],"snakes": [{"id":"9a6b2c23-9485-4d7b-b459-d0a8689e10d8","coords":[[3,1]]}], "our-snake-id":"9a6b2c23-9485-4d7b-b459-d0a8689e10d8"},"west")	