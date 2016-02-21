WEIGHT  = 1

# Returns a positive integer that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction

def run(data, direction):
    head = [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]["coords"][0][:]
    next_loc = move(direction, head)
    # if not is_clear(data, next_loc):
    #     return None
    if not left_or_right_clear(data, direction, next_loc):
        return None
    return 0.0

# prevent moving through a one space wide opening
def left_or_right_clear(data, direction, loc):
    if direction in ['north','south']: # if moving north/south, check east and west coords
        return is_clear(data, [loc[0]-1, loc[1]]) or is_clear(data, [loc[0]+1, loc[1]])
    elif direction in ['west','east']: # if moving east/west, check north and south coords
        return is_clear(data, [loc[0], loc[1]-1]) or is_clear(data, [loc[0], loc[1]+1])
    else:
        raise

def is_clear(data, loc):
    if data.get("walls") != None:
        return loc not in data['walls'] and not is_snake_body(data, loc)
    else:
        return True

def is_snake_body(data, loc):
    snake_bodies = [snake["coords"][1:] for snake in data["snakes"]]
    coords = []
    for body in snake_bodies:
        for coord in body:
            coords.append(coord)
    return loc in coords

def move(direction, current):
    move =  {
                'north': [current[0], current[1] - 1],
                'south': [current[0], current[1] + 1],
                'west': [current[0] - 1, current[1]],
                'east': [current[0] + 1, current[1]]
            }
    return move[direction]

