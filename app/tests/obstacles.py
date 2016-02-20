WEIGHT  = 1

# Returns a positive integer that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction

def run(data, direction):
    head = [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]["coords"][0][:]
    real_head = head[:]
    if direction == "north":
        head[1] -= 1

    if direction == "south":
        head[1] += 1

    if direction == "west":
        head[0] -= 1

    if direction == "east":
        head[0] += 1

    #print "\n head " + direction
    #print head
    #print real_head
    #print "\n"

    if head[1] >= data["height"] or head[1] < 0:
        return None

    if head[0] >= data["width"] or head[0] < 0:
        return None

    bad_places = []
    ## Dont hit your own body
    bad_places += [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]["coords"][1:]
    ## Dont hit other snakes bodies
    for snake in data["snakes"]:
        ## Dont worry about the head
        bad_places += snake["coords"][1:]
    ## Dont hit a wall
    if data.get("walls") != None:
        bad_places += data["walls"]

    for place in bad_places:
        print place
        if place[0] == head[0] and place[1] == head[1]:
            return None
    return 1
