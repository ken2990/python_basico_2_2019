#del

from Agenda import agendapacientes

def addpatient(id,telefono,nombre,direccion,enfermedad, medicamento):
    agendapacientes[id] = {'telefono' : telefono, 'nombre': nombre, 'direccion' : direccion, 'enfermedad' : enfermedad, 'medicamento' : medicamento}

def delpatient():
    del agendapacientes[id]