import raylib;
import std.stdio;

void main(){
	InitWindow(800, 600, "Edit Craft");
	SetTargetFPS(60);
	while (!WindowShouldClose()){
		BeginDrawing();
		ClearBackground(Colors.BLACK);
		//DrawText("Hello, User...", 250, 250, 28, Colors.RAYWHITE);
		
		DrawRectangle(100, 100, 100, 100, Colors.RED);
		
		EndDrawing();
	}
	CloseWindow();
}