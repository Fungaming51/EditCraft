import raylib;
import std.stdio;

void main(){
	InitWindow(800, 600, "Edit Craft");
	SetTargetFPS(60);
	while (!WindowShouldClose()){
		BeginDrawing();
		ClearBackground(Colors.RAYWHITE);
		DrawText("Hello, User...", 400, 300, 28, Colors.BLACK);
		EndDrawing();
	}
	CloseWindow();
}