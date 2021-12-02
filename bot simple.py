preguntas_respuestas = {
  "Hola, soy Manuel": "Muy buenas Manuel, soy Botarate.",
  "¿Qué tal estás?": "Estupendo, ¿Qué edad tienes Manuel?", "Tengo 21 años": "Muy bien, ¿En qué puedo ayudarte?",
  "¿lloverá mañana?": "Es muy probable, así que coge el paraguas", "¿A qué hora será?": "A partir de las 3 de la tarde",
    "Y pasado mañana": "También, según la predicción", "Qué temperatura hará": "Disculpa, no manejo esa información"
}

respuesta = ""

while respuesta != "salir":
    respuesta = input("> ")
    if respuesta in preguntas_respuestas:
        salida = preguntas_respuestas.get(respuesta)
    else:
        salida = "Lo siento, aún no tengo la respuesta paara esa pregunta"
    print(salida)
