#Crear un codigo que calcule las soluciones de la ecuacion cuadrada  ax(a la 2) + bx + c = 0


import math

#a = float(input(1))

#b = float(input(2))

#c = float(input(1))

#print('ax**2 + bx + c = 0')

# Solucion Profe


#Ecuacion cuadratica

a = float(input('Deme a'))
b = float(input('Deme b'))
c = float(input('Deme c'))

discriminante = b ** 2 - 4*a*c

raiz = math.sqrt(discriminante)

x1 = (-b + raiz) / (2*a)
x2 = (-b - raiz) / (2*a)

print(x1, x2)


# if discriminante < 0:
# raiz = math.sqrt(-discriminante)
# else
# raiz = math.sqrt(discriminante)










