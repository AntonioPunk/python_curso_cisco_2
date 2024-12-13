pi = "pi = Pi, pi, pi"
sin = "sin = Sin, sin, sin"

print(pi)
print(sin)

# Ahora vamos a importar solo un elemento del módulo math:

from math import pi

# Para usar 'pi' del módulo ya no necesitamos escribir math.pi
# Esto entraría en conflicto con la variable 'pi' que existía en nuestro código,
# por ello el namespace hace que pi de math sustituya a "nuestro" pi.
# Ejemplo:

print(pi)

# Otra forma de importar un módulo es:

from math import *

# Este método importa todas las entidades del módulo y nos libera de
# tener que enumerar las entidades cuando las usamos (ejem: math.py).
# NO es recomendable ya que podrían entrar en conflicto con entidades de nuestro código
# sin darnos cuenta.

print(sin)
print(sin(pi/2))

# CONCEPTO DE 'ALIASING':
# Consiste en importar un módulo y cambiarle el nombre con el que
# deseamos enumerar sus entidades.
# Ejemplo:

import sys as s

print(f"La versión de Python es: {s.version}")

# Si lo que deseamos es cambiar el nombre de la entidad en vez del módulo:

from math import sin as seno

print(seno(pi/2))