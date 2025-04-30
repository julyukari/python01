def imprime_nome(nome):
    print(f"nome:{nome}")

def solicitaNome():
    nome= input("digite seu nome")
    return nome
def piramide (num):
    for x in range (1,num+1,1):
        for i in range (0,x):
            print(x,end=" ")
        print()

def contaVogais(texto):
    texto = "o rato roeu a roupa do rei de roma"
    cont = 0
    for x in range(len(texto)):
        if texto[x] == "a" or texto[x] == "e" or texto[x] == "i" or texto[x] == "o" or texto[x] == "u":
            cont = cont + 1
    print(cont)

def estoque(produto,quantidade, valorUnitario):
    valortotal=quantidade*valorUnitario
    return valortotal

def positivoNegativo(num):
    if num > 0:
        print("P")
    elif num == 0:
        print("Z")
    else:
        print("N")

def soma(*a):
    soma=0
    for x in range(len(a)):
        soma=soma+a[x]
    print(soma)



