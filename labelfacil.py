from tkinter import *
from functools import partial

botoes = []
def button(textoBotao,info,funcao,exib=1,sal=9):
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    #root.geometry("682x1250+3170+0")
    root.geometry("200x{}+{}+{}".format(1100,0,0))
    root.config(bg="#343434")
    root.overrideredirect(1)
    #root.wm_attributes('-topmost',0)
    root.wm_attributes('-topmost','true')
    root.wm_attributes("-transparentcolor", "#343434")
    
    if len(funcao) > 0:
        funcao = funcao*len(textoBotao)
    loadimage = PhotoImage(file="b1-50.png")
    loadimage2 = PhotoImage(file="bbb2.png")
    disc = 132
    def callback(a,b,c,d):
        #print(a)
        #print(b)
        #print(b[a])
        b[a].config(image=loadimage2)
    def callback2(a,b,c,d):
        #print(a)
        #print(b)
        #print(b[a])
        b[a].config(image=loadimage)
    for i in range(0,len(textoBotao)):
        #var = StringVar()
        #print(hex(65+(i*4))[2:])
        label = Label( root, textvariable=info )
        corff = hex(45+(i*8))[2:]
        botoes.append(Button(root, text=textoBotao[i],
        fg="#eeeeee",bg="#3535{}".format(corff),
        activebackground="#3535{}".format(corff),
        font=('', sal), border = "0",image=loadimage,
        compound="center",command=partial(funcao[i],i,botoes,root)))
        botoes[-1].bind("<Button-1>", partial(callback,i,botoes,root))
        botoes[-1].bind("<ButtonRelease-1>", partial(callback2,i,botoes,root))
        botoes[-1].place(x=0,y=disc)
        disc = disc+54
        #botoes[-1].pack(side=TOP,anchor=NW, expand=NO, fill=NONE)
    loe = PhotoImage(file="ll33.png")
    logo = Label(width = 300,bg="#333333",image=loe)
    #logo.place(x=0,y=0)
    logo.pack()
    root.mainloop()







    
