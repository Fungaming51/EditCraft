import pyglet
pyglet.options["shadow_window"] = False
pyglet.options["debug_gl"] = False
import pyglet.gl as gl

class Window(pyglet.window.Window):
    def __init__(self, **args):
        super(Window, self).__init__(**args)

    def onDraw(self):
        gl.glClearColor(1.0, 0.5, 1.0, 1.0)
        self.clear()

    def onResize(self, width, height):
        print(f"Resize {width} * {height}")  #for testing only

#the width & height didn't print, changing it not being hard coded didn't work
#it did something weird though, went off center.
#tried a different method, it didn't work
class Game:
    def __init__(self):
        self.config = gl.Config(major_version = 3)
        self.window = Window(config = self.config, width = 800, height = 600, caption = "EditCraft", resizable = True, vsync = False)

    def run(self):
        pyglet.app.run()

if __name__ == "__main__":
    game = Game()
    game.run()
