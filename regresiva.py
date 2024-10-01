import sys
import time


#cuenta regresiva debera llegar a 0

argumentos = sys.argv

try:
    desde = int(argumentos[1])
except IndexError:
    print("no hay argumentos")
    sys.exit()
except ValueError:
    print("el argumento no es un entero")
    sys.exit()


for n in range(desde,0,-1):
    print(n)
    time.sleep(1)
