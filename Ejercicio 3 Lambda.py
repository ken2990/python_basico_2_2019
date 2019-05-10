'''
Ejercicios:
1. Crear una calculadora que sume, reste, multplique, divida, a^b, raiz. Utilizando lambdas
'''

#1. suma
suma=lambda x,y:x+y
resta=lambda x,y:x-y
multiple=lambda x,y:x*y
divide=lambda x,y:x/y
import math
potencia=lambda x,y:math.pow(x,y)
raiz=lambda x,y:math.pow(x, 1/y)

x=3
y=2

lista_funciones = [suma,resta,multiple,divide,potencia,raiz]
for mi_funcion in lista_funciones:
    print('resultado=', mi_funcion(x,y))

'''
Ejercicios:
2. Crear un diccionario de funciones
'''

calculadora = {
    'suma' : lambda x,y :x+y,
    'resta' : resta,
    'multiplica' : multiple,
    'divide' : divide,
    'potencia' : potencia,
    'raiz' : raiz
}

#usando dict
print('usando dict')
for g in calculadora.values():
    print('resultados=',g(x,y))


pass