#definindo a funcao
def f(x):
    return 1/x

#definindo o intervalo
a = float(input("Entre o valor do limite inferior do intervalo:\n"))
b = float(input("Entre o valor do limite superior do intervalo:\n"))
n = int(input("Entre a quantidade de subintervalos:\n"))

#terco simpson composto
def terco_simpson(f,a,b,n):
    h=(b-a)/n #amplitude
    som1 = 0 #primeiro somatorio
    som2 = 0 #segundo somatorio
    for i in range(1, int(n / 2 + 1)):
        som1 += f(a + (2 * i - 1) * h)
    for i in range(1, int(n / 2)):
        som2 += f(a + (2 * i) * h)
    integral = h/3*(f(a)+4*som1+2*som2+f(b)) #utilizando a formula
    return integral

print(terco_simpson(f,a,b,n))
