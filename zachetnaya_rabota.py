from module1 import*
from tkinter import*
from tkinter.messagebox import*

oige=0

def count(vst,vas):
    global oige,countclck
    countclck+=1
    vastus=vst.get()
    if vastus==vas: 
        oige+=1

def sign():
    global passw,loginas
    f=open('users.txt', 'r')
    userslist=[]
    for stroka in f:
        userslist.append(stroka.strip())
    f.close()
    login=loginas.get()
    if login not in userslist:
        newwd=Toplevel() #tk()
        Label(newwd,text="Kasutaja ei ole olema, palun regestreerida",font="Calibri 20").grid(row=0,column=0)
    else:
        pswords1 = open('pswords.txt', 'r')
        pswords=[]
        for string in pswords1:
            pswords.append(string.strip())
        pswords1.close()
        pswor=passw.get()
        if pswor not in pswords:
            neww=Toplevel() #tk()
            Label(neww,text="Vale parool, proovi uuesti",font="Calibri 20").grid(row=0,column=0)
        else:
            if userslist.index(login) != pswords.index(pswor):
                newwo=Toplevel()
                Label(newwo,text="Vale parool või kasutaja nimi, proovi uuesti",font="Calibri 20").grid(row=0,column=0)
            else:
                mathtest()

def signup():
    global loginas,passw
    f=open('users.txt', 'r')
    users=[]
    for stroka in f:
        users.append(stroka.strip())
    f.close()
    log=loginas.get()
    if askyesno("Parool","Kas sa tahad kasutada automaatseltloomatud parool?"):
        pswordA=autopsword()
        msg=Toplevel()
        if log in users or log=="" or log==" ":
            Label(msg,text="See kasutaja nimi on võetud või vali",font="Calibri 20").grid(row=0,column=0)
        else:
            Label(msg,text="sinu parool: "+pswordA+"\n"+"sinu login: "+log,font="Calibri 20").grid(row=0,column=0)
            with open("users.txt", "a") as user:
                user.write(log+"\n")
            with open("pswords.txt", "a") as pswrd:
                pswrd.write(pswordA + "\n")
            mathtest()

    else:
         psword=passw.get()
         ans=psword_check(psword) #подходит ли пароль
         if ans != True:
             no=Toplevel()
             Label(no,text="Parool ei sobi",font="Calibri 20").grid(row=0,column=0)
         else:
            msg=Toplevel()
            if log in users or log=="" or log==" ":
                Label(msg,text="See kasutaja nimi on võetud või vali",font="Calibri 20").grid(row=0,column=0)
            else:
                Label(msg,text="sinu parool: "+pswordA+"\n"+"sinu login: "+log,font="Calibri 20").grid(row=0,column=0)
                with open("users.txt", "a") as user:
                    user.write(log+"\n")
                with open("pswords.txt", "a") as pswrd:
                    pswrd.write(psword + "\n")
                mathtest()

def mathtest():
    math=Toplevel()
    Label(math,text="Vale tase",font="Calibri 26").grid(row=1,column=0,columnspan=3,sticky=N+S+W+E)
    Label(math,text="Ülesandete arv: ").grid(row=0,column=0,columnspan=2)
    kogus_=Spinbox(math,from_=1,to=25)
    kogus_.grid(row=0,column=2,columnspan=3)
    kog=kogus_.get()
    tase1=Button(math,text="tase 1",font="Calibri 20",command=lambda:tasekaks(kog,math))
    tase1.grid(row=2,column=0,sticky=N+S+W+E)
    tase2=Button(math,text="tase 2",font="Calibri 20",command=lambda:tasekaks(kog,math))
    tase2.grid(row=2,column=1,sticky=N+S+W+E)
    tase3=Button(math,text="tase 3",font="Calibri 20",command=lambda:tasekolm(kog,math))
    tase3.grid(row=2,column=2,sticky=N+S+W+E)
countclck=0
def taseuks(a,math):
    global oige,loginas,countclck
    #command=lambda:math.destroy()
    kog=int(a)
    taseuksTk=Toplevel()
    abc=Label(taseuksTk,text="",font="Arial 20")
    abc.grid(row=0,column=0,columnspan=3,sticky=N+S+W+E)
    countclck=0
    while countclck!=kog:
        arv1=randint(0,100)
        arv2=randint(0,100)
        tehe=randint(1,2)
        if tehe==1:
            mark="+"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1+arv2
        else:
            mark="-"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1-arv2
        vst=Entry(taseuksTk,width=3,font="Arial 20",fg="green",bg="lightblue")
        vst.grid(row=0,column=3)
        entr=Button(taseuksTk,text="Edasi",font="Arial 20",command=count(vst,vas))
        entr.grid(row=1,column=0,columnspan=4)
    result=(oige/kog)*100
    if result>=90:
        hinne="5"
    elif 75<=result<90:
        hinne="4"
    elif 60<=result<75:
        hinne="3"
    else:
        hinne="2"
    abc.destroy()
    res=Label(taseuksTk,text="Sinu hinne on "+hinne+" result on "+round(result,0),font="Arial 20").grid(row=0,column=0)
    if askyesno("result","Kas te tahate salvastada resultat failist"):
        with open("resultFile.txt", "a") as user:
             user.write(loginas.get()+"-"+result+"\n")
    else:
        pass

def resulttable():
    Result={}
    with open("resultFile.txt","r") as f:
	    for i in f: # создаем цикл по кол-ву строк
		    k,v=i.strip().split("-") # отделяем слова на строчке в строчке по знаку "-"
		    Capitals[k.strip()]=v.strip() # добавляем в словарь
    table=""
    table1=""
    for key, value in Result.items():
        table1=table+key+"-"+value+"\n"
    print(table1)

def tasekaks(a,math):
    global oige,loginas
    #command=lambda:math.destroy()
    kog=int(a)
    taseuksTk=Toplevel()
    abc=Label(taseuksTk,text="",font="Arial 20")
    abc.grid(row=0,column=0,columnspan=3,sticky=N+S+W+E)
    for i in range (1,kog+1):
        arv1=randint(-100,100)
        arv2=randint(-100,100)
        tehe=randint(1,4)
        if tehe==1:
            mark="+"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1+arv2
        elif tehe==2:
            mark="-"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1-arv2
        elif tehe==3:
            mark="*"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1*arv2
        else:
            mark="/"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1/arv2
        vst=Entry(taseuksTk,width=3,font="Arial 20",fg="green",bg="lightblue")
        vst.grid(row=0,column=3)
        entr=Button(taseuksTk,text="Edasi",font="Arial 20",command=count(vst,vas))
        entr.grid(row=1,column=0,columnspan=4)
    result=(oige/kog)*100
    if result>=90:
        hinne="5"
    elif 75<=result<90:
        hinne="4"
    elif 60<=result<75:
        hinne="3"
    else:
        hinne="2"

def tasekolm(a,math):
    global oige
    #command=lambda:math.destroy()
    kog=int(a)
    taseuksTk=Toplevel()
    abc=Label(taseuksTk,text="",font="Arial 20")
    abc.grid(row=0,column=0,columnspan=3,sticky=N+S+W+E)
    for i in range (1,kog+1):
        arv1=randint(-200,200)
        arv2=randint(-200,200)
        tehe=randint(1,7)
        if tehe==1:
            mark="+"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1+arv2
        elif tehe==2:
            mark="-"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1-arv2
        elif tehe==3:
            mark="*"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1*arv2
        elif tehe==4:
            mark="//"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1//arv2
        elif tehe==5:
            mark="%"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1%arv2
        elif tehe==6:
            mark="**"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1**arv2
        else:
            mark="/"
            abc.configure(text=str(arv1)+mark+str(arv2)+ "=")
            vas=arv1/arv2
        vst=Entry(taseuksTk,width=3,font="Arial 20",fg="green",bg="lightblue")
        vst.grid(row=0,column=3)
        entr=Button(taseuksTk,text="Edasi",font="Arial 20",command=count(vst,vas))
        entr.grid(row=1,column=0,columnspan=4)
    result=(oige/kog)*100
    if result>=90:
        hinne="5"
    elif 75<=result<90:
        hinne="4"
    elif 60<=result<75:
        hinne="3"
    else:
        hinne="2"



wind=Tk()
wind.title("login ja mateematika")

Label(wind,text="login: ",fg="black").grid(row=1,column=0,sticky=N+S+W+E)
loginas=Entry(wind,bg="lightblue")
loginas.grid(row=1,column=2,columnspan=6,sticky=N+S+W+E)
Label(wind,text="parool: ").grid(row=2,column=0,sticky=N+S+W+E)
passw=Entry(wind,bg="lightblue")
passw.grid(row=2,column=2,columnspan=6,sticky=N+S+W+E)
pres=Button(wind,text="Sise",command=sign)
pres.grid(row=3,column=3,columnspan=4,sticky=N+S+W+E)

reg=Button(wind,text="regestreerimine",fg="black",command=signup)
reg.grid(row=5,column=2,columnspan=6,sticky=N+S+W+E)

wind.mainloop()



