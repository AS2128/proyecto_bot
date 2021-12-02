import re
from datetime import datetime


def main():
    nombre = re.compile("(.*)HOLA, SOY\s(.+)$")
    campos = re.compile("(.*)¿QUÉ SABES DE\s(.+)$\s?")
    hora = re.compile("(.*)DIME LA HORA EXACTA\s?")
    now = datetime.now()
    ui = ""

    while ui.upper() != "SALIR":
        ui = input(">  ")
        usuario = nombre.findall(ui.upper())
        user = campos.findall(ui.upper())
        horas = hora.findall(ui.upper())

        if len(usuario) > 0:
            response = (">  Muy buenas, " + usuario[0][1] + ". Soy Botarate")
        elif len(user) > 0:
            response = (">  Pues la verdad de eso sé poco.")
        elif len(horas) > 0:
            response = (">  Esta es la hora actual: {}:{}:{}".format(now.hour, now.minute, now.second))

        else:
            response = ">  Hasta luego."
        print(response)


opcion = 0
Salir = False
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

    if opcion == 1:
        print("1) Bot simple (respuestas planas...")

    elif opcion == 2:
        print("2) Bot simple (respuestas REGEX)")
        print()
        print("Bot a la escucha... (pregunta cuando quieras)")
        if __name__ == "__main__":
            main()

    elif opcion == 3:
        print("3) Bot simple mejorado desde fichero")

    elif opcion == 4:
        print("4) Informe de la conversación (PDF)")

    elif opcion == 5:
        print("Salir")
        Salir = True

    else:
        print("Debe introducir un número entre 1 y 5")

def botfichero():
    fichero = open("preguntasrespuestas", 'wb')
    listaPatronesRespuestas = [[patronSaludoNombre, patronNombre, patronSaludoSimple, patronPregunta,
                                patronQueDiaEsHoy],
                               ["\t\t>Muy buenas, xx. Soy Botarate", "\t\t>Encantado de conocerte, xx.",
                                respuestasSaludo, "\t\t>De xx se poco la verdad", "\t\t>Hoy es xx"]]
    pickle.dump(listaPatronesRespuestas, fichero)
    fichero.close()

    entrada = ""
    print("\t\tBot a la escucha...(pregunta cuando quieras)\n")
    # Mientras no se ponga "salir" o "Salir" funcionará el bot.
    while entrada.casefold() != "salir".casefold():
        entrada = input("\t\t>")
        comprobarentradafichero(entrada)

    print("\t\t>¡Hasta la próxima!\n")
    c = open("conversacion.txt", "a")
    c.write("\t\t>¡Hasta la próxima!\n")
