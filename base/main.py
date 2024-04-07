import ctypes
import pyglet
pyglet.options["shadow_window"] = False
pyglet.options["debug_gl"] = False
import pyglet.gl as gl
import shader

vertex_positions = [ 
	-0.5,  0.5, 1.0,
	-0.5, -0.5, 1.0,
	 0.5, -0.5, 1.0,
	 0.5,  0.5, 1.0,
]

indices = [#makes a square (this is for me not for you)
    0, 1, 2, #first tri
    0, 2, 3, #second tri
    ]

class Window(pyglet.window.Window):
    def __init__(self, **args):
        super(Window, self).__init__(**args)

        #vertex array object

        self.vao = gl.GLuint(0)
        gl.glGenVertexArrays(1, ctypes.byref(self.vao))
        gl.glBindVertexArray(self.vao)

        #vertex buffer object

        self.vbo = gl.GLuint(0)
        gl.glGenBuffers(1, ctypes.byref(self.vbo))
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)

        gl.glBufferData(gl.GL_ARRAY_BUFFER,
                        ctypes.sizeof(gl.GLfloat * len(vertex_positions)),
                        (gl.GLfloat * len(vertex_positions)) (*vertex_positions),
                        gl.GL_STATIC_DRAW)

        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, 0)
        gl.glEnableVertexAttribArray(0)

        #index buffer object

        self.ibo = gl.GLuint(0)

        gl.glGenBuffers(1, self.ibo)
        gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, self.ibo)

        gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER,
                        ctypes.sizeof(gl.GLuint * len(indices)),
                        (gl.GLuint * len(indices)) (*indices),
                        gl.GL_STATIC_DRAW)

        self.shader = shader.Shader("vert.glsl", "frag.glsl")
        self.shader.use()

    def onDraw(self):
        gl.glClearColor(1.0, 0.5, 1.0, 1.0)
        self.clear()

        gl.glDrawElements(
            gl.GL_TRIANGLES,
            len(indices),
            gl.GL_UNSIGNED_INT,
            None)

    def onResize(self, width, height):
        print(f"Resize {width} * {height}")  #for testing only
        gl.glViewport(0, 0, width, hieght)

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
