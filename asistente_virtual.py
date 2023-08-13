import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

from speech_recognition import Recognizer

# esuchar microfono y devolder el audio como texto

def transformar_audio_en_texto():

    #almacenar recognizer en variable
    r = sr.Recognizer()

    #configurar microfono
    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold = 0.8

        #informar que comenzo la grabacion
        print("Escuchando")

        #guardar lo que se escuche como audio

        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio, language="es-mx")

            #prueba de que pudo ingresar
            print("Tu: " + pedido)

            #devolver pedido
            return pedido

        #en caso de que no comprenda el audio
        except sr.UnknownValueError:

            #prueba de que no comprendio el audio
            print("Ups, no entendi lo que dijiste!")

            #devolver error
            return "Sigo escuchando"

            #en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("Ups, no hay servicio!")

            # devolver error
            return "Sigo escuchando"

            #error inesperado
        except:

            # prueba de que no comprendio el audio
            print("Ups, algo salio mal!")

            # devolver error
            return "Sigo escuchando"

transformar_audio_en_texto()