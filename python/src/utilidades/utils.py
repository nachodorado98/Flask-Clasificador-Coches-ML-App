import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from typing import Optional, Any

# Funcion para crear una carpeta si no existe 
def crearCarpeta(ruta:str)->bool:

	if not os.path.exists(ruta):

		os.mkdir(ruta)
		return True

	return False

# Funcion para vaciar una carpeta
def vaciarCarpeta(ruta:str)->bool:

	if os.path.exists(ruta):

		for archivo in os.listdir(ruta):

			os.remove(os.path.join(ruta, archivo))

		return True

	return False

# Funcion para cargar el algoritmo
def cargarAlgoritmo(ruta:str)->Optional[Any]:

	try:

		ruta_modelo=os.path.join(ruta, "algoritmo", "modelo.h5")

		return load_model(ruta_modelo)

	except:

		return None

# Funcion para obtener la prediccion del coche
def obtenerPrediccion(modelo:Any, ruta_imagen:str)->str:

	imagen=load_img(ruta_imagen, target_size=(224,224))

	imagen_array=img_to_array(imagen)

	imagen_reescalada=imagen_array/255

	imagen_expandida=np.expand_dims(imagen_reescalada, axis=0)
	
	imagen_final=preprocess_input(imagen_expandida)

	resultado=modelo.predict(imagen_final)

	valor=np.argmax(resultado, axis=1)

	if valor==0:

		return "Audi" 

	elif valor==1:

		return "Lamborghini"

	else:

		return "Mercedes"