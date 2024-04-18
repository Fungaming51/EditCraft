import pyglet
from pyglet.gl import *
from pyglet.window import *
from pyglet.shapes import *
import shader

window = pyglet.window.Window(800,600,"EditCraft")
window.set_location(400, 200)


@window.event
def on_draw():
    window.clear()
if __name__ == '__main__':
    pyglet.app.run()