def corrigir_palavra(palavra): #1.2.1
    """
    Esta funcao recebe uma string com caracteres possivelmente modificados e devolve a correcao desta mesma.

    Input: string
    Output: string
    """
    for i in range(len(palavra)):
        words = sorted(list(set(list((palavra.upper()))))) #Cria uma list com todas as letras diferentes no input
        for c in words: #Procura e elimina os surtos de letras
            if c + c.lower() in palavra:
                palavra = palavra[:palavra.index(c + c.lower())] + palavra[palavra.index(c + c.lower())+2:] 
            if c.lower() + c in palavra:
                palavra = palavra[:palavra.index(c.lower() + c)] + palavra[palavra.index(c.lower() + c)+2:]
    return palavra

def eh_anagrama(word_1, word_2): #1.2.2
    """
    Esta funcao recebe duas strings e verifica se estas sao anagramas uma da outra.

    Input: string, string
    Output: string
    """
    return (sorted(word_1.upper()) == sorted(word_2.upper()))
    
def corrigir_doc(document): #1.2.3
    """
    Esta funcao recebe uma string que representa o texto com erros da documentacao da BDB e devolve uma string corrigida.
    
    Input: string
    Output: string
    """
    if type(document) != str or "  " in document or len(document) == 0:
        raise ValueError("corrigir_doc: argumento invalido") 
    #verifica se o documento e constituido apenas por letras
    words = document.split()
    correcao = ""
    for w in words: 
        for l in range(len(w)):
            if ord(w[l]) <  65 or ord(w[l]) > 122:
                raise ValueError("corrigir_doc: argumento invalido")
        correcao += " " + corrigir_palavra(w) 
    words = correcao.split()
    res = words
    for c in words:
        for d in words: #Procura e remove anagramas
            if  eh_anagrama(c,d) and c.upper() != d.upper():
                del res[words.index(d)]
    return " ".join(res)

def obter_posicao(cad, pos): #2.2.1
    """
    Esta funcao recebe uma das letras ("C", "B", "E" ou "D") e um inteiro (posicao atual)
    e devolve o inteiro que corresponde a posicao apos o movimento.
    Input: string, int
    Output: int
    """
    if cad == "C" and pos not in (1,2,3):
        pos -= 3
    elif cad == "B" and pos not in (7,8,9):
        pos += 3
    elif cad == "E" and pos not in (1,4,7):
        pos -= 1
    elif cad == "D" and pos not in (3,6,9):
        pos += 1
    return pos 

def obter_digito(moves, pos): #2.2.2
    """
    Esta funcao recebe uma string contendo uma sequencia de movimentos e um inteiro correspondente a posicao inicial 
    e devolve a posicao apos os movimentos.
    Input: string, int
    Output: int
    """
    for letter in moves:
        pos = obter_posicao(letter,pos)
    return pos

def obter_pin(moves): #2.2.3
    """
    Esta funcao recebe um tuplo entre 4 e 10 sequencias de movimentos e devolve o tuplo de inteiros que contem o pin codificado.

    Input: tuple
    Output: tuple
    """
    pos,res = 5,[]
    if type(moves) != tuple or len(moves) < 4 or len(moves) > 10:
        raise ValueError("obter_pin: argumento invalido")
    for c in moves:
        if type(c) != str or len(c) == 0:
            raise ValueError("obter_pin: argumento invalido")
        for l in c:
            if l not in ("C","B","E","D"):
                raise ValueError("obter_pin: argumento invalido")
        pos = obter_digito(c, pos)
        res += [pos]
    return tuple(res)

def eh_entrada(arg): #3.2.1
    """
    Esta funcao recebe um argumento de qualquer tipo e devolve True se e so se o seu argumento corresponde a uma entrada da BDB.
    
    Input: any
    Output: bool
    """
    if type(arg) != tuple or len(arg) != 3: #Verifica a validade do tuplo
        return False
    if type(arg[0]) != str or len(arg[0]) == 0 or arg[0][0] == "-" or "--" in arg[0] or arg[0][-1] == "-": #Verifica a validade da cifra
        return False
    for c in arg[0]:
        if (ord(c) < ord("a") or  ord(c) > ord("z")) and c != "-":
            return False
    controlo = arg[1]
    if type(controlo) != str or len(controlo) != 7 or controlo[0] != "[" or controlo[6] != "]": #Verifica a validade do checksum
        return False
    for c in controlo[1:6]:
        if ord(c) < ord("a") or  ord(c) > ord("z"):
            return False 
    if type(arg[2]) != tuple or len(arg[2]) < 2: #Verifica a validade dos numeros de seguranca
        return False
    for c in arg[2]:
        if type(c) != int or c < 0:
            return False
    return True
      
def validar_cifra(cifra,controlo): #3.2.2
    """
    Esta funcao recebe uma string contendo uma cifra e uma outra string contendo uma sequencia de controlo, e devolve True se e so se a sequencia de
    controlo for coerente com a cifra.
    
    Input: string, string
    Output: bool
    """
    cifra = cifra.replace('-', "") #remove os "-"
    repeats = {}
    while cifra != "": #Cria um dicionario "repeats" com todas as letras na cifra e o numero de vezes que estas se repetem
        repeats[cifra[0]] = cifra.count(cifra[0])
        cifra = cifra.replace(cifra[0], "")
    #Organiza o dicionario "repeats" pela ordem do controlo
    repeats = dict(sorted(repeats.items()))
    repeats = dict(sorted(repeats.items(), key=lambda item: item[1],reverse=True))
    if list(controlo[1:6]) != list(repeats)[:5]: #Verifica o controlo
        return False
    return True

def filtrar_bdb(lista): #3.2.3
    """
    Esta funcao recebe uma lista contendo uma ou mais entradas da BDB e devolve apenas a lista contendo as entradas em que o checksum nao e coerente com a cifra.
    
    Input: list
    Output: list
    """
    if type(lista) != list or len(lista) == 0:
        raise ValueError("filtrar_bdb: argumento invalido")
    for c in lista[::-1]:
        if not eh_entrada(c):
            raise ValueError("filtrar_bdb: argumento invalido")
        if validar_cifra(c[0],c[1]):
            del lista[lista.index(c)]
    return lista

def obter_num_seguranca(arg): #4.2.2
    """
    Esta funcao recebe um tuplo de numeros inteiros positivos e devolve o numero de seguranca conforme descrito.

    Input: tuple
    Output: int
    """
    seguranca = abs(max(arg) - min(arg))
    for num_1 in range(len(arg)):
        for num_2 in range(len(arg)):
            if abs(arg[num_1] - arg[num_2]) < seguranca and num_1 != num_2:
                seguranca = abs(arg[num_1] - arg[num_2])
    return seguranca

def decifrar_texto(cifra,seguranca): #4.2.3
    """
    Esta funcao recebe uma string contendo uma cifra e um numero de seguranca, e devolve o texto decifrado.

    Input: string, int
    Output: string
    """
    for c in range(len(cifra)):
        aumento = seguranca % 26 #Reduz o numero de seguranca ao valor a avancar cada letra
        if cifra[c] == "-":
            cifra = cifra[:c] + " " + cifra[c+1:]
        elif c % 2 == 0:
            new = ord(cifra[c]) + aumento + 1 
            while new > ord("z"):
                new -= 26
            cifra = cifra[:c] + chr(new) + cifra[c+1:]
        else:
            new = ord(cifra[c]) + aumento - 1
            while new > ord("z"):
                new -= 26
            cifra = cifra[:c] + chr(new) + cifra[c+1:] 

    return cifra

def decifrar_bdb(arg): #4.2.4
    """
    Esta funcao recebe uma lista contendo uma ou mais entradas da BDB e devolve uma lista de igual tamanho, 
    contendo o texto das entradas decifradas na mesma ordem.

    Input: list
    Output: list
    """
    if type(arg) != list or len(arg) == 0:
        raise ValueError("decifrar_bdb: argumento invalido")
    res = []
    for c in arg:
        if not eh_entrada(c):
            raise ValueError("decifrar_bdb: argumento invalido")
        seguranca = obter_num_seguranca(c[2])
        res += [decifrar_texto(c[0],seguranca)]
    return res

def eh_utilizador(arg): #5.1
    """
    Esta funcao recebe um argumento de qualquer tipo e devolve True se e so se o seu argumento corresponde a um dicionario 
    contendo a informacao de utilizador relevante da BDB.

    Input: any
    Output: bool
    """
    if type(arg) != dict or len(arg) != 3:
        return False
    elif "name" not in arg or "pass" not in arg or "rule" not in arg:
        return False
    elif type(arg["name"]) != str or type(arg["pass"]) != str or type(arg["rule"]) != dict:
        return False
    elif len(arg["name"]) == 0 or len(arg["pass"]) == 0 or len(arg["rule"]) != 2:
        return False
    elif "vals" not in arg["rule"] or "char" not in arg["rule"]:
        return False
    elif type(arg["rule"]["vals"]) != tuple or type(arg["rule"]["char"]) != str:
        return False
    elif len(arg["rule"]["char"]) > 1:
        return False
    elif ord(arg["rule"]["char"]) > ord("z") or ord(arg["rule"]["char"]) < ord("a"):
        return False
    elif type(arg["rule"]["vals"][0]) != int or type(arg["rule"]["vals"][1]) != int:
        return False
    elif arg["rule"]["vals"][0] < 0 or arg["rule"]["vals"][1] < 0 or arg["rule"]["vals"][0] > arg["rule"]["vals"][1]:
        return False
    else:
        return True

def eh_senha_valida(password,rule): #5.2
    """
    Esta funcao recebe uma cadeia de carateres correspondente a uma senha e um dicionario contendo a regra individual de criacao da senha, 
    e devolve True se e so se a senha cumpre com todas as regras de definicao.

    Input: string, dict
    Output: bool
    """
    t = 0
    for c in ("a","e","i","o","u"): #Verifica se existem 3 vogais na password
        t += password.count(c)
    if t < 3:
        return False
    geral = False
    for c in password: #Procura a repeticao de 2 carateres
        if c+c in password:
            geral = True
    if not geral:
        return False
    if password.count(rule["char"]) < rule["vals"][0] or password.count(rule["char"]) > rule["vals"][1]:
        return False
    return True

def filtrar_senhas(senhas): #5.3
    """
    Esta funcao recebe uma lista contendo um ou mais dicionarios correspondentes as entradas da BDB, e devolve a lista ordenada alfabeticamente
    com os nomes dos utilizadores com senhas erradas.

    Input: list
    Output: list
    """
    if type(senhas) != list or len(senhas) == 0:
        raise ValueError("filtrar_senhas: argumento invalido")
    res = []
    for c in senhas:
        if not eh_utilizador(c):
            raise ValueError("filtrar_senhas: argumento invalido")
        if not eh_senha_valida(c["pass"],c["rule"]):
            res += [c["name"]]
    return sorted(res)
