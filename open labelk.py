import labelfacil

idlepath = r"C:\Users\Ray-pc\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\IDLE (Python 3.7 32-bit).lnk"
path_daniel=r"C:\NCS\versoes\Daniel\danielFronter - Atalho.lnk"
path_marcio =r"C:\NCS\versoes\Marcio\marcioFronter - Atalho.lnk"
path_build = r"C:\NCS\versoes\Build.lnk"
path_senha = r"C:\NCS\versoes\Daniel\pass.py"
path_sqllock = r"C:\Users\Ray-pc\Desktop\SET PAR_VERSION.pyw"

#funcao base para abrir arquivo
def start_file(file):
    os.startfile(file)
    
def restart(a,b,c):
    start_file(path_sqllock)
def build_open(a,b,c):
    start_file(path_build)
def senha_copy(a,b,ro):
    start_file(path_senha)
def daniel_open(a,b,ro):
    start_file(path_daniel)
    
def pp(a,b,ro):
    width = ro.winfo_screenwidth()
    #height = ro.winfo_screenheight()
    #ro.geometry("10x{}+{}+{}".format(height,width,0))
    ro.geometry("200x{}+{}+{}".format(1100,width,0))
def posi_normal(a,b,ro):
    #width = ro.winfo_screenwidth()
    #height = ro.winfo_screenheight()
    #ro.geometry("10x{}+{}+{}".format(height,width,0))
    ro.geometry("200x{}+{}+{}".format(1100,0,0))
def qui(a,b,c):
    quit()

func = [pp,posi_normal]
with open("botoes.txt","r") as lklk:
    bb2= lklk.read()
    bb = bb2.split(",")
labelfacil.button(bb,"exemplo",func,1,sal=15)
