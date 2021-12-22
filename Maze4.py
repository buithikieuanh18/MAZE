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
base = Tk()
base.title('Maze game')
base.geometry("300x500")




def play():
    

    X_MARGIN = 0
    LANEWIDTH = 60

    CARWIDTH = 40
    CARHEIGHT = 60
    CARSPEED = 3
    CARIMG = pygame.image.load('nhanvat.png')

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
            GREEN = (0, 255, 0,)
            PINK = (255, 0, 255)
            YELLOW = (255, 255, 0)
            WHITE_CHECK = (255, 255, 255, 255)

            # initalise Pygame
            pygame.init()
            pygame.mixer.init()
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Python Maze Generator")
            clock = pygame.time.Clock()

            # setup maze variables
            x = 0  # x axis
            y = 0  # y axis
            w = S  # width of cell
            grid = []
            visited = []
            stack = []
            solution = {}

            # build the grid
            def build_grid(x, y, w):
                for i in range(1, length):
                    x = S  # set x coordinate to start position
                    y = y + S  # start a new row
                    for j in range(1, length):
                        pygame.draw.line(screen, WHITE, [x, y], [x + w, y])  # top of cell
                        pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])  # right of cell
                        pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])  # bottom of cell
                        pygame.draw.line(screen, WHITE, [x, y + w], [x, y])  # left of cell
                        grid.append((x, y))  # add cell to grid list
                        x = x + S  # move cell to new position

            def push_up(x, y):
                # return None
                pygame.draw.rect(screen, PINK, (x + 1, y - w + 1, S - 1, S + 19),
                                0)  # draw a rectangle twice the width of the cell
                pygame.display.update()  # to animate the wall being removed

            def push_down(x, y):
                # return None
                pygame.draw.rect(screen, PINK, (x + 1, y + 1, S - 1, S + 19), 0)
                pygame.display.update()

            def push_left(x, y):
                # return None
                pygame.draw.rect(screen, PINK, (x - w + 1, y + 1, S + 19, S - 1), 0)
                pygame.display.update()

            def push_right(x, y):
                # return None
                pygame.draw.rect(screen, PINK, (x + 1, y + 1, S + 19, S - 1), 0)
                pygame.display.update()

            def single_cell(x, y):
                pygame.draw.rect(screen, GREEN, (x + 1, y + 1, S - 2, S - 2), 0)  # draw a single width cell
                pygame.display.update()

            def backtracking_cell(x, y):
                pygame.draw.rect(screen, PINK, (x + 1, y + 1, S - 2, S - 2),
                                0)  # used to re-colour the path after single_cell

                pygame.display.update()  # has visited cell

            def solution_cell(x, y):
                pygame.draw.rect(screen, YELLOW, (x + (S / 2 - 4), y + (S / 2 - 4), 5, 5), 0)  # used to show the solution
                pygame.display.update()  # has visited cell

            def carve_out_maze(x, y):
                single_cell(x, y)  # starting positing of maze
                stack.append((x, y))  # place starting cell into stack
                visited.append((x, y))  # add starting cell to visited list
                while len(stack) > 0:  # loop until stack is empty
                    time.sleep(0)  # slow program now a bit
                    cell = []  # define cell list
                    if (x + w, y) not in visited and (x + w, y) in grid:  # right cell available?
                        cell.append("right")  # if yes add to cell list

                    if (x - w, y) not in visited and (x - w, y) in grid:  # left cell available?
                        cell.append("left")

                    if (x, y + w) not in visited and (x, y + w) in grid:  # down cell available?
                        cell.append("down")

                    if (x, y - w) not in visited and (x, y - w) in grid:  # up cell available?
                        cell.append("up")

                    if len(cell) > 0:  # check to see if cell list is empty
                        cell_chosen = (random.choice(cell))  # select one of the cell randomly
                        if cell_chosen == "right":  # if this cell has been chosen
                            push_right(x, y)  # call push_right function
                            solution[(x + w, y)] = x, y  # solution = dictionary key = new cell, other = current cell
                            x = x + w  # make this cell the current cell
                            visited.append((x, y))  # add to visited list
                            stack.append((x, y))
                            # a[int(x/20)+1][int(y/20)]=1                              # place current cell on to stack

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
                            # a[int(x/20)][int(y/20)-1]=1
                        elif cell_chosen == "up":
                            push_up(x, y)
                            solution[(x, y - w)] = x, y
                            y = y - w
                            visited.append((x, y))
                            stack.append((x, y))
                            # a[int(x/20)][int(y/20)+1]=1
                    else:
                        x, y = stack.pop()  # if no cells are available pop one from the stack
                        single_cell(x, y)  # use single_cell function to show backtracking image
                        time.sleep(.00)  # slow program down a bit
                        backtracking_cell(x, y)  # change colour to green to identify backtracking path

            def plot_route_back(x, y):
                solution_cell(x, y)  # solution list contains all the coordinates to route back to start
                while (x, y) != (S, S):  # loop until cell position == start position
                    x, y = solution[x, y]  # "key value" now becomes the new key
                    solution_cell(x, y)  # animate route back
                    time.sleep(.01)

            def plot_route_back2(x, y):
                solution_cell(x, y)  # solution list contains all the coordinates to route back to start
                while (x, y) != ((length - 1) * S, (length - 1) * S):  # loop until cell position == start position
                    x, y = solution[x, y]  # "key value" now becomes the new key
                    solution_cell(x, y)  # animate route back
                    time.sleep(.01)

            x, y = S, S  # starting position of grid
            build_grid(40, 0, S)  # 1st argument = x value, 2nd argument = y value, 3rd argument = width of cell
            carve_out_maze(x, y)  # call build the maze  function
            plot_route_back((length - 1) * S, (length - 1) * S)  # call the plot solution function
            running = True


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
            pygame.draw.rect(DISPLAYSURF, (255, 0, 255), (self.x, self.y, 31, 50), 0)
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
        headingSuface = font.render('GAMEOVER', True, (255, 0, 0))
        headingSize = headingSuface.get_size()

        font = pygame.font.SysFont('consolas', 20)
        commentSuface = font.render('Press "space" to replay', True, (255, 0, 0))
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
def bye():
    ld = Tk()
    ld.title('Maze game')
    ld.geometry("300x500")
    lable1=Label(ld,text="luudanh",font=("Consolas",16,"bold"),fg="red",width=10,height=1)
    lable1.place(x=0,y=0)
    button1=Button(ld,text='Library',bg="Yellow",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4)
    button1.place(x=0,y=25)
    button1=Button(ld,text='Library',bg="Yellow",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4)
    button1.place(x=150,y=25)
    button1=Button(ld,text='Library',bg="Yellow",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4)
    button1.place(x=0,y=75)
    button1=Button(ld,text='Library',bg="Yellow",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4)
    button1.place(x=150,y=75)
    # button2=Button(ld,text='Library',bg="Yellow",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4)
    # button2.pack(side=tk.LEFT)
    
    ld.mainloop()

button=Button(base,text='Library',bg="Yellow",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=bye)
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