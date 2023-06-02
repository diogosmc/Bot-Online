from colorama import Fore, init
import blocon
from conect import *
from tempon import ver_tempo



init(convert=True, autoreset=True)
print(Fore.CYAN+ 'Olá Bem Vindo ao BOT para Ativos ( Somente Paridades Digitais ) !!!')
print('-Feito por : Diogo\n')

# Conectando na Conta e Escolhendo Real ou Practice
conectar(blocon.email,blocon.senha,blocon.rp)

# Verificação de ERROS
par = verificar_par(blocon.par)
entrada = ver_entradas(blocon.entrada)
direcao = ver_direcao(blocon.direcao)
timeframe = ver_timeframe(blocon.timef)
gale = ver_gale(blocon.gale)

# Tempo para execução
ver_tempo(blocon.tempo)

#Entrada
entra_gale(par,entrada,direcao,gale,timeframe)

