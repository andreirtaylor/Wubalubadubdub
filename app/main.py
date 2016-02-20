import bottle
from bottle import run
import os
import snake


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    return {
        'color': snake.color(),
        'head': snake.head(bottle)
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    return {
        'taunt': snake.taunt(data)
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'move': snake.get_move(data),
        'taunt': snake.taunt(data)
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': snake.taunt(data)
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'), reloader=True)

