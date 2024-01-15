numeros=([1,2,3])
numero=10

def somanumero(list):
    return sum(list)

def antesus(numero):
    antec= numero-1
    suc=numero+1
    
    return antec, suc

def mensagem():
    print("Seja bem vindo!")

print(somanumero(numeros))
print(antesus(numero))
print (mensagem())


    