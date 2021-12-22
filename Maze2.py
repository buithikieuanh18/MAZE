from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os 
import random
import tkinter as tk
import tkinter.font as tkFont
from pygame.locals import *
import pygame, sys
import json
base = Tk()
base.title('Maze game')
base.geometry("350x600")
help=True

def play():
    
    score=0
    score2=0
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
    score=array[2]
    lever=array[3]
    IMG=0
    COLOR = 0
    if(array[0]==1):
        IMG= pygame.image.load('nhanvat1.png')
    elif(array[0]==2):
        IMG= pygame.image.load('nhanvat2.png')
    elif(array[0]==3):
        IMG= pygame.image.load('nhanvat3.png')
    elif(array[0]==4):
        IMG= pygame.image.load('nhanvat4.png')
    elif(array[0]==5):
        IMG= pygame.image.load('nhanvat5.png')
    elif(array[0]==6):
        IMG= pygame.image.load('nhanvat6.png')
    elif(array[0]==7):
        IMG= pygame.image.load('nhanvat7.png')
    else:
        IMG= pygame.image.load('nhanvat8.png')


    if(array[1]==1):
        COLOR= (255,106,106)
    elif(array[1]==2):
        COLOR= (188,238,104)
    elif(array[1]==3):
        COLOR= (238,58,140)
    elif(array[1]==4):
        COLOR= (118,238,198)
    elif(array[1]==5):
        COLOR= (238,213,210)
    else:
        COLOR= (122,103,238)
    X_MARGIN = 0
    showcoin1=[]
    WIDTHF = 40
    HEIGHTF = 60
    SPEED = 3
    pygame.init()
    S = 65
    FPS = 60
    fpsClock = pygame.time.Clock()
    WIDTH = (lever+1)*S
    HEIGHT = (lever+1)*S
    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))#dùng để vẽ nhân vật cũng như là các hình ảnh ở lớp trên
    solution = {}
    screen = pygame.display.set_mode((WIDTH, HEIGHT))#dùng để vẽ màu, mê cũng , các hình đơn giản ở phía dưới
    class Background():
        def __init__(self):
            self.x = 0
            self.y = 0
        def draw(self):
            
            WHITE = (255, 255, 255)
           
            pygame.init()
            pygame.mixer.init()
            
            pygame.display.set_caption("Python Maze Generator")
            x = 0 
            y = 0  
            w = S 
            grid = []
            visited = []
            stack = []
            

           
            def build_grid(x, y, w):
                for i in range(1, lever):
                    x = S 
                    y = y + S
                    for j in range(1, lever):
                        pygame.draw.line(screen, WHITE, [x, y], [x + w, y])
                        pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w]) 
                        pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])  
                        pygame.draw.line(screen, WHITE, [x, y + w], [x, y]) 
                        grid.append((x, y))
                        x = x + S 
                
            def push_up(x, y):
                pygame.draw.rect(screen, COLOR, (x + 1, y - w + 1, S - 3, S + 17),
                                0)
                pygame.display.update()

            def push_down(x, y):
                pygame.draw.rect(screen, COLOR, (x + 1, y + 1, S - 3, S + 17), 0)
                pygame.display.update()

            def push_left(x, y):
                pygame.draw.rect(screen, COLOR, (x - w + 1, y + 1, S + 17, S - 3), 0)
                pygame.display.update()

            def push_right(x, y):
                pygame.draw.rect(screen, COLOR, (x + 1, y + 1, S + 17, S - 3), 0)
                pygame.display.update()

            def backtracking_cell(x, y):
                pygame.draw.rect(screen, COLOR, (x + 1, y + 1, S - 2, S - 2),
                                0)  

                pygame.display.update()  
            def carve_out_maze(x, y):
                stack.append((x, y))  
                visited.append((x, y)) 
                while len(stack) > 0:  
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



            x, y = S, S  
            build_grid(40, 0, S)  
            carve_out_maze(x, y)
    def coin():
        def showcoin(x,y):
            pygame.draw.rect(screen,(249,244,0),(x,y,10,10),0)
            pygame.display.update()
        for i in range(5):
            a=random.randint(S,S*(lever-2))
            b=random.randint(S,S*(lever-2))
            for h in range (7):
                for k in range(7):
                    if( DISPLAY.get_at((a+h, b+k))==(255, 255, 255, 255) 
                    or DISPLAY.get_at((a-h, b-k))==(255, 255, 255, 255) 
                    or DISPLAY.get_at((a+h, b-k))==(255, 255, 255, 255) 
                    or DISPLAY.get_at((a-h, b+k))==(255, 255, 255, 255)):
                        a=a+7
                        b=b+7
            showcoin1.append(a)
            showcoin1.append(b)
            showcoin(a,b)
            pygame.draw.rect(screen,(55,55,55),(S*(lever-1)+40,S*(lever-1),25,S),0)
            pygame.display.update()
    def suggest():
        YELLOW=(55,188,188)
        def plot_route_back(x, y):
            solution_cell(x, y) 
            while (x, y) != (S, S): 
                    x, y = solution[x, y] 
                    solution_cell(x, y)

        def plot_route_back2(x, y):
            solution_cell(x, y) 
            while (x, y) != ((lever - 1) * S, (lever - 1) * S): 
                x, y = solution[x, y]
                solution_cell(x, y) 
        def solution_cell(x,y):
            pygame.draw.rect(screen, YELLOW, (x+(S/2-5), y+(S/2-5), 9, 9), 0)             # used to show the solution
            pygame.display.update() 
        plot_route_back((lever - 1) * S, (lever - 1) * S)                                    
    class nv():
        def __init__(self):
            self.width = WIDTHF
            self.height = HEIGHTF
            self.x = 77
            self.y = 70
            self.speed = SPEED

        def draw(self):
            pygame.draw.rect(DISPLAY,COLOR, (self.x, self.y, 31, 50), 0)
            DISPLAY.blit(IMG, (int(self.x), int(self.y)))


        def update(self, moveLeft, moveRight, moveUp, moveDown):
            for i in range (8):
                score3=score
                if(i%2==1):
                    i=i+1
                for h in range(30):
                    for k in range(50):
                       
                        if((self.x==(showcoin1[i]+h+10) and self.y==(showcoin1[i+1]+k+20))
                        or (self.x==(showcoin1[i]+h+10) and self.y==(showcoin1[i+1]-k+40))
                        or (self.x==(showcoin1[i]-(h-20)) and self.y==(showcoin1[i+1]+k+20))
                        or (self.x==(showcoin1[i]-h+20) and self.y==(showcoin1[i+1])-k+40)):
                            a=i
                            score3+=50
                            showcoin1[a]=10000000
                            showcoin1[a+1]=1000000000
                            data={}
                            data['users']=[]
                            data['users'].append({"figure":array[0],"bg":array[1],"score":score3,"lever":lever})
                            with open('maze.json','w') as f:
                                json.dump(data,f)
            if moveLeft == True:
                check = True
                for i in range(50):
                    if DISPLAY.get_at((self.x - 1, self.y + i)) == (255, 255, 255, 255) \
                            or DISPLAY.get_at((self.x - 2, self.y + i)) == (255, 255, 255, 255) \
                            or DISPLAY.get_at((self.x - 3, self.y + i)) == (255, 255, 255, 255):
                        check = False
                        break
                if check is True:
                    self.x -= self.speed
            if moveRight == True:
                check = True
                for i in range(50):
                    if DISPLAY.get_at((self.x + 30, self.y + i)) == (255, 255, 255, 255) \
                            or DISPLAY.get_at((self.x + 31, self.y + i)) == (255, 255, 255, 255) \
                            or DISPLAY.get_at((self.x + 32, self.y + i)) == (255, 255, 255, 255) \
                            or DISPLAY.get_at((self.x + 33, self.y + i)) == (255, 255, 255, 255)\
                            or DISPLAY.get_at((self.x + 34, self.y + i)) == (255, 255, 255, 255):
                        check = False
                        break
                if check is True:
                    self.x += self.speed
            if moveUp == True:
                check = True
                for i in range(30):
                    if DISPLAY.get_at((self.x + i, self.y - 1)) == (255, 255, 255, 255) \
                            or DISPLAY.get_at((self.x + i, self.y - 2)) == (255, 255, 255, 255) \
                            or DISPLAY.get_at((self.x + i, self.y - 3)) == (255, 255, 255, 255):
                        check = False
                        break
                if check is True:
                    
                    self.y -= self.speed
            if moveDown == True:
                check = True
                for i in range(30):
                    if DISPLAY.get_at((self.x + i, self.y + 50)) == (255, 255, 255, 255) \
                            or DISPLAY.get_at((self.x + i, self.y + 51)) == (255, 255, 255, 255) \
                            or DISPLAY.get_at((self.x + i, self.y + 52)) == (255, 255, 255, 255) \
                            or DISPLAY.get_at((self.x + i, self.y + 53)) == (255, 255, 255, 255) \
                            or DISPLAY.get_at((self.x + i, self.y + 54)) == (255, 255, 255, 255):
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
        if rect1[0] >= (S*(lever-1)+20) and rect1[1] >= S*(lever-1):
            return True
        return False

    
    def isGameover(nv):
        nvRect = [nv.x, nv.y, nv.width, nv.height]
        if rectCollision(nvRect) == True:
            return True

        return False
        

    def gamePlay(bg, nv):
        nv.__init__()
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
                if event.type == pygame.KEYUP:
                    if event.key == K_SPACE:
                        if(score>300):
                            score2=score-300
                            suggest()
                            data={}
                            data['users']=[]
                            data['users'].append({"figure":array[0],"bg":array[1],"score":score2,"lever":lever})
                            with open('maze.json','w') as f:
                                json.dump(data,f)

                       
            if isGameover(nv):
                return
            nv.draw()
            nv.update(moveLeft, moveRight, moveUp, moveDown)
            pygame.display.update()
            fpsClock.tick(FPS)
            help=False
    
    def gameOver(bg, nv):
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
            
            DISPLAY.blit(headingSuface, (int((WIDTH - headingSize[0]) / 2), 100))
            DISPLAY.blit(commentSuface, (int((WIDTH - commentSize[0]) / 2), 300))
            #up lever mới
            lever1=lever+1
            score2=score+100
            data={}
            data['users']=[]
            data['users'].append({"figure":array[0],"bg":array[1],"score":score2,"lever":lever1})
            with open('maze.json','w') as f:
                json.dump(data,f)
            pygame.display.update()
            fpsClock.tick(FPS)
        # bg.draw()
        # car.draw()
    

    bg = Background()
    bg.draw()    
    nv = nv()

    coin()
    while True:    
        gamePlay(bg, nv)   
        gameOver(bg, nv) 
    
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
img=ImageTk.PhotoImage(Image.open ("tutorial.png"))
lb3=Label(width=10,height=2,text='Name:Lươn',font=("Consolas",14,"bold"))
lb3.pack()
img=ImageTk.PhotoImage(Image.open ("background.png"))
lab=Label(image=img,width=300,height=200)
lab.pack()
lb1=Label(width=10,height=1,text=array[3],font=("Consolas",14,"bold"))
lb1.pack()
lb2=Label(width=10,height=1,text=array[2],font=("Consolas",14,"bold"))
lb2.pack()
btn=Button(base,text="Play",bg="Yellow",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=play)
btn.place(x=20,y=320)
def buy():
    ld = Toplevel()
    bg=1
    figure=1
    ld.title('Maze game')
    ld.geometry("300x500")
    
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

    # Image 1
    img1 = ImageTk.PhotoImage(Image.open("nhanvat1.png"))
    lab = Label(ld, image=img1)
    lab.place(x=20, y=240)
    button1 = Button(ld, text='pic', bg="#F5A89A", fg="black", width=8, height=1, border=1, command=figure1)
    button1.place(x=10, y=300)

    # Image 2
    img2=ImageTk.PhotoImage(Image.open ("nhanvat2.png"))
    lab=Label(ld, image=img2)
    lab.place(x=90,y=240)
    button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure2)
    button1.place(x=80,y=300)

    # Image 3
    img3=ImageTk.PhotoImage(Image.open ("nhanvat3.png"))
    lab=Label(ld, image=img3)
    lab.place(x=160,y=240)

    # Image 4
    button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure3)
    button1.place(x=150,y=300)
    img4=ImageTk.PhotoImage(Image.open ("nhanvat4.png"))
    lab=Label(ld, image=img4)
    lab.place(x=230,y=240)

    # Image 5
    button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure4)
    button1.place(x=220,y=300)
    img5=ImageTk.PhotoImage(Image.open ("nhanvat5.png"))
    lab=Label(ld, image=img5)
    lab.place(x=20,y=360)

    # Image 6
    button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure5)
    button1.place(x=10,y=420)
    img6=ImageTk.PhotoImage(Image.open ("nhanvat6.png"))
    lab=Label(ld, image=img6)
    lab.place(x=90,y=360)

    # Image 7
    button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure6)
    button1.place(x=80,y=420)
    img7=ImageTk.PhotoImage(Image.open ("nhanvat7.png"))
    lab=Label(ld, image=img7)
    lab.place(x=160,y=360)

    # Image 8
    button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure7)
    button1.place(x=150,y=420)
    img8=ImageTk.PhotoImage(Image.open ("nhanvat8.png"))
    lab=Label(ld, image=img8)
    lab.place(x=230,y=360)

    #Button
    button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1,command=figure8)
    button1.place(x=220,y=420)
    button1=Button(ld,text='Quit',bg="black",fg="white",width=12,height=1,border=1,command=ld.quit)
    button1.place(x=100,y=460)
    ld.mainloop()


def tutorial():
    ld  = Toplevel()
    ld.title('Maze game')
    ld.geometry("450x350")
    img=ImageTk.PhotoImage(Image.open ("tutorial.png"))
    lab=Label(ld, image=img)
    lab.place(x=-3,y=-3)
    text="-Chức năng khác \n -Ăn vàng trong màn chơi để \ncộng thêm 50v+qua màn 100 vàng \n -Dùng vàng để thay đổi \nbackround hay nhân vật \n -Dùng vàng để sử dụng sự \ntrợ giúp (tìm đường đi):300v \n-Thắng màn hiện tại \nđể mở màn cao hơn\n -Thoát ra sẽ bắt đầu lại\n game gần nhất mà bạn chơi,\n vàng cùng nhân vật hiện tại \nsẽ ko thay dổi khi vào lại\n -click chọn để \nthêm nhân vật muốn chọn\n và sẽ mất 500 vàng mỗi lần\n thay đổi"
    lable1=Label(ld,text=text,font=("Consolas",10,"bold"),fg="black",width=50,height=18)
    lable1.place(x=50,y=38) 
    mainloop()   
def guide():
    ld  = Toplevel()
    ld.title('Maze game')
    ld.geometry("450x350")
    img=ImageTk.PhotoImage(Image.open ("guide.png"))
    lab=Label(ld, image=img)
    lab.place(x=-3,y=-3)
    text="Hướng dẫn chơi game\n-Nhấn nút Play để bắt đầu chơi game\n-Sửa dụng các phím trái phải lên xuống \nđể  di chuyển nhân vật tới đích\n-Bạn có thể thay đổi ngoại hình nhân vật \n cũng như nền của mê cung tại mục Library\n-Nhấn exit khi muốn thoát trò chơi"

    lable1=Label(ld,text=text,font=("Consolas",10,"bold"),fg="black",width=50,height=18)
    lable1.place(x=50,y=48) 
    mainloop()  
button=Button(base,text='Library',bg="Yellow",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=buy)
button.place(x=180,y=320)
button=Button(base,text='Guide',bg="Gray",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=guide)
button.place(x=20,y=380)
button=Button(base,text='Tutorial',bg="Gray",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=tutorial)
button.place(x=180,y=380)
button=Button(base,text='Exit',bg="Gray",fg="orange",font=("Consolas",14,"bold"),width=13,height=1,border=4,command=base.quit)
button.place(x=100,y=440)

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