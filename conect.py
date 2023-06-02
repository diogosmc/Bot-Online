from iqoptionapi.stable_api import IQ_Option
import sys
from time import sleep
from colorama import Fore, init
import blocon
init(convert=True, autoreset=True)

API = IQ_Option(blocon.email, blocon.senha)
def conectar(email, senha, rp):
    global API

    email = email
    senha = senha
    
    rp = str.upper(rp)
    lrp = ['REAL','PRACTICE']
    if rp not in lrp:
        print(Fore.RED+'ERRO: Digite Somente REAL ou PRACTICE !')
        sleep(10)
        sys.exit()
    print(' ')
    print(Fore.LIGHTYELLOW_EX+'Aguarde um momento estou verificando...')
    print(' ')

    API = IQ_Option(email, senha)
    API.connect()

    if API.check_connect():
        print(Fore.GREEN+' Conectado com sucesso!\n')
    else:
        print(Fore.RED+'ERRO: LOGIN ou SENHA Incorretos ou Autenticação em 2 etapas Ativado !')
        input('\n\n Aperte enter para sair')
        sys.exit()

    API.change_balance(rp) #REAL / PRACTICE

def verificar_par(par):
    paridades = API.get_all_open_time()
    par = str.upper(par)
    for p in paridades['digital']:
        if paridades['digital'][p]['open'] == True:
            lpar = []
            lpar.append(p)
            if par not in lpar:
                print(Fore.RED+'ERRO: Par Não Encontrado ou Não Ativado!')
                sleep(10)
                sys.exit()
            else:
                return par
            
def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def ver_entradas(entrada):
    if is_float(entrada) == False:
        entrada = entrada
        entrada = entrada.replace(',','.')
        if is_float(entrada) == False:
            print(Fore.RED+'ERRO: Digite somente números Ex(2.0),(2)')
            sleep(10)
            sys.exit()
        entrada = float(entrada)
        return entrada
    else:
        return entrada
        
def ver_direcao(direcao):
    direcao = str.lower(direcao)
    ldirecao = ['put','call']
    if direcao not in ldirecao:
        print(Fore.RED+'ERRO: Digite Somente o exemplo (put ou call)')
        sleep(10)
        sys.exit()
    else:
        return direcao

def ver_timeframe(timeframe):
    timeframe = int(blocon.timef)
    ltimeframe = [1,5,15]
    if timeframe not in ltimeframe:
        print(Fore.RED+'ERRO: Digite Somente os Exemplos (1, 5, 15)')
        sleep(10)
        sys.exit()
    else:
        return timeframe
  
def ver_gale(gale):
    gale = str.lower(gale)
    lgale = ['semgale','gale1','gale2']
    if gale not in lgale:
        print(Fore.RED+'ERRO: Digite Somente os Exemplos (semgale, gale1, gale2)')
        sleep(10)
        sys.exit()
    else:
        return gale

def entra_gale(par,entrada,direcao,gale,timeframe):

    if gale == 'semgale':
        print('Executando Sem Gale, Boa Sorte !')
        _,id = API.buy_digital_spot(par, entrada, direcao, timeframe)
        if isinstance(id, int):
            while True:
                status,lucro = API.check_win_digital_v2(id)
                if status:
                    if lucro > 0:
                        print('Resultado: win: '+str(round(lucro, 2)))
                        sleep(30)
                        sys.exit()
                    else:
                        print('Resultado: loss: '+str(round(entrada)))
                        sleep(30)
                        sys.exit()

    elif gale == 'gale1':
        print('Executando Gale 1, Boa Sorte !')
        _,id = API.buy_digital_spot(par, entrada, direcao, timeframe)
        if isinstance(id, int):
            while True:
                status,lucro = API.check_win_digital_v2(id)
                if status:
                    if lucro > 0:
                        print('Resultado: win: '+str(round(lucro, 2)))
                        sleep(30)
                        sys.exit()
                        
                    else:
                        _,id = API.buy_digital_spot(par, entrada*2, direcao, timeframe)
                        if isinstance(id, int):
                            while True:
                                status,lucro = API.check_win_digital_v2(id)
                                if status:
                                    if lucro > 0:
                                        print('Resultado: win: '+str(round(lucro, 2)))
                                        sleep(30)
                                        sys.exit()
                                    else:
                                        print('Resultado: loss: '+str(round(entrada*2)))
                                        sleep(30)
                                        sys.exit()
                        break

    elif gale == 'gale2':
        print('Executando Gale 2, Boa Sorte !')
        _,id = API.buy_digital_spot(par, entrada, direcao, timeframe)
        if isinstance(id, int):
            while True:
                status,lucro = API.check_win_digital_v2(id)
                if status:
                    if lucro > 0:
                        print('Resultado: win: '+str(round(lucro, 2)))
                        sleep(30)
                        sys.exit()
                    else:
                        _,id = API.buy_digital_spot(par, entrada*2, direcao, timeframe)
                        if isinstance(id, int):
                            while True:
                                status,lucro = API.check_win_digital_v2(id)
                                if status:
                                    if lucro > 0:
                                        print('Resultado: win: '+str(round(lucro, 2)))
                                        sleep(30)
                                        sys.exit()
                                    else:
                                        _,id = API.buy_digital_spot(par, entrada*4, direcao, timeframe)
                                        if isinstance(id, int):
                                            while True:
                                                status,lucro = API.check_win_digital_v2(id)
                                                if status:
                                                    if lucro > 0:
                                                        print('Resultado: win: '+str(round(lucro, 2))) 
                                                        sleep(30)
                                                        sys.exit()  
                                                    else:
                                                        print('Resultado: loss: '+str(round(entrada*4)))
                                                        sleep(30)
                                                        sys.exit()
                                        break
                            break    


