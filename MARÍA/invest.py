
"""Imprimir el total dels diners acumulats 
després de 7 anys, utilitzant variables (comentari a afegir al codi)
"""

savings = 100

increase = 1.1

result = savings*increase

for i in range(0,6):
    result += savings*increase


print(result)