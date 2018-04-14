import tkinter as tk


window = tk.Tk()
window.title('my window')
window.geometry('400x400')

canvas = tk.Canvas(window, bg = 'yellow', height=200, width=400)
image_file = tk.PhotoImage(file='../ins.gif')
imgae = canvas.create_image(10,10, anchor='nw', image=image_file) #anchor是定起始点， NW,N,WE,W,CENTER,E,SW,S,SE

x0,y0,x1,y1 = 50, 50, 80, 80
line = canvas.create_line(x0,y0,x1+15,y1+15) 
oval = canvas.create_oval(x0,y0,x1,y1, fill = 'red')
arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=30,extent=300)
rect = canvas.create_rectangle(100,30,100+50,30+50)
canvas.pack()

def moveit_up():
	canvas.move(rect,0,-10)
def moveit_down():
	canvas.move(rect,0,10)
def moveit_left():
	canvas.move(rect,-10,0)
def moveit_right():
	canvas.move(rect,10,0)

up = tk.Button(window,text='Go up', command = moveit_up).place(bordermode='outside', anchor='center',x=200,y=230,height=50,width=100)
down = tk.Button(window,text='Go down', command = moveit_down).place(anchor='center',x=200,y=300,height=40,width=100)
left = tk.Button(window,text='Go left', command = moveit_left).place(anchor='center',x=150,y=265,height=40,width=100)
right = tk.Button(window,text='Go right', command = moveit_right).place(anchor='center',x=250,y=265,height=40,width=100)


window.mainloop()