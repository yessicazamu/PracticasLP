import nltk
import nltk.data
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


def tokensito(ruta):
# Tokenizador TokTok (palabras)
	# Tokenizador de oraciones
	# Obtener oraciones de un parrafo
	with open (ruta,'r',encoding="utf8")as file:
		parrafo = file.read()
		toktok = ToktokTokenizer()
		es_tokenizador_oraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
		oraciones = es_tokenizador_oraciones.tokenize(parrafo)
		# Obtener tokens de cada oracion´
		lista=[]
		for s in oraciones:
			lista=lista+([t for t in toktok.tokenize(s)])
		return(lista)

def frecuencia(token): #contar
	listaGeneral= []
	listaNumero = []
	listaPalabras =[]
	longitud=len(token)
	primera=token[0]
	listaPalabras.append(primera)
	listaNumero.append(1)
	#print(longitud)
	contador=0
	while(contador<longitud-1):
		if(primera==token[contador+1]):
			listaNumero[0]=listaNumero[0]+1
		elif(token[contador + 1] in listaPalabras):
			#Puntar en que posición se tiene guardada para aumentarle el contador 
			indice = listaPalabras.index(token[contador + 1])
			#Agrega el valor en la pcisión que tiene la palabra igual
			listaNumero[indice] = listaNumero[indice] + 1
		else:
			listaPalabras.append(token[contador + 1])
			listaNumero.append(1)
		contador = contador + 1
	for i in range(len(listaPalabras)):
		listaGeneral.append((listaNumero[i],listaPalabras[i]))
	listaGeneral.sort(reverse=True)
	return listaGeneral

def reduccion(token): #reducción de palabras funcionales
	contador=0 #lleva el ciclo
	longitud=len(token)
	auxiliar=0 #lleva los indices
	palabrasfuncionales=stopwords.words("spanish")
	while (contador<longitud):
		if(token[auxiliar]in palabrasfuncionales):
			token.remove(token[auxiliar])
			auxiliar=auxiliar-1
		contador=contador+1
		auxiliar=auxiliar+1
	longitudnueva=len(token)
	#print(longitud)
	#print(longitudnueva)
	return token

def stemizacion(token):
	lista=[]
	stemmer = SnowballStemmer("spanish")
	for t in token:
		lista.append(stemmer.stem(t)) # Obtener la raiz
	return lista #regresas la lista 

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
			
	return listafinal

#llamar funcion
token=tokensito('practica3.txt')#se guarda lo que regresa la función 
#print(token) #imprime el token original

lista=frecuencia(token) #las frecuencias del todo token
#print(lista) #imprime el token con su frecuencia

listaReducida=reduccion(token) #reduccion de palabras funcionales
#print(listaReducida) #imprime el token con la reducción (quita las palabras funcionales)

frecuenciaSinFuncion=frecuencia(listaReducida) #las frecuencias sin palabras funcionales
#print(frecuenciaSinFuncion) #imprime la frecuencia del token sin palabras funcionales

listastemming=stemizacion(listaReducida) #stemming
#print(listastemming)
frecuenciaStem=frecuencia(listastemming) #esta es la lista que sacas con el stremming 
#print(frecuenciaStem)

listaReducida=reduccion(token) #cargar token sin palabras funcionales
lema=lematizar('lemmatization-es.txt',listaReducida) #donde se va a lematizar sin palabras funcionales (Lematizado)
listaConFrecuencia=frecuencia(lema) #cuentas las frecuencias de la lematizacion sin palabras funcionales
print(listaConFrecuencia) #imprimes

