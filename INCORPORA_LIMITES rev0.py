TEXTO = []
stOUTPUT_FILE_NAME = str(input("Por favor ingrese el nombre del archivo a modificar (*.txt):\n"))
#stOUTPUT_FILE_NAME = "ALARMAS RTU1401A.txt"
fOUTPUT_FILE_NAME = open(stOUTPUT_FILE_NAME, 'r')
TEXTO = fOUTPUT_FILE_NAME.readlines()
fOUTPUT_FILE_NAME.close()
stINPUT_FILE_NAME = str(input("Por favor ingrese el nombre del archivo a procesar (*.rcp):\n "))
#stINPUT_FILE_NAME = "RTU1401A.rcp"
fINPUT_FILE = open(stINPUT_FILE_NAME, 'r')
stOUTPUT_FILE_NAME = stOUTPUT_FILE_NAME[:-4] + "_modificado.txt"
fOUTPUT_FILE = open(stOUTPUT_FILE_NAME, 'w')
LINEA = fINPUT_FILE.readline()
while LINEA != "":
    iEND = LINEA.index(" ")
    stSEÑAL = LINEA[:iEND]
    stVALOR = LINEA[iEND + 1:-1]
    for L in TEXTO:
        if stSEÑAL in L:
            iINDEX = TEXTO.index(L)
            N = L.replace(stSEÑAL, stVALOR)
            TEXTO.remove(L)
            TEXTO.insert(iINDEX, N)
            break
    LINEA = fINPUT_FILE.readline()
else: #while LINEA != "" :
    for L in TEXTO:
        if "~" in L:
            stNEWLINE = L.replace("~","")
            iINDEX = TEXTO.index(L)
            TEXTO.remove(L)
            TEXTO.insert(iINDEX, stNEWLINE)
            fOUTPUT_FILE.write(TEXTO[iINDEX])
        else:
            fOUTPUT_FILE.write(L)
    fINPUT_FILE.close()
    fOUTPUT_FILE.close()
