#ifndef HEXGRID_H
#define HEXGRID_H
#include <cstdio>
struct position{
	short x, y;
};
position operator+(const position& p1, const position& p2);
bool operator==(const position& p1, const position& p2);
enum direction{NORTH_EAST=0, EAST=1, SOUTH_EAST=2, SOUTH_WEST=3, WEST=4, NORTH_WEST=5};
class cell
{
public:
	char getSymbol(){ return ascii; }
private:
	char ascii = '.';
};

class hexGrid
{
public:
	hexGrid(unsigned short width, unsigned short height);
	~hexGrid();
	cell getCell(position pos);
	position getCellNeighborPosition(position pos, direction dir);
	void setCell(position pos, const cell& c);
	unsigned short getWidth() {return width; }
	unsigned short getHeight() {return height; }
private:
	cell* getCellP(position pos);
	cell* cells = NULL;
	unsigned short width, height;
};

#endif // HEXGRID_H
