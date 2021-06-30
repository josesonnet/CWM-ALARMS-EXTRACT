PARAMETROS, SEÑAL, ALARMAS = [], [], []
# stINPUT_FILE_NAME = str(input("Por favor ingrese el nombre del archivo a procesar: "))
stINPUT_FILE_NAME = "__vardef.ini"
fINPUT_FILE = open(stINPUT_FILE_NAME, 'r')
stOUTPUT_FILE_NAME = str(input("Por favor ingrese el nombre del archivo destino: "))
# stOUTPUT_FILE_NAME = "prueba1.txt"
fOUTPUT_FILE = open(stOUTPUT_FILE_NAME, 'w')
LINEA = fINPUT_FILE.readline()
while LINEA != "" :
    if LINEA[:5] == "[SIG_":
        LINEA = fINPUT_FILE.readline()
        while LINEA[:5] !=  "[SIG_":
            PARAMETROS.append(LINEA[:-1]) #guardo sin \n
            LINEA = fINPUT_FILE.readline()
            if LINEA == "": break
        else:
            for P in PARAMETROS:
                if P[:9] == "Name=@GV.":
                    SEÑAL.append("Nombre: " + P[9:])
                elif P[:6] == "Alarm=":
                    SEÑAL.append("Tipo: " + P[6:])
                elif P[:7] == "LogPri=":
                    SEÑAL.append("Pri= " + P[7:])
                elif P[:5] == "HiDB=" or P[:5] == "LoDB=":
                    pass
#                 elif P[:8] == "HiHiPri=":
#                     SEÑAL.append(P)
#                 elif P[:6] == "HiPri=":
#                     SEÑAL.insert(3, P[6:])
#                 elif P[:6] == "LoPri=":
#                     SEÑAL.insert(4, P[6:])
#                 elif P[:8] == "LoLoPri=":
#                     SEÑAL.insert(5, P[8:])
#                 elif P[:5] == "Desc=":
#                     SEÑAL.insert(6, P[5:])
#                 elif P[:6] == "Units=":
#                     SEÑAL.insert(7, P[6:])
                else:
                    SEÑAL.append(P)
            else: #si termino con PARAMETROS
                PARAMETROS = []
            if SEÑAL[1][:6] == "Tipo: ":
                ALARMAS.append(SEÑAL)
            SEÑAL = []
    else:
        LINEA = fINPUT_FILE.readline()
else: #while LINEA != "" :
    ALARMAS.sort()
    for A in ALARMAS:
        fOUTPUT_FILE.write(str(A) + '\n')
    fINPUT_FILE.close()
    fOUTPUT_FILE.close()
