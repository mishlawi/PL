import re

key = re.compile(r'^\((\+|\-)?[0-9]?[0-9](\.[0-9]{1,})?\,\s(\+|\-)?(180|1[0-7][0-9]|[0-9]?[0-9])((\.[0-9]{1,})?)\)$')


print("nr de elems a considerar")
n = int(input())
print("Input:")
bools =[]
for i in range(n):
	x = True
	linha = input()
	res = key.search(linha)
	
	if not res:
		x=False

	bools.append(x)
print("Output:")
for tof in bools:
	if tof:
		print("valido")
	else:
		print("invalido")
