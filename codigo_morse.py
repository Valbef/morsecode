import re

MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",

    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-."
}

# Diccionario inverso: Morse -> carácter
MORSE_INVERSO = {valor: clave for clave, valor in MORSE.items()}


def traducir_a_morse(texto):

    #Convierte texto/números a Morse.

    #Las palabras se separan mediante dos espacios.
    #Las letras se separan mediante un espacio.


    palabras = texto.upper().split()
    resultado = []

    for palabra in palabras:
        letras = []

        for caracter in palabra:
            if caracter in MORSE:
                letras.append(MORSE[caracter])
            else:
                letras.append(f"[{caracter}]")

        resultado.append(" ".join(letras))

    # Dos espacios = separación entre palabras
    return "  ".join(resultado)


def traducir_desde_morse(morse):

    #Convierte Morse a texto.
    #Se admiten dos formas de separar palabras:
    #1. Dos o más espacios.
    #2. Una barra.
    #Un espacio simple separa letras.

    morse = morse.strip()

    # Convertimos "/" rodeada de espacios en separación de palabras.
    morse = re.sub(r"\s*/\s*", "  ", morse)

    # Dos o más espacios = separación entre palabras
    palabras = re.split(r"\s{2,}", morse)

    resultado = []

    for palabra in palabras:
        letras = palabra.split()
        texto = ""

        for codigo in letras:
            if codigo in MORSE_INVERSO:
                texto += MORSE_INVERSO[codigo]
            else:
                texto += f"[{codigo}]"

        resultado.append(texto)

    return " ".join(resultado)


def main():
    print("===============================")
    print(" TRADUCTOR BIDIRECCIONAL MORSE")
    print(" By:Valbef              v1.0.0")
    print("===============================")

    while True:
        print("\nSelecciona una opción:")
        print("1. Texto/Números -> Morse")
        print("2. Morse -> Texto/Números")
        print("3. Salir")

        opcion = input("\nOpción: ").strip()

        if opcion == "1":
            texto = input("\nIntroduce el texto o números: ")

            resultado = traducir_a_morse(texto)

            print("\nResultado en Morse:")
            print(resultado)

        elif opcion == "2":
            morse = input("\nIntroduce el código Morse: ")

            resultado = traducir_desde_morse(morse)

            print("\nResultado en texto:")
            print(resultado)

        elif opcion == "3":
            print("\n¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Elige 1, 2 o 3.")


if __name__ == "__main__":
    main()
