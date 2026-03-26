# # 4  tipos
# # str      int             float    bool
# # textos numeros inteiros reais lógicos
# # 'texto',  10 ,  5.2 ,  True , False
# # 'Bom dia', 2026,1.80, 1 , 0
# # 'Seu nome:',1, 60.200, 
# # 'R$'


# # ESTRUTURAS DE DADOS ****


# # espaços na memória ram da maquina
# # variar
# # variaveis são dados únicos
# # interpertador 
# # meio termo linguagem 
# # força indentação = organização
# # OUTPUT - SAIDA - print()
# # nomear de forma semantica  -  boa pratica


# # regras para criar variáveis:
# # _ ou letra
# # não pode começar por números 
# # não pode carcateres especiais 
# # pode utilizar números(só não pode começar)
# # palavra composta snake_case


# # linguagem alto nivel
# # interpretada
# # dinamica - variáveis


# print('CADASTRO DE USUÁRIOS:')


# nome = 'Lucas Lima'
# idade  =  25
# email_usuario = 'lucas@gmail.com'
# peso = 80.50
# altura =  1.90
# endereco = 'Rua 10, Jd X'
# graduacao = 'ADS'
# casado = False 


# # SAÍDA
# print(nome)
# print(idade)
# print(email_usuario)
# print(endereco)
# print(graduacao)
# print(peso)
# print(altura)
# print(casado)


# # ENTRADA


# #nome_2 = input('digite seu nome: ')
# #print(nome_2)

# #numero1 = float(input('Digite um número:'))
# #numero2 = float(input('Digite outro número:'))

# #soma = numero1 + numero2
# #print(soma)

# print('IMC')


# peso =  float(input('Digite seu peso: '))
# altura  =  float(input('Digite sua altura: '))
# imc  =  peso/altura**2
# print('IMC', imc)

# print('SINAIS DE CALCULO ARITMÉTICO')



# print(10+200) # soma
# print(10-200) # subtração
# print(10*200) # multiplicalçi
# print(10/200) # divisão
# print('modulo', 10%200) #módulo
# print(10**2) # potencia
# print(10//200.0) # divisão c/ 2 barras


# # variáveis -  estruturas de dados 
# # funções  - print() input() float() int()
# # sinais aritmétivos 



# # sinais lógicos


# print(10 == 200) # comparar
# print(10 > 200) # verifa se 1º numero é maior
# print(10<200) # verifa se 1º numero é menor
# print(10>=200) # maior ou iguael
# print(10<=200) # menor ou igual
# print(10 != 2) # diferente

# numero1 = float(input('Digite um número:'))
# numero2 = float(input('Digite outro número:'))

# soma = numero1 + numero2
# subtracao = numero1 - numero2
# multiplicacao = numero1 * numero2
# divisao = numero1 / numero2

# print(f'Soma = {soma}, Subtração = {subtracao}, Multiplição = {multiplicacao}, Divisão = {divisao}')

# if numero1 == numero2:
#      print('Os 2 números são iguais!')
# else:
#         print('Os 2 números são diferentes!')

# if numero1 > numero2:
#     print(f'{numero1} é maior que {numero2}!')
# else:
#     print (f'{numero1} é menor ou igual a {numero2}')

# if numero1 >10 or numero2 > 10:
#      print('Um dos números é maior que 10!')
# else:
#      print('Nenhum dos números é maior que 10!')

# produto = float(input('Insira o valor de um produto:'))
# porcentagem = 10
# desconto = produto * (porcentagem/100)
# resultado = produto - desconto
# print(f'O valor com desconto de 10% é:{resultado}')

# if resultado > 100:
#     print('O valor deu mais de 100 conto!')
# else:
#     print('O valor deu menos de 100 conto!')

# if resultado < 50:
#     print('Ficou no precinho!')
# else:
#     print('Tá salgado ainda!')

#Forma que a professoa fez:
# Peça o valor de um produto e:
# produto =  float(input('Digite o valor do produto: '))


# # Calcule um desconto de 10%.


# desconto = produto * 0.10


# Mostre o valor final.


# valor_prod = produto - desconto
# print('Valor do produto R$', valor_prod)


# # Verifique se o valor final é maior que 100.


# print('Verifique se o valor final é maior que 100 - ', valor_prod > 100)


# # Verifique se o produto ficou barato (menor que 50).


# print('Verifique se o produto ficou barato (menor que 50) - ', valor_prod < 50)

listas = [1,2,3,4,5]
#         0 1 2 3 4
lista_texto = ['um','dois','três','quatro','cinco']
#               0     1      2       3        4
lista_mista = ['a', True, 5.5]
#               0    1     2
lista_vazia = []
#Adicionar um dado a lista
lista_vazia.append(100)
print(lista_vazia)
lista_vazia.remove(100)
print(lista_vazia)
lista_vazia.append(15)
lista_vazia.append(360)
lista_vazia.append('one')
print(lista_vazia)
lista_vazia.insert(2, 720)
lista_vazia.pop()
lista_vazia.count(15)
print(lista_vazia)
print('Contagem:', lista_vazia.count(15))

l = [1,2,3]
indice = l.index(1)
l.pop(indice)
print(l)