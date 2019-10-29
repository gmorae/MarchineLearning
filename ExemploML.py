#Biblioteca sklearn
#Vamos trabalhar com arore de decisão => tree
#Vamos trabalhar tambem com arvore de decisões
from sklearn import tree

lisa = 1
irregular = 0 

maça = 1
laranja = 0 

#--------------------------------------|
#               TABELA                 |
#--------------------------------------|
#   PESO    |  SUPERFICE  |  RESULTADO |
#--------------------------------------|
#   150     |  lisa       |  maça      |
#   130     |  lisa       |  maça      |
#   180     |  irregular  |  laranja   |
#   160     |  irregular  |  laranja   |
#--------------------------------------|

#lista dentro de lista
pomar = [[150, lisa], [130, lisa], [180, irregular], [160, irregular]]

resultado = [maça, maça, laranja, laranja]

#criar um classificador que é igual a uma arvore de decisão
classificador = tree.DecisionTreeClassifier()
#fit serve para ele fazer uma analise entre pomar e resultado
classificador = classificador.fit(pomar, resultado)

#inputs para os usuarios entrar com os dados 
peso = input("Entre com o peso: ")
superficie = input("Entre com a superficie ( 1 -> lisa, 0 -> irregular)")

#predit ele pega os dados que o usuario entrou e 
# verifica onde ele mais se enqudra dentro do lassificador 
result = classificador.predict([[peso, superficie]])

if result == 1 :
    print("É uma maça")
else:
    print("É uma laranja")



