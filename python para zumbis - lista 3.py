# exercício 1
valor = 11
while valor > 10:
	valor = int(input('digite um valor de 0 (zero) a 10 (dez) para desabilitar o shell: '))

# exercício 2
print ('\ndigite usuário e senha \n###### USUÁRIO E SENHA NÃO PODEM SER OS MESMOS ######')
usuário = str(input('usuário: '))
senha = str(input('senha: '))
if usuário == senha:
	while usuário == senha:
		print ('digite usuário e senha \n###### USUÁRIO E SENHA NÃO PODEM SER OS MESMOS ######')
		usuário = str(input('usuário: '))
		senha = str(input('senha: '))

# exercício 3
print ('\naumento da população A em comparação com a população B')
população_A = 80000
população_B = 200000
quantia_ano = 0
if população_A <= população_B:
	while população_A <= população_B:
		aumento_A = (população_A * 3) / 100 + população_A
		aumento_B = (população_B * 1.5) / 100 + população_B
		população_A = aumento_A
		população_B = aumento_B
		quantia_ano = quantia_ano + 1
print ('o tempo é de %d anos' %quantia_ano)

# exercício 4
print ('\nFormula de Fibonacci: (F 1 = 1, F 2 = 1, F 3 = 2)\nEx: se valor a for 1 e valor 2 for 1 a sequencia ficará 1,1,2,3,5,8,13,21,34,55,89...')

na = int(input('digite um número inteiro: '))
nb = int(input('digite outro número inteiro: '))
nc = na + nb
while na < 1000:
	print(na,nb)
	na = nc
	nb = nb + nc
	nc = na + nb

# exercício 5
print ('\ndeterminando DMC entre inteiros positivos utilizando algoritmo de euclides')
c = 1
a = int(input('digite um número inteiro: '))
b = int(input('digite outro número inteiro: '))
while a or b or c != 0:
	if a > b:
		c = int(a % b)
		if c == 0:
			print ('o D.M.C é %d' %b)
			break
		if a == 0:
			print ('o D.M.C é %d' %c)
			break
		if b == 0:
			print ('o D.M.C é %d' %a)
			break
		a = c
	if a < b:
		c = int(b % a)
		if c == 0:
			print ('o D.M.C é %d' %a)
			break
		if a == 0:
			print ('o D.M.C é %d' %b)
			break
		if b == 0:
			print ('o D.M.C é %d' %c)
			break
		b = c
