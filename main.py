import pyglet
from pyglet.gl import *
from pyglet.window import *
from pyglet.math import Mat4, Vec3
from mobs.monsters.skeleton import Skeleton
#from pyglet.shapes import *
#import shader

batch = pyglet.graphics.Batch()
window = pyglet.window.Window(800,600,"EditCraft", resizable=True)
window.set_location(400, 200)
time = 0

@window.event
def on_resize(width, height):
    window.viewport = (0,0, *window.get_framebuffer_size())
    window.projection = Mat4.perspective_projection(window.aspect_ratio,z_near=0.1,z_far=255)
    return pyglet.event.EVENT_HANDLED


@window.event
def on_draw():
    window.clear()
    batch.draw()


if __name__ == '__main__':
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    #model_knife = pyglet.model.load("Knife.obj", batch=batch)
    Skeleton.skeleton
    window.view = Mat4.look_at(position=Vec3(0,0,5), target=Vec3(0,0,0), up=Vec3(0,1,0))
    pyglet.app.run()