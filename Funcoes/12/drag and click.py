import tkinter as tk
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage
from functools import partial

root = tk.Tk()
img = Image.open("bk.png")#.resize((400, 650))

back = PhotoImage(img)
fundo = Label(root,image=back,bg="#777777")
fundo.pack()
drag_id = ''
def dragging(event):
    global drag_id
    if event.widget is root:  # do nothing if the event is triggered by one of root's children
        if drag_id == '':
            pass
        else:
            root.after_cancel(drag_id)
        drag_id = root.after(100, stop_drag)
def stop_drag():
    global drag_id
    drag_id = '' 
ee = []
def exemplo(e):
    global ee
    #zzz = e.y
    #zzz2 = e.x
    #ee = [int(zzz),int(zzz2)]
    ee=[e.y,e.x]
sobre_b = False

def moti(e):
    global sobre_b
    
    if sobre_b == False:
        x = root.winfo_pointerx()
        #b = root.winfo_rootx()
        y = root.winfo_pointery()
        #v = root.winfo_rooty()
        #print(x,b,y,v)
        #print(ee)
        root.wm_geometry("400x650+{}+{}".format(x-ee[1],y-ee[0]))
    else:
        sobre_b = False

root.overrideredirect(True)
root.wm_attributes('-topmost','true')
root.config(bg="#343434")
root.wm_attributes("-transparentcolor", "#777777")
root.bind("<ButtonPress-1>", exemplo)
root.bind("<B1-Motion>",moti)
root.bind('<Configure>', dragging)

def ru(a,b,c):
    global sobre_b
    sobre_b = False
def callback3(a,b,c,d):
    global click_and_out
def callback2(a,b,c,d):
    global sobre_b
    sobre_b =True

botoes = []
textoBotao = ["BBBBBB"]
corff = "#333333"
sal = 20
disc = 89
discX = 30
funcao = [ru]
for i in range(10):
    botoes.append(Button(root, text=textoBotao[-1]+str(i),
    fg="#eeeeee",bg="{}".format(corff),
    activebackground="{}".format(corff),
    font=('', sal), border = "0",
    compound="center",command=partial(funcao[-1],i,botoes,root)))
    botoes[-1].bind("<B1-Motion>", partial(callback2,i,botoes,root))
    botoes[-1].bind("<Button-1>", partial(callback3,i,botoes,root))
    botoes[-1].place(x=discX,y=disc)
    disc = disc+54
    discX = discX
    
    

root.mainloop()
