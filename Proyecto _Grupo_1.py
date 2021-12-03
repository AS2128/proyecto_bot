#Importamos las librerias que utilizaremos
import re
from datetime import datetime
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader
import operator

#Definimos la opción 1
def palabras():
    preguntas_respuestas = {
        "Hola, soy Manuel": ">  Muy buenas Manuel, soy Botarate. ",
        "¿Qué tal estás?": ">  Estupendo, ¿Qué edad tienes Manuel?",
        "Tengo 21 años": ">  Muy bien, ¿En qué puedo ayudarte?",
        "¿lloverá mañana?": ">  Es muy probable, así que coge el paraguas",
        "¿A qué hora será?": ">  A partir de las 3 de la tarde",
        "Y pasado mañana": ">  También, según la predicción",
        "Qué temperatura hará": ">  Disculpa, no manejo esa información"
    }

    respuesta = False

#bucle de pregunta
    while respuesta != True:
        respuesta = input(">  ")
        listasum.append(">  " + respuesta)
        if respuesta in preguntas_respuestas:
            salida = preguntas_respuestas.get(respuesta)
            listasum.append(salida)
            print(salida)
        elif respuesta == "salir":
            listasum.append("salir")
            respuesta = True
        else:
            salida = ">  Lo siento, aún no tengo la respuesta para esa pregunta"
            listasum.append(salida)
            print(salida)

#Definimos la funcion 2
def main():
    nombre = re.compile("(.*)HOLA, SOY\s(.+)$")
    campos = re.compile("(.*)¿QUÉ SABES DE\s(.+)$\s?")
    hora = re.compile("(.*)DIME LA HORA EXACTA\s?")
    now = datetime.now()
    ui = ""
    lista=[]

    #Bucle opcion 2
    while ui.upper() != "SALIR":
        ui = input(">  ")
        lista.append(">  "+ui)
        usuario = nombre.findall(ui.upper())
        user = campos.findall(ui.upper())
        horas = hora.findall(ui.upper())

        #Comprobamos la respuesta
        if len(usuario) > 0:
            response = (">  Muy buenas, " + usuario[0][1] + ". Soy Botarate. ")
            lista.append(response)
            print(response)
        elif len(user) > 0:
            response = (">  Pues la verdad de eso sé poco. ")
            lista.append(response)
            print(response)
        elif len(horas) > 0:
            response = (">  Esta es la hora actual: {}:{}:{}".format(now.hour, now.minute, now.second))
            lista.append(response)
            print(response)
        elif ui == "salir":
            response = "Adiós"
        else:
            response = ">  Hasta luego. "
            lista.append(response)
            print(response)

    return lista

#Definimos la funcion para contar las letras
def palabrarep(quitar,listanueva):
    dicfre = {}
    for p in palabras:
        if p == "":
            dicfre[p] = 0
        elif p in dicfre:
            dicfre[p] += 1
        else:
            dicfre[p] = 1
    return dicfre

#Definimos variables generales
listasum = []
today = date.today()
opcion = 0
contadorpalabra = 0
contadorletra = 0
Salir = False
fecha=("La conversación es del {}-{}-{}.".format(today.day, today.month, today.year))
quitar = ",.;<\n"

#Menu de opciones
while Salir == False:
    print()
    print("                                         APLICACIÓN BOT-ARATE")
    print()
    print("1) Bot simple (respuestas planas...")
    print("2) Bot simple (respuestas REGEX)")
    print("3) Bot simple mejorado desde fichero")
    print("4) Informe de la conversación (PDF)")
    print("5) Salir")
    print()
    opcion = int(input("Opción: "))
    print()

#Opcion 1
    if opcion == 1:
        print("1) Bot simple (respuestas planas...")
        print()
        print(palabras())

#Opcion 2
    elif opcion == 2:
        print("2) Bot simple (respuestas REGEX)")
        print()
        print("Bot a la escucha... (pregunta cuando quieras)")
        if __name__ == "__main__":
            lista=main()
        for i in lista:
            listasum.append(i)

#Opcion 3 (Vacio)
    elif opcion == 3:
        print("3) Bot simple mejorado desde fichero")
        print()

#Opcion 4
    elif opcion == 4:
        print("4) Informe de la conversación (PDF)")
        print()

        listanueva = " \n".join(str(v) for v in listasum)
        f = open("conversacion.txt", "w")
        f.write(listanueva)
        f.close()

        texto = listanueva.replace(">", "").replace("\n", "").replace("  "," ").replace("   "," ")
        texto = texto.lower()
        palabras = texto.split(" ")
        listasum2 = " ".join(listasum)
        lista2 = listasum2.replace(">", "").replace(",", "").replace(".", "").replace("\n", "").replace(" ", "")
        contadorletra = len(lista2)

        dic = palabrarep(quitar, listanueva)
        palrep = max(dic.items(), key=operator.itemgetter(1))[0]

        canvas = canvas.Canvas("informe_conversación.pdf", pagesize=A4, )

        canvas.setFont('Helvetica', 12)

        canvas.drawString(40 * mm, 150 * mm, fecha)
        canvas.drawString(40 * mm, 140 * mm, "Consta de {} caracteres".format(contadorletra))
        canvas.drawString(40 * mm, 130 * mm, "Está compuesta por {} palabras.".format(contadorpalabra))
        canvas.drawString(40 * mm, 120 * mm, "La palabra {} aparece {} veces.".format(palrep, dic.get(palrep)))
        canvas.drawString(40 * mm, 110 * mm, listanueva)
        logo = ImageReader('chatbot_python.jpg')
        canvas.drawImage(logo, 80 * mm, 200 * mm, width=80 * mm, height=50 * mm, preserveAspectRatio=True)
        canvas.save()

#Opcion 5
    elif opcion == 5:
        print("Salir")
        Salir = True

#Comprueba que no se introduzcan datos sin opcion correspondiente
    else:
        print("Debe introducir un número entre 1 y 5")
        print()