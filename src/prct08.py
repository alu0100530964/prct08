#!/user/bin/python
#! encoding: UTF-8

import sys
import math
import modulo
# Programa principal

argumentos = sys.argv[1:]
 # print argumentos         Imprime la lista con los parametros que le des desde la consola
if (len(argumentos) == 8):  # Ocho argumentos
  n = int(argumentos[0])
  aproximaciones = int(argumentos[1])
  umbral = []
  for i in range (2,7):
    umbral.append(float (argumentos[i]))
  nombre_fichero = argumento [7]
else:
  print "Introduzca el nº de intervalos (n>0):"
  n = int (raw_input())
  print "Introduzca el nº de aproximaciones (aproximaciones>0):"
  aproximaciones = int(raw_input())
  print "Introduce 5 umbrales"
  umbral = []
  for i in range (5):
    print "Introduzca el umbral", i,":"
    umbral.append(float(raw_input()))
  print "Introduzca el nombre del fichero para almacenar los resultados:"
  nombre_fichero = raw_input()
if (n > 0):
  try:
    fichero = open (nombre_fichero, "a")
  except:
    fichero = open (nombre_fichero, "w")
  fichero.write ("Nº de intervalos:%d\n"%(aproximaciones))
  for i in range (5):
    porcentaje=modulo.error (n,aproximaciones, umbral[i])
    fichero.write ("%2.2f%% de fallos para el umbral %2.5f\n"%(porcentaje,umbral[i]))
  fichero.close()
else:
  print "EL valor de los intervalos debe ser mayor que 0"