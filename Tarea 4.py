#Suponga que se tiene una lista de listas que se tiene diversas cantidades por persona.
# La primera columna con números representa la cantidad en miles de colones que tienen en la cuenta del banco,
# la segunda columna la cantidad en crédito en miles de colones y
# la tercer columna en miles de colones en deuda.



import statistics

hoja_calculo = {'': None, 'carlos': {'debito': 54.54,
                               'credito': 6.57,
                               'deuda': 3.64, },

           'juan': {'debito': 5.54,
                     'credito': 9.57,
                     'deuda': 4.64, },

            'luis': {'debito': 9.54,
                     'credito': 7.57,
                     'deuda': 1.64, }}

aveValue1 = statistics.mean(d['debito'] for d in hoja_calculo.values() if d)
sumValue2 = sum(d['deuda'] for d in hoja_calculo.values() if d)
#mulValue3 = multiple(d['credito'] for d in hoja_calculo.values() if d)

#meter lambda suma y el average

print(aveValue1)
print(sumValue2)
#print(mulValue3)



pass






































