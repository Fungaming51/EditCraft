import std.stdio;
import derelict.opengl;

void main(){
	DerelictGL3.load();
	
	myCreateContext();
	
	DerelictGL3.reload();
	
	writeln("Edit source/app.d to start your project.");
}
