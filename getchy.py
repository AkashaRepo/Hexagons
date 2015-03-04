import sys, tty, termios

def getch():
    """An implementation of getch() for python. Modified from, 
    http://www.raspberrypi.org/forums/viewtopic.php?t=69046
    I don't understand most of it but it seems to work."""
    fd = sys.stdin.fileno()                                 #voodoo
    old_settings = termios.tcgetattr(fd)                    #saves term settings
    tty.setraw(sys.stdin.fileno())                          #voodoo
    keypress = sys.stdin.read(1)                            #gets the keypress
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  #resets the settings
    return keypress                                         #returns the key pressed

print "Press any key to continue"
ch = getch()
print 'you pressed the "%s" key!' %(ch)
