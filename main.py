from tkinter import Label,Frame,Canvas,Tk,IntVar
import random
def generate_food():
    global activefruit,fruit_x,fruit_y
    j=0
    while j==0:    
        fruit_x=random.randint(1,39)
        fruit_y=random.randint(1,38)

        for i in range(len(snake_x)):
            if fruit_x==snake_x[i] and fruit_y==snake_y[i]:
                j=0
                break
            else:
                j=1
    canvas.create_rectangle(fruit_x*10-5,fruit_y*10-5,fruit_x*10+5,fruit_y*10+5,fill='red',tag='fruit')
    activefruit=0
def check_condition():
    global winning,fruit_x,fruit_y,activefruit,score,speed
    if snake_x[0]==0 or snake_x[0]==40:
        canvas.create_text(200,150,text='Game over',font='times 20 bold',tag='game_over')
        root.bind('<space>',go)
        winning=1
    if snake_y[0]==0 or snake_y[0]==39:
        canvas.create_text(200,150,text='Game over',font='times 20 bold',tag='game_over')
        root.bind('<space>',go)
        winning=1
    if snake_x[0]==fruit_x and snake_y[0]==fruit_y:
        canvas.delete('fruit')
        activefruit=1
        snake_x.append(len(snake_x)-1)
        snake_y.append(len(snake_y)-1)
        score.set(score.get()+1)
    if score==10:
        speed+=15
    if score==15:
        speed+=5
    if score==20:
        speed+=10
    if score==25:
        speed+=10
    if score==30:
        speed+=15
def next():
    global snake_x,snake_y,turn,winning,activefruit,speed
    if activefruit==1:
        generate_food()
    i=len(snake_x)-1
    while i>0:
        snake_x[i]=snake_x[i-1]
        snake_y[i]=snake_y[i-1]
        i-=1
    if turn=='UP':
        snake_y[0]-=1
    elif turn=='DOWN':
        snake_y[0]+=1
    elif turn=='LEFT':
        snake_x[0]-=1
    elif turn=='RIGHT':
        snake_x[0]+=1
    for i in range(len(snake_x)):
        canvas.delete(f'snake_{i}')
    canvas.create_oval(snake_x[0]*10-6,snake_y[0]*10-6,snake_x[0]*10+6,snake_y[0]*10+6,fill='black',width=2,tag=f'snake_0')
    for i in range(1,len(snake_x)):
        canvas.create_oval(snake_x[i]*10-6,snake_y[i]*10-6,snake_x[i]*10+6,snake_y[i]*10+6,width=2,tag=f'snake_{i}')
    check_condition()
    if winning==0:
        root.after(100-speed,next)
def side_up(event):
    global turn
    if turn=='LEFT' or turn=='RIGHT' or turn=='UP':
        turn='UP'
def side_down(event):
    global turn
    if turn=='LEFT' or turn=='RIGHT' or turn=='DOWN':
        turn='DOWN'
def side_left(event):
    global turn
    if turn=='UP' or turn=='DOWN' or turn=='LEFT':
        turn='LEFT'
def side_right(event):
    global turn
    if turn=='UP' or turn=='DOWN' or turn=='RIGHT':
        turn='RIGHT'
def go(event):
    global turn,winning,snake_x,snake_y,activefruit,score,speed
    root.unbind("<space>")
    canvas.delete('game_over')
    canvas.delete('fruit')
    for i in range(len(snake_x)):
        canvas.delete(f'snake_{i}')
    snake_x=[22,21,20,19]
    snake_y=[20,20,20,20]
    turn='RIGHT'
    winning=0
    activefruit=1
    score.set(0)
    speed=0
    root.after(300-speed,next)
#---------------------------------------------------------------------------------------------
snake_x=[22,21,20,19]
snake_y=[20,20,20,20]
turn='RIGHT'
root=Tk()
root.title('Snake Game')
root.geometry('600x400+200+100')
root.resizable(0,0)
root.bind('<space>',go)
root.bind('<Up>',side_up)
root.bind('<w>',side_up)
root.bind('<W>',side_up)
root.bind('<Down>',side_down)
root.bind('<s>',side_down)
root.bind('<S>',side_down)
root.bind('<Left>',side_left)
root.bind('<a>',side_left)
root.bind('<A>',side_left)
root.bind('<Right>',side_right)
root.bind('<d>',side_right)
root.bind('<D>',side_right)
#---------------------------------------------------------------------------
frame1=Frame(root,bd=3,relief='sunken',width=400,height=400)
frame1.pack(side='left')
frame2=Frame(root,bd=3,relief='ridge',width=200,height=400)
frame2.pack(side='right')
#-------------------------------------------------------------------------
canvas=Canvas(frame1,width=400,height=400,bg='lightyellow')
canvas.pack()
canvas.create_rectangle(4,4,400,390,width=4)
canvas.create_oval(snake_x[0]*10-6,snake_y[0]*10-6,snake_x[0]*10+6,snake_y[0]*10+6,fill='black',width=2,tag=f'snake_0')
for i in range(1,len(snake_x)):
    canvas.create_oval(snake_x[i]*10-6,snake_y[i]*10-6,snake_x[i]*10+6,snake_y[i]*10+6,width=2,tag=f'snake_{i}')
#-------------------------------------------------------------------------
score=IntVar()
score.set(0)
Label(frame2,text='Snake Game',font='arial 20 bold underline',fg='blue').pack(pady=19)
Label(frame2,text='press space for start',fg='red').pack(pady=(4,12))
Label(frame2,text='press Up key for Move',fg='black').pack(pady=1)
Label(frame2,text='press Down key for Move',fg='black').pack(pady=1)
Label(frame2,text='press Left key for Move',fg='black').pack(pady=1)
Label(frame2,text='press Right key for Move',fg='black').pack(pady=1)
Label(frame2,text='You can use A,W,S,D for Move',fg='black').pack(pady=1)
Label(frame2,text='Score :',font='arial 18 bold',fg='black',width=14).pack(pady=(25,0))
Label(frame2,textvariable=score,font='arial 18 bold',fg='red',width=14).pack(pady=(0,15))
Label(frame2,text='Enjoy the Game',font='arial 14',fg='yellow',bg='black',width=18,height=2).pack(pady=(15,0))
root.mainloop()