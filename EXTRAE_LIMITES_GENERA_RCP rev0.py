ROW = []
stINPUT_FILE_NAME = str(input("Por favor ingrese el nombre del archivo a procesar: "))
#stINPUT_FILE_NAME = "__vardef.ini"
fINPUT_FILE = open(stINPUT_FILE_NAME, 'r')
stOUTPUT_FILE_NAME = str(input("Por favor ingrese el nombre del archivo destino: "))
# stOUTPUT_FILE_NAME = "prueba1.txt"
fOUTPUT_FILE = open(stOUTPUT_FILE_NAME, 'w')
LINEA = fINPUT_FILE.readline()
while LINEA != "" :
    while "~@GV." in LINEA:
        iSTART = LINEA.index("~@GV.")
        iEND = LINEA.index("'",iSTART)
        stSEÑAL = LINEA[iSTART + 1:iEND]
        ROW.append(stSEÑAL + " 0")
        LINEA = LINEA[iSTART + 1:]
    else:
        LINEA = fINPUT_FILE.readline()
else: #while LINEA != "" :
    ROW.sort()
    for R in ROW:
        fOUTPUT_FILE.write(str(R) + '\n')
    fINPUT_FILE.close()
    fOUTPUT_FILE.close()
