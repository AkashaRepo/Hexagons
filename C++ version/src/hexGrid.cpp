#include "hexGrid.h"
position operator+(const position& p1, const position& p2)
{
	position out;
	out.x = p1.x + p2.x;
	out.y = p1.y + p2.y;
	return out;
}
bool operator==(const position& p1, const position& p2)
{
	if(p1.x==p2.x && p1.y == p2.y)
		return true;
	return false;
}
hexGrid::hexGrid(unsigned short w, unsigned short h)
{
	cells = new cell [w*h];
	width = w;
	height = h;
}
hexGrid::~hexGrid()
{
	delete cells;
}
cell* hexGrid::getCellP(position pos)
{
	if(pos.x<width && pos.y<height)
		return (cells+(pos.y*width + pos.x));
	return NULL;
}
cell hexGrid::getCell(position pos)
{
	return *getCellP(pos);
}
void hexGrid::setCell(position pos, const cell& c)
{
	*getCellP(pos) = c;
}
position hexGrid::getCellNeighborPosition(position pos, direction dir)
{
	switch(dir){
	case NORTH_EAST:
		if(pos.y%2==0)
			pos.x++;
		pos.y--;
		break;
	case EAST:
		pos.x++;
		break;
	case SOUTH_EAST:
		if(pos.y%2==0)
			pos.x++;
		pos.y++;
		break;
	case NORTH_WEST:
		if(pos.y%2==1)
			pos.x--;
		pos.y--;
		break;
	case WEST:
		pos.x--;
		break;
	case SOUTH_WEST:
		if(pos.y%2==1)
			pos.x--;
		pos.y++;
		break;
	}
	return pos;
}
