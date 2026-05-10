
import re
from functions.text_analysis import buscar_palabras, calcula_percentual

def buscar_cpf(texto):
    CPF = re.findall('[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}', texto)
    if len(CPF)>0:
        return CPF
    else:
        False

def buscar_documento(texto):
    documento = re.findall('[0-9]{8}', texto)
    if len(documento) > 0:
        return documento
    else:
        return False

def buscar_data(texto):
    DATA = re.findall('[0-9]{2}/[0-9]{2}/[0-9]{4}', texto)
    if len(DATA)>0:
        return DATA
    else:
        False


def buscar_palavras_mas(texto):
    return buscar_palabras(texto, "palabras_malas.txt")

def buscar_palavras_boas(texto):
    return buscar_palabras(texto, "palabras_buenas.txt")



def sumarizar_cpf(cpf):
    CPF = ""
    for i in cpf:
        CPF += i + "<br>"
    return CPF

def sumarizar_datas(datas):
    DATA = ""
    for i in datas:
        DATA += i+". "
    return DATA
