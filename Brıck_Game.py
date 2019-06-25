class Ball():
    def __init__(self, xlocation=46, xspeed=0, ylocation=30, yspeed=(-3)):
        self.xlocation = xlocation
        self.xspeed = xspeed
        self.ylocation = ylocation
        self.yspeed = yspeed
    def movement(self):
        # VERTICEL MOVEMENT
        for i in range(abs(self.yspeed)):
            if self.yspeed > 0:
                self.ylocation += 1
            else:
                self.ylocation -= 1
            # TOUCHING BRICKS
            if bricks.locations.__contains__([self.ylocation, self.xlocation]):
                bricks.locations.remove([self.ylocation, self.xlocation])
            # TOP WALL
            if self.ylocation < 1:
                self.ylocation = 1 - self.ylocation
                self.yspeed = (-1) * self.yspeed
            # BAR AND GAME OVER
            if self.ylocation > 30:
                if ((self.xlocation - bar.location) <= 6) and ((self.xlocation - bar.location)>= 0):
                    self.ylocation = 30 - (self.ylocation - 30)
                    self.yspeed = (-1) * self.yspeed
                    self.xspeed = self.xspeed + (self.xlocation -(bar.location + 3))
                if (self.xspeed > 9):
                    self.xspeed = 9
                elif self.xspeed < -9:
                    self.xspeed = -9
        #HORIZONTAL MOVEMENT
        for i in range(abs(self.xspeed)):
            if self.xspeed > 0:
                self.xlocation +=1
            else:
                self.xlocation -= 1
            # TOUCHING BRICKS
            if bricks.locations.__contains__([self.ylocation, self.xlocation]):
                bricks.locations.remove([self.ylocation, self.xlocation])
            if self.xlocation < 1:
                self.xlocation = 1 - self.xlocation
                self.xspeed = (-1)*self.xspeed
            if self.xlocation > 91:
                self.xlocation = 91 - (self.xlocation -91)
                self.xspeed = (-1)*self.xspeed





class Bar():
    def __init__(self, location=43):
        self.location = location
    def right(self):
        for i in range(3):
            if self.location == 86:
                return
            self.location += 1
    def left(self):
        for i in range(3):
            if self.location == 1:
                return
            self.location -= 1



class Bricks():
    def __init__(self):
        self.locations = [[y,x] for y in range(3,18) for x in range(11,81)]





def Screen_Maker(screen):
    rowone = []
    for i in range(93):
        rowone.append("_")
    screen.append(rowone)

    for a in range(32):
        rows = []
        for b in range(93):
            if b == 0 or b == 92:
                rows.append("|")
            elif (b== ball.xlocation and a == ball.ylocation):
                rows.append("o")
            elif (a==31 and b >= bar.location and b <= (bar.location+6)):
                rows.append("T")
            elif bricks.locations.__contains__([a,b]):
                rows.append("#")
            else:
                rows.append(" ")
        screen.append(rows)
    return screen


def visual():
    for rows in screen:
        for a in rows:
            print(a,end='')
        print(end='\n')


bricks = Bricks()
ball = Ball()
bar = Bar()
screen = []

while True:
    Screen_Maker(screen)
    visual()
    key = input()
    if key == " ": #Space is for no movement
        ball.movement()
    elif key == "a":
        bar.left()
        ball.movement()
    elif key == "d":
        bar.right()
        ball.movement()
    if ball.ylocation > 31:
        print("""
        ***********************************************
        ********* G A M E  *** O V E R ****************
        ***********************************************
        
        """)
        gameoverinp = input("If you want to start a new game press n/to quit press any key:")
        if gameoverinp == "n":
            bricks = Bricks()
            ball = Ball()
            bar = Bar()
            screen =[]
        else:
            break

