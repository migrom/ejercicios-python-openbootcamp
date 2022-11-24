from datetime import datetime

now = datetime.now()

#print( now.hour )

hora_salida = 19

tiempo_restante = hora_salida - now.hour

if (hora_salida == now): print( 'Hora de irse a casa')
else:
    if (tiempo_restante < 0):
        print('¡¡¡¡Que haces ahí aún!!!!')
    else: print ('Quedan {} horas para salir'.format(str(tiempo_restante)))




