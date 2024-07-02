from tkinter import *
import math
screen = Tk()
screen.configure(bg='red')
screen.title('Smart Calculator')
screen.geometry('440x410')


def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)

def equal():
    global operator
    result = eval(operator)
    operator= str(result)
    tex.set(result)

def cmsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...',parent=win)

def cmcos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...',parent=win)

def cmtan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...',parent=win)

def cmsqrt():
    global operator
    try:    
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...',parent=win)

def cmlog():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...',parent=win)

tex = StringVar()
operator = ''

########################################################## 
#################################  Entry Box

entry1 = Entry(screen,bg='CornflowerBlue',font=('arial',20,'italic bold'),bd='20',insertwidth=4,justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)

################################  End Entry Box
########################################################## 


########################################################## 
#############################  Buttons

btn7 =  Button(screen,text='7',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(7),
                activebackground='DarkMagenta',activeforeground='cyan')
btn7.grid(row=1,column=0)

btn8 =  Button(screen,text='8',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(8),
                activebackground='DarkMagenta',activeforeground='cyan')
btn8.grid(row=1,column=1)

btn9 =  Button(screen,text='9',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(9),
                activebackground='DarkMagenta',activeforeground='cyan')
btn9.grid(row=1,column=2)

btnAdd =  Button(screen,text='+',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('+'),
                activebackground='DarkMagenta',activeforeground='cyan')
btnAdd.grid(row=1,column=3)

btn4 =  Button(screen,text='4',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(4),
                activebackground='DarkMagenta',activeforeground='cyan')
btn4.grid(row=2,column=0)

btn5 =  Button(screen,text='5',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(5),
                activebackground='DarkMagenta',activeforeground='cyan')
btn5.grid(row=2,column=1)

btn6 =  Button(screen,text='6',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(6),
                activebackground='DarkMagenta',activeforeground='cyan')
btn6.grid(row=2,column=2)

btnSub =  Button(screen,text='-',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('-'),
                activebackground='DarkMagenta',activeforeground='cyan')
btnSub.grid(row=2,column=3)

btn3 =  Button(screen,text='3',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(3),
                activebackground='DarkMagenta',activeforeground='cyan')
btn3.grid(row=3,column=0)

btn2 =  Button(screen,text='2',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(2),
                activebackground='DarkMagenta',activeforeground='cyan')
btn2.grid(row=3,column=1)

btn1 =  Button(screen,text='1',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(1),
                activebackground='DarkMagenta',activeforeground='cyan')
btn1.grid(row=3,column=2)

btnDiv =  Button(screen,text='/',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('/'),
                activebackground='DarkMagenta',activeforeground='cyan')
btnDiv.grid(row=3,column=3)

btn0 =  Button(screen,text='0',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(0),
                activebackground='DarkMagenta',activeforeground='cyan')
btn0.grid(row=4,column=0)

btnclear =  Button(screen,text='c',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=clear,
                activebackground='DarkMagenta',activeforeground='cyan')
btnclear.grid(row=4,column=1)

btnMulti =  Button(screen,text='*',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('*'),
                activebackground='DarkMagenta',activeforeground='cyan')
btnMulti.grid(row=4,column=2)

btnEql =  Button(screen,text='=',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=equal,
                activebackground='DarkMagenta',activeforeground='cyan')
btnEql.grid(row=4,column=3)

btnSin =  Button(screen,text='Sin',font=('arial',17,'italic bold'),bd=8,padx=16,pady=16,command=cmsin,
                activebackground='DarkMagenta',activeforeground='cyan')
btnSin.grid(row=1,column=4)

btnCos =  Button(screen,text='Cos',font=('arial',17,'italic bold'),bd=8,padx=16,pady=16,command=cmcos,
                activebackground='DarkMagenta',activeforeground='cyan')
btnCos.grid(row=2,column=4)

btnTan =  Button(screen,text='Tan',font=('arial',17,'italic bold'),bd=8,padx=16,pady=16,command=cmtan,
                activebackground='DarkMagenta',activeforeground='cyan')
btnTan.grid(row=3,column=4)

btnSqrt =  Button(screen,text='sqrt',font=('arial',17,'italic bold'),bd=8,padx=16,pady=16,command=cmsqrt,
                activebackground='DarkMagenta',activeforeground='cyan')
btnSqrt.grid(row=4,column=4)

btnLog =  Button(screen,text='Log',font=('arial',17,'italic bold'),bd=8,padx=16,pady=16,command=cmlog,
                activebackground='DarkMagenta',activeforeground='cyan')
btnLog.grid(row=0,column=4)

#############################  Buttons End
########################################################## 

screen.mainloop()