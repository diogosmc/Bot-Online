from time import sleep
import sys
from colorama import Fore
from time import localtime, mktime, sleep
from datetime import *
from blocon import *

def ver_tempo(tempo):
    
    if len(tempo) != 8:
        print(Fore.RED+'ERRO: Tente Novamente Formato do Horário Invalido')
        sleep(10)
        sys.exit()
    else:
        n = ['0', '1','2','3','4','5','6','7','8','9']
        a=tempo[0]
        b=tempo[1]
        a1=':'
        c=tempo[3]
        d=tempo[4]
        a2=':'
        e=tempo[6]
        f=tempo[7]
        l = [a,b,c,d,e,f]
        for num in l:
            if num not in n:
                print(Fore.RED+'ERRO: Somente números na Formatação do Horário')
                sleep(10)
                sys.exit()
        if tempo != f'{a}{b}{a1}{c}{d}{a2}{e}{f}':
            print(Fore.RED+'ERRO: Formato do Horario invalido ')
            sleep(10)
            sys.exit()
    print(' ')
    a=int(tempo[:2])
    b=int(tempo[3:5])
    c=int(tempo[6:8])
    data = datetime.now()
    data = str(data)
    ano = data[:4]
    mes = data[5:7]
    dia = data[8:10]
    dia,mes,ano = int(dia),int(mes),int(ano)
    then = datetime(ano, mes, dia, a, b, c) 
    now = datetime.now()
    falta = then - now
    falta = str(falta)
    print(Fore.YELLOW+'Sua operação sera executada em', Fore.RED+f'{falta[:7]}', Fore.YELLOW+'Aguarde  !!')

    print(' ')


    x1 = mktime(localtime())
    h = localtime()
    futuroLista = list(h)
    futuroLista[3] = a
    futuroLista[4] = b
    futuroLista[5] = c
    futuro = tuple(futuroLista)
    y = mktime(futuro)
    tp = abs(x1-y)
    sleep(tp)

