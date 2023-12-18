from tkinter import *
from PIL import Image, ImageTk
import wolframalpha
import os
flag=0
alf="АаBbСсDdЕеFfGgHhIiKkLlMmNnОоPpQqRrSsTtUuVvXxYyZz,_*+-/|[]"


def proverka():
    if vyraj.get()=="":
        delete["state"]="disabled"
        delete1["state"]="disabled"
    else:
        delete["state"]="normal"
        delete1["state"]="normal"

def otvobr():
    otvet['state'] = 'normal'
    otvet.delete(1.0, END)
    otvet['state'] = 'disabled'

def delete():
    global flag
    if flag==1:
        vyraj.delete(0, END)
        otvobr()
        otvet['state'] = 'normal'
        otvet.insert(1.0, "Здесь будет показан ответ.")
        otvet['state'] = 'disabled'
        proverka()
    else:
        otvet['state'] = 'normal'
        otvet.insert(1.0, "Здесь будет показан ответ.")
        otvet['state'] = 'disabled'
        vyraj.delete(0, END)
        proverka()
    proverka()
    
def delete1():
    ins=vyraj.index(INSERT)
    if len(vyraj.get())==1 and ins!=0:
        otvobr()
        otvet['state'] = 'normal'
        otvet.insert(1.0, "Здесь будет показан ответ.")
        otvet['state'] = 'disabled'
        proverka()
    vyraj.delete(ins-1, INSERT)
    proverka()
        
def kor():
    otvobr()
    vyraj.insert(INSERT, "sqrt(x)")
    proverka()
    
def mod():
    otvobr()
    vyraj.insert(INSERT, "abs(x)")
    proverka()
    
def per():
    otvobr()
    vyraj.insert(INSERT, "x")
    proverka()
    
def stepen():
    otvobr()
    vyraj.insert(INSERT, "^2")
    proverka()
    
def delen():
    otvobr()
    vyraj.insert(INSERT, "/")
    proverka()
    
def umnoj():
    otvobr()
    vyraj.insert(INSERT, "*")
    proverka()
    
def minus():
    otvobr()
    vyraj.insert(INSERT, "-")
    proverka()
    
def plus():
    otvobr()
    vyraj.insert(INSERT, "+")
    proverka()
    
def odin():
    otvobr()
    vyraj.insert(INSERT, "1")
    proverka()
    
def dva():
    otvobr()
    vyraj.insert(INSERT, "2")
    proverka()
    
def tri():
    otvobr()
    vyraj.insert(INSERT, "3")
    proverka()
    
def sem():
    otvobr()
    vyraj.insert(INSERT, "7")
    proverka()
    
def vosem():
    otvobr()
    vyraj.insert(INSERT, "8")
    proverka()
    
def devyat():
    otvobr()
    vyraj.insert(INSERT, "9")
    proverka()
    
def chet():
    otvobr()
    vyraj.insert(INSERT, "4")
    proverka()
    
def pyat():
    otvobr()
    vyraj.insert(INSERT, "5")
    proverka()
    
def shes():
    otvobr()
    vyraj.insert(INSERT, "6")
    proverka()
    
def nol():
    otvobr()
    vyraj.insert(INSERT, "0")
    proverka()
    
def rav():
    otvobr()
    vyraj.insert(INSERT, "=")
    proverka()
    
def zap():
    otvobr()
    vyraj.insert(INSERT, ".")
    proverka()
    
def bol():
    otvobr()
    vyraj.insert(INSERT, ">")
    proverka()
    
def bolr():
    otvobr()
    vyraj.insert(INSERT, ">=")
    proverka()
    
def men():
    otvobr()
    vyraj.insert(INSERT, "<")
    proverka()
    
def menr():
    otvobr()
    vyraj.insert(INSERT, "<=")
    proverka()
    
def sin():
    otvobr()
    vyraj.insert(INSERT, "sin(x)")
    proverka()
    
def cos():
    otvobr()
    vyraj.insert(INSERT, "cos(x)")
    proverka()
    
def tan():
    otvobr()
    vyraj.insert(INSERT, "tan(x)")
    proverka()
    
def ctg():
    otvobr()
    vyraj.insert(INSERT, "cot(x)")
    proverka()
    
def pi():
    otvobr()
    vyraj.insert(INSERT, "pi")
    proverka()
    
def ee():
    otvobr()
    vyraj.insert(INSERT, "e")
    proverka()
    
def ln():
    otvobr()
    vyraj.insert(INSERT, "ln(x)")
    proverka()
    
def lg():
    otvobr()
    vyraj.insert(INSERT, "lg(x)")
    proverka()
    
def logo():
    otvobr()
    vyraj.insert(INSERT, "log(2,x)")
    proverka()
    
def vlev():
    otvobr()
    vyraj.insert(INSERT, "(")
    proverka()
    
def vpra():
    otvobr()
    vyraj.insert(INSERT, ")")
    proverka()
    
def click1():
    r=Toplevel(wind)
    r["bg"]="#fafafa"
    r.title("Справка")
    r.geometry("479x308+1140+250")
    img=ImageTk.PhotoImage(Image.open("spravka.jpg"))
    panel = Label(r, image = img)
    panel.pack()
    r.mainloop()

def click():
    global flag
    vvod=vyraj.get()
    if vvod=="":
        messagebox.showerror('Ошибка!', 'Вы ничего не ввели!')
    else:
        flag=1
        otvobr()
        poisk()
    proverka()

def poisk():
    s=""
    vvod=vyraj.get()
    app_id = "PA7Y36-L7KEQHL4PV"
    client = wolframalpha.Client(app_id)
    res = client.query(vvod)
    for pod in res.pods:
        for sub in pod.subpods:
            if ("="  in vvod) or (">" in vvod) or ("<" in vvod):
                if str(sub.plaintext)!="None": #and not("|" in str(sub.plaintext)) and not("%" in str(sub.plaintext)) and not("digits" in str(sub.plaintext)) and not("is" in str(sub.plaintext)) and not(str(sub.plaintext)[len(str(sub.plaintext))-1]=="."):
                    s+=str(sub.plaintext)+"\n"
            else:
                sign=0
                for i in alf:
                    if i in str(sub.plaintext):
                        sign=1
                        break
                if sign==0:
                    s+=str(sub.plaintext)+"\n"
                else:
                    break
    a=[]
    if "sqrt" in s:
        s=s.replace("sqrt", "√", s.count("sqrt"))
    if "element" in s:
        s=s.replace("element", "∈", s.count("element"))
    otvet["state"]="normal"
    otvet.insert(0.0, s)
    otvet["state"]="disabled"
    proverka()

wind = Tk()
wind["bg"]="#fafafa"
wind.title("Калькулятор+")
#wind.iconbitmap("C:/Users/pivandriy/Desktop/-/нужное/proekt/программа/icon1.ico")
wind.iconbitmap("icon1.ico")
wind.wm_attributes("-alpha")
wind.geometry("334x593+810+250")
wind.resizable(False, False)

frame = Frame(wind, bg="#9dbfb9")
frame.place(relwidth=1, relheight=1)

title = Label(frame, text="Введите выражение", bg="#9dbfb9", font="Calibri 15 bold", )
title.place(x=70, y=2)

vyraj = Entry(frame, bg="#687d79",bd=5, width=34, font="Calibri 13", fg="black", selectbackground="#9dbfb9")
vyraj.focus()
vyraj.place(x=9, y=31)

btn1 = Button(frame, text="Справка",bd=5, bg="black", fg="white",  command=click1, font="Calibri 13 bold", activebackground="#687d79")
btn1.place(x=9, y=70)

btn = Button(frame, text="Ответ", bd=5,bg="black", fg="white", command=click, font="Calibri 13 bold", height=1, width=7, activebackground="#687d79")
btn.place(x=245, y=70)

delete = Button(frame, text="✕",bd=5, bg="black", fg="white", command=delete, font="Calibri 13 bold", height=1, width=6, activebackground="#687d79")
delete.place(x=166, y=70)
delete["state"]="disabled"

delete1 = Button(frame, text="←",bd=5, bg="black", fg="white", command=delete1, font="Calibri 13 bold", height=1, width=6, activebackground="#687d79")
delete1.place(x=91.5, y=70)
delete1["state"]="disabled"

sqrt = Button(frame, text="√x", bg="black",bd=5, fg="white", command=kor, font="Arial 11 bold", height=1, width=2, activebackground="#687d79")
sqrt.place(x=290, y=240)

mod = Button(frame, text="|x|", bg="black", bd=5,fg="white", command=mod, font="Arial 11 bold", height=1, width=2, activebackground="#687d79")
mod.place(x=290, y=200)

per = Button(frame, text="x", bg="black", bd=5,fg="white", command=per, font="Arial 11 bold", height=1, width=2, activebackground="#687d79")
per.place(x=290, y=120)

stepen = Button(frame, text="x²", bg="black",bd=5, fg="white", command=stepen, font="Arial 11 bold", height=1, width=2, activebackground="#687d79")
stepen.place(x=290, y=160)

delen = Button(frame, text="/", bg="black",bd=5, fg="white", command=delen, font="Arial 11 bold", height=1, width=2, activebackground="#687d79")
delen.place(x=202, y=120)

umnoj = Button(frame, text="*", bg="black",bd=5, fg="white", command=umnoj, font="Arial 11 bold", height=1, width=2, activebackground="#687d79")
umnoj.place(x=202, y=160)

minus = Button(frame, text="-", bg="black", bd=5,fg="white", command=minus, font="Arial 11 bold", height=1, width=2, activebackground="#687d79")
minus.place(x=202, y=200)

plus = Button(frame, text="+", bg="black", bd=5,fg="white", command=plus, font="Arial 11 bold", height=1, width=2, activebackground="#687d79")
plus.place(x=202, y=240)

odin = Button(frame, text="1", bd=5, bg="black", fg="white", command=odin,  font="Arial 11 bold", height=1, width=5, activebackground="#687d79")
odin.place(x=10, y=120)

dva = Button(frame, text="2", bd=5,bg="black", fg="white", command=dva,  font="Arial 11 bold", height=1, width=5, activebackground="#687d79")
dva.place(x=73, y=120)

tri = Button(frame, text="3",bd=5, bg="black", fg="white", command=tri,  font="Arial 11 bold ", height=1, width=5, activebackground="#687d79")
tri.place(x=136, y=120)

sem = Button(frame, text="7", bd=5,bg="black", fg="white", command=sem,  font="Arial 11 bold", height=1, width=5, activebackground="#687d79")
sem.place(x=10, y=200)

vosem = Button(frame, text="8",bd=5, bg="black", fg="white", command=vosem,  font="Arial 11 bold", height=1, width=5, activebackground="#687d79")
vosem.place(x=73, y=200)

devyat = Button(frame, text="9", bd=5,bg="black", fg="white", command=devyat,  font="Arial 11 bold", height=1, width=5, activebackground="#687d79")
devyat.place(x=136, y=200)

chet = Button(frame, text="4",bd=5, bg="black", fg="white", command=chet,  font="Arial 11 bold", height=1, width=5, activebackground="#687d79")
chet.place(x=10, y=160)

pyat = Button(frame, text="5", bd=5,bg="black", fg="white", command=pyat,  font="Arial 11 bold", height=1, width=5, activebackground="#687d79")
pyat.place(x=73, y=160)

shes = Button(frame, text="6",bd=5, bg="black", fg="white", command=shes,  font="Arial 11 bold", height=1, width=5, activebackground="#687d79")
shes.place(x=136, y=160)

nol = Button(frame, text="0",bd=5, bg="black", fg="white", command=nol,  font="Arial 11 bold", height=1, width=5, activebackground="#687d79")
nol.place(x=10, y=240)

rav = Button(frame, text="=", bd=5,bg="black", fg="white", command=rav,  font="Arial 11 bold", height=1, width=5, activebackground="#687d79")
rav.place(x=136, y=240)

zap = Button(frame, text=".",bd=5, bg="black", fg="white", command=zap,  font="Arial 11 bold", height=1, width=5, activebackground="#687d79")
zap.place(x=73, y=240)

bol = Button(frame, text=">", bd=5,bg="black", fg="white", command=bol, font="Arial 11 bold", height=1, width=3, activebackground="#687d79")
bol.place(x=245, y=120)

bolr = Button(frame, text="≥",bd=5, bg="black", fg="white", command=bolr, font="Arial 11 bold", height=1, width=3, activebackground="#687d79")
bolr.place(x=245, y=160)

men = Button(frame, text="<", bd=5,bg="black", fg="white", command=men, font="Arial 11 bold", height=1, width=3, activebackground="#687d79")
men.place(x=245, y=200)

menr = Button(frame, text="≤",bd=5, bg="black", fg="white", command=menr, font="Arial 11 bold", height=1, width=3, activebackground="#687d79")
menr.place(x=245, y=240)

sin = Button(frame, text="sinx",bd=5, bg="black", fg="white", command=sin, font="Arial 10 bold", height=1, width=7, activebackground="#687d79")
sin.place(x=10, y=288)

cos = Button(frame, text="cosx", bd=5,bg="black", fg="white", command=cos, font="Arial 10 bold", height=1, width=7, activebackground="#687d79")
cos.place(x=90, y=288)

tan = Button(frame, text="tanx", bd=5,bg="black", fg="white", command=tan, font="Arial 10 bold", height=1, width=7, activebackground="#687d79")
tan.place(x=170.5, y=288)

ctg = Button(frame, text="ctgx",bd=5, bg="black", fg="white", command=ctg, font="Arial 10 bold", height=1, width=7, activebackground="#687d79")
ctg.place(x=252, y=288)

pi = Button(frame, text="π",bd=5, bg="black", fg="white", command=pi, font="Arial 10 bold", height=1, width=4, activebackground="#687d79")
pi.place(x=10, y=325)

ee = Button(frame, text="e", bd=5,bg="black", fg="white", command=ee, font="Arial 10 bold", height=1, width=4, activebackground="#687d79")
ee.place(x=62.5, y=325)

logo = Button(frame, text="log₂x",bd=5, bg="black", fg="white", command=logo, font="Arial 10 bold", height=1, width=7, activebackground="#687d79")
logo.place(x=115, y=325)

lg = Button(frame, text="lgx",bd=5, bg="black", fg="white", command=lg, font="Arial 10 bold", height=1, width=6, activebackground="#687d79")
lg.place(x=191, y=325)

ln = Button(frame, text="lnx",bd=5, bg="black", fg="white", command=ln, font="Arial 10 bold", height=1, width=6, activebackground="#687d79")
ln.place(x=260, y=325)

vlev = Button(frame, text="(",bd=5, bg="black", fg="white", command=vlev, font="Arial 10 bold", height=1, width=17, activebackground="#687d79")
vlev.place(x=10, y=363)

vpra = Button(frame, text=")", bd=5,bg="black", fg="white", command=vpra, font="Arial 10 bold", height=1, width=17, activebackground="#687d79")
vpra.place(x=170.5, y=363)

otvet=Text(frame,bd=5, width=34, height=8, bg="#687d79", fg="black", font="Calibri 13 italic", wrap=WORD, selectbackground="#9dbfb9")
otvet.place(x=9, y=405)
otvet.insert(1.0, "Здесь будет показан ответ.")
otvet['state'] = 'disabled'

wind.mainloop()