"""1. Texto a Voz
La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible
en formato mp3. Para ello puedes hacer uso de bibliotecas existenes como nltk (kit de
herramientas de lenguaje natural), newspaper3k y gtts (puedes seguir las instrucciones de
instalación de pip).
Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para
luego manejar la conversión de texto a voz."""

import newspaper
from gtts import gTTS
import os

# Función para convertir texto a voz y guardar como archivo mp3
def texto_a_voz(texto, nombre_archivo):
    # Crear objeto gTTS con el texto y el idioma
    tts = gTTS(text=texto, lang='es')

    # Guardar el archivo de audio como mp3
    tts.save(nombre_archivo + ".mp3")

    # Reproducir el archivo de audio
    os.system("ffplay -nodisp -autoexit " + nombre_archivo + ".mp3")

# Función para extraer el texto de un artículo de una URL y convertirlo a voz
def convertir_articulo_a_voz(url):
    # Crear objeto de artículo utilizando la URL proporcionada
    articulo = newspaper.Article(url)
    articulo.download()
    articulo.parse()

    # Obtener el texto del artículo
    texto_articulo = articulo.text

    # Convertir el texto a voz y guardarlo como archivo mp3
    texto_a_voz(texto_articulo, "articulo")

# URL del artículo a convertir
url_articulo = input("Ingrese la URL del artículo: ")

# Llamar a la función para convertir el artículo a voz
convertir_articulo_a_voz(url_articulo)