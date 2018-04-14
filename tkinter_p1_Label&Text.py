import tkinter as tk


window = tk.Tk()
window.title('my window')
window.geometry('200x200')


var1 = tk.StringVar()
l = tk.Label(window, bg='yellow',width =8, textvariable=var1)
l.pack()


e = tk.Entry(master=None)
e.pack()
# l.pack() #放在那里
# l.place() #具体放在某个点

# on_hit = False

# def hit_me():
# 	global on_hit
# 	if on_hit == False:
# 		on_hit = True
# 		var.set('you hit me')
# 	else:
# 		on_hit = False
# 		var.set('')



def print_selection():
	value = t.get(t.curselection())
	var1.set(value)


def insert_end():
	var = e.get()
	t.insert('end', var)
	# or t.insert('insert', var)
# 	# or t.insert(1.0, var) #第1行第0位置

b1 = tk.Button(window, text = 'insert end', width = 15, height=2, command =insert_end)  #tk里的第一个都是大写
b1.pack()

b2 = tk.Button(window, text = 'print selection', width = 15, height=2, command =print_selection)  #tk里的第一个都是大写
b2.pack()

t = tk.Listbox(window, width = 25,height=10)
t.pack()

# var2 = tk.StringVar()
# var2.set((11,22,33,44)) #为变量设置值

#创建Listbox

# lb = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox

# #创建一个list并将值循环添加到Listbox控件中
# list_items = [1,2,3,4]
# for item in list_items:
#     lb.insert('end', item)  #从最后一个位置开始加入值
# lb.insert(1, 'first')       #在第一个位置加入'first'字符
# lb.insert(2, 'second')      #在第二个位置加入'second'字符
# lb.delete(2)                #删除第二个位置的字符
# lb.pack()


window.mainloop() #必须有，得一直存在
