WEIGHT  = 10

# Returns a positive integer that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction
def run(data, direction):
    # setup gold holder and my_head
    gold = []
    my_head = [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]["coords"][0]

    print(my_head)
    
    #find current closest based on number of moves
    for i in data["gold"]:
        x_moves = abs(my_head[0] - i[0])
        y_moves = abs(my_head[1] - i[1])
        moves = x_moves + y_moves
        gold.append(moves)

    closest_gold = data["gold"][gold.index(min(gold))]
    
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
     
    gold = []
    #build an array of number of moves to get to gold coins at our new position
    for i in data["gold"]:
        x_moves = abs(my_head[0] - i[0])
        y_moves = abs(my_head[1] - i[1])
        moves = x_moves + y_moves
        gold.append(moves)
    
    #find the new gold coin from potential position
    new_closest_gold = data["gold"][gold.index(min(gold))]

    print("old closest gold: " + closest gold)
    print("new closest gold: " + new_closest_gold)

    if(new_closest_gold > closest_gold): return 0.5
    if(new_closest_gold < closest_gold): return 1


   
    
