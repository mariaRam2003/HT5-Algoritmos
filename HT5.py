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

def Run(name,env,CPUrunning,CPUOfComputer): #Funcion que muestra cada programa que ingresa al CPU
    global TimeTotal
    
    yield env.timeout(CPUrunning) #vtiempo aleatorio previo a ingresar al CPU
    
    ending = env.now #Tiempo de llegada al CPU
    
    #Simulacion del tiempo cada programa para llegar al CPU
    TimeProgram = random.randint(1, 10) #AQUI SE ELIGE EL PROGRAMA PARA EL INCISO (b)
    print (name + ' llega a las ' + ending ' necesita ' + TimeProgram + ' instrucciones para salir del CPU.')
    
    with CPUOfComputer.request() as turn: #Agregar a la cola en caso la ejecucion este llena
        yield turn
        yield env.timeout(TimeProgram)
        print ( name + ' sale del CPU a las ' + env.now )
        
    tiempoTotal = env.now - ending
    print (name + ' se tardo '  + tiempoTotal)
    TimeTotal = TimeTotal + tiempoTotal
    
env = simpy.Environment() #simulacion del programa
CPUOfComputer = simpy.Resource(env,capacity = 3) 
random.seed(10)

TimeTotal = 0
for i in range(25): #AQUI SE ESATBLECE LA CANTIDAD DE PROGRAMAS A CORRER

    env.process(Run('Programa %d'%i,env,random.expovariate(1.0/10),CPUOfComputer))

env.run(until=500) #Tiempo que se necesita simular 

#Tiempo de ejecucion
fin = time.time()
print(fin-inicio)
