import raylib;
import std.stdio;

void main(){
	validateRaylibBinding();
	InitWindow(800, 600, "Edit Craft");
	SetTargetFPS(60);
	while (!WindowShouldClose()){
		BeginDrawing();
		ClearBackground(Colors.BLACK);
		DrawText("Hello, User...", 400, 300, 28, Colors.RAYWHITE);
		EndDrawing();
	}
	CloseWindow();
}