def estudiantes():
    archivo = open('Estudiantes.prn', 'r')

    cadena = archivo.read()
    listEst = cadena.split("\n")

    archivo.close()
    list = set()
    for mnp in listEst:
        tupla=(mnp[:8], mnp[8:])
        list.add(tupla)
    return list

def materias():
    archivo = open('Kardex.txt', 'r')

    cadena = archivo.read()
    listEst = cadena.split("\n")

    archivo.close()
    conjunto = set()
    for mnp in listEst:
        mnp1 = mnp.split("|")
        tupla=(mnp1[0], mnp1[1], mnp1[2])
        conjunto.add(tupla)
    return conjunto

def todo(consultar):
    estudiante = estudiantes()
    materia = materias()
    list = []
    ban = True
    for info in consultar:
        for est in estudiante:
            dir = {}
            if info == int(est[0]):
                ban = False
                dir["Nombre"] = est[1]
                listaMaterias = []
                for mat in materia:
                    if info == int(mat[0]):
                        listaMaterias.append(mat[1])
                dir["Materias"] = listaMaterias
                list.append(dir)
    if ban:
        for est in estudiante:
            dir = {}
            dir["Nombre"] = est[1]
            listaMaterias = []
            for mat in materia:
                if int(est[0]) == int(mat[0]):
                    listaMaterias.append(mat[1])
            dir["Materias"] = listaMaterias
            list.append(dir)
    return list



datos=todo([18420427,18420428])
print(datos)