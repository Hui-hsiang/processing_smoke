class air:
    def __init__(self):
        self.smokes = list()
        self.airmap = [[0] * 500 for n in range(800)]
    
    def drawsmoke(self):
        for s in self.smokes:
            s.drawsmoke()
    
    def smokemove(self):
        for s in self.smokes:
            x = s.px
            y = s.py
            if x<10 or y<10 or x>=789 or y>=489:
                self.smokes.remove(s)
                continue
            table = [self.airmap[x-1][y-1],self.airmap[x][y-1],self.airmap[x+1][y-1],
                 self.airmap[x-1][y],self.airmap[x][y],self.airmap[x+1][y],
                 self.airmap[x-1][y+1],self.airmap[x-1][y-1],self.airmap[x+1][y+1]] 
            move = ['ul','uc','ur',
                    'l','c','r',
                    'dl','dc','dr']
        
            for i in range(9):
                for j in range(8):
                    if table [j] > table[j+1]:
                        t = table[j]
                        table[j] = table[j+1]
                        table[j+1] = t
                        t = move[j]
                        move[j] = move[j+1]
                        move[j+1] = t
            
            rdm = 0
            for i in table:
                if i == table[0]:
                    rdm += 1
                else:
                    break
            
            rdm = random(rdm)
            rdm = int(rdm)
            dir = move[rdm]
            
            self.airmap[x][y] -= 1
            s.px += int(random(-5,5))
            s.py += int(random(-5,5))
            self.airmap[s.px][s.py] += 1            
            s.dnsity -= 0.01
            if s.dnsity <= 0:
                self.smokes.remove(s)


class smoke:
    def __init__(self,px,py,c):
        self.px = px
        self.py = py
        self.c = c
        self.dnsity = 100
    def drawsmoke(self):
        self.c[3] *= self.dnsity / 100
        
        fill(color(self.c[0],self.c[1],self.c[2],self.c[3]))
        circle(self.px,self.py,2)
        

a = air()

def setup():
    size(800,500)
    print("HI")
    

def draw():
    background(0)
    noStroke()
    a.smokemove()
    a.drawsmoke()
#    print (mouseX,mouseY)
    if mousePressed:
        if mouseX < 800 and mouseY < 500:
            for i in range(1):
                colorMode(RGB,100)
                pen = [random(0,255),random(0,255),random(0,255),100]
                
                s = smoke(mouseX,mouseY,pen)
                a.smokes.append(s)
                a.airmap[mouseX][mouseY] += 1

        
