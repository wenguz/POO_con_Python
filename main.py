import cv2
"""Proyecto en python para POO - Vision Artifical
De Wendy Guzman Rojas
"""

class Imagen:
	"""Clase base imagen que permite leer una imagen, obtener su informacion basica y guardarla """

	def __init__(self,nombre="",ruta=""):
		"""Inicializar atributos de la imagen"""
		self.name_img=nombre
		self.path_img=ruta

	def __str__(self):
		"""Metodo especial para devolver una cadena de caracteres con la informacion de la imagen"""
		return "Nombre de imagen: {} \nRuta:{}".format(self.name_img ,self.path_img)

	def leer_imagen(self):
		"""Leer una imagen desde el disco y devolver un objeto"""

		if isinstance(self.path_img,str):
			img=cv2.imread(self.path_img)
			#Mostrar la imagen en una ventana que debe ser cerrada para continuar
			cv2.imshow(self.name_img,img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
			return img
		else:
			print("Formato no valido")
			return None

	@classmethod
	def guardar_imagen(cls,img,nombre_img):
		"""Guardar una imagen procesada en formato jpg"""
		guarda_nombre=nombre_img + ".jpg"
		cv2.imwrite(guarda_nombre,img)
		print("Imagen guardada")

class VisionArtificial:
	def __init__(self,img=Imagen()):
		self.img=img
		self.fila=img.shape[0]
		self.columna=img.shape[1]
		self.canal=img.shape[2]
		self.piexeles=img.size

	def __str__(self):
		"""Metodo especial para devolver una cadena de caracteres con la informacion de la imagen"""
		return "Fila/alto:{} \nColumnas/ancho: {} \nCanales:{} \nCantidad de pixeles: {} ".format(self.fila,self.columna,self.canal,self.piexeles)

	@classmethod
	def capas(cls,img,name):
		"""Divide la imagen original en las capas RGB y las almacena"""

		b,g,r=cv2.split(img)
		print("Capa b:")
		Imagen.guardar_imagen(b,name + "_capa_1")
		print("Capa g:")
		Imagen.guardar_imagen(g,name + "_capa_2")
		print("Capa r:")
		Imagen.guardar_imagen(r,name + "_capa_3")
		return None

	@classmethod
	def region(cls,img1=Imagen(),img2=Imagen()):
		"""Sobrepone la region de una imagen sobnre una region del mismo tamaño de otra iamgen """

		#Obtiene la altura minima de las imagenes
		if img2.shape[0] >= img1.shape[0]:
			alto=img1.shape[0]
		else:
			alto=img2.shape[0]
		#Obtiene el ancho minimo de las iamgenes
		if img2.shape[1] >=img1.shape[1]:
			ancho=int(img1.shape[1]/2)
		else:
			ancho=int(img2.shape[1]/2)
		print(f"Ancho region:{ancho} , Alto region:{alto}")
		if img2.shape >= img1.shape:
			#obtener la parte de la imagen mas grande que se sobrepondra
			region1 = img2[0:alto,0:ancho]
			#colocar la parte de la imagen 2 sobre una region de la imagen pequeña
			img1[0:alto,ancho+1:]=region1
			Imagen.guardar_imagen(img1,"Imagenes sobrepuestas1")
		else:
			region1 = img1[0:alto,0:ancho]
			#colocar la parte de la imagen 2 sobre una region de la imagen pequeña
			img2[0:alto,ancho+1:]=region1
			Imagen.guardar_imagen(img2,"Imagenes sobrepuestas1")

	@staticmethod
	def imagen_gris(img):
		"""Recibe una iamgen y la devuleve en escala de grises"""

		img_gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		Imagen.guardar_imagen(img_gris,"Imagen gris")
		return img_gris


if __name__ == '__main__':
	print("--------INFORMACION IMAGEN 1---------------")
	# Instancia 1 de la clase Imagen
	gato=Imagen("Gato","images/cat.jpg")
	print(gato)
	img_gato = gato.leer_imagen()
	v1=VisionArtificial(img_gato)
	print(v1)
	img_capav1=VisionArtificial.capas(img_gato,gato.name_img)
	print(" ")
	print("--------INFORMACION IMAGEN 2---------------")

	# Instancia 2 de la clase Imagen
	carro=Imagen("Carro","images/carro.jpg")
	print(carro)
	img_carro = carro.leer_imagen()
	v2=VisionArtificial(img_carro)
	print(v2)
	img_capav2=VisionArtificial.capas(img_carro,carro.name_img)
	print(" ")
	print("-------SOBREPONER REGIONES DE DOS IMAGENES--------")
	unidas=VisionArtificial.region(img_carro,img_gato)

	print("-------OBTENER IMAGEN EN ESCALA DE GRISES------------")
	imgris=VisionArtificial.imagen_gris(img_gato)
