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
