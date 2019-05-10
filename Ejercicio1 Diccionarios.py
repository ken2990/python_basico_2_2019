'''
1. Crear una agenda de contactos, utilizando diccionario.
Con los siguientes nombres e informacion

Juan Perez      83013040    jperez@gmail.com
Carlos Rojas    87001030    crojas@hotmail.com
Ana Marin       91000813    amarin@yahoo.com

( ) -> tupla
[ ] -> lista

2. Cuantos contactos hay en la agenda?
3. Quienes estan en la agenda?
4. Utilizando el diccionario creado en 1. imprima las informaciones de cada contacto, de la siguiente manera;
    Nombre: Juan Perez      Telefono: xxxxx Correo: xxxx
    Nombre: Carlos Rojas    Telefono: xxxxx Correo: xxxx
    Nombre: Ana Marin       Telefono: xxxxx Correo: xxxx
5. Suponga que Juan Perez cambio de telefono, tiene 2 telefonos nuevos; 63101111, 233333
6. Nuevo contacto, Sofia, telefono 3333333, correo: sofia@gmail.com
'''

#1. Gmo
AgendaGmo = {

'Juan Perez' : ('Perez', 'Juan', '83013040', 'jperez@gmail.com'),
'Carlos Rojas' : ('Rojas, Carlos', '87001030', 'crojas@hotmail.com'),
'Ana Marin' : ('Marin, Ana', '91000813', 'amarin@yahoo.com')

}
#1. Profe
agenda = {
    'juan perez' : {'telefono':'83103040',
                    'correo':'jperez@gmail.com'},
    'carlos rojas' : {'telefono':'87001030',
                      'correo':'crojas@hotmail.com'},
    'ana marin' : {'telefono':'91000813',
                   'correo':'amarin@yahoo.com'}

}

#Evaluate expression:
# agenda ['juan perez']['telefono']


#2. Cuantos contactos hay en la agenda?
#evaluate expression
len(agenda)


#3. Quienes estan en la agenda?
#evaluate expression
list(agenda.keys())

#4. Utilizando el diccionario creado en 1. imprima las informaciones de cada contacto (ver Linea14)
#Comando: for   +  .keys(), items(), values()
#for x,y in agenda.items():

#Gmo
# for contacto in agenda.items(): print(contacto)

#Profe
#Usando keys()
for persona in agenda.keys():
    print('nombre:', persona,
          'telefono:', agenda[persona]['telefono'],
          'correo:', agenda[persona]['correo'])

#Usando items() -> me da una lista de tuplas
print('con items')
for persona, info in agenda.items():
    print('nombre:',persona,
          'telefono:', info['telefono'],
          'correo:',info['correo'])

#5. Suponga que Juan Perez cambio de telefono, tiene 2 telefonos nuevos; 63101111, 233333
agenda['juan perez']['telefono']=['6310111', '23333333']

#6. Nuevo contacto, Sofia, telefono 3333333, correo: sofia@gmail.com
#Opcion1: podemos crear un diccionario para Sofia
sofia = {'telefono': 33333333,
         'correo':'sofia@gmail.com'}

agenda['sofia castro']=sofia

#Opcion2: update en un diccionario
agenda.update({'sofia alfaro':sofia})





pass