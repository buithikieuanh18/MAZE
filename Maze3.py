from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os 
import random
import tkinter as tk
import tkinter.font as tkFont
import time
from pygame.locals import *
import pygame, sys
import pgzrun
import json
base = Tk()
base.title('Maze game')
base.geometry("300x500")
help=0

CARIMG = pygame.image.load('nhanvat7.png')
PINK = (127,127,127)
def play():
    

    X_MARGIN = 0
    LANEWIDTH = 60

    CARWIDTH = 40
    CARHEIGHT = 60
    CARSPEED = 3


    BGSPEED = 1.5
    BGIMG = pygame.image.load('background.png')

    pygame.init()
    length = 7
    S = 65
    FPS = 60
    fpsClock = pygame.time.Clock()
    WIDTH = (length+1)*S
    HEIGHT = (length+1)*S
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('RACING')

    
    class Background():
        def __init__(self):
            self.x = 0
            self.y = 0
            self.img = BGIMG

        def draw(self):
            
            WHITE = (255, 255, 255)
            YELLOW = (255, 255, 0)
            WHITE_CHECK = (255, 255, 255, 255)

           
            pygame.init()
            pygame.mixer.init()
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Python Maze Generator")
            clock = pygame.time.Clock()

           
            x = 0 
            y = 0  
            w = S 
            grid = []
            visited = []
            stack = []
            solution = {}

           
            def build_grid(x, y, w):
                for i in range(1, length):
                    x = S 
                    y = y + S
                    for j in range(1, length):
                        pygame.draw.line(screen, WHITE, [x, y], [x + w, y])
                        pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w]) 
                        pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])  
                        pygame.draw.line(screen, WHITE, [x, y + w], [x, y]) 
                        grid.append((x, y))
                        x = x + S 

            def push_up(x, y):
                pygame.draw.rect(screen, PINK, (x + 1, y - w + 1, S - 3, S + 17),
                                0)
                pygame.display.update()

            def push_down(x, y):
                pygame.draw.rect(screen, PINK, (x + 1, y + 1, S - 3, S + 17), 0)
                pygame.display.update()

            def push_left(x, y):
                pygame.draw.rect(screen, PINK, (x - w + 1, y + 1, S + 17, S - 3), 0)
                pygame.display.update()

            def push_right(x, y):
                pygame.draw.rect(screen, PINK, (x + 1, y + 1, S + 17, S - 3), 0)
                pygame.display.update()

            def backtracking_cell(x, y):
                pygame.draw.rect(screen, PINK, (x + 1, y + 1, S - 2, S - 2),
                                0)  

                pygame.display.update()  

            def solution_cell(x, y):
                pygame.draw.rect(screen, YELLOW, (x + (S / 2 - 4), y + (S / 2 - 4), 5, 5), 0) 
                pygame.display.update()  

            def carve_out_maze(x, y):
                stack.append((x, y))  
                visited.append((x, y)) 
                while len(stack) > 0:  
                    time.sleep(0) 
                    cell = []  
                    if (x + w, y) not in visited and (x + w, y) in grid:  
                        cell.append("right") 

                    if (x - w, y) not in visited and (x - w, y) in grid: 
                        cell.append("left")

                    if (x, y + w) not in visited and (x, y + w) in grid:  
                        cell.append("down")

                    if (x, y - w) not in visited and (x, y - w) in grid:
                        cell.append("up")

                    if len(cell) > 0: 
                        cell_chosen = (random.choice(cell)) 
                        if cell_chosen == "right": 
                            push_right(x, y) 
                            solution[(x + w, y)] = x, y 
                            x = x + w
                            visited.append((x, y))
                            stack.append((x, y))

                        elif cell_chosen == "left":
                            push_left(x, y)
                            solution[(x - w, y)] = x, y
                            x = x - w
                            visited.append((x, y))
                            stack.append((x, y))
                        # a[int(x/20)-1][int(y/20)]=1

                        elif cell_chosen == "down":
                            push_down(x, y)
                            solution[(x, y + w)] = x, y
                            y = y + w
                            visited.append((x, y))
                            stack.append((x, y))
                           
                        elif cell_chosen == "up":
                            push_up(x, y)
                            solution[(x, y - w)] = x, y
                            y = y - w
                            visited.append((x, y))
                            stack.append((x, y))
                           
                    else:
                        x, y = stack.pop()  
                        backtracking_cell(x, y)

            def plot_route_back(x, y):
                solution_cell(x, y) 
                while (x, y) != (S, S): 
                    x, y = solution[x, y] 
                    solution_cell(x, y)
                    time.sleep(.01)

            def plot_route_back2(x, y):
                solution_cell(x, y) 
                while (x, y) != ((length - 1) * S, (length - 1) * S): 
                    x, y = solution[x, y]
                    solution_cell(x, y) 
                    time.sleep(.01)

            x, y = S, S  
            build_grid(40, 0, S)  
            carve_out_maze(x, y) 
            if(help==1):
                plot_route_back((length - 1) * S, (length - 1) * S)

    class Car():
        def __init__(self):
            self.width = CARWIDTH
            self.height = CARHEIGHT
            self.x = 77
            self.y = 70
            self.speed = CARSPEED
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill((255, 255, 255))

        def draw(self):
            pygame.draw.rect(DISPLAYSURF, PINK, (self.x, self.y, 31, 50), 0)
            DISPLAYSURF.blit(CARIMG, (int(self.x), int(self.y)))


        def update(self, moveLeft, moveRight, moveUp, moveDown):
            if moveLeft == True:
                check = True
                for i in range(50):
                    if DISPLAYSURF.get_at((self.x - 1, self.y + i)) == (255, 255, 255, 255) \
                            or DISPLAYSURF.get_at((self.x - 2, self.y + i)) == (255, 255, 255, 255) \
                            or DISPLAYSURF.get_at((self.x - 3, self.y + i)) == (255, 255, 255, 255):
                        check = False
                        break
                if check is True:
                    self.x -= self.speed
            if moveRight == True:
                check = True
                for i in range(50):
                    if DISPLAYSURF.get_at((self.x + 30, self.y + i)) == (255, 255, 255, 255) \
                            or DISPLAYSURF.get_at((self.x + 31, self.y + i)) == (255, 255, 255, 255) \
                            or DISPLAYSURF.get_at((self.x + 32, self.y + i)) == (255, 255, 255, 255) \
                            or DISPLAYSURF.get_at((self.x + 33, self.y + i)) == (255, 255, 255, 255)\
                            or DISPLAYSURF.get_at((self.x + 34, self.y + i)) == (255, 255, 255, 255):
                        check = False
                        break
                if check is True:
                    self.x += self.speed
            if moveUp == True:
                check = True
                for i in range(30):
                    if DISPLAYSURF.get_at((self.x + i, self.y - 1)) == (255, 255, 255, 255) \
                            or DISPLAYSURF.get_at((self.x + i, self.y - 2)) == (255, 255, 255, 255) \
                            or DISPLAYSURF.get_at((self.x + i, self.y - 3)) == (255, 255, 255, 255):
                        check = False
                        break
                if check is True:
                    
                    self.y -= self.speed
            if moveDown == True:
                check = True
                for i in range(30):
                    if DISPLAYSURF.get_at((self.x + i, self.y + 50)) == (255, 255, 255, 255) \
                            or DISPLAYSURF.get_at((self.x + i, self.y + 51)) == (255, 255, 255, 255) \
                            or DISPLAYSURF.get_at((self.x + i, self.y + 52)) == (255, 255, 255, 255) \
                            or DISPLAYSURF.get_at((self.x + i, self.y + 53)) == (255, 255, 255, 255) \
                            or DISPLAYSURF.get_at((self.x + i, self.y + 54)) == (255, 255, 255, 255):
                        check = False
                        break
                if check is True:
                    self.y += self.speed
            if self.x < X_MARGIN:
                self.x = X_MARGIN
            if self.x + self.width > WIDTH:
                self.x = WIDTH - self.width
            if self.y < 0:
                self.y = 0
            if self.y + self.height > HEIGHT:
                self.y = HEIGHT - self.height


    def rectCollision(rect1):
        if rect1[0] >= S*(length-1) and rect1[1] >= S*(length-1):
            return True
        return False


    def isGameover(car):
        carRect = [car.x, car.y, car.width, car.height]
        if rectCollision(carRect) == True:
            return True

        return False
        

    def gamePlay(bg, car):
        car.__init__()
        bg.__init__()
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        CARIMG = pygame.image.load('nhanvat2.png')
                        moveLeft = True
                    if event.key == K_RIGHT:
                        moveRight = True
                    if event.key == K_UP:
                        moveUp = True
                    if event.key == K_DOWN:
                        moveDown = True
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        moveLeft = False
                    if event.key == K_RIGHT:
                        moveRight = False
                    if event.key == K_UP:
                        moveUp = False
                    if event.key == K_DOWN:
                        moveDown = False
                    
            if isGameover(car):
                return
            car.draw()
            car.update(moveLeft, moveRight, moveUp, moveDown)
            pygame.display.update()
            fpsClock.tick(FPS)


    def gameOver(bg, car):
        font = pygame.font.SysFont('consolas', 60)
        headingSuface = font.render('YOU WIN', True, (255, 0, 0))
        headingSize = headingSuface.get_size()

        font = pygame.font.SysFont('consolas', 20)
        commentSuface = font.render('Press "space" to next lever', True, (255, 0, 0))
        commentSize = commentSuface.get_size()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == K_SPACE:
                        pygame.quit()
				        
                        

            DISPLAYSURF.blit(headingSuface, (int((WIDTH - headingSize[0]) / 2), 100))
            DISPLAYSURF.blit(commentSuface, (int((WIDTH - commentSize[0]) / 2), 300))
            pygame.display.update()
            fpsClock.tick(FPS)
        # bg.draw()
        # car.draw()
    

    bg = Background()
    bg.draw()    
    car = Car()
    # ld=pygame.transform.scale(pygame.image.load('coin.png'),(20,20))
    # for i in range(5):
    #     a=random.randint(85,WIDTH-88)
    #     b=random.randint(85,HEIGHT-88)
    #     DISPLAYSURF.blit(ld,(a,b))

    pygame.display.flip()
    while True:    
        gamePlay(bg, car)   
        gameOver(bg, car)  
lb3=Label(width=10,height=2,text='Name:Lươn',font=("Consolas",14,"bold"))
lb3.pack()
img=ImageTk.PhotoImage(Image.open ("luudanh.jpg"))
lab=Label(image=img,width=300,height=200)
lab.pack()
lb1=Label(width=10,height=1,text='Màn:3',font=("Consolas",14,"bold"))
lb1.pack()
lb2=Label(width=10,height=1,text="vàng:1000",font=("Consolas",14,"bold"))
lb2.pack()
btn=Button(base,text="Play",bg="Yellow",fg="orange",font=("Consolas",14,"bold"),width=12,height=1,border=4,command=play)
btn.pack()
la=Label(width=1,height=1)
la.pack()
def buy():
    ld = Tk()
    bg=1
    figure=1
    ld.title('Maze game')
    ld.geometry("300x500")
    score=0
    lever=5
    def push(a,b,c,d):
        data={}
        data['users']=[]
        data['users'].append({"figure":a,"bg":b,"score":c,"lever":d})
        with open('maze.json','w') as f:
            json.dump(data,f)
    def pull():
        data1=""
        with open('maze.json','r') as file:
            data1=json.load(file)
        data2=data1['users']
        data3=data2[0]
        array=[]
        array.append(data3['figure'])
        array.append(data3['bg'])
        array.append(data3['score'])
        array.append(data3['lever'])
        return array

    def background1():
        array=pull()
        array[1]=1
        push(array[0],array[1],array[2],array[3])
    def background2():
        array=pull()
        array[1]=2
        push(array[0],array[1],array[2],array[3])
        print(array)
    def background3():
        array=pull()
        array[1]=3
        push(array[0],array[1],array[2],array[3])
    def background4():
        array=pull()
        array[1]=4
        push(array[0],array[1],array[2],array[3])
    def background5():
        array=pull()
        array[1]=5
        push(array[0],array[1],array[2],array[3])
    def background6():
        array=pull()
        array[1]=6
        push(array[0],array[1],array[2],array[3])

    lable1=Label(ld,text="Background",font=("Consolas",20,"bold"),fg="red",width=10,height=1)
    lable1.place(x=70,y=0)
    button1=Button(ld,text='Library',bg="#EE7C6B",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=background1)
    button1.place(x=0,y=45)
    button1=Button(ld,text='Library',bg="#AFD788",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=background2)
    button1.place(x=150,y=45)
    button1=Button(ld,text='Library',bg="#AF4A92",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=background3)
    button1.place(x=0,y=95)
    button1=Button(ld,text='Library',bg="#B7B7B7",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=background4)
    button1.place(x=150,y=95)
    button1=Button(ld,text='Library',bg="#FEF889",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=background5)
    button1.place(x=0,y=145)
    button1=Button(ld,text='Library',bg="#AA87B8",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=background6)
    button1.place(x=150,y=145)
    lable1=Label(ld,text="Figure",font=("Consolas",20,"bold"),fg="red",width=10,height=1)
    lable1.place(x=80,y=195)

    def figure1():
        array=pull()
        array[0]=1
        push(array[0],array[1],array[2],array[3])
    def figure2():
        array=pull()
        array[0]=2
        push(array[0],array[1],array[2],array[3])
    def figure3():
        array=pull()
        array[0]=3
        push(array[0],array[1],array[2],array[3])
    def figure4():
        array=pull()
        array[0]=4
        push(array[0],array[1],array[2],array[3])
    def figure5():
        array=pull()
        array[0]=5
        push(array[0],array[1],array[2],array[3])
    def figure6():
        array=pull()
        array[0]=6
        push(array[0],array[1],array[2],array[3])
    def figure7():
        array=pull()
        array[0]=7
        push(array[0],array[1],array[2],array[3])
    def figure8():
        array=pull()
        array[0]=8
        push(array[0],array[1],array[2],array[3])
    def show():
        img1=ImageTk.PhotoImage(Image.open ("nhanvat1.png"))
        lab=Label(image=img1)
        lab.place(x=20,y=240)
        button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure1)
        button1.place(x=10,y=300)
        img2=ImageTk.PhotoImage(Image.open ("nhanvat2.png"))
        lab=Label(image=img2)
        lab.place(x=90,y=240)
        button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure2)
        button1.place(x=80,y=300)
        img3=ImageTk.PhotoImage(Image.open ("nhanvat3.png"))
        lab=Label(image=img3)
        lab.place(x=160,y=240)
        button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure3)
        button1.place(x=150,y=300)
        img4=ImageTk.PhotoImage(Image.open ("nhanvat4.png"))
        lab=Label(image=img4)
        lab.place(x=230,y=240)
        button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure4)
        button1.place(x=220,y=300)
        img5=ImageTk.PhotoImage(Image.open ("nhanvat5.png"))
        lab=Label(image=img5)
        lab.place(x=20,y=360)
        button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure5)
        button1.place(x=10,y=420)
        img6=ImageTk.PhotoImage(Image.open ("nhanvat6.png"))
        lab=Label(image=img6)
        lab.place(x=90,y=360)
        button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure6)
        button1.place(x=80,y=420)
        img7=ImageTk.PhotoImage(Image.open ("nhanvat7.png"))
        lab=Label(image=img7)
        lab.place(x=160,y=360)
        button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure7)
        button1.place(x=150,y=420)
        img8=ImageTk.PhotoImage(Image.open ("nhanvat8.png"))
        lab=Label(image=img8)
        lab.place(x=230,y=360)
        button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure8)
        button1.place(x=220,y=420)
    show()
    button1=Button(ld,text='Quit',bg="black",fg="white",width=12,height=1,border=1,command=ld.quit)
    button1.place(x=100,y=460)
    ld.mainloop()



button=Button(base,text='Library',bg="Yellow",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=buy)
button.pack()
lb=Label(width=1,height=1)
lb.pack()
button=Button(base,text='Exit',bg="Gray",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=base.quit)
button.pack()
base.mainloop()






# root = Tk()
# root.title('Maze game')
# root.geometry('300x500')
# img = ImageTk.PhotoImage(Image.open("anh111.png"))
# panel = Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# root.mainloop() 












# root = Tk()
# root.geometry("550x300+300+150")
# root.resizable(width=True, height=True)

# def openfn():
#     filename = filedialog.askopenfilename(title='open')
#     return filename
# def open_img():
#     x = openfn()
#     img = Image.open(x)
#     img = img.resize((250, 250), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     panel = Label(root, image=img)
#     panel.image = img
#     panel.pack()

# btn = Button(root, text='open image', command=open_img).pack()

# root.mainloop()