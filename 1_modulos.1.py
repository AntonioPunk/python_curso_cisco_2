# Vamos a importar 2 módulos, math y sys (se recomienda importarlos en líneas
# separadas aunque se puede en 1 sola mediante ','):

import math
import sys

# Los módulos se pueden importar en cualquier punto del código
# pero SIEMPRE ANTES DE UTILIZARLOS

# Para acceder a un elemento (objeto, clase, constante...) de math lo haremos así:

print(math.pi)

# Esto es así para que el nombre de los elementos del módulo
# no interfiera con posibles elementos de nuetro código que se llamen igual.
# Concepto de: namespace

pi = "Pi, pi, pi"

print(pi)
print(math.pi)

