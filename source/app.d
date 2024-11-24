import raylib;
import std.stdio;

void main(){
	InitWindow(800, 600, "Edit Craft");
	
	Texture2D texture = LoadTexture("player_sprite.png");
	
	SetTargetFPS(60);
	while (!WindowShouldClose()){
		BeginDrawing();
		ClearBackground(Colors.BLACK);
		//DrawText("Hello, User...", 250, 250, 28, Colors.RAYWHITE);
		
		//DrawRectangle(100, 100, 100, 100, Colors.RED);
		
		DrawTexture(texture, 100, 400, Colors.WHITE);
		
		EndDrawing();
	}
	
	//UnloadTexture();
	
	CloseWindow();
}