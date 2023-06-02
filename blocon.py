bloco = open('infos.txt','r')


for p in bloco:
    p = p.rstrip()
    if 'email' in p:
        p = list(p.split())
        email = p[1]
    if 'senha' in p:
        p = list(p.split())
        senha = p[1]
    if 'rp' in p:
        p = list(p.split())
        rp = p[1]
    if 'paridade' in p:
        p = list(p.split())
        par = p[1]
    if 'valor' in p:
        p = list(p.split())
        entrada = p[1]
    if 'direcao' in p:
        p = list(p.split())
        direcao = p[1]
    if 'timef' in p:
        p = list(p.split())
        timef = p[1]
    if 'gales' in p:
        p = list(p.split())
        gale = p[1]
    if 'tempo' in p:
        p = list(p.split())
        tempo = p[1]

bloco.close()



        