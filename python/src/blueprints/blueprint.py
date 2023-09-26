from flask import Blueprint, render_template, request
import os

from src.utilidades.utils import crearCarpeta, vaciarCarpeta, cargarAlgoritmo, obtenerPrediccion

bp=Blueprint("blueprint", __name__)

@bp.route("/", methods=["GET"])
def inicio():

	return render_template("inicio.html")


@bp.route("/", methods=["POST"])
def predecir():

	imagen=request.files["imagen"]

	if imagen.filename=="" or imagen.filename.split(".")[-1] not in ["jpg", "jpeg", "png"]:

		return render_template("inicio.html")

	ruta=os.path.dirname(os.path.join(os.path.dirname(__file__)))

	carpeta=os.path.join(ruta, "imagenes")

	crearCarpeta(carpeta)

	vaciarCarpeta(carpeta)

	ruta_imagen=os.path.join(carpeta, imagen.filename)

	imagen.save(ruta_imagen)

	modelo=cargarAlgoritmo(ruta)

	resultado=obtenerPrediccion(modelo, ruta_imagen)

	return render_template("inicio.html", prediccion=resultado)