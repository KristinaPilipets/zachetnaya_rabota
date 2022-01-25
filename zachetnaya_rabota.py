from module1 import*
from tkinter import*
from tkinter.messagebox import*

countclck=0
oige=0
vas=0
tex=""

count=lambda vas,vst:
    global countclck,oige
    print(vas,vst)
    countclck+=1
    vastus=vst.get()
    if vastus.isdigit()==True:
        if float(vastus)==float(vas): 
            oige+=1
        else:
            pass
    else:
        pass

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
    #Label(math,text="Ülesandete arv: ").grid(row=0,column=0,columnspan=2)
    #kogus_=Spinbox(math,from_=1,to=25)
    #kogus_.grid(row=0,column=2,columnspan=3)
    #kog=kogus_.get()
    tase1=Button(math,text="tase 1",font="Calibri 20",command=lambda tase=1:taseexc(tase,math))
    tase1.grid(row=2,column=0,sticky=N+S+W+E)
    tase2=Button(math,text="tase 2",font="Calibri 20",command=lambda tase=2:taseexc(tase,math))
    tase2.grid(row=2,column=1,sticky=N+S+W+E)
    tase3=Button(math,text="tase 3",font="Calibri 20",command=lambda tase=3:taseexc(tase,math))
    tase3.grid(row=2,column=2,sticky=N+S+W+E)

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

def exce(tase:int):
    if tase==1:
        arv1=randint(0,100)
        arv2=randint(0,100)
        tehe=randint(1,2)
        if tehe==1:
            mark="+"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1+arv2
        else:
            mark="-"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1-arv2

    elif tase==2:
        arv1=randint(-100,100)
        arv2=randint(-100,100)
        tehe=randint(1,4)
        if tehe==1:
            mark="+"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1+arv2
        elif tehe==2:
            mark="-"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1-arv2
        elif tehe==3:
            mark="*"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1*arv2
        else:
            mark="/"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1/arv2

    else:
        arv1=randint(-200,200)
        arv2=randint(-200,200)
        tehe=randint(1,7)
        if tehe==1:
            mark="+"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1+arv2
        elif tehe==2:
            mark="-"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1-arv2
        elif tehe==3:
            mark="*"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1*arv2
        elif tehe==4:
            mark="//"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1//arv2
        elif tehe==5:
            mark="%"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1%arv2
        elif tehe==6:
            mark="**"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1**arv2
        else:
            mark="/"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1/arv2
    vastt=round(vast,2)
    return vastt,text

def taseexc(tase,math):
    global countclck,taseuksTk,vas,tex
    math.destroy()
    taseuksTk=Toplevel()
    countclck=-1
    oige=0        
    vst=Entry(taseuksTk,width=3,font="Arial 20",fg="green",bg="lightblue")
    vst.grid(row=0,column=3)
    vas,tex=exce(tase)
    abc=Label(taseuksTk,text=tex,font="Arial 20")
    abc.grid(row=0,column=0,columnspan=3,sticky=N+S+W+E)
    entr=Button(taseuksTk,text="Edasi",font="Arial 20",command=lambda:newlah(abc,tase))
    entr.grid(row=1,column=0,columnspan=4)
    vst.bind("<Return>",count(vas,vst))
    end=Button(taseuksTk,text="Lõpetama",font="Arial 20",command=lambda:lopetama(tase))
    end.grid(row=3,column=0,columnspan=4)

def newlah(abc,tase):
    global taseuksTk
    vas,tex=exce(tase)
    abc.destroy()
    ab=Label(taseuksTk,text=tex,font="Arial 20")
    ab.grid(row=0,column=0,columnspan=3,sticky=N+S+W+E)

def lopetama(tase:int):
    global loginas,oige,countclck
    if oige==0 or countclck==0:
        result=0
    else:
        result=oige/countclck*100

    if result>=90:
        hinne="5"
    elif 75<=result<90:
        hinne="4"
    elif 60<=result<75:
        hinne="3"
    else:
        hinne="2"
    taseuTk=Toplevel()
    res=Label(taseuTk,text="Sinu hinne on "+hinne+" result on "+str(round(result,0)),font="Arial 20").grid(row=0,column=0)
    if askyesno("result","Kas te tahate salvastada resultat failist"):
        with open("resultFile.txt", "a") as user:
                user.write(loginas.get()+"-"+str(round(result,2))+str(tase)+" "+"ülisanded arv-"+str(countclck)+"\n")
    else:
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



