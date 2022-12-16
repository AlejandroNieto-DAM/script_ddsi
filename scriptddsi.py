import requests
import csv

urls = [

"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/diseno-desarrollo-sistemas-informacion/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/fundamentos-redes/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/informatica-grafica/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/ingenieria-servidores/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/modelos-computacion/guia-docente",

"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/administracion-bases-datos-esistinformac/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/administracion-bases-datos-esistinformac/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/aprendizaje-automaticoecomputacy-sistintelig/guia-docente",
"https://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/arquitectura-sistemas-einga-computadores/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/arquity-computacde-altas-prestacioneseingcom/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/computacubicua-inteligambiental-etecnolinf/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/desarrollo-hardware-digitaleingcomputador/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/desarrollo-sistemas-distribuidos-eing-soft/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/desarrollo-software-eingenieria-software/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/diseno-interfaces-usuario-ing-software/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/diseno-sistemas-electronicos-eingcomputador/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/ingenieria-sistemas-informacionesistinf/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/ingenieria-conocimientoecomputy-sistint/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/metaheuristicas-ecomputacy-sistinteligentes/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/modelos-avanzados-computacionecompsist/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/programacion-web-esistemas-informacion/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/servidores-web-altas-prestaciones-etecinf/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/sistemas-graficos-ingenieria-software/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/sistemas-multidimensionales-espsistinformacion/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/sistemas-multimedia-etecnologias-informac/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/sistemas-microprocesadores-eingcomputador/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/sistemas-informacion-basados-webeingsoft/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/sistemas-informacion-empresasesistinf/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/tecnologias-web-esp-tecnologias-informacion/guia-docente",
"http://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica/transmisde-datos-redes-computadetecinf/guia-docente"

]


data = {}
asignatura = ""


for url in urls:

    r = requests.get(url, allow_redirects=True)
    open('a', 'wb').write(r.content)

    title = url.split("/")

    print(title[6])
    asignatura = title[6]

    file1 = open('a', 'r')
    Lines = file1.readlines()

    diccionario = [" SPA", " WAF", " C++", "Ruby", "Back-End", "Front-End", " XML", 
    "JAVA", "JSON", "HTML", "CSS", " JavaScript",  "Javascript", "Python", "PHP", 
    "Business Logic", "COBOL", "AJAX", " JSP", " ASP"]

    list_word = set()
    search = False
    for line in Lines:

        if "Bibliografía" in line:
            break

        if "contenidos" in line:
            search = True

        if search:
            line_split = line.split(" ")
            for word1 in line_split:
                if word1 == "C" or word1 == "Java":
                    list_word.add(word1)
            for word in diccionario:
                if word in line and not "/" + word in line:
                    list_word.add(word)

                
                
    if search:
        data[asignatura] = list_word


print(data)

columns = ['Asigntura', 'Contenidos']

with open('Salida.csv', 'w') as f:
    for key in data.keys():
        f.write("%s, %s\n" % (key, data[key]))



