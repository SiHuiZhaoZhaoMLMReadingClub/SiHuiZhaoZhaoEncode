import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import filedialog
from tkinter import ttk
import base64
import pyperclip
import random
from os import getcwd
import os
import time

class FileEncode(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(bg="#CD5C5C")
        self.geometry("600x700")
        self.title("文件加密程序")
        self.iconbitmap(".\logo.gif")
        self.mdvar = tk.StringVar()
        self.mdvar.set("ECB")
        tk.Label(self, text="这是此程序的文件加密部分",\
            bg="#CD5C5C",\
            font=("方正姚体", 18),\
            fg="gold").pack(side=tk.TOP)
        tk.Label(self, text="请输入文件地址：",\
            bg="#CD5C5C",\
            font=("方正姚体", 18),\
            fg="gold").pack(side=tk.TOP, padx=10)
        self.path = tk.Entry(self, font="华文中宋")
        self.path.pack(padx=10, fill=tk.X, side=tk.TOP)
        tk.Button(self, command=self._openfile, text="选择", fg="#dbac10", bg="#fff897", font="华文中宋").pack(pady=5, side=tk.TOP)
        tk.Label(self, text="请输入文件密码：",\
            bg="#CD5C5C",\
            font=("方正姚体", 18),\
            fg="gold").pack(side=tk.TOP, padx=10)
        self.psw = tk.Entry(self, font="华文中宋")
        self.psw.pack(padx=10, fill=tk.X, side=tk.TOP)
        tk.Button(self, command=self._encode, text="加密文件", fg="#dbac10", bg="#fff897", font="华文中宋").pack(pady=5, side=tk.TOP)
        tk.Button(self, command=self._decode, text="解密文件", fg="#dbac10", bg="#fff897", font="华文中宋").pack(pady=5, side=tk.TOP)
        tk.Button(self, command=self._exit, text="退出", fg="#dbac10", bg="#fff897", font="华文中宋").pack(pady=5, side=tk.BOTTOM)
        self.mainloop()

    def crypto(self):
        win = tk.Toplevel(master=self)
        win.geometry("200x100")
        win.configure(bg="#CD5C5C")
        win.title("进度条")
        tk.Label(win, text="这是进度条", bg="#CD5C5C", fg="gold", font=("方正姚体", 16)).pack(side=tk.TOP)
        pro = ttk.Progressbar(win, mode="determinate", value=0, max=200, length=200)
        pro.pack(side=tk.TOP)
        for i in range(200):
            time.sleep(0.05)
            pro["value"] += 1
        os.system("start https://www.bilibili.com/video/BV1GJ411x7h7/")
        if msgbox.askokcancel(title="你被骗了", message="哈哈哈，你被骗了！由于加密程序没来得及做好，先点击确定，打开别人的加密程序吧。"):
            os.system("BitMapGUI.exe")

    def _openfile(self):
        self.path.delete("0", "end")
        self.path.insert("0", filedialog.askopenfilename())

    def _encode(self):
        self.crypto()

    def _decode(self):
        self.crypto()

    def _exit(self):
        res = msgbox.askokcancel(message="确认要退出文件加密窗口吗？", title="确认退出")
        if res:
            self.destroy()

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        menubar = tk.Menu(self)
        mfile = tk.Menu(menubar, tearoff=0)
        mfile.add_command(label="退出", command=self._exit)
        menubar.add_cascade(label="文件", menu=mfile)
        mhelp = tk.Menu(menubar, tearoff=0)
        mhelp.add_command(label="关于...", command=self._about)
        menubar.add_cascade(label="帮助", menu=mhelp)
        self.str = "qwertyuiop[]asdfghjklzxcvnm./;()*&^%$#@!~"
        self.geometry("800x900")
        self.title("左人的秘制加密解密程序")
        self.iconphoto(True, tk.PhotoImage(file=getcwd() + "\logo.gif"))
        self.config(menu=menubar)
        self.configure(bg="#CD5C5C")
        l0 = tk.Label(self, text="同志，您好，欢迎来到我的电脑端文字、文件、图片加密软件",\
            bg="#CD5C5C",\
            font=("方正姚体", 18),\
            fg="gold")
        l0.pack(side=tk.TOP)
        l1 = tk.Label(self, text="这是左人们秘制的加密程序，使用nuitka打包并加密，网警就别想破解了",\
            bg="#CD5C5C",\
            font=("方正姚体", 18),\
            fg="gold")
        l1.pack(side=tk.TOP)
        l2 = tk.Label(self, text="请输入您想加密或解密的文字：",\
            bg="#CD5C5C",\
            font=("方正姚体", 18),\
            fg="gold")
        l2.pack(side=tk.TOP)
        self.e1 = tk.Entry(self, font="华文中宋")
        self.e1.pack(side=tk.TOP, padx=0, pady=20, fill=tk.X)
        l3 = tk.Label(self, text="请输入随机掺杂次数：",\
            bg="#CD5C5C",\
            font=("方正姚体", 18),\
            fg="gold")
        l3.pack(side=tk.TOP)
        self.e3 = tk.Entry(self, font="华文中宋")
        self.e3.pack(side=tk.TOP, padx=0, pady=20)
        btn1 = tk.Button(self, command=self.__clear, text="一键清除", fg="#dbac10", bg="#fff897", font="华文中宋")
        btn1.pack(pady=5, side=tk.TOP)
        btn1 = tk.Button(self, command=self.__paste, text="一键粘贴", fg="#dbac10", bg="#fff897", font="华文中宋")
        btn1.pack(pady=5, side=tk.TOP)
        btn_encode = tk.Button(self, command=self._encode, text="加密", fg="#dbac10", bg="#fff897", font="华文中宋")
        btn_encode.pack(pady=5, side=tk.TOP)
        btn_decode = tk.Button(self, command=self._decode, text="解密", fg="#dbac10", bg="#fff897", font="华文中宋")
        btn_decode.pack(pady=5, side=tk.TOP)
        btn_exit = tk.Button(self, command=self._exit, text="退出", fg="#dbac10", bg="#fff897", font="华文中宋")
        btn_exit.pack(pady=5, side=tk.TOP)
        btn_openf = tk.Button(self, command=self._openf, text="打开文件加密部分", fg="#dbac10", bg="#fff897", font="华文中宋")
        btn_openf.pack(pady=5, side=tk.TOP)
        self.mainloop()

    def _decode(self):
        n = self.e1.get()
        a = base64.b64decode(n).decode()
        b = ""
        for i in a:
            if not i in self.str:
                b += i
        c = ""
        p = ""
        for i in b:
            if i == ",":
                c += chr(int(p))
                p = ""
                continue
            p += i
        ans = c
        if msgbox.askokcancel(title="结果显示", message="结果为:\n"+ans+"\n请选择是否要复制结果"):
            pyperclip.lazy_load_stub_copy(ans)

    def _encode(self):
        if self.e3.get() == "":
            tmp = 0
        else:
            try:
                tmp = int(self.e3.get())
            except TypeError:
                msgbox.showerror("请输入一个有效数字")
                return
        if tmp <= 10:
            msgbox.showwarning(title="警告", message="掺杂次数过低会导致安全性减弱。同志，请您最好增加参杂次数。")
        a = self.e1.get()
        b = ""
        for i in a:
            b += str(ord(i)) + ","
        x = len(b)
        k = [i for i in b]
        for _ in range(tmp):
            k.insert(random.randint(0, x - 1), random.choice(self.str))
        b = ""
        for i in k:
            b += i
        ans = base64.b64encode(b.encode()).decode()
        if msgbox.askokcancel(title="结果显示", message="结果为:\n"+ans+"\n请选择是否要复制结果"):
            pyperclip.lazy_load_stub_copy(ans)

    def __clear(self):
        res = msgbox.askokcancel(message="是否清除文本框内所有文字？", title="确认清除")
        if res:
            self.e1.delete("0", "end")

    def __paste(self):
        res = msgbox.askokcancel(message="是否清除文本框内所有文字以粘贴新的文字？", title="确认清除")
        if res:
            self.e1.delete("0", "end")
            self.e1.insert("0", pyperclip.paste())

    def _exit(self):
        res = msgbox.askokcancel(message="确认要退出吗？", title="确认退出")
        if res:
            self.destroy()

    def _openf(self):
        FileEncode()

    def _about(self):
        win = tk.Toplevel(master=self)
        win.geometry("600x500+0+0")
        win.configure(bg="#CD5C5C")
        win.title("关于")
        tk.Label(win, text="关于本软件的信息", bg="#CD5C5C", fg="gold", font=("方正姚体", 16)).pack(side=tk.TOP)
        tk.Label(win, text="""
同志，您好。本软件旨在能让网警无法获取聊天的文字信息以让各位同志能够更方
便地交流。但是，本软件的安全性尚且不足，仍需改进，因此我劝各位同志千万不
要掉以轻心，网警是有可能破解的。本软件归“思辉昭昭马列主义学习群”所有。本
软件也最好不要传播出去，除非在完全信赖的情况下。
以下是说明：
文本框可填入要加密或解密的文字，一键清除则是为了快速清除文本框内文字，粘
贴会清除文本框并粘贴您所复制的文字。掺杂次数是我研制的掺杂加密法，掺杂越
多，越安全，但是加密后的文字越长，因此，越敏感的信息掺杂次数应越长。文件
解密需要正确的密码，否则保存的文件无法使用。本软件与我的网页端用的不是一
种加密方式，不是互通的，因此不能混用。网站用到了摩尔斯电码，因此字母不分
大小写，空格、回车等会消失，因此本加密软件的加密结果不能再我的网站上二次
加密，但是反着可以（网站上加密后在这里二次加密）。
以下是此软件的版本号：
alpha2.0
qq：@乙烯一克一克 于2024.8.11日编写
""", bg="#CD5C5C", fg="gold", font=("方正姚体", 12)).pack(padx=5, pady=5)
        tk.Label(win, text="全世界无产者，联合起来！\n★", bg="#CD5C5C", fg="gold", font=("方正姚体", 14)).pack(side=tk.BOTTOM)
        win.mainloop()

if __name__ == "__main__":
    Application()
