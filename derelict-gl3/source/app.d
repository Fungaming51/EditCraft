import std.stdio;
import derelict.opengl;
import derelict.glfw3;


void main(){
	DerelictGLFW3.load();
	DerelictGL3.load();
	
	if (!glfwInit()){
		writeln("Failed to initialized GLFW...");
		return;
	}
	
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
	
	auto window = glfwCreateWindow(800, 600, "Edit Craft", null, null);
	
	if (window is null){
		writeln("Failed to create GLFW window...");
		glfwTerminate();
		return;
	}
	
	glfwMakeContextCurrent(window);
	DerelictGL3.reload();
	//main loop
	while (!glfwWindowShouldClose(window)){
		glClearColor(0.1f, 0.2f, 0.3f, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT);
		
		glfwSwapBuffers(window);
		glfwPollEvents();
	}
	glfwDestroyWindow(window);
	glfwTerminate();
}
