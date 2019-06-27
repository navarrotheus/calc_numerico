#entradas da tabela
n = int(input("Qual o numero de pontos?\n"))
x = [] #abscissas dos pontos
y = [] #ordenadas dos pontos
i = 0
while len(x) < n:
    xi = float(input("Entre o valor do x"+str(i)+":\n"))
    i += 1
    x.append(xi)
i = 0
while len(y) < n:
    yi = float(input("Entre o valor do y"+str(i)+":\n"))
    i += 1
    y.append(yi)

z = int(input("Entre o valor a ser interpolado:\n"))

#interpolacao de lagrange
def L(k,xi,x,n): #calculo do fator de lagrange L
    #k eh o indice do fator
    #xi sao as abscissas
    #x eh o valor a interpolar
    #n eh o numero de pontos
    L = 1
    for j in range(n):
        if k==j: #j!=k
            continue
        L *= float(x-xi[j])/float(xi[k]-xi[j]) #divisao dos produtorios da formula
    return L
def lagrange(xi,yi,x,n):
    #xi e yi sao as coordenadas dos pontos
    #x eh o valor a interpolar
    #n eh o numero de pontos
    somatorio = 0
    for k in range(n):
        somatorio += yi[k]*L(k,xi,x,n) #somatorio da formula
    return somatorio

print(lagrange(x,y,z,n))
