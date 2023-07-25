# TAD Posicao

# Representacao: (coluna, linha)
# cria_posicao: int × int -> posicao
# eh_posicao: universal -> boolean
# cria_copia_posicao: posicao -> posicao
# obter_pos_x: posicao -> int
# obter_pos_y: posicao -> int
# posicoes_iguais: posicao × posicao -> boolean
# posicao_para_str: posicao -> str
# obter_posicoes_adjacentes: posicao -> tuplo
# ordenar_posicoes: tuple -> tuple

def cria_posicao(x,y):
    """
    cria_posicao: int × int -> posicao

    Recebe os valores correspondentes as coordenadas de uma posicao e devolve a posicao correspondente.
    """
    if type(x) != int or type(y) != int or x<0 or y<0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (x,y)
def eh_posicao(arg):
    """
    eh_posicao: universal -> boolean

    Verifica se o argumento e ou nao uma posicao.
    """
    return not (type(arg) != tuple or len(arg) != 2 or \
            type(arg[0]) != int or type(arg[1]) != int or \
             arg[0] < 0 or arg[1] < 0)
def cria_copia_posicao(pos):
    """
    cria_copia_posicao: posicao -> posicao
    Recebe uma posicao e devolve uma copia nova da posicao.
    """
    return cria_posicao(pos[0],pos[1])
def obter_pos_x(pos):
    """
    obter_pos_x: posicao -> int

    Devolve a componente x da posicao
    """
    return pos[0]
def obter_pos_y(pos):
    """
    obter_pos_y: posicao -> int

    Devolve a componente y da posicao
    """
    return pos[1]
def posicoes_iguais(pos1,pos2):
    """
    posicoes_iguais: posicao × posicao -> boolean

    Verifica se as posicoes sao iguais.
    """
    return pos1 == pos2
def posicao_para_str(pos):
    """
    posicao_para_str: posicao -> str

    Devolve a string "(x, y)" que representa o seu argumento.
    """
    return str(pos)
def obter_posicoes_adjacentes(pos):
    """
    obter_posicoes_adjacentes: posicao -> tuplo

    Devolve um tuplo com as posicoes adjacentes, comecando pela posicao acima e seguindo no sentido horario.
    """
    x,y = obter_pos_x(pos),obter_pos_y(pos)
    adjacent = []
    for c in ((x,y-1),(x+1,y),(x,y+1),(x-1,y)):
        if -1 not in c:
            adjacent += [cria_posicao(c[0],c[1])]
    return tuple(adjacent)
def ordenar_posicoes(tuple_pos):
    """
    ordenar_posicoes: tuple -> tuple

    Devolve um tuplo contendo as mesmas posicoes do tuplo fornecido como argumento, ordenadas de acordo com a ordem de leitura do prado.
    """
    return tuple(sorted(sorted(tuple_pos,key=lambda x: obter_pos_x(x)), key=lambda x: obter_pos_y(x))) #Ordena primeiro por x e depois por y

#TAD Animal

# Representacao: [especie,frequencia de reproducao,frequencia de alimentacao,idade,fome]
# cria_animal: str × int × int -> animal
# eh_animal: universal -> boolean
# cria_copia_animal: animal -> animal
# obter_especie: animal -> str
# obter_freq_reproducao: animal -> int
# obter_freq_alimentacao: animal -> int
# obter_idade: animal -> int
# obter_fome: animal -> int
# aumenta_idade: animal -> animal
# reset_idade: animal -> animal
# aumenta_fome: animal -> animal
# reset_fome: animal -> animal
# eh_predador: universal -> boolean
# eh_presa: universal -> boolean
# animais_iguais: animal × animal -> boolean
# animal_para_char: animal -> str
# animal_para_str: animal -> str
# eh_animal_fertil: animal -> boolean
# eh_animal_faminto: animal -> boolean
# reproduz_animal: animal -> animal

def cria_animal(species,reproduction,feeding):
    """
    cria_animal: str × int × int -> animal

    Recebe uma string nao vazia correspondente a especie do animal e dois valores inteiros correspondentes
    a frequencia de reproducao r (maior do que 0) e a frequencia de alimentacao a (maior ou
    igual a 0); e devolve o animal.
    """
    if type(species) != str or type(reproduction) != int or type(feeding) != int or \
        species == "" or reproduction <= 0 or feeding < 0:
        raise ValueError("cria_animal: argumentos invalidos")
    return [species,reproduction,feeding,0,0]
def eh_animal(animal):
    """
    eh_animal: universal -> boolean

    Devolve True caso o seu argumento seja um TAD animal e False caso contrario.
    """
    return type(animal) == list and len(animal) == 5 and type(animal[0]) == str and \
            type(animal[1]) == int and type(animal[2]) == int and animal[0] != "" and \
            animal[1] >= 0 and animal[2] >= 0 and animal[3] >= 0 and animal[4] >= 0 
def cria_copia_animal(animal):
    """
    cria_copia_animal: animal -> animal

    Recebe um animal (predador ou presa) e devolve uma nova copia deste.
    """
    if eh_animal(animal):
        return animal.copy()
def obter_especie(animal):
    """
    obter_especie: animal -> str

    Devolve a string correspondente a especie do animal.
    """
    return animal[0]
def obter_freq_reproducao(animal):
    """
    obter_freq_reproducao: animal -> int

    Devolve a frequencia de reproducao do animal.
    """
    return animal[1]
def obter_freq_alimentacao(animal):
    """
    obter_freq_alimentacao: animal -> int

    Devolve a frequencia de alimentacao do animal.
    """
    return animal[2]
def obter_idade(animal):
    """
    obter_idade: animal -> int

    Devolve a idade do animal.
    """
    return animal[3]
def obter_fome(animal):
    """
    obter_fome: animal -> int

    Devolve a fome do animal.
    """
    return animal[4]
def aumenta_idade(animal):
    """
    aumenta_idade: animal -> animal

    Modifica destrutivamente o animal incrementando o valor da sua idade em uma unidade,
    e devolve o proprio animal
    """
    animal[3] += 1
    return animal
def reset_idade(animal):
    """
    reset_idade: animal -> animal

    Modifica destrutivamente o animal alterando o valor da sua idade para 0,
    e devolve o proprio animal
    """
    animal[3] = 0
    return animal
def aumenta_fome(animal):
    """
    aumenta_fome: animal -> animal

    Modifica destrutivamente o animal incrementando o valor da sua fome em uma unidade,
    e devolve o proprio animal
    """
    if eh_predador(animal):
        animal[4] = obter_fome(animal) + 1
    return animal
def reset_fome(animal):
    """
    reset_fome: animal -> animal

    Modifica destrutivamente o animal alterando o valor da sua fome para 0,
    e devolve o proprio animal
    """
    animal[4] = 0
    return animal
def eh_predador(animal):
    """
    eh_predador: universal -> boolean

    Devolve True caso o seu argumento seja um TAD animal do tipo predador e False caso contrario.
    """
    try:
        return obter_freq_alimentacao(animal) > 0
    except:
        return False
def eh_presa(animal):
    """
    eh_presa: universal -> boolean

    Devolve True caso o seu argumento seja um TAD animal do tipo presa e False caso contrario.
    """
    try:
        return obter_freq_alimentacao(animal) == 0
    except:
        return False
def animais_iguais(animal1,animal2):
    """
    animais_iguais: animal × animal -> boolean

    Devolve True caso os animais sejam iguais e False caso contrario.
    """
    return animal1 == animal2
def animal_para_char(animal):
    """
    animal_para_char: animal -> str

    Devolve a cadeia de caracteres dum unico elemento correspondente ao primeiro caracter 
    da especie do animal passado por argumento, em maiuscula para animais predadores e 
    em minuscula para presas.
    """
    if eh_predador(animal):
        return animal[0][0].upper()
    else:
        return animal[0][0].lower()
def animal_para_str(animal):
    """
    animal_para_str: animal -> str

    Devolve a string que representa o animal.
    """
    if eh_predador(animal):
        return f"{obter_especie(animal)} [{obter_idade(animal)}/{obter_freq_reproducao(animal)};{obter_fome(animal)}/{obter_freq_alimentacao(animal)}]"
    else:
        return f"{obter_especie(animal)} [{obter_idade(animal)}/{obter_freq_reproducao(animal)}]"
def eh_animal_fertil(animal):
    """
    eh_animal_fertil: animal -> boolean

    Devolve True caso o animal a tenha atingido a idade de reproducao e False caso contrario.
    """
    return obter_idade(animal) >= obter_freq_reproducao(animal)
def eh_animal_faminto(animal):
    """
    eh_animal_faminto: animal -> boolean

    Devolve True caso o animal a tenha atingindo um valor de fome igual ou superior a sua 
    frequencia de alimentacao e False caso contrario. As presas devolvem sempre False.

    """
    return eh_predador(animal) and obter_fome(animal) >= obter_freq_alimentacao(animal)
def reproduz_animal(animal):
    """
    reproduz_animal: animal -> animal

    Recebe um animal e devolve um novo animal da mesma especie com idade e fome igual a 0.
    """
    animal = reset_idade(animal)
    return cria_animal(obter_especie(animal),obter_freq_reproducao(animal),obter_freq_alimentacao(animal))

#TAD Prado

# Representacao: {"Size": tamanho,"rocks": (posicoes dos obstaculos),"animals": [animais],"animal_pos": [posicoes dos animais]}
# cria prado: posicao × tuplo × tuplo × tuplo -> prado
# eh_prado: universal -> boolean
# cria copia prado: prado -> prado
# obter_tamanho x: prado -> int
# obter_tamanho y: prado -> int
# obter_numero_predadores: prado -> int
# obter_numero_presas: prado -> int
# obter_posicao_animais: prado -> tuplo posicoes
# obter_animal: prado × posicao -> animal
# eliminar_animal: prado × posicao -> prado
# mover_animal: prado × posicao × posicao -> prado
# inserir_animal: prado × animal × posicao -> prado
# eh_posicao_animal: prado × posicao -> boolean
# eh_posicao_obstaculo: prado × posicao -> boolean
# eh_posicao_livre: prado × posicao -> boolean
# prados_iguais: prado × prado -> boolean
# prado_para_str: prado -> str
# obter_valor_numerico: prado × posicao -> int
# obter_movimento: prado × posicao -> posicao

def cria_prado(size,rocks,animals,animal_pos):
    """
    cria prado: posicao × tuplo × tuplo × tuplo -> prado

    Recebe uma posicao, um tuplo correspondente as posicoes dos rochedos, um tuplo de 1 ou mais animais 
    e um tuplo com as posicoes respetivas dos animais e devolve o prado que representa internamente o 
    mapa e os animais presentes 
    """
    if not eh_posicao(size) or type(rocks) != tuple or type(animals) != tuple or len(animals) < 1 or\
        type(animal_pos) != tuple or len(animals) != len(animal_pos):
        raise ValueError("cria_prado: argumentos invalidos")
    for r in rocks:
        if not eh_posicao(r) or obter_pos_x(r) >= obter_pos_x(size) or obter_pos_y(r) >= obter_pos_y(size) or 0 in [obter_pos_x(r),obter_pos_y(r)]:
            raise ValueError("cria_prado: argumentos invalidos")
    for a in animal_pos:
        if not eh_posicao(a) or obter_pos_x(a) > obter_pos_x(size) or obter_pos_y(a) > obter_pos_y(size):
            raise ValueError("cria_prado: argumentos invalidos")
    for animal in animals:
        if not eh_animal(animal):
            raise ValueError("cria_prado: argumentos invalidos")
    prado = {
        "size": size,
        "rocks": rocks,
        "animals": list(animals),
        "animal_pos": list(animal_pos)}
    return prado
def eh_prado(arg):
    """
    eh_prado: universal -> boolean

    Verifica se o argumento e um TAD prado.
    """
    #Verifica a validade geral
    if type(arg) != dict or len(arg) != 4 or "size" not in arg or "rocks" not in arg or \
           "animals" not in arg or "animal_pos" not in arg or not eh_posicao(arg["size"]) or \
           type(arg["rocks"]) != tuple or type(arg["animals"]) != list or \
           type(arg["animal_pos"]) != list or len(arg["animals"]) < 1 or len(arg["animals"]) != len(arg["animal_pos"]):
            return False
    for r in arg["rocks"]: #verifica a validade das posicoes de obstaculos
        if not eh_posicao(r) or obter_pos_x(r) > obter_pos_x(arg["size"]) or obter_pos_y(r) > obter_pos_y(arg["size"]) or 0 in [obter_pos_x(r),obter_pos_y(r)]:
            return False
    for a in arg["animals"]: #verifica a validade dos animals
        if not eh_animal(a):
            return False
    for c in arg["animal_pos"]: #verifica a validade das posicoes de animais
        if not eh_posicao(c) or obter_pos_x(c) > obter_pos_x(arg["size"]) or obter_pos_y(c) > obter_pos_y(arg["size"]) or 0 in [obter_pos_x(c),obter_pos_y(c)]:
            return False
    return True   
def cria_copia_prado(prado):
    """
    cria copia prado: prado -> prado

    Recebe uma prado e devolve uma copia nova do prado.
    """
    if eh_prado(prado):
        #copia a estrutura e valores inalteraveis do prado
        copy = {"size": cria_copia_posicao(prado["size"]),"rocks": prado["rocks"],"animals": [], "animal_pos": []}
        for a in prado["animals"]: #copia os animais 
            copy["animals"] += [cria_copia_animal(a)]
        for p in prado["animal_pos"]: #copia as posicoes dos animais
            copy["animal_pos"] += [cria_copia_posicao(p)]
        return copy
    else:
        raise ValueError("cria_copia_prado: argumentos invalidos")
def obter_tamanho_x(prado):
    """
    obter_tamanho x: prado -> int

    Devolve o valor inteiro que corresponde a dimensao Nx do prado.

    """
    return obter_pos_x(prado["size"]) + 1
def obter_tamanho_y(prado):
    """
    obter_tamanho y: prado -> int

    Devolve o valor inteiro que corresponde a dimensao Ny do prado.

    """
    return obter_pos_y(prado["size"]) + 1
def obter_numero_predadores(prado):
    """
    obter_numero_predadores: prado -> int

    Devolve o numero de animais predadores no prado.
    """
    x = 0
    for a in prado["animals"]:
        if eh_predador(a):
            x += 1
    return x
def obter_numero_presas(prado):
    """
    obter_numero_presas: prado -> int
    
    Devolve o numero de presas no prado.
    """
    x = 0
    for c in prado["animals"]:
        if eh_presa(c):
            x += 1
    return x
def obter_posicao_animais(prado):
    """
    obter_posicao_animais: prado -> tuplo posicoes

    Devolve um tuplo contendo as posicoes do prado ocupadas por animais, 
    ordenadas em ordem de leitura do prado.
    """
    return tuple(ordenar_posicoes(tuple(prado["animal_pos"])))
def obter_animal(prado,pos):
    """
    obter_animal: prado × posicao -> animal

    Devolve o animal do prado que se encontra na posicao pretendida. 
    """
    for i in range(len(prado["animal_pos"])):
        if posicoes_iguais(prado["animal_pos"][i],pos):
            return prado["animals"][i]
def eliminar_animal(prado,pos):
    """
    eliminar_animal: prado × posicao -> prado

    Elimina o animal que se encontra na posicao pretendida do prado.
    """
    for i in range(len(prado["animal_pos"])):
        if posicoes_iguais(prado["animal_pos"][i],pos):
            x = i
    del prado["animals"][x]
    del prado["animal_pos"][x]
    return prado
def mover_animal(prado,pos1,pos2):
    """
    mover_animal: prado × posicao × posicao -> prado

    Move o animal para a nova posicao pretendida no prado.
    """
    for i in range(len(prado["animal_pos"])):
        if posicoes_iguais(prado["animal_pos"][i],pos1):
            x = i
    prado["animal_pos"][x] = pos2
    return prado
def inserir_animal(prado,animal,pos):
    """
    inserir_animal: prado × animal × posicao -> prado

    Insere um novo animal no prado.
    """
    prado["animals"] += [animal]
    prado["animal_pos"] += [pos]
    return prado
def eh_posicao_animal(prado,pos):
    """
    eh_posicao_animal: prado × posicao -> boolean

    Verifica se a posicao esta ocupada por um animal
    """
    for i in range(len(prado["animal_pos"])):
        if posicoes_iguais(prado["animal_pos"][i],pos):
            return True
    return False
def eh_posicao_obstaculo(prado,pos):
    """
    eh_posicao_obstaculo: prado × posicao -> boolean

    Verifica se a posicao esta ocupada por uma rocha ou montanha
    """
    for i in range(len(prado["rocks"])):
        if posicoes_iguais(prado["rocks"][i],pos):
            return True
    return 0 in [obter_pos_x(pos),obter_pos_y(pos)] or obter_pos_x(prado["size"]) <= obter_pos_x(pos) or obter_pos_y(prado["size"]) <= obter_pos_y(pos)
def eh_posicao_livre(prado,pos):
    """
    eh_posicao_livre: prado × posicao -> boolean

    Verifica se a posicao esta livre, ou seja nao esta ocupada por animais ou rochas
    """
    return eh_posicao(pos) and not eh_posicao_animal(prado,pos) and not eh_posicao_obstaculo(prado,pos)
def prados_iguais(prado1,prado2):
    """
    prados_iguais: prado × prado -> boolean

    Verifica se os prados sao iguais.
    """     
    if eh_prado(prado1) and eh_prado(prado2) and posicoes_iguais(prado1["size"],prado2["size"]):
        if len(prado1["animals"]) != len(prado2["animals"]) or len(prado1["animal_pos"]) != len(prado2["animal_pos"]):
            return False
        for i in range(len(prado1["rocks"])):
            if not posicoes_iguais(prado1["rocks"][i],prado2["rocks"][i]) or len(prado1["rocks"]) != len(prado2["rocks"]):
                return False
        for i in range(len(prado1["animals"])):
            if not eh_animal(prado1["animals"][i]) or not eh_animal(prado2["animals"][i]) or \
                not animais_iguais(prado1["animals"][i],prado2["animals"][i]):
                return False
        for i in range(len(prado1["animal_pos"])):
            if not eh_posicao(prado1["animal_pos"][i]) or not eh_posicao(prado2["animal_pos"][i]) or \
                not posicoes_iguais(prado1["animal_pos"][i],prado2["animal_pos"][i]):
                return False
        return True
    else:
        return False
def prado_para_str(prado):
    """
    prado_para_str: prado -> str

    Devolve uma string que representa o prado.
    """
    img,x = "+",0
    while x < obter_pos_x(prado["size"]) - 1: #Cria a primeira e ultima linha.
        img += "-"
        x += 1
    last = img
    img += "+\n"
    for y in range(1,obter_tamanho_y(prado)-1): #Cria as linhas intermedias.
        x = 1
        img += "|"
        while x < obter_pos_x(prado["size"]):
            if eh_posicao_obstaculo(prado,cria_posicao(x,y)):
                img += "@"
            elif eh_posicao_animal(prado,cria_posicao(x,y)):
                img += animal_para_char(obter_animal(prado,cria_posicao(x,y)))
            else:
                img += "."
            x += 1
        img += "|\n"
    img += last + "+"
    return img
def obter_valor_numerico(prado,pos):
    """
    obter_valor_numerico: prado × posicao -> int

    Devolve o valor numerico da posicao correspondente a ordem de leitura no prado
    """
    return obter_tamanho_x(prado)*(obter_pos_y(pos)) + obter_pos_x(pos)
def obter_movimento(prado,pos):
    """
    obter_movimento: prado × posicao -> posicao

    Devolve a posicao seguinte do animal na posicao pretendida dentro do prado. 
    """
    presas,possible = [],[]
    for p in obter_posicoes_adjacentes(pos):
        if eh_predador(obter_animal(prado,pos)): #Analisa as posicoes adjacentes em caso de carnivoro

            if not (eh_posicao_obstaculo(prado,p) or (eh_posicao_animal(prado,p) and eh_predador(obter_animal(prado,p)))): #Verifica se nao e um obstaclo ou um predador

                if eh_posicao_animal(prado,p): #Verifica se possivel possicao tem uma presa
                    presas += [p]
                else:
                    possible += [p]  

        elif eh_presa(obter_animal(prado,pos)): #Analisa as posicoes adjacentes em caso de presa

            if not (eh_posicao_obstaculo(prado,p) or (eh_posicao_animal(prado,p))): #Verifica se nao e um obstaclo ou um predador

                    possible += [p]  
    if len(presas) > 0:
        return presas[obter_valor_numerico(prado,pos) % len(presas)]
    elif len(possible) > 0:
        return possible[obter_valor_numerico(prado,pos) % len(possible)]
    else:
        return pos

#Funcoes Gerais
def geracao(prado):
    """
    geracao: prado -> prado

    Modifica o prado fornecido como argumento de acordo com a evolucao correspondente a uma 
    geracao completa, e devolve o proprio prado.
    """
    eaten = []
    def isEaten(pos): #Auxiliar que verifica se o animal a ser movido nao foi predado
        for e in eaten:
            if posicoes_iguais(e,pos):
                return True
        return False
    for pos in ordenar_posicoes(obter_posicao_animais(prado)):
        if eh_posicao_animal(prado,pos) and not isEaten(pos):
            animal = obter_animal(prado,pos)
            animal = aumenta_idade(animal)
            new_pos = obter_movimento(prado,pos)
            if eh_predador(animal):
                animal = aumenta_fome(animal)
                if eh_posicao_animal(prado,new_pos) and eh_presa(obter_animal(prado,new_pos)): #Predacao
                    prado = eliminar_animal(prado,new_pos)
                    animal = reset_fome(animal)
                    eaten += [new_pos]
            if eh_posicao_livre(prado,new_pos): #Movimentacao
                prado = mover_animal(prado,pos,new_pos)
            if not posicoes_iguais(new_pos,pos) and eh_animal_fertil(animal): #Reproducao
                prado = inserir_animal(prado,reproduz_animal(animal),pos)
                animal = reset_idade(animal)
            if eh_predador(animal) and obter_fome(animal) == obter_freq_alimentacao(animal): #Morte
                prado = eliminar_animal(prado,new_pos)
    return prado
def simula_ecossistema(file_name,gens,loud):
    """
    simula_ecossistema: str × int × boolean -> tuple

    Permite simular o ecossistema de um prado. A funcao recebe uma string, um integer e um boolean
    e devolve o tuplo de dois elementos correspondentes ao numero de predadores e presas no 
    prado no fim da simulacao. No modo quiet mostra-se pela saıda standard o prado, o numero de 
    animais e o numero de geracao no inıcio da simulacao e apos a ultima geracao. No modo verboso, 
    apos cada geracao, mostra-se tambem o prado, o numero de animais e o numero de geracao, 
    apenas se o numero de animais predadores ou presas se tiver alterado.
    """
    #Leitura de ficheiro de configuracao
    with open(file_name,"r") as file:
        config = file.readlines()
    for i in range(len(config)):
        if "\n" in config[i]:
            config[i] = eval(config[i][:-1])
        else:
            config[i] = eval(config[i])
    size = cria_posicao(config[0][0],config[0][1])
    rocks,animals,animals_pos = [],[],[]
    for rock in config[1]:
        rocks += [cria_posicao(rock[0],rock[1])]
    for animal in config[2:]:
        animals += [cria_animal(animal[0],animal[1],animal[2])]
        animals_pos += [cria_posicao(animal[3][0],animal[3][1])]
    prado = cria_prado(size,tuple(rocks),tuple(animals),tuple(animals_pos))
    #Auxiliar que conta os animais no prado
    def countAnimals(predators,prey):
        for c in obter_posicao_animais(prado):
            if eh_predador(obter_animal(prado,c)):
                predators += 1
            else:
                prey += 1
        return (predators,prey)
    #Simulador
    i,predators,prey = 0,0,0
    if loud: #Modo Loud
        predators,prey = countAnimals(0,0)[0],countAnimals(0,0)[1]
        lastPredators,lastPrey = predators,prey
        print(f"Predadores: {predators} vs Presas: {prey} (Gen. 0)")
        print(prado_para_str(prado))
        while i < gens:
            prado = geracao(prado)
            predators,prey = countAnimals(0,0)[0],countAnimals(0,0)[1]
            i += 1
            if predators != lastPredators or prey != lastPrey:
                print(f"Predadores: {predators} vs Presas: {prey} (Gen. {i})")
                print(prado_para_str(prado))
            lastPredators,lastPrey = predators,prey
    else: #Modo Quiet
        predators,prey = countAnimals(0,0)[0],countAnimals(0,0)[1]
        print(f"Predadores: {predators} vs Presas: {prey} (Gen. 0)")
        print(prado_para_str(prado))
        while i < gens:
            prado = geracao(prado)
            predators,prey = countAnimals(0,0)[0],countAnimals(0,0)[1]
            i += 1
        print(f"Predadores: {predators} vs Presas: {prey} (Gen. {i})")
        print(prado_para_str(prado))
    return(obter_numero_predadores(prado),obter_numero_presas(prado))


