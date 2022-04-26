#creando mi primer juego
##modulo que nos brinda numeros aletorios
import random

def adivina_numero(x):
    print("""
    ========================
       BIENVENID@ AL JUEGOO  
    ========================
    Tu meta es saber el numero
    que lacomputadora
    esta pensando  """)
    #numero aleatorio entre 1 y x 
    numeroAL=random.randint(1,x)
    prediccion=0
    while  prediccion != numeroAL :
        #utilisando la funcion f-string
        prediccion =int(input(f'ingrese un numero entre el 1 y{x} :'))
        if prediccion > numeroAL:
            print('el nuemro es muy grande intente otro numero')
        elif prediccion < numeroAL:
            print('el nuemro es muy pequeño intente otro numero :')
    print(f'felicidades ya adivinaste el numero {numeroAL}')

#como saber como usar un modulo?
#python docs (nombre del modulo) module 
if __name__=="__main__":
    num=int(input('ingrese un numero '))
    adivina_numero(num)
    print ('a hora buena')
