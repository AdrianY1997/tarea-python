import pyttsx3

engine = pyttsx3.init()

texto = "Hola, estoy utilizando pyttsx3 para hablar en Python."

engine.setProperty('rate', 150)  
engine.setProperty('volume', 1.0)  

engine.say(texto)

engine.runAndWait()
