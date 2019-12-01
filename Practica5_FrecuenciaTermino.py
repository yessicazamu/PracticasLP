import nltk
import nltk.data
import math
from nltk.metrics.distance import edit_distance

#= solo uno para asiganar dos == para preguntar 

def frecuenciatermino(doc,termin):
	documento=doc
	termino=termin
	contador=0
	with open (doc,'r',encoding="utf8")as file:
		documento = file.read()
		texto=documento.split()
	for i in texto:
		if (i==termino):
			contador=contador+1
	return contador

def contarTerminos(termino,Documentos):
	contador=0
	for i in Documentos:
		if(termino in i):
			contador=contador+1
	return contador

def funciontfidf(doc,Documentos,termino):

	contador=0
	with open (doc,'r',encoding="utf8")as file:
		document = file.read()
		documento=document.split()
	izquierda=frecuenciatermino(doc,termino)/len(documento)
	derecha=math.log(len(Documentos)/(contarTerminos(termino,Documentos)))
	#print(contarTerminos(termino,Documentos))
	tfidf=izquierda*derecha
	return tfidf

def matriztfidf(termino,Documentos):
	documentos=[]
	fila=[]
	columna=[]
	for i in Documentos:
		with open(i,'r',encoding="utf8")as file:
			document=file.read()
			doc=document.split()
		documentos.append(doc)
	for i in range(len(Documentos)):
		for j in termino:
			fila.append(funciontfidf(Documentos[i],documentos,j))
		columna.append(fila)
		fila=[]
	return columna

def coseno(vectorA,vectorB):
	suma=0
	sumaA=0
	sumaB=0
	raizA=0
	raizB=0
	multiplicacion=0
	resultadoCoseno=0
	for i in range(len(vectorA)):
		suma=(vectorA[i]*vectorB[i])+suma
		sumaA=(vectorA[i]*vectorA[i])+sumaA #el cuadrado del vector a
		sumaB=(vectorB[i]*vectorB[i])+sumaB #el cuadraro del vector B
	raizA=math.sqrt(sumaA) 
	raizB=math.sqrt(sumaB)
	multiplicacion=raizA*raizB
	resultadoCoseno=suma/multiplicacion
	return resultadoCoseno
def matrizCoseno(matriz):
	fila=[]
	columna=[]
	for i in matriz: #valor de la izquierda de los valores (A,A)
		for j in matriz: #para el valor derecho de los valores (A,A)
			fila.append(coseno(i,j))
		columna.append(fila)
		fila=[]
	return columna

termino=["hola","como"]
Documentos=["prueba.txt","doc2.txt"]
matriz=matriztfidf(termino,Documentos)
print(matriz)
formulacoseno=coseno(matriz[0],matriz[1])
print(formulacoseno)
matrizsimilitud=matrizCoseno(matriz)
print(matrizsimilitud)



