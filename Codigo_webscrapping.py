from urllib.request import urlopen


def webscrapping():
    """
    Función que obtiene 20 palabras aleatorias de una página web, las guarda en un archivo, las lee y las imprime desde el mismo
    :return:
    """
    url = "https://www.epasatiempos.es/sopas-de-letras-al-azar.php"
    page = urlopen(url)
    html = page.read().decode("utf-8")

    wordlist_index = html.find("wordlist=[")
    iterador = wordlist_index+10
    cadena = ""
    while html[iterador] != "]":
        cadena += html[iterador]
        iterador += 1
    linea = cadena.strip('"').split('","')
    diccionario_vocales_especiales = {"\\u00c1":"Á", "\\u00e1":"á", "\\u00c9":"É", "\\u00e9":"é", "\\u00cd":"Í",
                                      "\\u00ed":"í", "\\u00d3":"Ó", "\\u00f3":"ó", "\\u00da":"Ú", "\\u00fa":"ú",
                                      "\\u00dc":"Ü", "\\u00fc":"ü", "\\u00d1":"Ñ", "\\u00f1":"ñ"}

    arch_palabras = open("palabras.txt", "w")
    variable = 0
    for palabra in linea:
        for iterador in range (len(palabra)-1):
            if 0 < variable < 6:
                variable += 1
                continue
            if palabra[iterador:iterador+1] == "\\":
                arch_palabras.write(diccionario_vocales_especiales[palabra[iterador:iterador+6]])
                variable = 1
            else:
                arch_palabras.write(palabra[iterador])
        arch_palabras.write(palabra[iterador+1] + "\n")
    arch_palabras.close()
    arch_palabras = open("palabras.txt", "r")
    palabras = arch_palabras.readlines()
    print("PALABRAS:\n")
    for palabra in palabras:
        print(palabra, end="")
    arch_palabras.close()
def main():
    webscrapping()

main()
