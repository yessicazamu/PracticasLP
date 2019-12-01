import nltk
import nltk.data
from nltk.metrics.distance import edit_distance
#= solo uno para asiganar dos == para preguntar 

def corrector(rutamal,rutabien):
	var=50
	txtbien=[]
	with open (rutamal,'r',encoding="utf8")as file:
		auxmal = file.read()
		textomal=auxmal.split()
	with open (rutabien,'r',encoding="utf8")as file:
		auxdic = file.read()
		diccionario=auxdic.split()
	for i in range(len(textomal)): #ciclo para recorrer las palabras
		for j in range(len(diccionario)):
			distancia=edit_distance(textomal[i],diccionario[j],1,False)
			if(distancia<var):
				var=distancia
				palabra=diccionario[j]
		var=50		
		print(palabra)		
		txtbien.append(palabra)
	cadena=" ".join(txtbien)
	with open("corregido.txt",'w',encoding="utf8")as file:
		file.write(cadena)

corrector('corrigeme.txt','listado-general.txt')
