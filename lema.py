import nltk
import nltk.data
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

def lematizar(ruta,token):
	listaizq=[]
	listader=[]
	listafinal=[]
	with open (ruta,'r',encoding="utf8")as file:
		texto = file.read()
		archivo=texto.split()
	#return(archivo)	
	for i in range(len(archivo)):
		if(i%2==0): #para saber si es par 
			listader.append(archivo[i])
		else:
			listaizq.append(archivo[i])

	for i in token:
		if(i in listader):
			indice=listader.index(i)
			listafinal.append(listaizq[indice])
		else:
			listafinal.append(i)
			
	return resultado




listaCargada=lematizar('lemmatization-es.txt')
print(listaCargada)
