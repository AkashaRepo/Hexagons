RoundMap = {-3:{-3:None,-2:None,-1:None,0:'.' ,1:'.' ,2:'.' ,3:'.' },
            -2:{-3:None,-2:None,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:'.' },
            -1:{-3:None,-2:'.' ,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:'.' },
             0:{-3:'.' ,-2:'.' ,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:'.' },
             1:{-3:'.' ,-2:'.' ,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:None},
             2:{-3:'.' ,-2:'.' ,-1:'.' ,0:'.' ,1:'.' ,2:None,3:None},
             3:{-3:'.' ,-2:'.' ,-1:'.' ,0:'.' ,1:None,2:None,3:None}}
def renderMap(grid, size):
    """Proof of concept"""
    for Y in range (-size, size+1):
        if Y != 0:
            for x in range (0, abs(Y)):
                print "",
        for X in range (-size, size+1):
            if grid[Y][X] != None:
                print grid[Y][X],
        print ""
#renderMap(RoundMap, 3)
