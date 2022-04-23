print('hola mundo')
##INICIO DE COMO VAMOS HACER NUESTRO APLICATIVO DE HISTORIAS LOCAS go
# concatedenar cadenas
#supongamos que queremos crear una cadena que diga 
#aprende a programasr con ___________________.


#primera forma
nombre='jhon'
texto='aprende a programar con '
print(texto+' '+nombre)
#segunda forma
#llamando a un metodo
print('es la primera vezz que {} aprende a programar'.format(nombre))
#tercera forma f-string
print(f'aprende programar con {nombre}')
#creando las historias locas
verbo1='jugar'
verbo2='pelear'
adj='feo '
verbo3='pelear'
#usando alt z 
madlib =f" mi abuelito ,que {verbo1} 75 ainos y casi {verbo2} me  hoy : tu abuela es la mujer  mas {adj} ,asi que?. he {verbo3} por un momento y luego le he dicho!" 
print(madlib)
#utilixzando shift+alt +a
madlib =f"""   mi abuelito ,que {verbo1} 75 ainos y casi {verbo2} me  hoy : tu abuela es la mujer  mas {adj} ,asi que?. he {verbo3} por un momento y luego le he dicho!"""
print(madlib)