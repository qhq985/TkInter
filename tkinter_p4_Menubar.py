import tkinter as tk


window = tk.Tk()
window.title('My Calculator')
window.geometry('300x400')

var1 = tk.StringVar() #整数var形式
var2 = tk.IntVar() #整数var形式
var3 = tk.IntVar() #整数var形式
var4 = tk.IntVar() #整数var形式
var5 = tk.IntVar() #整数var形式
var6 = tk.IntVar() #整数var形式
var7 = tk.IntVar() #整数var形式
var8 = tk.IntVar() #整数var形式
var9 = tk.IntVar() #整数var形式
var0 = tk.IntVar() #整数var形式
var_plus = tk.IntVar() #整数var形式
var_minus = tk.IntVar() #整数var形式
var_times = tk.IntVar() #整数var形式
var_devide = tk.IntVar() #整数var形式
var_equal = tk.IntVar() #整数var形式

l = tk.Label(window,bg='gray',height =1, width =40)
l.place(anchor = 'center',x = 150, y=20)

var1.set(' ')

o = tk.Label(window,bg='yellow',textvariable=var1, font=('Helvetica',15),height =2, width =40)
o.place(anchor = 'center',x = 150, y=60)



counter = 0
def do_job():
    global counter
    l.config(text='Do '+ str(counter))
    counter+=1



menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='Login', command=do_job)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)

filemenu.add_separator()##这里就是一条分割线

filemenu.add_command(label='Exit', command=window.quit)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)##给放入的菜单`submenu`命名为`Import`
submenu.add_command(label="Submenu1", command=do_job)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)


window.config(menu=menubar)#这就相当于pack
def insert_1():
	value = var1.get()
	if value[-1] != '0':
		value += '1'
	var1.set(value)

def insert_2():
	value = var1.get()
	if value[-1] != '0':
		value += '2'
	var1.set(value)

def insert_3():
	value = var1.get()
	if value[-1] != '0':
		value += '3'
	var1.set(value)

def insert_4():
	value = var1.get()
	if value[-1] != '0':
		value += '4'
	var1.set(value)

def insert_5():
	value = var1.get()
	if value[-1] != '0':
		value += '5'
	var1.set(value)

def insert_6():
	value = var1.get()
	if value[-1] != '0':
		value += '6'
	var1.set(value)

def insert_7():
	value = var1.get()
	if value[-1] != '0':
		value += '7'
	var1.set(value)

def insert_8():
	value = var1.get()
	if value[-1] != '0':
		value += '8'
	var1.set(value)

def insert_9():
	value = var1.get()
	if value[-1] != '0':
		value += '9'
	var1.set(value)

def insert_0():
	value = var1.get()
	if value[-1] != '/':
		value += '0'
	var1.set(value)

def insert_point():
	value = var1.get()
	if value[-1] != '.':
		value += '.'
	var1.set(value)

def insert_00():
	value = var1.get()
	if value[-1] != '/':
		value += '00'
	var1.set(value)

def insert_plus():
	value = var1.get()
	if value[-1] not in ['+']:
		value += '+'
	var1.set(value)

def insert_minus():
	value = var1.get()
	if value[-1] not in ['-']:
		value += '-'
	var1.set(value)

def insert_times():
	value = var1.get()
	if value[-1] not in [' ','*','/']:
		value += '*'
	var1.set(value)

def insert_devide():
	value = var1.get()
	if value[-1] not in [' ','*','/']:
		value += '/'
	var1.set(value)

def clear():
	var1.set(' ')

def equal():
	value = var1.get()
	if value != ' ' and value[-1] != '+' and value[-1] != '-' and value[-1] != '*'and value[-1] != '/':
		value = eval(value)
	var1.set(str(value))

def cc():
	value = var1.get()
	if value != ' ':
		value = value[:-1]
	var1.set(value)

x0,y0 = 50, 110




bc = tk.Button(window, text = 'Clear', width = 50, height=50, command =clear)  
bc.place(bordermode='outside',anchor='center',x=75,y=y0,height=60,width=75)

bequal = tk.Button(window, text = '=', width = 15, height=2, command =equal)  
bequal.place(bordermode='outside',anchor='center',x=150,y=y0,height=50,width=75)

bcc = tk.Button(window, text = 'Undo', width = 50, height=50, command =cc)  
bcc.place(bordermode='outside',anchor='center',x=225,y=y0,height=60,width=75)
 
b7 = tk.Button(window, text = '7', width = 15, height=2, command =insert_7)  
b7.place(bordermode='outside',anchor='center',x=x0,y=y0+60,height=50,width=50)
b8 = tk.Button(window, text = '8', width = 15, height=2, command =insert_8)  
b8.place(bordermode='outside',anchor='center',x=x0+60,y=y0+60,height=50,width=50)
b9 = tk.Button(window, text = '9', width = 15, height=2, command =insert_9)  
b9.place(bordermode='outside',anchor='center',x=x0+120,y=y0+60,height=50,width=50)
b4 = tk.Button(window, text = '4', width = 15, height=2, command =insert_4)  
b4.place(bordermode='outside',anchor='center',x=x0,y=y0+120,height=50,width=50)
b5 = tk.Button(window, text = '5', width = 15, height=2, command =insert_5)  
b5.place(bordermode='outside',anchor='center',x=x0+60,y=y0+120,height=50,width=50)
b6 = tk.Button(window, text = '6', width = 15, height=2, command =insert_6)  
b6.place(bordermode='outside',anchor='center',x=x0+120,y=y0+120,height=50,width=50)
b1 = tk.Button(window, text = '1', width = 15, height=2, command =insert_1)  
b1.place(bordermode='outside',anchor='center',x=x0,y=y0+180,height=50,width=50)
b2 = tk.Button(window, text = '2', width = 15, height=2, command =insert_2)  
b2.place(bordermode='outside',anchor='center',x=x0+60,y=y0+180,height=50,width=50)
b3 = tk.Button(window, text = '3', width = 15, height=2, command =insert_3)  
b3.place(bordermode='outside',anchor='center',x=x0+120,y=y0+180,height=50,width=50)
b0 = tk.Button(window, text = '0', width = 15, height=2, command =insert_0)  
b0.place(bordermode='outside',anchor='center',x=x0,y=y0+240,height=50,width=50)
bpoint = tk.Button(window, text = '.', width = 15, height=2, command =insert_point)  
bpoint.place(bordermode='outside',anchor='center',x=x0+60,y=y0+240,height=50,width=50)
b00 = tk.Button(window, text = '00', width = 15, height=2, command =insert_00)  
b00.place(bordermode='outside',anchor='center',x=x0+120,y=y0+240,height=50,width=50)
bplus = tk.Button(window, text = '+', width = 15, height=2, command =insert_plus)  
bplus.place(bordermode='outside',anchor='center',x=x0+180,y=y0+60,height=50,width=50)
bminus = tk.Button(window, text = '-', width = 15, height=2, command =insert_minus)  
bminus.place(bordermode='outside',anchor='center',x=x0+180,y=y0+120,height=50,width=50)
btims = tk.Button(window, text = '*', width = 15, height=2, command =insert_times)  
btims.place(bordermode='outside',anchor='center',x=x0+180,y=y0+180,height=50,width=50)
bdevide = tk.Button(window, text = '/', width = 15, height=2, command =insert_devide)  
bdevide.place(bordermode='outside',anchor='center',x=x0+180,y=y0+240,height=50,width=50)




window.mainloop()