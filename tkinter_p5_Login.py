import tkinter as tk
import pickle #存放数据
import tkinter.messagebox


window = tk.Tk()
window.title('Welcome to Mark Python')
window.geometry('450x300')

# Welcome Image
canvas = tk.Canvas(window, height =200, width= 500)
image_file = tk.PhotoImage(file='welcome.gif')
image =canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')


# User Information
tk.Label(window, text='User name:').place(x=50, y=150)
tk.Label(window, text='Password:').place(x=50, y=190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@ncsu.edu')
entry_usr_name = tk.Entry(window,width = 30,textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window,textvariable=var_usr_pwd,width=30,show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
    	with open('usrs_info.pickle','rb') as usr_file:
    		usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
    	with open('usrs_info.pickle','wb') as usr_file:
    		usrs_info = {'admin':'admin'} ##的用户和密码写入，即用户名为`admin`密码为`admin`。
    		pickle.dump(usrs_info,usr_file)
    #如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗`how are you?`加上你的用户名。

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'Mark': '123'}
            pickle.dump(usrs_info, usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            tk.messagebox.showerror(title = 'Error',message='Error, your password is wrong, try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome',
                               'You have not sign up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()


def usr_sign_up():
    def sign_to_Mark_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and comfirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()#关闭窗口

    window_sign_up = tk.Toplevel(window)#弹出新窗口
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()#将输入的注册名赋值给变量
    new_name.set('example@ncsu.edu')#将最初显示定为'example@python.com'
    tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)#将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)#创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=150, y=10)#`entry`放置在坐标（150,10）.

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    # 下面的 sign_to_Mofan_Python 我们再后面接着说
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mark_Python)
    btn_comfirm_sign_up.place(x=150, y=130)

# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)#定义一个`button`按钮，名为`Login`,触发命令为`usr_login`
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)




window.mainloop()
