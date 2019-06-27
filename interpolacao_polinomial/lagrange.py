#entradas da tabela
g = int(input("Qual o grau do polinomio?\n"))
x = [] #coordenadas x's dos pontos
y = [] #coordenadas y's dos pontos
i = 0
while len(x) < g+1:
    xi = float(input("Entre o valor do x"+str(i)+":\n"))
    i += 1
    x.append(xi)
i = 0
while len(y) < g+1:
    yi = float(input("Entre o valor do y"+str(i)+":\n"))
    i += 1
    y.append(yi)

xx = int(input("Entre o valor do dominio do polinomio a ser calculado:\n"))

#interpolacao de lagrange
def lagrange(xi,yi,x,g):
    #xi e yi sao as coordenadas dos pontos
    #x eh o valor a ser calculado no polinomio
    #g eh o grau do polinomio
    somatorio = 0
    n = g+1 #numero de pontos
    for k in range(n):
        def L(k): #calculo do fator de lagrange L
            L = 1
            for j in range(n):
                if k==j: #j!=k
                    continue
                L *= float(x-xi[j])/float(xi[k]-xi[j]) #produtorio da formula
            return L
        somatorio += yi[k]*L(k) #somatorio da formula
    return somatorio

print(lagrange(x,y,xx,g))
