from pyglet.gl import *
#glEnable(texture.target)

batch = pyglet.graphics.Batch()

class Skeleton(batch=batch):
    torso = pyglet.model.load(r"C:\Users\SHANT\Desktop\f\programing\projects\EditCraft\mobs\monsters\skeleton\torso.obj", batch=batch)
