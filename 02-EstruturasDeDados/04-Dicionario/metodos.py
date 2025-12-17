'''Metodos da classe dict

{}.clear -> limpa  
{}.copy -> copia 
{}.fromkeys -> Cria chaves sem atribuições
{}.get -> acessa valores dentro do dicionario 
{}.items
{}.keys -> Retorna só os valores das chaves sem levar em conta os elementos a ela atribuido
{}.pop -> remove a chave. 
{}.update -> atualiza o dicionario com outro dicionario 
{}.values ->  Retorna apenas os valores das chaves
{}.in -> forma de saber se uma chave existe no dicionario
{}.del -> remove um valor do dicionario


'''

carros = { "jeep" : {"nome": "Renegade", "ano": 2025, "motor" : "T270"},
          "fiat" : {"nome": "Mobi", "ano": 2018, "motor" : "Firefly"},
          "VW" : {"nome": "polo", "ano": 2020, "motor": " 1.6 MSI"}
}

novos_carros = carros.copy()
#print(novos_carros)

#carros.clear()
#print(carros)
#print(novos_carros.get("jeep",{}).get("motor"))
#print(novos_carros.get("fiat", {}).get("nome"))
#print(novos_carros.get("VW",{}).get("ano"))

novos_carros.update({"Toyota" : {"nome": "corolla", "ano" : 2020, "motor" : "2.0 Dynamic Force Flex"}})

#print(novos_carros)
novos_carros.pop("jeep")
print(novos_carros)