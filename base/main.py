import pyglet
from pyglet.gl import *
from pyglet.window import *
#from pyglet.shapes import *
#import shader

batch = pyglet.graphics.Batch()
window = pyglet.window.Window(800,600,"EditCraft")
window.set_location(400, 200)


@window.event
def on_draw():
    window.clear()
    batch.draw()


if __name__ == '__main__':
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    model = pyglet.model.load("Knife.obj", batch=batch)
    pyglet.app.run()