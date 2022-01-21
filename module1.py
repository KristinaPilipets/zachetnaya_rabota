from random import*

def psword_check(psword:str)->bool:
    """функция вернет True если пароль будет соответствовать всем параметрам
    """
    digit="d"
    alpha="a"
    upper="e"
    lower="f"
    symbl="w"
    if len(psword)!=12:
        ans=False
    else:
        psword=list(psword)
        for i in psword:
            if i.isdigit()== True: #string index out of range
                digit="True"
            if i.isalpha()== True:
                alpha="True"
            if i.isupper()== True:
                upper="True"
            if i.islower()==True:
                lower="True"
            if i in [".","_","/","@"]:
                symbl="True"
        if digit=="True" and upper=="True" and alpha=="True" and lower=="True" and symbl=="True": 
            ans=True
        else:
            ans=False
    return ans
def autopsword()->str:
    """automaatseltloomatud parool
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    #print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3 #сплошной текст со всеми str
    ls = list(str4) #создает список значений каждый символ через запятую ["q","w","1"...и тд]
    shuffle(ls) #перемешиваем значения
    psword = "".join([choice(ls) for x in range(12)]) # Извлекаем из списка 12 произвольных значений
    # Пароль готов
    return psword

def abcde():
    oige=0
    kogus=0
    #tase 1 +,-,0-100
    #tase 2 +,-,*,/, -100-100
    #tase 3 +,-,*,/,//,%,** -200-200
    if tase==1:
        pass
    elif tase==2:
        kogus=int(input("Ülesandete arv: "))
        for i in range (1,kogus+1):
            arv1=randint(-100,100)
            arv2=randint(-100,100)
            tehe=randint(1,4)
            if tehe==1:
                mark="+"
                print(f"{arv1} {mark} {arv2} =")
                vas=arv1+arv2
            elif tehe==2:
                mark="-"
                print(f"{arv1} {mark} {arv2} =")
                vas=arv1-arv2
            elif tehe==3:
                mark="*"
                print(f"{arv1} {mark} {arv2} =")
                vas=arv1*arv2
            else:
                mark="/"
                print(f"{arv1} {mark} {arv2} =")
                vas=arv1/arv2
            vastus=int(input())
            if vastus==vas: oige+=1
    else:
        kogus=int(input("Ülesandete arv: "))
        for i in range (1,kogus+1):
            arv1=randint(-200,200)
            arv2=randint(-200,200)
            tehe=randint(1,7)
            if tehe==1:
                mark="+"
                print(f"{arv1} {mark} {arv2} =")
                vas=arv1+arv2
            elif tehe==2:
                mark="-"
                print(f"{arv1} {mark} {arv2} =")
                vas=arv1-arv2
            elif tehe==3:
                mark="*"
                print(f"{arv1} {mark} {arv2} =")
                vas=arv1*arv2
            elif tehe==4:
                mark="//"
                print(f"{arv1} {mark} {arv2} =")
                vas=arv1//arv2
            elif tehe==5:
                mark="%"
                print(f"{arv1} {mark} {arv2} =")
                vas=arv1%arv2
            elif tehe==6:
                mark="**"
                print(f"{arv1} {mark} {arv2} =")
                vas=arv1**arv2
            else:
                tehe="/"
                print(f"{arv1} {mark} {arv2} =")
                vas=arv1/arv2
            vastus=int(input("Vastus= "))
            if vastus==round(vas): 
                oige+=1
    if (oige/kogus)*100>=90:
        hinne="5"
    elif 75<=(oige/kogus)*100<90:
        hinne="4"
    elif 60<=(oige/kogus)*100<75:
        hinne="3"
    else:
        hinne="2"
    print(f"Kokku oli {kogus} ülesandeid, õigesti oli lahendatud {oige} \n Sinu hinne on {hinne}")