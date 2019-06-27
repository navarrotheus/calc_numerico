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