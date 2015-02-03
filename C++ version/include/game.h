#ifndef game_H
#define game_H
#include "hexGrid.h"
#include <stdlib.h>
#include <conio.h>
#define CONSOLE_WIDTH 80
#define DISPLAY_HEIGHT 10	//does NOT include borders
class gameContext
{
	public:
		gameContext();
		~gameContext();
	private:
		void gameLoop();
		void drawScreen();
		void acceptKeypress();
		position playerPosition = {0, 0};
		hexGrid *currentLevel=NULL;

};

#endif // game_H
