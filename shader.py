from pyglet.graphics.shader import Shader, ShaderProgram
import pyglet

vertex_source = """#version 330
    layout(location = 0) in vec2 vertices;
    layout(location = 1) in vec4 colors;
    out vec4 newColor;

    uniform mat4 projection;

    void main()
    {
        gl_Position = vec4(vertices, 0.0f, 1.0f);
        newColor = colors;
    }
"""

fragment_source = """#version 330
    in vec4 newColor;
    out vec4 outColor;

    void main()
    {
        outColor = newColor;
    }
"""

vert_shader = Shader(vertex_source, 'vertex')
frag_shader = Shader(fragment_source, 'fragment')
program = ShaderProgram(vert_shader, frag_shader)

