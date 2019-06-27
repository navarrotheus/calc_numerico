#entradas da tabela
g = int(input("Qual o grau do polinomio?"))
x = []
y = []
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

#funcao para calculo dos fatores de lagrange
def fator(k,x,g,xi):
    p1 = []#numerador
    p2 = []#denominador
    for i in range(0,g):
        if i==k:
            continue
        p1i = (x-xi[i])
        p1.append(p1i)
        p2i = (xi[k]-xi[i])
        p2.append(p2i)
    #realizando o produtorio
    numerador = 1
    for i in p1:
        numerador *= i
    denominador = 1
    for i in p2:
        denominador *= i
    fator = numerador/denominador
    return fator

#funcao lagrange
def lagrange(x,g,xi,yi):
    s = []
    for i in range(0,g):
        si = (yi[i])*(fator(i,x,g,xi))
        s.append(si)
    #realizando o somatorio
    somatorio = 0
    for i in s:
        somatorio += i
    return somatorio

#programa principal
n = int(input("Entre o valor de n"))
p = int(input("Entre o valor de x"))
print(lagrange(p,n,x,y))


     


