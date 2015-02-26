RoundMap = {-3:{-3:None,-2:None,-1:None,0:'.' ,1:'.' ,2:'.' ,3:'.' },
            -2:{-3:None,-2:None,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:'.' },
            -1:{-3:None,-2:'.' ,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:'.' },
             0:{-3:'.' ,-2:'.' ,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:'.' },
             1:{-3:'.' ,-2:'.' ,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:None},
             2:{-3:'.' ,-2:'.' ,-1:'.' ,0:'.' ,1:'.' ,2:None,3:None},
             3:{-3:'.' ,-2:'.' ,-1:'.' ,0:'.' ,1:None,2:None,3:None}}

OtherMap = {0:{0:None,1:None,2:None,3:'A' ,4:'1' ,5:'1' ,6:'B' },
            1:{0:None,1:None,2:'A' ,3:'2' ,4:'2' ,5:'2' ,6:'B' },
            2:{0:None,1:'A' ,2:'3' ,3:'3' ,4:'3' ,5:'3' ,6:'B' },
            3:{0:'A' ,1:'4' ,2:'4' ,3:'4' ,4:'4' ,5:'4' ,6:'B' },
            4:{0:'A' ,1:'5' ,2:'5' ,3:'5' ,4:'5' ,5:'B' ,6:None},
            5:{0:'A' ,1:'6' ,2:'6' ,3:'6' ,4:'B' ,5:None,6:None},
            6:{0:'A' ,1:'7' ,2:'7' ,3:'B' ,4:None,5:None,6:None}}

#print RoundMap
SquareMap = {0:{-2:None,-1:None,0:'.' ,1:'.' ,2:'.' ,3:'.' ,4:'.' ,5:'.' },
             1:{-2:None,-1:None,0:'.' ,1:'.' ,2:'.' ,3:'.' ,4:'.' ,5:'.' },
             2:{-2:None,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:'.' ,4:'.' ,5:None},
             3:{-2:None,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:'.' ,4:'.' ,5:None},
             4:{-2:'.' ,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:'.' ,4:None,5:None},
             5:{-2:'.' ,-1:'.' ,0:'.' ,1:'.' ,2:'.' ,3:'.' ,4:None,5:None}}
#print SquareMap

def renderMap(grid, size):
    """Renders a hexagonal map, will be part of the map class which also creates and stores the map."""
    for Y in range (-size, size+1):
        if Y != 0:
            for x in range (0, abs(Y)):
                print "",
        for X in range (-size, size+1):
            if grid[Y][X] != None:
                print grid[Y][X],
        print ""
renderMap(RoundMap, 3)
