import tkinter as tk
import random
all = 0
bll = 0
a = tk.Tk()
a.geometry("400x600")
a.title("鳥")
x = 50
y = 150
鳥 = tk.Label(a,text="鳥",font=("教育部隸書",25))
鳥.place(x=x,y=y)
def 重力():
    global x,y
    y += 2
    鳥.place(x=x,y=y)
    a.after(10,重力)
重力()
def 跳躍():
    global x,y
    for _ in range(70):
        y -= 1
    鳥.place(x=x,y=y)
跳 = tk.Button(a,text="跳",font=("教育部標準楷書",25),command=跳躍)
跳.place(x=180,y=450)
#地圖
a.configure(bg="skyblue")
果 = tk.Label(text="果",font=("教育部隸書",15))
總數 = tk.Label(text=f"目前得到{all}顆果實\n漏掉{bll}顆果實",font=("教育部隸書",15))
總數.place(x=10,y=10)
gx = 410
gy = 0
def 果循環():
    global 果,gy,gx
    gy = random.randint(10 , 300)
    果.place(x=gx,y=gy)
    def asd():
        global 果,gy,gx,x,y,all,bll
        gx -= 25
        果.place(x=gx,y=gy)
        if gx <= -100:
            bll += 1
            總數.config(text=f"目前得到{all}顆果實\n漏掉{bll}顆果實")
            gy = random.randint(10 , 300)
            gx = 410
            果.place(x=gx,y=gy)
        elif abs(x - gx) <= 30 and abs(y - gy)<= 30:
            all += 1
            總數.config(text=f"目前得到{all}顆果實\n漏掉{bll}顆果實")
            gy = random.randint(10 , 300)
            gx = 410
            果.place(x=gx,y=gy)
        a.after(100 ,asd)
    asd()
果循環()
a.mainloop()
