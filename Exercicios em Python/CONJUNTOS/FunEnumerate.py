#As vezes é necessário saber o indice do objeto dentro do
# laço for. Para isso usamos Enumerate.

carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")