import cv2

class Imagen:

    @staticmethod
    def read_image(path_img):
        """Leer una imagen desde el disco y devolver in objeto imagen"""
        if isinstance(path_img, str):
            img = cv2.imread(path_img)  #lee la imagen
            #Mostrar La imagen, esperar tecla para cerrar y destruir ventanas
            cv2.imshow('imagen original',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return img
        else:
            print("formato no valido")
            return None

    @classmethod
    def save_img(cls,img, name_img):
        # escribir validador de string, regex, validar que un string termine en jpg
        name_img = name_img + ".jpg"
        cv2.imwrite(name_img, img)

    @classmethod
    def capas(cls,img,name):
        #Division de capas de imagen
        b,g,r = cv2.split(img)
        #une las capas nuevamente
        img = cv2.merge((b,g,r))
        cls.save_img(img=b, name_img=name +"_capas1")
        cls.save_img(img=g, name_img=name + "_capas2")
        cls.save_img(img=r, name_img=name+"_capas3")
        return None

    @classmethod
    def region(cls,img1):
        img2= cv2.imread("images/carro.jpg")
        #obtener la parte de la imagen en estas posiciones
        region = img2[43:600, 260:713] 
        #colocar la imagen 2 en la posicion de 1
        img1[0:557, 530:983] = region
        #guardar la imagen
        cls.save_img(img=img1, name_img="gatito_carro")
        
    @staticmethod
    def dimensiones(img):
        #filas,columnas,canales
        print(f"Filas,columnas,canales: {img.shape}")
        #tamaño
        print(f"Cantidad de pixeles: {img.size}")

        
    @staticmethod
    def img_to_gray_scale(img):
        #Recibe un objeto imagen y devuleve la imagen en blanco y negro"""
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray_img


if __name__ == '__main__':
    img_gato=Imagen()
    img_gato = img_gato.read_image("images/cat.jpg")
    print("Datos Gato")
    Imagen.dimensiones(img_gato)

    img_gray = Imagen.img_to_gray_scale(img_gato)
    Imagen.save_img(img=img_gray, name_img="gatito_gris")
    print("Imagen gris guradada")

    img_capa1=Imagen.capas(img_gato,"gato")
    print("Capas RGB guardadas")

    Imagen.region(img_gato)
    print("Imagen gato y region carro guardada")
    print("--------------------------------")
    img_carro=Imagen()
    img_carro=img_carro.read_image("images/carro.jpg")
    print("Datos carro")
    Imagen.dimensiones(img_carro)

    img_capa2=Imagen.capas(img_carro,"carro")
    print("Capas RGB guardadas")
