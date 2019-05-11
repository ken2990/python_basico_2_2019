
# crear una clase llamada bebe

# declarar 4 acciones, respirar, comer, llorar, dormir

# simular un dia normal un bebe


class bebe:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad


    def respirar(self):
        print('bebe respira')

    def comer(self):
        print('bebe come')

    def llorar(self):
        print('bebe llora')

    def dormir(self):
        print('bebe duerme')

    def crecer(self, edad=1):
        if (self.edad + edad) > 24:
            self.vivo = False

        else:
            self.edad += edad
            self.vivo = True


dude = bebe('panchito', 1)

print('cual es tu nombre?', dude.nombre)


print('mi edad es', dude.edad)

dude.crecer(2)

print('mi edad es', dude.edad)



dude.respirar()
dude.llorar()
dude.dormir()
dude.comer()

