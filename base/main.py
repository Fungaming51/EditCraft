import pyglet
pyglet.options["shadow_window"] = False
pyglet.options["debug_gl"] = False
import pyglet.gl as gl

class Window(pyglet.window.Window):
    def __init__(self, **args):
        super(Window, self).__init__(**args)
        
