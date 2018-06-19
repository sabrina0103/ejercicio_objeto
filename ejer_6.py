class ArtefactoElectrico:
	def __init__(self,marca,modelo,color,estado = 'APAGADO'):
		self.__marca = marca
		self.__modelo =modelo
		self.__color = color
		self.__estado = estado

	def encender(self):
		self.__estado = "ENCENDIDO"

	def apagar(self):
		self.__estado = "APAGADO"

	def get_estado(self):
		print("Estado: ",self.__estado)

	def ver_info(self):
		# print("Marca: ",self.__marca+"\nModelo: ",self.__modelo+"\nColor: ",self.__color)
		print("Marca: ",self.__marca+"\nModelo: ",self.__modelo+"\nColor: ",self.__color)

	def __str__(self):
		return 'Marca: {}\nModelo: {}\nColor: {}'.format(self.__marca,self.__modelo,self.__color)

