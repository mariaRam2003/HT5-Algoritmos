'''
Universidad del Valle de Guatemala
Hoja de Trabajo 5
Algoritmos y Estructuras de Datos
Moises Alonso
Maria Marta Ramirez Gil 21342
'''

'Importar las clases necesarias'
import random
import simpy
import time

'Crear la variable de inicio'
inicio = time.time()

def Run(name, env, CPUrunning, CPUOfComputer): #Funcion que muestra cada programa que ingresa al CPU
    global TimeTotal
    
    yield env.timeout(CPUrunning) #vtiempo aleatorio previo a ingresar al CPU
    
    ending = env.now #Tiempo de llegada al CPU
    
    #Simulacion del tiempo cada programa para llegar al CPU
    TimeProgram = random.randint(1, 10) #AQUI SE ELIGE EL PROGRAMA PARA EL INCISO (b)
    print ('%s llega a las %f necesita %d instrucciones para salir del CPU' % (name,ending,TimeProgram))
    
    with CPUOfComputer.request() as turn: #Agregar a la cola en caso la ejecucion este llena
        yield turn
        yield env.timeout(TimeProgram)
        print ('%s sale del CPU a las %f' % (name, env.now))
        
    tiempoTotal = env.now - ending
    print ('%s se tardo %f' % (name, tiempoTotal))
    TimeTotal = TimeTotal + tiempoTotal
    
env = simpy.Environment() #simulacion del programa
CPUOfComputer = simpy.Resource(env,capacity = 1)
random.seed(10)

TimeTotal = 0
for i in range(25): #AQUI SE ESATBLECE LA CANTIDAD DE PROGRAMAS A CORRER

    env.process(Run('Programa %d'%i,env,random.expovariate(1.0/10),CPUOfComputer))

env.run(until=500) #Tiempo que se necesita simular 

#Tiempo de ejecucion
fin = time.time()
print(fin-inicio)
