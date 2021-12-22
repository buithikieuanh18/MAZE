import pgzrun
from tkinter import *
from PIL import ImageTk ,Image
ld = Tk()
bg=1
figure=1
ld.title('Maze game')
ld.geometry("300x500")
def background1():
    bg=1
    print(bg)
    
def background2():
    bg=2
    print(bg)
def background3():
    bg=3
    print(bg)
def background4():
    bg=4
    print(bg)
def background5():
    bg=5
    print(bg)
def background6():
    bg=6
    print(bg)
lable1=Label(ld,text="background",font=("Consolas",20,"bold"),fg="red",width=10,height=1)
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
lable1=Label(ld,text="figure",font=("Consolas",20,"bold"),fg="red",width=10,height=1)
lable1.place(x=80,y=195)
def figure1():
    figure=1
def figure2():
    figure=2
def figure3():
    figure=3
def figure4():
    figure=4
def figure5():
    figure=5
def figure6():
    figure=6
def figure7():
    figure=7
def figure8():
    figure=8
img1=ImageTk.PhotoImage(Image.open ("nhanvat1.png"))
lab=Label(image=img1)
lab.place(x=20,y=240)
button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1)
button1.place(x=10,y=300)
img2=ImageTk.PhotoImage(Image.open ("nhanvat2.png"))
lab=Label(image=img2)
lab.place(x=90,y=240)
button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1)
button1.place(x=80,y=300)
img3=ImageTk.PhotoImage(Image.open ("nhanvat3.png"))
lab=Label(image=img3)
lab.place(x=160,y=240)
button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1)
button1.place(x=150,y=300)
img4=ImageTk.PhotoImage(Image.open ("nhanvat4.png"))
lab=Label(image=img4)
lab.place(x=230,y=240)
button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1)
button1.place(x=220,y=300)
img5=ImageTk.PhotoImage(Image.open ("nhanvat5.png"))
lab=Label(image=img5)
lab.place(x=20,y=360)
button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1)
button1.place(x=10,y=420)
img6=ImageTk.PhotoImage(Image.open ("nhanvat6.png"))
lab=Label(image=img6)
lab.place(x=90,y=360)
button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1)
button1.place(x=80,y=420)
img7=ImageTk.PhotoImage(Image.open ("nhanvat7.png"))
lab=Label(image=img7)
lab.place(x=160,y=360)
button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1)
button1.place(x=150,y=420)
img8=ImageTk.PhotoImage(Image.open ("nhanvat8.png"))
lab=Label(image=img8)
lab.place(x=230,y=360)
button1=Button(ld,text='pic',bg="#F5A89A",fg="black",width=8,height=1,border=1)
button1.place(x=220,y=420)
button1=Button(ld,text='quit',bg="black",fg="white",width=12,height=1,border=1,command=ld.quit)
button1.place(x=100,y=460)
ld.mainloop()