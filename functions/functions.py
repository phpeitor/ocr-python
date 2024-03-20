
import re

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
    cont_mau = 0
    with open("functions/palabras_malas.txt", encoding='utf-8') as f:
        palavras_mas = f.read().splitlines()
    
    palavras_texto = re.split(r'\W+', texto.upper())
    
    palavras_encontradas = []
    for palavra in palavras_texto:
        if palavra in palavras_mas:
            cont_mau += 1
            palavras_encontradas.append(palavra)
    
    percentual = calcula_percentual(cont_mau, len(palavras_texto))
    return cont_mau, percentual, palavras_encontradas

def buscar_palavras_boas(texto):
    cont_bem = 0
    with open("functions/palabras_buenas.txt", encoding='utf-8') as f:
        palavras_boas = f.read().splitlines()
    
    palavras_texto = re.split(r'\W+', texto.upper())
    
    palavras_encontradas = []
    for palavra in palavras_texto:
        if palavra in palavras_boas:
            cont_bem += 1
            palavras_encontradas.append(palavra)
    
    percentual = calcula_percentual(cont_bem, len(palavras_texto))
    return cont_bem, percentual, palavras_encontradas



def calcula_percentual(quantidade, tamanho):
    if tamanho > 0:
        return (quantidade / tamanho) * 100
    else:
        return 0

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