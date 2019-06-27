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
    if j==0: #verifica se eh de ordem 0
        return y[0]
    elif j-l==1: #verifica se eh de ordem 1
        return (y[j]-y[l])/(x[j]-x[l])
    else: #ultimo caso ordem > 1
        return (d(j,l+1,x,y)-d(j-1,l,x,y))/(x[j]-x[l])

