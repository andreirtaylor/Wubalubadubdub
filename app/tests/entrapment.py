def run(data, direction):
    head = head(data)
    next_loc = move(direction, head)
    if not is_clear(next_loc):
        return None
    if not left_or_right_clear(data, direction, next_loc):
        return None
    return 0.0


def left_or_right_clear(data, direction, loc):
    if direction in ['up','down']:
        return is_clear(data, [loc[0]-1, loc[1]]) or is_clear(data, [loc[0]+1, loc[1]])
    elif direction in ['left','right']:
        return is_clear(data, [loc[0], loc[1]-1]) or is_clear(data, [loc[0], loc[1]+1])
    else:
        raise

def is_clear(data, loc):
    return loc not in data['walls'] and not is_snake_body(data, loc)

def is_snake_body(data, loc):
    snake_bodies = [snake["coords"][1:] for snake in data["snakes"]]
    coords = []
    for body in snake_bodies:
        for coord in body:
            coords.append(coord)
    return loc in coords

def head(data):
    return [s for s in data["snakes"] if s["id"] == data["our-snake-id"]][0]["coords"][0]

def move(direction, current):
    move =  {
                'up': [current[0], current[1] - 1],
                'down': [current[0], current[1] + 1],
                'left': [current[0] - 1, current[1]],
                'right': [current[0] + 1, current[1]]
            }
    return move[direction]

