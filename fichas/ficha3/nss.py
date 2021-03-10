import re

def querie():
	bools = []
	key = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')
	print("INSIRA NR DE DADOS A CONSIDERAR")
	n = int(input())
	
	if n<1 or n>=101:
		print("ERROR.\nOversize")
		exit()
	else:
		print("*******************************")
		for elem in range(n):
			data = input()
			res = key.search(data)
			if res:
				bools.append(True)
			else:
				bools.append(False)
	for elems in bools:
		if elems == True:
			print("YES")
		if elems == False:
			print("NO")


querie()