import sys, tty, termios

class HexMap(object):
    """A hexagonal map."""
    def __init__(self, radius, symbol):
        """Creates a new map with the specified radius and blank tile symbol."""
        self.rad = radius
        self.blank = symbol
        self.grid = {}
        for Y in range (-self.rad, self.rad+1):       #populates the dictonary with empty rows.
            self.grid[Y] = {}
        for Y in range (-self.rad, self.rad+1):       #populates the rows.
            for X in range (-self.rad, self.rad+1):
                if Y < 0 and X < -self.rad + abs(Y):  #top padding
                    self.grid[Y][X] = None
                elif Y > 0 and X > self.rad - abs(Y): #bottom padding
                    self.grid[Y][X] = None
                else:                                 #places the actual cells.
                    self.grid[Y][X] = HexCell(self,Y,X,self.blank) 
        self.renderMap()
    def renderMap(self):
        """Renders a the map, should be called whenever the map updates."""
        print ""
        for Y in range (-self.rad, self.rad+1):
            if Y != 0:
                for x in range (0, abs(Y)):
                    print "",
            for X in range (-self.rad, self.rad+1):
                if self.grid[Y][X] != None:
                    print self.grid[Y][X].draw(),
            print ""
    def eraseCell(self, Y, X):
        """Calls the erase method on the HexCell object at the specified cords."""
        self.grid[Y][X].erase()
    def placeSymbol(self, Y, X, symbol):
        """Calls the drawSymbol method on the HexCell object at the specified cords."""
        self.grid[Y][X].drawSymbol(symbol)
        self.renderMap()
    def getRad(self):
        return self.rad

class HexCell(object):
    """A cell on a hexagonal map"""
    def __init__(self,location,Y,X,symbol):
        """Creates a new map tile with a specified X,Y value and blank symbol."""
        self.grid = location
        self.Y = Y
        self.X = X
        self.blank = symbol
        self.contents = None
    def draw(self):
        """returns the contents of a cell, or a blank tile if none exist."""
        if self.contents == None:
            return self.blank
        else:
            return self.contents
    def drawSymbol(self, symbol):
        """adds a symbol to the cell"""
        self.contents = symbol
    def erase(self):
        """removes the cell's contents"""
        self.contents = None
    def isOccupied(self):
        if self.contents == None:
            return False
        else:
            return True
    
class actor(object):
    """a character on the map"""
    def __init__(self, location, Y, X, symbol):
        self.grid = location
        self.Y = Y
        self.X = X
        self.icon = symbol
        self.grid.placeSymbol(self.Y,self.X,self.icon)
    def step(self, direction):
        neighbors = {'w':(self.Y-1,self.X),
                     'e':(self.Y-1,self.X+1),
                     'a':(self.Y,self.X-1),
                     'd':(self.Y,self.X+1),
                     'z':(self.Y+1,self.X-1),
                     'x':(self.Y+1,self.X)}
        Y = neighbors[direction][0]
        X = neighbors[direction][1]
        if X > self.grid.getRad() or X < -self.grid.getRad():
            pass
        elif Y > self.grid.getRad() or Y < -self.grid.getRad():
            pass
        elif self.grid.grid[Y][X].isOccupied():
            pass
        else:
            return self.moveTo(Y,X)
    def moveTo(self, Y, X):
        self.grid.eraseCell(self.Y,self.X)
        self.Y = Y
        self.X = X
        self.grid.placeSymbol(Y,X,self.icon)

def getch():
    """Waits for a single keypress from the user.
    I don't understand most of it but it seems to work."""
    fd = sys.stdin.fileno()                                #saves settings
    old_settings = termios.tcgetattr(fd)                   #saves settings
    tty.setraw(sys.stdin.fileno())                         #voodoo
    keypress = sys.stdin.read(1)                           #gets the keypress
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) #resets settings
    return keypress                                        #returns the key pressed


theMap = HexMap(11,'.')
thePlayer = actor(theMap, 0,0,'@')
aWall = actor(theMap,0,1,'#')

game = True
while game == True:
    key = getch()
    
    if key in ['w','e','a','d','z','x']:
        thePlayer.step(key)
    elif key == 'q':
        game = False
    elif key == 's':
        thePlayer.moveTo(0,0)
    else:
        pass
