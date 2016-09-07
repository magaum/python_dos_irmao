#exercício 1
import random
vetor = []
contador = 0
num_maior = 0
num_menor = 100
while contador <= 9:
#biblioteca para gerar números aleatórios
	c = random.randint(0,100)
#adicionando valor a lista 'vetor'
	vetor.append(c)
	c = vetor [contador]
	contador = contador + 1

	if c >= num_maior:
		num_maior = c

	if c <= num_menor:
		num_menor = c
#sort organiza a lista em ordem crescente
vetor.sort()
#print (vetor,'\nO menor número da lista é: ',vetor[0],'\nO maior número da lista é: ',vetor[9])
print ('\n',vetor, '\nnumero menor: ',num_menor,'\nnumero maior: ', num_maior)

#exercício 2
import random
vetor = []
par = []
impar = []
for reprtição in range (19):
	c = random.randint(0,100)
	b = vetor.append(c)
	if c % 2 == 0:
		par.append(c)
	else:
		impar.append(c)
print ('\nLista inteira', vetor[:], '\nLista com números pares',  par[:],'\nListas com números impares', impar[:])

#exercício 3
# criando vetores com números aleatórios de 1 a 100 e um terceiro vetor com o conteudo dos dois anteriores intercalados

# importando biblioteca random
import random

# definindo variáveis
primeira_lista = []
segunda_lista = []
terceira_lista = []
#repetição
for contador in range (9):
# jogando valores aleatórios na lista
	lista = primeira_lista.append(random.randint(0,100))
	lista = segunda_lista.append(random.randint(0,100))
# pegando valores das listas 1 e 2 e jogando na 3
	lista = primeira_lista[contador]
	terceira_lista.append(lista)
	lista = segunda_lista[contador]
	terceira_lista.append(lista)
print ('\nprimeira lista' ,primeira_lista [:], '\nsegunda lista', segunda_lista [:], '\nterceira lista', terceira_lista[:])

#exercício 4
lista_python = []
lista = '''the python software foundation and the global python community welcome and encourage participation by everyone
our community is based on mutual respect tolerance and encouragement and we are working to help each other live up to these principles
we want our community to be more diverse whoever you are and whatever your background we welcome you'''.split()
#contador = 0
print ('\n',lista)
for contador in range (len (lista)):
#while contador < len(lista):
	palavra_lista = lista [contador]
	if palavra_lista [0] in "python":
		lista_python.append(palavra_lista)
	if palavra_lista [-1] in "python":
		lista_python.append(palavra_lista)
#	contador += 1
print('\n',lista_python)

#exercício 5
lista_python = []
lista = '''the python software foundation and the global python community welcome and encourage participation by everyone
our community is based on mutual respect tolerance and encouragement and we are working to help each other live up to these principles
we want our community to be more diverse whoever you are and whatever your background we welcome you'''.split()
#contador = 0
print ('\n',lista)
for contador in range (len (lista)):
#while contador < len(lista):
	palavra_lista = lista [contador]
	if palavra_lista [0:-0] in 'python' and (len(palavra_lista))> 4:
		lista_python.append(palavra_lista)
#	contador += 1
print('\nO número de palavras com as letras de "python" e com mais de 4 letras é',len(lista_python),'\n')
