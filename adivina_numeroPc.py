from pyexpat import XML_PARAM_ENTITY_PARSING_NEVER
import random
def adivinaComputadora (x):
    print('''=================
          bienvenido al juego
          =================== ''')
    print(f'''ingrese un numero entre 1 y {x} para que la computadora 
          intente adivinarlo  ''')
    limInf= 1
    limSup= x
    respuesta =' '
    while respuesta !='c':
    #generando prediccion
        if limInf != limSup:
            prediccion = random.randint(limInf,limSup)
        else:
            prediccion = limSup
            #tambien podria ser le limite superior
        #obtener una respuesta del usuario
        respuesta =input(f'''mi pridiccion es {prediccion} si es muy alta ingrese a
        ,si es bajo ingrese b  y si es correcto ingrese c : ''').lower()
        
        if respuesta == 'a':
            limSup = prediccion-1
        elif respuesta == 'b':
            limInf = prediccion +1
    print (f'siii la computadra halo tu numero  {prediccion} ')


if __name__=="__main__":
    adivinaComputadora(20)
    print('bien hecho pc')
#if name =='__name__' :
