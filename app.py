#enviar
# Autor: Cristian Balsanelli
# Linguagem: Python 3
# Programa que calcula a quantidade de respostas 
#processamento de dados
excelente = 0 # excelente recebe 0
ruim = 0 # ruim recebe 0
for i in range(1, 51): # laço de repetição que vai de 1 a 51, ou seja, 50 vezes
    nome = input("Digite seu nome: ") # captura nome digitado e guarda na variavel nome
    idade = input("Digite sua idade: ") # captura idade digitado e guarda na variavel idade
    opiniao = input("Digite sua opiniao: 1-EXCELENTE 2-BOM 3-RUIM: ") # captura opiniao digitado e guarda na variavel opiniao
    if opiniao == "1": #se opiniao for igual a 1, entao executa linha abaixo
        excelente = excelente + 1 #calcula excelente  = execelente + 1
    elif opiniao == "3": # se opiniao for igual a 3, entao executa linha abaixo
        ruim = ruim + 1 #calcula ruim = ruim + 1
    else: #senao, se opiniao for diferente de 1 e 3, entao executa linha abaixo
         print("Digite uma opiniao valida") #imprime na tela a mensagem "Digite uma opiniao valida"
#saidas
print("Teve", excelente, "notas excelente.")#Imprime na tela a quantidade de notas excelente
print("Teve", ruim, "notas ruim.")#Imprime na tela a quantidade de notas ruim
