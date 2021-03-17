def html (texto):

	if res := re.search(r'encoding\s*=\s*(\"[^"]+\")', texto):

		print(f'''<!DOCTYPE html>

<html>

	<head>

		<title>Relatório</title>

		<meta charset={res.group(1)}/>

	</head>''')


	elif (re.search(r'<relatorio>', texto)):

		print("\t<body>")


	elif (re.search(r'<\/relatorio>', texto)):

		print("\t</body>\n</html>")


	elif res := re.search(r'<titulo>((.|\n)*)<\/titulo>', texto):

		print("\t\t<h1>", res.group(1), "</h1>")


	elif res := re.search(r'<data>((.|\n)*)<\/data>', texto):

		print("\t\t<h1>", res.group(1), "</h1>")


	elif (re.search(r'<autores>', texto)):

		print("\t\t<h3>Autores</h3>\n\t\t<ul>")


	elif (re.search(r'<\/autores>', texto)):

		print("\t\t</ul>")


	elif (re.search(r'<autor>', texto)):

		print("\t\t\t<li>", end='')


	elif (re.search(r'<\/autor>', texto)):

		print("</li>")


	elif res := re.search(r'<nome>((.|\n)*)<\/nome>', texto):

		print(res.group(1), end='')


	elif res := re.search(r'<numero>((.|\n)*)<\/numero>', texto):

		print(" (", res.group(1), end=')')


	elif res := re.search(r'<email>((.|\n)*)<\/email>', texto):

		print(": ", res.group(1), end='')


	elif (re.search(r'<descricao>', texto)):

		print("\t\t<h3>Resumo</h3>")


	elif (re.search(r'<\/descricao>', texto)):

		pass


	else:

		print(texto)
