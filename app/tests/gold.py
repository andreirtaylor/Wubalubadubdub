WEIGHT  = 10

# Returns a positive integer that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction
def run(data, direction):
    # setup gold holder
    gold = []

    my_head = []

    for x in data["snakes"]:
        if x["id"] == "9a6b2c23-9485-4d7b-b459-d0a8689e10d8":
            my_head = x["coords"][0][:]

    print(my_head)
    
    #find current closest based on number of moves
    for i in data["gold"]:
        x_moves = abs(my_head[0] - i[0])
        y_moves = abs(my_head[1] - i[1])
        moves = x_moves + y_moves
        gold.append(moves)


    closest_gold = data["gold"][gold.index(min(gold))]
    num_moves_closest = abs(my_head[0] - closest_gold[0]) + abs(my_head[1] - closest_gold[1])
    
    #check which direction has been passed in and move our head
    if(direction == "north"):
        my_head[1] -= 1
    if(direction == "south"):
        my_head[1] += 1
    if(direction == "east"):
        my_head[0] += 1
    if(direction == "west"):
        my_head[0] -= 1

    print(my_head)
    
    new_gold = []
    #build an array of number of moves to get to gold coins at our new position
    for i in data["gold"]:
        x_moves = abs(my_head[0] - i[0])
        y_moves = abs(my_head[1] - i[1])
        moves = x_moves + y_moves
        new_gold.append(moves)
    
    #find the new gold coin from potential position
    new_closest_gold = data["gold"][new_gold.index(min(new_gold))]

    #now we have the closest gold coords and the new closest gold coords

    num_moves_new_closest = abs(my_head[0] - new_closest_gold[0]) + abs(my_head[1] - new_closest_gold[1])

    print "original distance to closest gold:", num_moves_closest
    print "new distance to closest gold:", num_moves_new_closest

    if(num_moves_new_closest >= num_moves_closest): 
        print "bad"
        return 0
    print "good"
    return 10
