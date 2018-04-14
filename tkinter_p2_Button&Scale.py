import tkinter as tk


window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow',width =20)
l.pack()


def print_selection():
	if (var1.get()==1) &(var2.get()==0):
		l.config(text='I only love Python')
	elif (var1.get()==0) & (var2.get()==1):
		l.config(text='I only love C++')
	elif (var1.get()==0) & (var2.get()==0):
		l.config(text='I don\'t love either')
	else:
		l.config(text='I love both')

var1 = tk.IntVar() #整数var形式
var2 = tk.IntVar() #整数var形式

c1 = tk.Checkbutton(window, text = 'Python', variable =var1, onvalue=1, offvalue=0,
		command = print_selection)
c2 = tk.Checkbutton(window, text = 'C++', variable =var2, onvalue=1, offvalue=0,
		command = print_selection)

c1.pack()
c2.pack()

# Scale 滑动取值
# s = tk.Scale(window, label='Suck my dick', from_=4, to=28, orient=tk.HORIZONTAL, 
# 		length=200, showvalue=1, tickinterval=6, resolution=0.1, command=print_selection)
# s.pack()

window.mainloop()
