import re


#"../../inputs/xml.xml"
def htmlEz(file,final):
	fo = open (file)
	foL = fo.read()
	ficheiro = open(final , 'w')
	declXML = re.search(r'<\?[^?]+\?>', foL).group()

	encoding = re.search(r'encoding\s*=\s*(\"[^"]+\")', declXML).group(1)

	docHTML = re.sub(

		r'<\?[^?]+\?>',

		rf'''<!DOCTYPE html>

		<html>

			<head>

				<title>Relatório</title>

				<meta charset={encoding}/></head>''',

		foL

	)

	docHTML = re.sub(

		r'<relatorio>((.|\n)*)<\/relatorio>',

		r'<body>\n\1\n</body>\n</html>',

		docHTML

	)

	docHTML = re.sub(

		r'<titulo>((.|\n)*)<\/titulo>',

		r'<h1>\1</h1>',

		docHTML

	)

	docHTML = re.sub(

		r'<autores>((.|\n)*)<\/autores>',

		r'<h3>Autores</h3>\n<ul>\1</ul>',

		docHTML
	)

	docHTML = re.sub(
		r'<descricao>((.|\n)*)<\/descricao>',

		r'<h3>Resumo</h3>\n<p>\1</p>',

		docHTML
	)

	docHTML = re.sub(

		r'<data>((.|\n)*)<\/data>',

		r'<h2>\1</h2>',

		docHTML

	)


	print(docHTML)
	ficheiro.write(docHTML)



htmlEz("../../inputs/xml.xml","../../inputs/htmlOutput.html")


