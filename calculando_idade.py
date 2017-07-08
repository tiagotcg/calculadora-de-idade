import time

############################################################################### DEFININDO A DATA ATUAL:
data_atual = time.localtime()
dia_atual = int(data_atual.tm_mday)
mes_atual = int(data_atual.tm_mon)
ano_atual = int(data_atual.tm_year)


print("Hoje é dia {} do mês {} do ano {} ".format(dia_atual, mes_atual, ano_atual))
print("(Today is {} / {} / {} )".format(ano_atual, mes_atual, dia_atual))

print("------------------------------------------------------------------------------------------------------------------------------------------------------------ \n \n ")

############################################################################### SOLICITANDO OS DADOS DA DATA DE NASCIMENTO:
print("Digite a data no formato dd / mm / aaaa")
print("(Put the date like this: yyyy / mm / dd ) \n")

ano_nascimento = int(input("Qual o ano de nascimento? (What's the year of birth?) "))
mes_nascimento = int(input("Qual o mês de nascimento? (and the month of birth?) "))
dia_nascimento = int(input("Qual o dia de nascimento? (and the day of birth?) "))


############################################################################### FAZENDO A LISTA DOS ANOS BISSEXTOS (0 A 2100):
listaB = []		#criando a lista que irá agrupar os anos que foram/serão bissextos do ano 0 ao ano 2100.
x = 2016		# 2016 pq eu sei que foi ano bissexto!
while x >= 0:
	listaB.append(x)
	x -= 4

x = 2016
while x < 2100:
    listaB.append(x)
    x += 4

listaB.sort()


############################################################################### DEFININDO QUANTOS DIAS TEM CADA MÊS:

if mes_nascimento == 1:
	quantidade_dias_mes_referido = 31
elif mes_nascimento == 2:
	if ano_nascimento in listaB:
		quantidade_dias_mes_referido = 29
	else:
		quantidade_dias_mes_referido = 28
elif mes_nascimento == 3:
	quantidade_dias_mes_referido = 31
elif mes_nascimento == 4:
	quantidade_dias_mes_referido = 30
elif mes_nascimento == 5:
	quantidade_dias_mes_referido = 31
elif mes_nascimento == 6:
	quantidade_dias_mes_referido = 30
elif mes_nascimento == 7:
	quantidade_dias_mes_referido = 31
elif mes_nascimento == 8:
	quantidade_dias_mes_referido = 31
elif mes_nascimento == 9:
	quantidade_dias_mes_referido = 30
elif mes_nascimento == 10:
	quantidade_dias_mes_referido = 31
elif mes_nascimento == 11:
	quantidade_dias_mes_referido = 30
elif mes_nascimento == 12:
	quantidade_dias_mes_referido = 31
else:
	print("DATA INVÁLIDA! (invalid date!) ")
	exit()

############################################################################### CALCULANDO A IDADE:

# 1) Comparando anos:
anos_total = ano_atual - ano_nascimento

# 2) Comparando os meses e os dias:
## se mes_nascimento > mes_atual:
if mes_nascimento > mes_atual:
	anos_total -= 1
	### calculando os meses:
	meses_total = mes_atual + (12 - mes_nascimento)
	### calculando os dias:
	if dia_nascimento < dia_atual:
		dias_total = dia_atual - dia_nascimento
	elif dia_nascimento == dia_atual:
		dias_total = 0
	else:
		dias_total = (quantidade_dias_mes_referido - dia_nascimento) + dia_atual
		meses_total -= 1

## se mes_nascimento = mes_atual:
elif mes_nascimento == mes_atual:
	### calculando os meses:
	### calculando os dias:
	if dia_nascimento > dia_atual:
		anos_total -= 1
		meses_total = 11
		dias_total = (quantidade_dias_mes_referido - dia_nascimento) + dia_atual
	else:
		meses_total = 0
		dias_total = dia_atual - dia_nascimento

## se mes_nascimento < mes_atual:
else:
	### calculando os meses:
		#### comparando os dias:
			##### se dia_atual < dia_nascimento:
	if dia_atual < dia_nascimento:
		meses_total = mes_atual - mes_nascimento - 1
					###### calculando os dias:
		dias_total = dia_atual + (quantidade_dias_mes_referido - dia_nascimento)
			##### se dia_atual >= dia_nascimento:
	else:
		meses_total = mes_atual - mes_nascimento
					###### calculando os dias:
		dias_total = dia_atual - dia_nascimento

# 3) Definindo a idade:
print("\nSua idade é: {} anos {} meses e {} dias. ".format(anos_total, meses_total, dias_total))
print("Your age is: {} year(s) {} month(s) and {} day(s). \n".format(anos_total, meses_total, dias_total))


while True:
        continue
