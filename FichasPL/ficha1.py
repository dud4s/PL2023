#
# Ficha de Expressões Regulares 1
#

import re

def alinea_1_1(s):
    if re.match(r"hello", s):
        return True
    return False

def alinea_1_2(s):
    if re.search(r"hello", s):
        return True
    return False

def alinea_1_3(s):
    return re.findall(r"(?i:hello)", s)

def alinea_1_4(s):
    return re.sub(r"hello", "*YEP*", s)

def alinea_1_5(s):
    return re.split(r",", s)

def palavra_magica(s):
    return True if re.search(r"(por favor[.!?]+$", s) else False

def narcissismo(s):
    return len(re.findall(r"eu", s))

def troca_de_curso(linha, novo_curso):
    return re.sub(r"LEI", novo_curso, linha);

def soma_string(linha):
    return sum(map(int , re.split(r",", linha)))

def pronomes(linha):
    return list(map(lambda x: x[1], re.findall(r"( |^)([eE]u|[Tt]u|[Ee]l(es|as|e|a)|[Nn]os|[Vv]os)( |$)", linha)))

def variavel_valida(linha):
    return True if re.match(r"[a-zA-Z](\w*|\d*)", linha) else False

def inteiros(linha):
    return list(map(int, re.findall(r"-?\d+", linha)))

def underscores(linha):
    return re.sub(r"\s+", "_", linha)

def codigo_postais(codigos):
    return [re.split('-', l) for l in lista]
