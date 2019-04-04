import string

def nuevoparrafo(linea):
    resultado=linea.splitlines()
    return len(resultado)

a = input ("¿Qué archivo quieres leer?: ")
archivo = open(a, "r")
texto = archivo.read()

vocales= "aeiouáéíóúAEIOUAÉÍÓÚ"
digitos ="1234567890"
consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
especiales= "áéíóúäëïöüñ"
numerovocales = ""
numeroconsonantes = ""
numerodigitos =""
numeroespacioblanco = ""
numerootroscaracteres =""
numeromayusculas = ""
numerominusculas = ""
espacioblanco = " "

for letra in texto:
    if letra in digitos:
        numerodigitos += letra

palabras = len(texto.split(" ")) + len(texto.split("\n"))

for letra in texto:
    if letra in vocales:
        numerovocales += letra
for letra in texto:
    if letra in consonantes:
        numeroconsonantes += letra

for letra in texto:
    if letra in espacioblanco:
        numeroespacioblanco += letra

for letra in texto:
    if letra in string.punctuation:
        numerootroscaracteres += letra

for letra in texto:
    if letra in string.ascii_uppercase:
        numeromayusculas += letra

for letra in texto:
    if letra in (string.ascii_lowercase + especiales):
        numerominusculas += letra
        
cuentapalabras= str(palabras-len(numerodigitos))
cuentavocales= str(len(numerovocales))
cuentaconsonantes =  str(len(numeroconsonantes))
cuentamayusculas = str(len(numeromayusculas))
cuentaminusculas = str(len(numerominusculas))
cuentadigitos = str(len(numerodigitos))
cuentaespacios = str(len(numeroespacioblanco))
cuentacaracteres = str(len(numerootroscaracteres))
cuentaparrafo = str(nuevoparrafo(texto))

fEstadisticas= open('stats.txt', 'w+')
Estadisticas = ('Palabras: {}\nVocales: {}\nConsonantes: {}\nMayúsculas: {}\nMinúsculas: {}\nDígitos: {}\nEspacios: {}\nCaracteres: {}\nPárrafos: {}'.format(cuentapalabras, cuentavocales, cuentaconsonantes, cuentamayusculas, cuentaminusculas, cuentadigitos, cuentaespacios, cuentacaracteres, cuentaparrafo))
fEstadisticas.write(Estadisticas)
fEstadisticas.close()

archivo = open(a, "r")
textoprueba = archivo.read()

totalLineas = 0
listaLineas = []
todaslineas = []

with open(a) as textoprueba:
    lines = textoprueba.readlines()
    lineas = []
    for line in lines:
        lineprueba = line.split(".")
        lineprueba = [line.capitalize() for line in lineprueba]
        linea1 = (". ".join(lineprueba))
        linea2 = linea1.split()
        linea3 = (" ".join(linea2))
        line4 = linea3.split(" .")
        line5 = (".".join(line4))
        
        line6 = line5.split(",")
        line7 = (", ".join(line6))
        line8 = (line7.replace(" ,", ","))
        
        lineas.append(line8)
        lineasformato = ("\n".join(lineas))

fcorreccion= open('correct.txt', 'w+')
Correccion = (lineasformato)
fcorreccion.write(Correccion)
fcorreccion.close()