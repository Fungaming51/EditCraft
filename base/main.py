import pyglet
from pyglet.gl import *
from pyglet.window import *
from pyglet.shapes import *

window = pyglet.window.Window(800,600,"EditCraft")



class Player:
    def __init__(self, pos=(0,0,0), rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)
    def on_key_press():
        pass

    def on_mouse_press(self, dx, dy):
        dx/= 8
        dy/= 8
        self.rot[0] += dy
        self.rot[1] -= dx
        if self.rot[0] > 90:
            self.rot[0] = 90
        elif self.rot[0] < -90:
            self.rot[0] = -90



@window.event
def on_draw(self):
    pass
   # print("Hello")
   #self.clear()
   #self.set3d()
   #self.push(self.Player.pos, self.Player.rot)
   #self.model.draw()
   #glPopMatrix()
if __name__ == '__main__':
    pyglet.app.run()