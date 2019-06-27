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

z = int(input("Entre o valor a ser interpolado:\n"))

n = g+1 #numero de pontos

#funcao para encontrar as ordens d0,d1,...,dn
def d(x,y,j,l):
    #x,y coordenadas dos pontos
    #j,l indices do respectivo ponto
    if j==0: #verifica se eh de ordem 0
        return y[0]
    elif j-l==1: #verifica se eh de ordem 1
        return (y[j]-y[l])/(x[j]-x[l])
    else: #ultimo caso ordem > 1
        return (d(x,y,j,l+1)-d(x,y,j-1,l))/(x[j]-x[l]) #recursividade ate chegar em ordem 1

#funcao para o produtorio
def p(x,j,z):
    #x abscissas
    #j indice da respectiva abscissa
    #z valor interpolado
    produtorio = 1
    for i in range(j):
        produtorio *= (z-x[i])

#funcao para o somatorio
def s(x,y,z,n):
    #x,y coordenadas dos pontos
    #z valor interpolado
    #n numero de pontos
    somatorio = 0
    for j in range(n):
        somatorio += d(j,0,x,y)*p(j,z,x)
    return somatorio



