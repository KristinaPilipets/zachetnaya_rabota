from module1 import*
from tkinter import*
from tkinter.messagebox import*

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

def mathtest():
    math=Toplevel()
    Label(math,text="Vale tase",font="Calibri 26").grid(row=1,column=0,columnspan=3,sticky=N+S+W+E)
    Label(text="Ülesandete arv: ").grid(row=0,column=0,columnspan=2)
    kogus=Spinbox(math,from_=1,to=20).grid(row=0,column=1,columnspan=3)
    kog=kogus.get()
    tase1=Radiobutton(math,text="tase 1",font="Calibri 20",command=taseuks(kog))
    tase1.grid(row=2,column=0,sticky=N+S+W+E)
    tase2=Radiobutton(math,text="tase 2",font="Calibri 20",command=tasekaks(kog))
    tase2.grid(row=2,column=1,sticky=N+S+W+E)
    tase3=Radiobutton(math,text="tase 3",font="Calibri 20",command=tasekolm(kog))
    tase3.grid(row=2,column=2,sticky=N+S+W+E)

def taseuks(a):
    kog=a
    taseuksTk=Toplevel()
    for i in range (1,kog+1):
        arv1=randint(0,100)
        arv2=randint(0,100)
        tehe=randint(1,2)
        if tehe==1:
            mark="+"
            Label(taseuksTk,text=arv1+mark+arv2+ "=").grid(row=0,column=0,columnspan=3)
            vas=arv1+arv2
        else:
            mark="-"
            Label(taseuksTk,text=arv1+mark+arv2+ "=").grid(row=0,column=0,columnspan=3)
            vas=arv1-arv2
        vst=Entry(taseuksTk,row=0,column=0)
        vastus=vst.get()
        if vastus==vas: oige+=1

def tasekaks():
    pass

def tasekolm():
    pass



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



