import matplotlib.pyplot as plt
import random
def tabelaFGTS(saldo):
    if(saldo <= 500):
        return 0.5, 0
    elif(saldo > 500 and saldo <= 1000):
        return 0.4, 50
    elif(saldo > 1000 and saldo <= 5000):
        return 0.3, 150
    elif(saldo > 5000 and saldo <= 10000):
        return 0.2, 650
    elif(saldo > 10000 and saldo <= 15000):
        return 0.15, 1150
    elif(saldo > 15000 and saldo <= 20000):
        return 0.1, 1900
    elif(saldo > 20000):
        return 0.05, 2900

def calculaSaque(saldo):
    tabela = tabelaFGTS(saldo)
    saque = saldo*tabela[0] + tabela[1]
    resto = saldo - saque
    return saque, resto

historicoSaque = []
historicoSaldo = [10000]
valor = []
i = 0
while(i < 20):
    calc = calculaSaque(historicoSaldo[i])
    historicoSaque.append(calc[0])
    c = 1500 #random.randrange(1800, 3000)
    historicoSaldo.append(calc[1] + c)
    valor.append(calc[1])
    i=i+1

print (historicoSaque)
#print(valor)
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20], historicoSaque)
plt.show()
