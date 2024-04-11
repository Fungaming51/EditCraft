import pyglet
from pyglet.gl import *
from pyglet.window import *

window = pyglet.window.Window(800,600,"EditCraft")

#controls
def on_key_press(symbol, modifiers):
    pass

def on_mouse_press(x, y, button, modifiers):
    pass

@window.event
def on_draw():
   # print("Hello")
   glBegin(GL_LINES)
   glVertex3f(100.0,100.0,0.25)
   glVertex3f(200.0,300.0,-0.75)
   glEnd()
pyglet.app.run()