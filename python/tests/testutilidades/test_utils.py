import os

from src.utilidades.utils import crearCarpeta, vaciarCarpeta, cargarAlgoritmo, obtenerPrediccion

def borrarCarpeta(ruta):

	if os.path.exists(ruta):

		os.rmdir(ruta)

def crearArchivo(ruta):

	ruta_archivo=os.path.join(ruta, "Prueba2.txt")

	archivo=open(ruta_archivo,"w") 
	archivo.close()

def test_carpeta_no_existe():

	ruta_carpeta=os.path.join(os.getcwd(), "Prueba")

	assert crearCarpeta(ruta_carpeta)

def test_carpeta_existe():

	ruta_carpeta=os.path.join(os.getcwd(), "Prueba")

	assert not crearCarpeta(ruta_carpeta)

	borrarCarpeta(ruta_carpeta)

def test_vaciar_carpeta_no_existe():

	ruta_carpeta=os.path.join(os.getcwd(), "Prueba")

	assert not vaciarCarpeta(ruta_carpeta)

def test_vaciar_carpeta_existe():

	ruta_carpeta=os.path.join(os.getcwd(), "Prueba")

	crearCarpeta(ruta_carpeta)

	crearArchivo(ruta_carpeta)

	assert vaciarCarpeta(ruta_carpeta)

	borrarCarpeta(ruta_carpeta)

def test_cargar_algoritmo_error():

	ruta_relativa=os.path.abspath("..")

	assert cargarAlgoritmo(ruta_relativa) is None

def test_cargar_algoritmo():

	ruta_relativa=os.path.abspath("..")+"/src"

	assert cargarAlgoritmo(ruta_relativa) is not None

def test_obtener_prediccion():

	ruta_relativa=os.path.abspath("..")+"/src"

	modelo=cargarAlgoritmo(ruta_relativa) 

	ruta_imagen=os.path.join(os.getcwd(), "testapp", "imagen_tests.jpg")

	prediccion=obtenerPrediccion(modelo, ruta_imagen)

	assert prediccion=="Mercedes"