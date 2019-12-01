# -*- coding: utf-8 -*-

class ahorcado():


	def __init__(self, num_fallas,palabra): #atributos
		self.num_fallas = num_fallas
		self.palabra = palabra	
		self.adivinadas = []
		self.ya_gane = False
		self.ya_perdi = False
		self.falle = 0

	def jugar(self,letra): #metodos
		if letra in self.palabra:
			self.adivinadas.append(letra)
			gane= True
			for letra in self.palabra:
				if letra not in self.adivinadas:
					gane= False
				if gane:
					self.ya_gane
		else:	
			self.falle+=1
		if self.falle>=self.num_fallas:
			self.ya_perdi
		self.estado()

	def estado(self):
		temp_palabras = ""
		#errores = falle-1
		for letra in self.palabra:
			if letra in self.adivinadas:
				temp_palabras += letra
			else:
				temp_palabras +="-"
		print(temp_palabras)
		print("llevas %d errores"%(self.falle))


palabra = input('palabra: ')
num_fallas = int(input("numero de errores: "))
ah = ahorcado(num_fallas,palabra)
while not ah.ya_gane:
	nueva_letra = input("dame una nueva letra:")
	ah.jugar(nueva_letra)

