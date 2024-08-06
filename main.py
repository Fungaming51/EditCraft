import pyglet
from pyglet.gl import *
from pyglet.window import *
from pyglet.math import Mat4, Vec3
from mobs.monsters.skeleton import Skeleton
from noise import pnoise2
import numpy as np
#from pyglet.shapes import *
#import shader

batch = pyglet.graphics.Batch()
window = pyglet.window.Window(800,600,"EditCraft", resizable=True)
window.set_location(400, 200)
time = 0

# Terrian dimesions
terrain_width = 100
terrain_height = 100
scale = 10
z_scale = 5

# Generate height map using Perlin noise
def generate_height_map(width, height, scale):
    height_map = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            height_map[x][y] = pnoise2(x / scale, y / scale, octaves=6)
    return height_map

# Create vertex list from height map
def create_vertex_list(height_map, width, height, z_scale):
    vertices = []
    for x in range(width - 1):
        for y in range(height - 1):
            z = height_map[x][y] * z_scale
            vertices.extend([x, y, z])
            vertices.extend([x + 1, y, height_map[x + 1][y] * z_scale])
            vertices.extend([x + 1, y + 1, height_map[x + 1][y + 1] * z_scale])
            vertices.extend([x, y + 1, height_map[x][y + 1] * z_scale])
    return vertices
    
 # Generate terrain
height_map = generate_height_map(terrain_width, terrain_height, scale)
vertices = create_vertex_list(height_map, terrain_width, terrain_height, z_scale)

vertex_list = pyglet.graphics.vertex_list(int(len(vertices) / 3),
                                          ('v3f', vertices))

# Camera parameters
camera_x, camera_y, camera_z = terrain_width // 2, terrain_height // 2, 50
camera_pitch, camera_yaw = -60, 45


@window.event
def on_resize(width, height):
    window.viewport = (0,0, *window.get_framebuffer_size())
    window.projection = Mat4.perspective_projection(window.aspect_ratio,z_near=0.1,z_far=255)
    return pyglet.event.EVENT_HANDLED


@window.event
def on_draw():
    window.clear()
    batch.draw()
    glLoadIdentity()
    glTranslatef(-camera_x, -camera_y, -camera_z)
    glRotatef(camera_pitch, 1, 0, 0)
    glRotatef(camera_yaw, 0, 1, 0)
    vertex_list.draw(GL_QUADS)


if __name__ == '__main__':
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    #model_knife = pyglet.model.load("Knife.obj", batch=batch)
    Skeleton.skeleton
    window.view = Mat4.look_at(position=Vec3(0,0,5), target=Vec3(0,0,0), up=Vec3(0,1,0))
    pyglet.app.run()