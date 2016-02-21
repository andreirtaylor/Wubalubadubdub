WEIGHT  = 15

# Returns a positive integer that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction

def possible_moves(head, seen, data, bad_places):
    if head[1] >= data["height"] or head[1] < 0:
        return 0

    if head[0] >= data["width"] or head[0] < 0:
        return 0

    for place in bad_places:
        if place[0] == head[0] and place[1] == head[1]:
            return 0

    head = list(head)
    head_arr = head[:]
    head[1] -= 1
    head = tuple(head)

    if head in seen.keys():
        return 0

    seen[head] = True

    moves_north = possible_moves(head, seen, data, bad_places)
    head = head_arr[:]
    head[1] += 1
    head = tuple(head)
    moves_south = possible_moves(head, seen, data, bad_places)
    head = head_arr[:]
    head[0] -= 1
    head = tuple(head)
    moves_west = possible_moves(head, seen, data, bad_places)
    head = head_arr[:]
    head[0] += 1
    head = tuple(head)
    moves_east = possible_moves(head, seen, data, bad_places)
    return moves_east + moves_west + moves_south + moves_north + 1

def run(data, direction):
    head = [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]["coords"][0][:]
    if direction == "north":
        head[1] -= 1

    if direction == "south":
        head[1] += 1

    if direction == "west":
        head[0] -= 1

    if direction == "east":
        head[0] += 1

    bad_places = []
    ## Dont hit your own body
    bad_places += [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]["coords"][1:]
    ## Dont hit other snakes bodies
    for snake in data["snakes"]:
        ## Dont worry about the head
        bad_places += snake["coords"]
    ## Dont hit a wall
    if data.get("walls") != None:
        bad_places += data["walls"]

    return float(possible_moves(head, {tuple(head): True}, data, bad_places)) / float((data["height"] * data["width"] - len(bad_places)))
