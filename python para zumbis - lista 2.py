# exercício 1
lado_1 = int(input('digite o valor do primeiro lado do triangulo: '))
lado_2 = int(input('digite o valor do segundo lado do triangulo: '))
base = int(input('digite o valor da base do triangulo: '))

if lado_1 != lado_2 and lado_1 != base and lado_2 != base:
	print ('o triangulo é escaleno')

elif lado_1 == lado_2 and lado_1 == base and lado_2 == base:
	print ('o triangulo é equilátero')

else:
	print ('o triangulo é isoceles')

# exercício 2

ano = int(input('\ndigite o valor de um ano, e saiba se ele é bisexto: '))

if ano % 4 == 0 and ano % 100 != 0 and ano % 400 != 0:
	print ('ano bisexto!')
else:
	print ('ano não é bisexto')

#exercício 3
peso = float(input('\ndigite o peso do peixe: '))

if peso > 50:
	excesso = peso - 50
	multa = excesso * 4
	print ('a multa é de R$ %.2f' %multa)
else:
	print ('ZERO')

#exercício 4
print ('\ndigite 3 números e o maior deles será exibido na tela')
numero_1 = int(input('digite o primeiro número: '))
numero_2 = int(input('digite o segundo número: '))
numero_3 = int(input('digite o terceiro número: '))

print (max(numero_1, numero_2, numero_3))

#exercício 5
print ('\ndigite 3 números e o maior e o menor deles serão exibidos na tela')
numero_1 = int(input('digite o primeiro número: '))
numero_2 = int(input('digite o segundo número: '))
numero_3 = int(input('digite o terceiro número: '))

if numero_1 > numero_2 and numero_1 > numero_3:
	print ('numero %d é maior' %numero_1)
	
if numero_1 < numero_2 and numero_1 < numero_3:
	print ('numero %d é menor' %numero_1)

if numero_2 > numero_1 and numero_2 > numero_3:
	print ('numero %d é maior' %numero_2)
	
if numero_2 < numero_1 and numero_2 < numero_3:
	print ('numero %d é menor' %numero_2)

if numero_3 > numero_2 and numero_3 > numero_1:
	print ('numero %d é maior' %numero_3)

else:
	print ('numero %d é menor' %numero_3)

#exercício 6
salário_hora = float(input('\ndigite o valor do salário recebido por horas trabalhadas: '))
numero_hora = float(input('digite o número de horas trabalhadas: '))

salário_bruto = salário_hora * numero_hora
IR = salário_bruto * 11 / 100
INSS = salário_bruto * 8 / 100
sindicato = salário_bruto * 5 / 100
salário_líquido = salário_bruto - IR - INSS - sindicato

print ('\nSalário bruto: R$', salário_bruto, '\nIR: R$', IR, '\nINSS: R$', INSS, '\nSindicato: R$',sindicato, '\nSalário líquido R$', salário_líquido)

#exercício 7
metros = int(input('digite o valor em metros quadrados da área onde será pintada: '))
litros = metros / 3
quantidade = 1
preco = 80

if litros % 18 == 0:
    litros = litros / 18
    quantidade = litros
    preco = quantidade * 80
else:
    litros = int(litros / 18) + 1
    quantidade = litros
    preco = quantidade * 80
        

print ('o número de latas a ser comprado é: %d' %quantidade, 'e o valor é: R$ %d'%preco)
