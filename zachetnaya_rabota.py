from module1 import*
from tkinter import*
from tkinter.messagebox import*
oige=0
countclck=0
vas=0
tex=""

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
        Label(newwd,text="Kasutaja ei ole olema, palun regestreerida",font="Arial 15").grid(row=0,column=0)
    else:
        pswords1 = open('pswords.txt', 'r')
        pswords=[]
        for string in pswords1:
            pswords.append(string.strip())
        pswords1.close()
        pswor=passw.get()
        if pswor not in pswords:
            neww=Toplevel() #tk()
            Label(neww,text="Vale parool, proovi uuesti",font="Arial 15").grid(row=0,column=0)
        else:
            if userslist.index(login) != pswords.index(pswor):
                newwo=Toplevel()
                Label(newwo,text="Vale parool või kasutaja nimi, proovi uuesti",font="Arial 15").grid(row=0,column=0)
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
        if log in users or log=="" or log==" " or len(log)<=4:
            Label(msg,text="See kasutaja nimi on võetud või vale (min 4 sümbolid)",font="Arial 15").grid(row=0,column=0)
        else:
            Label(msg,text="sinu parool: "+pswordA+"\n"+"sinu login: "+log,font="Arial 15").grid(row=0,column=0)
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
            if log in users or log=="" or log==" " or len(log)<=4:
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
            Result[k.strip()]=v.strip() # добавляем в словарь
    table=""
    table1=[]
    for key, value in Result.items():
        table=key+"-"+value+"\n"
        table1.append(table)
    ta=Toplevel()
    table=Label(ta,text="".join(table1),font="Arial 26").grid(row=0,column=0)

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
        tehe=randint(1,6)
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
        else:
            mark="/"
            text=str(arv1)+mark+str(arv2)+ "="
            vast=arv1/arv2
    vastt=round(vast,0)
    return vastt,text

def taseexc(tase,math):
    global taseuksTk,vas,tex,oige    
    math.destroy()
    taseuksTk=Toplevel()   
    vst=Entry(taseuksTk,width=5,font="Arial 20",fg="green",bg="lightblue")
    vst.grid(row=0,column=3)
    abc=Label(taseuksTk,text="",font="Arial 20",width=10)
    vas,tex=exce(tase)
    abc.configure(text=tex)
    abc.grid(row=0,column=0,columnspan=3,sticky=N+S+W+E)
    entr=Button(taseuksTk,text="Edasi",font="Arial 20",command=lambda:newlah(abc,tase))
    entr.grid(row=1,column=0,columnspan=4)
    vst.bind("<Return>",lambda abcd:count(vas,vst))
    end=Button(taseuksTk,text="Lõpetama",font="Arial 20",command=lambda:lopetama(tase))
    end.grid(row=3,column=0,columnspan=4)

def count(vas,vst):
    global countclck,oige
    countclck+=1
    vastus=vst.get()
    if vastus.isdigit()==True:
        if int(vas)==int(vastus): 
            oige+=1
        else:
            pass
    else:
        pass
    print(vas,vst.get(),countclck,oige)

def newlah(abc,tase):
    global taseuksTk,vas,countclck
    vas,tex=exce(tase)
    abc.configure(text=tex)

def lopetama(tase:int):
    global loginas,oige,countclck
    taseuksTk.destroy()
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
                user.write(loginas.get()+"-"+str(round(result,0))+"%"+" "+" tase: "+str(tase)+" ülisanded arv: "+str(countclck)+"\n")
    else:
        pass
    if askyesno("resultat","Kas te tahate näha teiste reultatid?"):
        resulttable()
    else:
        pass


wind=Tk()
wind.title("login ja mateematika")

Label(wind,text="login: ",fg="black",font="Arial 17").grid(row=1,column=0,sticky=N+S+W+E)
loginas=Entry(wind,bg="lightblue")
loginas.grid(row=1,column=2,columnspan=6,sticky=N+S+W+E)
Label(wind,text="parool: ",font="Arial 17").grid(row=2,column=0,sticky=N+S+W+E)
passw=Entry(wind,bg="lightblue")
passw.grid(row=2,column=2,columnspan=6,sticky=N+S+W+E)
pres=Button(wind,text="Sise",font="Arial 15",command=sign)
pres.grid(row=3,column=3,columnspan=4,sticky=N+S+W+E)

reg=Button(wind,text="regestreerimine",font="Arial 15",fg="black",command=signup)
reg.grid(row=5,column=2,columnspan=6,sticky=N+S+W+E)

wind.mainloop()



