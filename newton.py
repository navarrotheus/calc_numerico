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

#funcao para encontrar a ordem d
def d(x,y,j,l):
    #x,y sao as coordenadas
    #j,l sao os indices das coordenadas
    if j==0: #verifica se eh de ordem 0
        return y[0] 
    elif j-l==1: #verifica se eh de ordem 1
        return (y[j]-y[l])/(x[j]-x[l]) 
    else:
        return (d(x,y,j,l+1)-d(x,y,j-1,l))/(x[j]-x[l]) #recursividade caso ordem > 1
        
#funcao para calcular o produtorio
def p(x,j,z):
    produtorio = 1
    for i in range(j):
        produtorio *= (z-x[i])
    return produtorio

#funcao para calcular o somatorio
def s(x,y,z,n):
    somatorio = 0
    for j in range(n):
        somatorio += d(x,y,j,0)*p(x,j,z)
    return somatorio

print(s(x,y,z,n))
