from random import *
s=nol=pos=neg=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => ")) 
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
        generaator(n,s,mini,maxi)
        print()
        print("Результаты:")
        print("Полученный список от",mini,"до",maxi,s)
        s.sort()
        print("Отсортированный список",s)
        jagamine(s,pos,neg,nol)
        print("Список положительных элементов",pos)
        print("Список отрицательных элементов",neg)
        print("Список нулевых элементов",nol)
        kesk=keskmine(pos)
        lisamine(s,kesk)
        print("Среднее положительных:",kesk)
        kesk=keskmine(neg)
        isamine(s,kesk)
        print("Среднее отрицательных:",kesk)
        print("Добавляем средние в изначалный массив:")
        s.sort()
        print(s)

def vahetus(a:int,b:int):
    '''Kui a>b siis vahetame neid
    :param int a: Arv, mis on suurem kui b
    :param int b: Arv, mis on väiksem kui a
    :rtype:int,int
    '''
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    '''Kui a>b siis vahetame neid
    :param int n: skolko 4icel
    :param list loend: 4itaet i zanoscit v spisok 4icla
    :param int a: minimalnoe 4iclo
    :param int b: maksimalnoe 4iclo
    '''
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:int,n:int,nol:int):
    '''
    :param list loend: 4itaet i zanoscit v spisok 4icla
    :param int p: polozitelnie 
    :param int n: otricatelnie
    :param int nol: nulevie
    '''
    for el in loend:
        if el>0:
            p(append(pos))
        elif el<0:
            n(append(neg))
        else:
            nol(append(nol))

def keskmine(loend:list):
    '''
    :param list loend: 4itaet i zanoscit v spisok 4icla
    '''
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:int):
    '''
    :param list loend: 4itaet i zanoscit v spisok 4icla
    :param int el:
    '''
    loend(append(el))
    loend(sort)

arvud_loendis()

