'''
FUNCIONES
LLamadas multiples veces

Palabra para funciones: def

'''

#Ejemplos de funciones

#Funcion para sumar 2 numeros
def mi_suma(a , b):
    return a + b

#por posicion
c = mi_suma(1,2)

#por nombre
c = mi_suma(b=3, a=4)

#funcion sin parametros
def f():
    a=9
    b=0
    print('hola',a,b)

f()

pass
