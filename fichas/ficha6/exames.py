from operator import itemgetter
import calendar
import re



#_id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado





fo = open ("../../inputs/emd.csv")
info = fo.read()
fo = open("../../inputs/emd.csv")
data = [elem.rstrip().split(",") for elem in fo][1:]

def querie1():
#Produz uma listagem apenas com o primeiro e ultimo nome do atleta e a cidade onde vive;

	namecity = [[elem[3] + ' ' + elem[4],elem[7]] for elem in data]

	print('Nome   ||','Cidade')
	print('+++++++++++++++++++')
	for elem in namecity:
		print(elem[0],'||',elem[1])


def querie2():
#Produz uma lista ordenada alfabeticamente dos clubes desportivos registados, no fim indica quantos sao;
	rascunho = [elem[9] for elem in data]
	rascunho.sort()
	clubes = []
	[clubes.append(elem) for elem in rascunho if elem not in clubes]
	print("***Nao repetidos***")
	for elem in clubes:
		print(elem)
	print("Nr:",len(clubes))
	print("*******Repetidos*******")
	for elem in rascunho:
		print(elem)
	print("Nr:", len(rascunho))
	
def querie3():
	#Produz uma lista ordenada alfabeticamente das modalidades registadas, no fim indica quantas sao

	rascunho = [elem[8] for elem in data]
	rascunho.sort()
	modalidades = []
	[modalidades.append(elem) for elem in rascunho if elem not in modalidades]
	print("***Nao repetidas***")
	for elem in modalidades:
		print(elem)
	print("Nr:",len(modalidades))
	print("*******Repetidas*******")
	for elem in rascunho:
		print(elem)
	print("Nr:", len(rascunho))
	

def querie4():
	#Qual a distribuicao de atletas registados por sexo?
	m = f = 0 
	mf = [elem[6] for elem in data]
	s, h = re.compile(r'[F]'), re.compile(r'[M]')
	print("Distribuicao tendo em conta o registo por sexo")
	for mfs in mf:
		resF = s.search(mfs)
		resM = h.search(mfs)
		if resF:
			f+=1
		if resM:
			m+=1
	print("Existem", m,"individuos do sexo masculino")
	print("Existem", f,"individuos do sexo feminino")
	print("Total de individuos:", len(data))

def querie5():
	tof = re.compile(r'true')
	fed = [elem[-1] for elem in data if tof.search(elem[-1])]
	apto = [elem[-2] for elem in data if tof.search(elem[-2])]
	print("Numero de atletas federados:",len(fed))
	print("Numero de atletas que passaram o teste:",len(apto))

def querie6():
	#Quantos  atletas  do  sexo feminino realizaram exame em 2020?  E em cada um dos outros anos
	dic = {}
	sr = re.compile(r'F')
	fem = [elem for elem in data if sr.search(elem[6])]
	print(len(fem))
	for date in fem:
		yr = re.search(r'\d{4}',date[2]).group()
		if yr in dic:
			dic.update({yr:dic[yr]+1})
		else:
			dic.update({yr:1})
	for elem in dic:
		print("Ano:",elem, "| Numero atletas femininas:", dic[elem])

def querie7():
	atl = re.compile(r'Atletismo')
	atletismo = [atletas for atletas in data if atl.search(atletas[8])]
	idades = sorted(atletismo,key=itemgetter(5))
	for elem in idades:
		print(elem[3] , elem[4], elem[5], "||", elem[8])

	
def querie8():

	dic = {}
	for elem in data:
		if elem[8] in dic:
			dic.update({elem[8]:dic[elem[8]]+1})
		else:
			dic.update({elem[8]:1})
	dicSorted = sorted(zip(dic.keys(),dic.values()))
	for elem in dicSorted:
		print(elem[0], "-->", elem[1] )



def querie9():
	dic = {}
	mes = re.compile(r'\-\d{2}\-')
	x = re.findall(mes,info)
	x= [re.sub(r'-','',elem) for elem in x]
	for elem in x:
		if elem in dic:
			dic.update({elem:dic[elem]+1})
		else:
			dic.update({elem:1})
	for elem in dic:
		print(calendar.month_name[int(elem)],':', dic[elem])






querie9()