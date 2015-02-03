#include "game.h"
gameContext::gameContext()
{
	currentLevel = new hexGrid(10, 10);
	gameLoop();
}

gameContext::~gameContext()
{
	//dtor
}
void clearScreen(){
	//todo replace with curses
	#ifdef _WIN32
		system("cls");
	#else
		system("clear");
	#endif
}
void drawLine(unsigned short width=CONSOLE_WIDTH){
	for(unsigned short x=0; x<width; x++)
		printf("-");
}
void gameContext::drawScreen(){
	position startDraw;	//top left corner of map drawn on screen
	startDraw.x = 0;
	startDraw.y = 0;
	clearScreen();
	drawLine();
	position drawPos;
	//TODO make less awful
	for(drawPos.y=0; drawPos.y<DISPLAY_HEIGHT && drawPos.y+startDraw.y<currentLevel->getHeight(); drawPos.y++){
		printf("|");
		if(drawPos.y%2==0)
			printf(" ");
		for(drawPos.x=0; drawPos.x<CONSOLE_WIDTH-2 && drawPos.x+startDraw.x<currentLevel->getWidth(); drawPos.x++){
			if(drawPos + startDraw == playerPosition)
				printf(" @");
			else
				printf(" %c", currentLevel->getCell(drawPos).getSymbol());
		}
		if(drawPos.y%2==1)
			printf(" ");
		printf(" |");
		if(drawPos.x<CONSOLE_WIDTH)
			printf("\n");
	}
	drawLine();
	printf(" W E\nA @ D\n Z X\n");
}
void gameContext::acceptKeypress(){
	char input = getch();
	bool tryMove = true;
	direction dir;
	switch(input){
	case 'w':	dir = NORTH_WEST;	break;
	case 'e':	dir = NORTH_EAST;	break;
	case 'a':	dir = WEST;			break;
	case 'd':	dir = EAST;			break;
	case 'z':	dir = SOUTH_WEST;	break;
	case 'x':	dir = SOUTH_EAST;	break;
	default: tryMove = false;
	}
	if(tryMove)
	{
		position target = currentLevel->getCellNeighborPosition(playerPosition, dir);
		if(target.x >= 0 && target.x < currentLevel->getWidth() && target.y >= 0 && target.y < currentLevel->getHeight())
			playerPosition = target;
	}
}
void gameContext::gameLoop(){
	while(true)
	{
		//update screen
		drawScreen();
		//wait for input
		acceptKeypress();
	}
}
