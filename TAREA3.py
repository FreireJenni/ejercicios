#1.1 Ejercicios resueltos de variables
#1 :
def ejer1_1():
    a=46
    a=15 
    a=30


#2:
def ejer2_1():
    a=10*2
    a-=5


#3:
def ejer3_1():
    a=10-2
    10+2

#4:
def ejer4_1():
    b=3*(4+2)
    a=b+2
    C=5
    a=b-C

#5:
def ejer5_1():
    a=25
    a+10

#6:
def ejer5_1():
    a=3
    b=a+6
    a=b+1

#3.1 Ejercicios resueltos con tablas de verdad

#3:
a=(len("jugar")>5) and (len("jugar")<10) 

#4:
"alto"[2]=="t" and a 

#5:
842913%10!=3 and len("cafe")==3 

#6
0!=0 or "a"<"y" 

#7:
True or int("50")>=50 

#8:
edad=20 
not(a) or edad%2==0 

#9:
es_cli=False
not(es_cli and not(edad<18)) 

#12:
#La longitud de la cadena no debe ser superior a 10 caracteres
cad = 0
len(cad)<10
#!Respuesta: len(cadena)<=10

#4.1 Ejercicios resueltos de strings

cade="si, profe, es cierto... yo me comi la tarea"

cade[10]
cad[-1] 
cad[0:9] 
cad[::3] 


s="   hola, ¿como estas?"
#1:
s[::-1] 

#2:
s[len(s)] 

#3:
s.count("o") 

#4:
s.count("Hola") 

#5: 
s[-4] 

#6:
s[15:] 

#7:
s.find("o") 

#8:
s.strip() 

#9:
x=s.upper() 
x==s

#10:
s[14:].upper 

#11:
len(s)%2!=0 

#12:
s.replace(" ", "*") 
#13:
s.replace("z", "Z") 


X="programar en python"

#5.1 Ejercicios resueltos de input y print
#1:
nombre = []
A=input(nombre, "¿cual es tu cancion favorita?")

#2:
precio=input("Precio")
total=precio+(precio*0.10) 

#3:
edad=int(input("Edad:"))
print("tu edad es, edad")

#4:
edad=int(input("Edad:"))
print("Veamos si tu edad es 18...", edad=18)

#Solucion:
N = str(input("Ingrese su nombre: "))
print("Ahora estàs en la matrix, ", N)

#!Hacer un programa que solicite al usuario cuanto costo una cena en un restaurante. A ese valor, sumarle un 6.2%
#!en conceptos de servicio. Imprimir en pantalla el monto final a pagar

Costo_cena=float(input("Ingrese el valor de la cena: "))
Total=Costo_cena + (Costo_cena*0.162)
print("EL valor total a pagar incluido el servicio y la propina es: ", Total)

#!Solicitar al usuario que ingrese el dia, mes y año de su nacimiento y almacenar cada uno de ellos en una variable
#!numerica (en total, tres variables diferentes). finalmente, mostrar la fecha en formato dd/mm/aaaa

#!Hacer otra version del programa, pero esta vez almacenando todo an una unica variable numerico, en la forma DDMMAAAA. 
#!¿Y si la variable fuera de tipo string?. 

dia=int(input("Dia de tu nacimiento: "))
mes=int(input("Mes de tu nacimiento: "))
anio=int(input("Año de tu nacimiento: "))
print(dia,"/",mes,"/",anio)

fecha=input("Fecha en formato DDMMAAAA: ")
dia=fecha[:2]
mes=fecha[2:4]
anio=fecha[4:]
print(dia,"/",mes,"/",anio)

#!Una pareja de motociclistas necesita hacer ciertos calculos antes de emprender un viaje en moto, para saber cuantos 
#!tanques de emprender un viaje en moto, para saber cuantos tanques de combustibles consumira el viaje entero. 
#!Para eso deben ingresar: cuantos kilometros puede recorrer su moto con 1 litro de combustible, que capacidad (en litro)
#!tiene el tanque y cuantos kilometros en total recorreran. 
#!Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustibles necesarios. 

capacidad=float(input("Capacidad del tanque: "))
kmxl=float(input("Rendimiento (km por litro): "))
recorrido=float(input("Km totales a recorrer: "))
kmxtanque=capacidad*kmxl
print("seran necesarios", recorrido/kmxtanque, "tanques.")


#5.2 Ejercicio resuelto de input y print
#1:
#!Un empresario que se dedica al espectaculo necesita un programa que le ayude a hacer ciertos calculos cada 
#!vez que organiza un concierto en un estadio deportivo. 
#!Lo primero que necesita saber es que capacidad de publico tendra cada concierto, para saber cuantas entradas o boletos tienen que imprimirse.
#!Para eso cuando contrata un estadio deportivo, pregunta cuantos metros cuadrados tiene. El sabe que, por metro cuadrado,
#!caben 4 personas. Tambien sabe que siempre hay un espacio con gradas y que normalmente estas ocupan un 20% de los metros
#!cuadrados totales. En cada estadio las gradas pueden ser diferentes, asi que el empresario consulta cuantas gente cabe en ellas. 
#!Cuando contra a la banda que dara el concierto, esta le indica que porcentaje del espacio disponible necesitan ellos
#!para mostrar su escenario. 
#!Con estos datos, debe calcularse cuanta gente va a caber en el estadio para un concierto determinado. El empresario, cada vez que 
#!use el programa, va a ingresar la cantidad de metros cuadrados que tiene el estadio que contrato, la cantidad de gente que 
#!cabe en las gradas y el porcentaje de espacio ocupado por el escenario. 
#!Luego, el quiere saber cuanto dinero ingresaria si vende todas las entradas disponibles, sabiendo que el 30% de las entradas 
#!vendidas seran "a precio especial" y el resto son "a precio comun." EL empresario ingresa el precio de cada tipo de entrada 
#!cuando usa el programa. 

CAPACIDADM2=4
PORCENTAJEGRADAS=0.2
PORCENTAJEESPECIALES=0.3
PORCENTAJESCOMUNES=0.7

dimensiones=float(input("Dimensiones del estadio (en m2): "))
personasengradas=int(input("capacidad de personas que caben en las gradas: "))
porcentajeescenario=int(input("Porcentaje que ocupa el escenario: "))
m2gradas=dimensiones*PORCENTAJEGRADAS
m2escenario=dimensiones*(porcentajeescenario/100)
m2disponibles=dimensiones-m2gradas-m2escenario
personastotales=(m2disponibles*4)+personasengradas
print("Caben", personastotales, "personas")
percioentradasespecial=float(input("Precio entrada especial: "))
precioentradacomun=float(input("Precio entrada comun: "))
print("Ingreso total de ventas: $", (personastotales*PORCENTAJEESPECIALES)*percioentradasespecial+(personastotales*PORCENTAJESCOMUNES*precioentradacomun))

#6.1 Ejercicios resueltos de if-else (y elif)
#1:
#!Escribir un programa que, dado un numero entero, muestre su valor absoluto. 
#!Nota:para los numeros positivos su valor absoluto es igual al numero (el valor absoluto de 52 es 52), mientras que, para los
#!negativos, su valor absoluto es el numero multiplicado por -1 (el valor absoluto de -52 es 52). 

numero=int(input("Numero: "))
if numero<0:
    numero=numero*-1
print("EL valor absoluto es ", numero)

#2:
#!Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenaran en dos variables. 
#!A continuacion, imprimir "coincidencia" si los nombres de ambas personas comienzan con la misma letra o si terminan 
#!con la misma letra. Si no es asi, imprimir "no hay coincidencia". 

nombre1=input("Un nombre: ")
nombre2=input("Otro nombre: ")
indice_final_nombre1=len(nombre1)-1
indice_final_nombre2=len(nombre2)-1
if nombre1[0]==nombre2[0] or nombre1[indice_final_nombre1]==nombre2[-1]:
    print("Coincidencia")
else:
    print("No hay cpincidencia")

#3:
#!Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: 
#!candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. 
#!Segun el candidato elegido (A, B o C) se le debe imprimir el mensaje "Usted ha votado por el partido 
#![color que corresponda al candidato elegido]". 
#!Si el usuario ingresa una opcion que no corresponde a ninguno de los candidatos disponibles, indicar "Opcion erronea". 

candidato=input("Candidato: ")
if candidato.upper()=="A":
    print("Usted ha votado por el partido rojo")
elif candidato.upper()=="B":
    print("Usted ha votado por el partido azul")
elif candidato.upper()=="C":
    print("Usted ha votado por el partido verde")
else:
    print("Opcion erronea")

#4:
#!Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje "es vocal". 
#!Se debe validar que el usuario ingrese solo un caracter. Si ingresa un string de mas de un caracter, informarle 
#!que no se puede procesar el dato. 

letra=input("letra: ")
if len(letra)!=1:
    print("Debe ser solo una letra")
else:
    if letra.lower() in "aeiou":
        print("Es vocal")

#5:
#!Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no
#!debe ser divisible por 100, excepto que tambien sea divisible por 400. 

anio=int(input("Año: "))
if anio%4 != 0:
    print("No es bisiesto.")
else:
    if anio%100 != 0 or anio%400 == 0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")

#6.2 Ejercicio de if-else (y elif)

#!Un instituto de enseñanza de ingles necesita un programa que le permita, cada dia, procesar observaciones sobre las clases
#!de ese dia. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un dia de la semana diferente:
#!los lunes se dicta el nivel inicial, los martes el nivel intermedio, los miercoles el nivel avanzado, los jueves son para 
#!practica hablada y los viernes se dicta ingles para viajeros. 

#!Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "dia, DD/MM", donde [dia] es un dia de la 
#!semana, DD es el numero de dia y MM es el numero de mes. Si el usuario ingresa un  dia de la semana inexistente o una fecha
#!cuyo dia supere el numero 31 o el mes supere al numero 12, finalizar el programa indicando que se produjo un error. Debe
#!Permitirse que ingrese el dia de la semana en minusculas o mayusculas indistintamente. Como precondicion se tiene que lo ingresado
#!por el usuario tendrà la forma <[alfanumerico], [numerico]/[numerico]>. 

#!Una vez indicada la fecha, el usuario necesita poder indicar si ese dia se tomaron examenes, pero eso solo si se trata de los 
#!niveles inicial, intermedio o avanzado, ya que las practicas habladas y el ingles para viajeros no tiene examenes. Si hubo examenenes
#!el usuario ingresara cuantos alumnos aprobaron y cuantos no, y el programa le mostrara el porcentaje de aprobados. 

#!Si el dia fue el correspondiente a practicas hablada, el usuario debera ingresar el porcentaje de asistencia a clases y el programa
#!le indicara "asistio la mayoria" en caso de la asistencia sea mayor al 50% o "no asistio la mayoria " si no es asi. 

#!SI se trata de ingles para viajeros y la fecha actual corresponde al dia 1 del mes 1 o del mes 7, se debera imprimir
#!"Comienzo de nuevo ciclo" y solicitar al usuario que ingrese la cantidad de alumnos de nuevo ciclo y el arancel en $ por
#!cada alumno, para luego imprimir el ingreso total en $. 

fecha=input("Fecha (formato dia, DD/MM): ")
fecha=fecha.lower()
diasemana=fecha[0:fecha.find(",")]
dianro=int(fecha[fecha.find(" ")+1:fecha.find("/")])
mesnro=int(fecha[fecha.find("/")+1:]) 
if dianro>31 or mesnro>12:
    print("Fecha incorrecta")
else:
    if diasemana in "lunes,martes,miercoles":
        respuesta=input("¿Se tomaron examenes? S/N: ")
        if respuesta.lower()=="s":
            aprobados=int(input("Cantidad de aprobados: "))
            resprobados=int(input("Cantidad de reprobados: "))
            print("Porcentajes de resprobados: ", (aprobados*100)/(aprobados+resprobados), "%")
    elif diasemana == "jueves":
        asistencia=int(input("Porcentajes de asistencia: "))
        if asistencia>50:
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")
    elif diasemana == "viernes":
        if dianro==1 and (mesnro==1 or mesnro==7):
            print("Comienzo de nuevo ciclo")
            alumnos=int(input("Cantidad de alumnos: "))
            arancel=float(input("Arancel: $"))
            print("Ingreso total: $", alumnos*arancel)
    else:
        print("Fecha incorrecta")
print("Fin del programa")

#7.1 Ejercicios resueltos de bucles for
#1:
#!escribir un programa que muestre la sumatoria de todos los numeros entre 0 y el 100. 
#!¿Que modificacion habria que hacer si ahora solo se deben sumar los numeros que sean multiplos de 3?. 

total=0
for i in range(101):
    total=total+i
print("Sumatoria: ", total)

total=0
for i in range(101):
    if i%3==0:
        total=total+i
print("Sumatoria: ", total)

#2:
#!Dado un numero entero positivo, mostrar su factorial. 
#!El factorial de un numero se obtiene multiplicando todos los numeros enteros positivos que hay entre 1 y ese numero. 
#!El factorial de 0 es 1.

numero=int(input("Numero: "))
f=1 
if numero != 0:
    for i in range (1, numero+1):
        f=f*i
    print("Factorial: ", f)

#3:
#!Crear un algoritmo que muestre los primeros 10 numeros de la sucesion de Fibonacci. La sucesion comienza con los numeros 0 y 1
#!y a partir de estos,cada elemento es la suma de los dos numeros anteriores en la secuencia:

n1=0
n2=1
print(n1)
print(n2)
for i in range(8):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3

#4:
#!Escribir un programa que permita al usuario ingresar 6 numeros enteros, que pueden ser positivos o negativos. Al finalizar
#!mostrar la sumatoria de los numeros negativos y el promedio de los positivos. 
#!No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se
#!ingresaron numeros positivos. 

sumaNegativos=0
sumaPositivos=0
CantidadPositivos=0
for i in range(6):
    nro=int(input("Numeros: "))
    if nro >=0:
        CantidadPositivos+=1
        sumaPositivos+=nro
    else:
        sumaNegativos+=nro
print("Sumatoria de negativos: ", sumaNegativos)
if CantidadPositivos!=0:
    print("Promedio de positivos: ", sumaPositivos/CantidadPositivos)
else:
    print("No se ingresaron numeros positivos")

#7.2 Ejercicio resuelto con bucles for anidados
#1:
#!Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno
#!donde un integrante de cada equipo es el "jefe" y los otros 5 son sus "oficiales". La regla mas importante del juego es que 
#!solo se comunicaran mediante un canal comun, por lo que deben buscar la forma de ocultar el contenido de sus mensajes. 
#!Uno de los equipos decide utilizar un metodo antiguo de encriptacion llamado "la cifra del cesar", que consiste en correr cada 
#!letra del mensaje -considerando la posicion de cada una en el alfabeto- una determinada cantidad de lugares. Ejemplo: 
#!si el corrimiento es de 2 lugares, la palabra "ATAQUE" se transforma en "CVCSWG". 

#!Cada dia, el "jefe" del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita 
#!encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se correran las letras) sera dado por el usuario 
#!antes de comenzar a encriptar. Los 5 mensajes usaran el mismo corrimiento. 

#!Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra "a"
#!Ejemplo: la palabra "EXTRA" corrida 3 lugares se convierte en "HAWUD". Utilizando el alfabeto español, de 27 letras, el 
#!siguiente calculo matematico permite volver a comenzar por el principio una vez que se llego a la "z":
#!(indice de la letra a correr+corrimiento)%27

#!Solo se encriptatan las letras de los mensajes, dejando al resto de caracteres sin modificacion. 

corrimiento=int(input("Corrimiento: "))
alfabeto="avcdefghijklmnñopqrstuvwxyz"

for i in range (5):
    mensaje=input("Mensaje a encriptar: ")
    encriptado=""
    for caracter in mensaje:
        if caracter.lower() in alfabeto:
            indice=alfabeto.find(caracter.lower())
            indice=(indice+corrimiento)%27
            encriptado+=alfabeto[indice]
        else:
            encriptado+=caracter
    print("***Mensaje encriptado:", encriptado)

#8.1 Ejercicios resueltos de bucles while
#1:
#!Crear un programa que permita al usuario procesar los montos de las compras de un cliente 
# !(se desconoce la cantidad de datos que cargara), cortando el ingreso de datos cuando el usuario ingrese el monto 0. 

#!Si ingresa un monto negativo, no se debe procesar y se debe pedir que proporcione un nuevo monto. Al finalizar, 
#!informar el pedir que proporcione un nuevo monto. Al analizar, informar el total a pagar teniendo en cuenta que, si las 
#!ventas superan el total de $1000, se le debe aplicar un 10% de descuento. 

total=0
monto=float(input("Monto de una venta: $"))
while monto != 0:
    if monto<0:
        print("Monto no valido")
    else:
        total+=monto
    monto=float(input("Monto de una venta: $"))
if total>1000:
    total-=total*0.1
print("Monto total a pagar: $", total)

#2:
#!Crear un programa que solicite el ingreso de numeros enteros positivos, hasta que el usuario ingrese el 0. Por cada numero,
#!informar cuantos digitos pares y cuantos impares tiene. 
#!Al finalizar, informar la cantidad de digitos pares y de digitos impares leidos en total. 

totalPares=0
totalImpares=0
numero=int(input("Numero: "))
while numero != 0:
    pares=0
    impares=0
    while numero != 0:
        ultimoDigito=numero%10
        if ultimoDigito%2==0:
            pares+=1
            totalPares+=1
        else:
            impares+=1
            totalImpares+=1
        numero=numero//10
        print("El numero ingresado tiene ", pares,"digitos pares y ", impares "digitos impares")
    numero=int(input("Numero: "))
print("Total de digitos pares: ",totalPares)
print("Total de digitos Impares: ",totalImpares)

#3:
#!Crear un programa que permita al usuario ingresar titulos de libros por teclado, finalizar el ingreso al leerse el string
#!"*" (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga solo una barra ("/") se considera
#!que termina una linea. 

#!Por cada linea completa, informar cuantos digitos numericos (del 0 al 9) aparecieron en total (en todos los titulos de libros
# !que componen esa linea). Finalmente, informar cuantas lineas completas se ingresaron. 

#!Ejemplo de ejecucion:
#!Libro: Los 3 mosqueteros
#!Libro: Historia de 2 ciudades
#!/
#!Linea completa. Aparecen 2 digitos numericos. 
#!Libro: 20000 leguas de viajes submarino
#!Libro: El señor de los anillos
#!Libro: /
#!Linea completa. Aparecen 5 digitos numericos. 
#!Libro: 20 años despues
#!Libro: *
#!Fin. Se leyeron 2 lineas completas. 

digitosEnLaLinea=0
cantLineas=0
titulo=input("Titulo del libro: ")
while titulo!="*":
    if titulo == "/":
        cantLineas+=1
        print("Linea completa. Aparecen", digitosEnLaLinea, "digitos")
        digitosEnLaLinea=0
    else:
        for caracter in titulo:
            if caracter in titulo:
                if caracter in "0123456789":
                    digitosEnLaLinea+=1
    titulo=input("Titulo del libro: ")
print("Fin. Se leyeron ", cantLineas, "lineas")

#8.2 Ejercicio resuelto de bucles while
#1:
#!Analizar el codigo mostrado a continuacion y, sin ejecutarlo previamente, describir que hace. 
#!¿Que salida se mostraria en pantalla si se ejecuta el programa sucesivamente con los siguientes datos?
#!Frase: "hola buen dia"
#!Frase: ""
#!Frase: "1234"
#!Frase: "hola buen dia!"

frase=input("Frase: ")
frase=frase.strip()
cantidad=0
len_p_mas_larga=0
while len(frase) != 0:
    cantidad=cantidad+1
    i=frase.find(" ")
    if i != -1:
        palabra=frase[0:i]
        while i < len(frase) and frase [i] == " ":
            i=i+1
        frase=frase[i:]
    else:
        palabra=frase
        frase=""
    if len(palabra) > len_p_mas_larga:
        len_p_mas_larga=len(palabra)
        p_mas_larga=palabra
if cantidad > 0:
    print("Palabra mas larga:", p_mas_larga)
print("Cantidad de palabras:", cantidad)

#Ejercicios para practicar la estructura de control de bucle o repetición condicional (while) usando Python.

#1
#!Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
# !Finalmente, mostrar la sumatoria de todos los números ingresados.

total=0
nro=int(input("Número: "))
while nro != 0:
    total+=nro
    nro=int(input("Número: "))

#2
#!Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
#!Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

positivos=0
n=int(input("Número (0 para terminar): "))
while n!=0:
    if n>0:
        positivos+=1
    n=int(input("Número (0 para terminar): "))
print("Cantidad de positivos:", positivos)

#3
#!Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
#!Informar cuál fue el mayor número ingresado.

mayor=-1
n=int(input("Número positivo:"))
while n>=0:
   if n>mayor:
       mayor=n
   n=int(input("Número positivo:"))
print("Mayor número ingresado:", mayor)

#4
#!Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

suma=0
n=int(input("Número positivo:"))
while n!=0:
    digito=n%10
    suma+=digito
    n=n//10
print("Suma de los dígitos:", suma)

#5
#!Solicitar al usuario que ingrese números enteros positivos y, 
#!por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. 
#!Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

pares=0
n=int(input("Número (-1 para terminar el programa): "))
while n!=-1:
    if n%2 == 0:
        pares+=1
    suma=0
    while n!=0:
        digito=n%10
        suma+=digito
        n=n//10
    print("Suma de sus dígitos:", suma)
    n=int(input("Número (-1 para terminar el programa): "))
print("Se ingresaron", pares, "números pares")

#6
#!Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
#!A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
#!Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, 
#!permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, 
#!se interrumpirá la impresión del menú y el programa finalizará.

while True:
    print("Opción 1 - comenzar programa")
    print("Opción 2 - imprimir listado")
    print("Opción 3 - finalizar programa")
    opcion=int(input("Opción elegida: "))
    if opcion==1:
        print("¡Comenzamos!")
    elif opcion==2:
        print("Listado:")
        print("Nadia, Esteban, Mariela, Fernanda")
    elif opcion==3:
        print("Hasta la próxima")
        break
    else:
        print("Opción incorrecta. Debe ingresar 1, 2 o 3")
#7
#!Solicitar al usuario el ingreso de una frase y de una letra 
#!(que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
#!Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
#!Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

frase=input("Frase: ")
l=input("Letra para buscar su posición: ")
i=0
while i!=len(frase):
    if l!=frase[i]:
        print("No se encontró en la posición", i)
        i+=1
        continue
    print("Se encontró en la posición", i)
    break

#8
#!Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
# !(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# !cortando el ingreso de datos cuando el usuario ingrese el monto 0.
#!Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
#!Al finalizar, informar el total a pagar teniendo que cuenta que, 
#!si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

total=0
monto=float(input("Monto de una venta: $"))
while monto!=0:
    if monto<0:
        print("Monto no válido.")
    else:
        total+=monto
    monto=float(input("Monto de una venta: $"))
if total>1000:
    total-=total*0.1
print("Monto total a pagar: $", total)

#9
#!Crear un programa que solicite el ingreso de números enteros positivos, 
#!hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
#!Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

numero=int(input("numero: "))
totalPares=0
totalImpares=0
while numero!=0:
   pares=0
   impares=0
   while numero!=0:   
       ultimodigito=numero%10
       if ultimodigito%2==0:
           pares+=1
           totalPares+=1
       else:
           impares+=1
           totalImpares+=1
       numero=numero//10
   print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares")
   numero=int(input("Otro número: "))
print("Total de dígitos pares:", totalPares)
print("Total de dígitos impares:", totalImpares)

#Crear un programa que permita al usuario ingresar títulos de libros por teclado, 
# finalizando el ingreso al leerse el string “*” (asterisco). 
# Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) 
# se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) 
# aparecieron en total (en todos los títulos de libros que componen en esa línea). 
# Finalmente, informar cuántas líneas completas se ingresaron.
# **Ejemplo de ejecución:**
# Libro: Los 3 mosqueteros
# Libro: Historia de 2 ciudades
# Libro: /
# Línea completa. Aparecen 2 dígitos numéricos.
# Libro: 20000 leguas de viaje submarino
# Libro: El señor de los anillos
# Libro: /
# Línea completa. Aparecen 5 dígitos numéricos.
# Libro: 20 años después
# Libro: *
# Fin. Se leyeron 2 líneas completas.

lineas=0
digitos="0123456789"
cantidadDigitos=0
cadena=input("Cadena: ")
while cadena!="*":
    for caracter in cadena:
        if caracter in digitos:
            cantidadDigitos+=1
    if cadena=="/":
        lineas+=1
        print("Aparecen ", cantidadDigitos, " dígitos en la línea")
        cantidadDigitos=0
    cadena=input("Cadena: ")
print("Se leyeron ",lineas," líneas completas")

#11
# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

cantidad=0
n=int(input("Número: "))
while n!=0:
 primo=True
 for i in range(2,n):
   if n%i==0:
     primo=False
     break
 if primo:
   cantidad+=1
 n=int(input("Número: "))
print("primos: ", cantidad)

#12
# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
# (en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
# Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

frase=input("Frase: ").strip()
cantidad=0
len_p_mas_larga=0
while len(frase) != 0:
    cantidad=cantidad+1
    i=frase.find(" ")
    if i != -1:
        palabra=frase[0:i]
        while i < len(frase) and frase[i] == " ":
            i=i+1
        frase=frase[i:]
    else:
        palabra=frase
        frase=""
    if len(palabra) > len_p_mas_larga:
        len_p_mas_larga=len(palabra)
        p_mas_larga=palabra
if cantidad > 0:
    print("Palabra más larga:", p_mas_larga)
print("Cantidad de palabras:", cantidad)

#10 Ejercicios para practicar programación usando funciones, con Python.

#1
# Solicitar al usuario que ingrese su dirección email. 
# Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
# Una dirección se considerará válida si contiene el símbolo "@".

def validar(email):
    caracterBuscado="@"
    emailValido=False
    for c in email:
        if c==caracterBuscado:
            return True
    return False

#programa principal
direccion=input("Tu email: ")
if validar(direccion):
    print("Dirección válida")
else:
    print("Dirección inválida")

#2
# Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).

def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

#!programa principal
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    num=int(input("Número a procesar: "))

#3
# Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos. 
# Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
# Reutilizar la misma función realizada en el ejercicio 2.
def sumaDigitos(numero):
  suma=0
  while numero!=0:
    digito=numero%10
    suma=suma+digito
    numero=numero//10
  return suma

#!programa principal
sumatoria=0
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    sumatoria=sumatoria+num
    num=int(input("Número a procesar: "))
print("Sumatoria:", sumatoria)
print("Dígitos:", sumaDigitos(sumatoria))

#4
# Requerir al usuario que ingrese un número entero e informar si es primo o no, 
# utilizando una función booleana que lo decida.

def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

#!programa principal
numero=int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")

#5
# Solicitar al usuario un número entero y luego un dígito. 
# Informar la cantidad de ocurrencias del dígito en el número, 
# utilizando para ello una función que calcule la frecuencia.

def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

#!programa principal
num=int(input("Número: "))
un_digito=int(input("Dígito: "))
print("Frecuencia del dígito en el número:",frecuencia(num,un_digito))

#6 
# Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, 
# al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

#!programa principal
cantidad=0
num=int(input("Número (-1 para cortar): "))
while num!=-1:
    print("Factorial:", factorial(num))
    cantidad+=1
    num=int(input("Número (-1 para cortar): "))
print("Se leyeron",cantidad,"números")

#7 
# Escribir un programa que pida números positivos al usuario. 
# Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números 
# cuya sumatoria de dígitos fue menor que 10. Utilizar una o más funciones, según sea necesario.

def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma

#!programa principal
cantidad=0
mayor=-1
numero=int(input("Número positivo: "))
while numero>=0:
    suma=sumaDigitos(numero)
    if suma > mayor:
          mayor=suma
          n_mayorsuma=numero
    if suma < 10:
        cantidad+=1
    numero=int(input("Número positivo: "))
print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
print("Cantidad con sumatoria menor a 10:",cantidad)

#8 
# Solicitar al usuario el ingreso de números primos. 
# La lectura finalizará cuando ingrese un número que no sea primo. 
# Por cada número, mostrar la suma de sus dígitos. 
# También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). 
# Al finalizar el programa, mostrar el factorial del mayor número ingresado.

def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma

#!programa principal
mayor=0
numero=int(input("Número primo: "))
while primo(numero):
    print("Suma de los dígitos:",sumaDigitos(numero))
    digito=int(input("Dígito: "))
    print("El",digito,"aparece",frecuencia(numero,digito),"veces")
    if numero > mayor:
          mayor=numero
    numero=int(input("Número primo: "))
print("Factorial de",mayor,":",factorial(mayor))

#9
# Sin ejecutar el siguiente programa, determinar cuál es la salida en pantalla si se ingresan los valores x=6, y=7:

def coordenadaZ(x,y):
  x=x+10
  y=y+15
  return x+y

#!programa principal
x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
  z=coordenadaZ(x,y)
  x=x+1
  y=y+1
print(x," . ",y)

#10
# El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero en su lugar imprime 5. 
# ¿Qué hay que corregir?

def maximo(a,b):
  if x>y:
    return x
  else:
    return y

def minimo(a,b):
  if x<y:
    return x
  else:
    return y

#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))

#11 
# Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def validarDNI(dni):
   cantidad=0
   while dni!=0:
       cantidad+=1
       dni//=10
   return cantidad==7 or cantidad==8
#12 
# Escribir una función que, dado un string, retorne la longitud de la última palabra. 
# Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro.

def lenUltimaPalabra(frase):
   if len(frase)==0:
       return 0
   cantidad=0
   for i in range(len(frase)):
       if frase[i]!=' ':
           cantidad+=1
       else:
           if i<len(frase)-1 and frase[i+1]!=' ':
               cantidad=0
   return cantidad

#13 
# Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. 
# Para eso ingresará nombre completo y número de DNI de cada socio, 
# indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío
# Precondición: el formato del nombre de los socios será: nombre apellido. 
# Podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. 
# Si un socio tuviera más de un apellido, el usuario sólo ingresará uno. 
# Se debe validar que el número de DNI tenga 7 u 8 dígitos. 
# En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, 
# la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. Ejemplo:
# Nombre: Alba María Linares
# DNI: 25834910
# Alba7258

def lenUltimaPalabra(cadena):
   longitud=len(cadena)
   if longitud==0:
       return 0
   cantidad=0
   for i in range(longitud):
       if cadena[i]!=' ':
           cantidad+=1
       else:
           if cadena[i]==' ' and i<(longitud-1) and cadena[i+1]!=' ':
               cantidad=0
   return cantidad

def DNIvalido(dni):
   cantidad=0
   while dni!=0:
       cantidad+=1
       dni//=10
   return cantidad==7 or cantidad==8

def primerosTresDigitos(numero):
   while numero >= 1000:
     numero = numero // 10
   return numero

def obtenerIdentificador(nombre, dni):
   nombre=nombre.strip()
   id=nombre[:nombre.find(" ")]
   id=id+str(lenUltimaPalabra(nombre))
   id=id+str(primerosTresDigitos(dni))
   return id

#programa principal
nombre=input("Nombre del socio: ")
while nombre!="":
   dni=int(input("DNI del socio: "))
   while (DNIvalido(dni)):
      print("Número inválido.")
      dni=int(input("DNI del socio: "))
   print(obtenerIdentificador(nombre,dni))
   nombre=input("Nombre del socio: ")
  
#14 
# Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo 
# la primera letra de cada palabra a mayúscula y las demás letras a minúscula, 
# dejando inalterados los demás caracteres. Precondición: el separador de palabras es el espacio: " ". 
# Agregar doctests con suficientes casos de prueba para validar que la función retorna el valor 
# esperado ante distintos argumentos.

def titulo(cadena):
    '''
    Recibe una cadena de caracteres y retorna una copia que tiene la
    primera letra de cada palabra en mayúsculas y el resto de las letras
    en minúsculas.
    >>> titulo('esto es una frase')
    'Esto Es Una Frase'
    >>> titulo('ESTO ES UNA FRASE')
    'Esto Es Una Frase'
    >>> titulo('palabra')
    'Palabra'
    >>> titulo('   esto es una frase')
    '   Esto Es Una Frase'
    >>> titulo('esto es una frase   ')
    'Esto Es Una Frase   '
    >>> titulo('esto   es   una   frase')
    'Esto   Es   Una   Frase'
    >>> titulo('')
    ''
    >>> titulo(' ')
    ' '
    >>> titulo('123')
    '123'
    >>> titulo('-1esto 2es 3una 4frase')
    '-1Esto 2Es 3Una 4Frase'
    >>> titulo('esto1 es2 una3 frase4---')
    'Esto1 Es2 Una3 Frase4---'
    '''
    nueva=""
    inicioPalabra=True              #indica el inicio de una palabra
    for caracter in cadena:
        if not caracter.isalpha():
            nueva=nueva+caracter
            inicioPalabra=True
        else:
            if inicioPalabra:
                nueva=nueva+caracter.upper()
                inicioPalabra=False  #ya no es el inicio de una palabra 
            else:
                nueva=nueva+caracter.lower()
    return nueva

#11 Ejercicios para practicar programación usando estructuras de datos, con Python.

#1
# A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
#  Finalizar al ingresar el número 0, el cual no debe guardarse.
# B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
# eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
# C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
# D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original 
# que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
# E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, 
# cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 
# Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

def sumatoria(lista):
    suma=0
    for n in lista:
        suma+=n
    return suma

def numerosMenores(lista, limite):
    nueva=[]
    for n in lista:
        if n<limite:
            nueva.append(n)
    return nueva

def frecuencias(lista):
    nueva=[]
    for n in lista:
        if [n, lista.count(n)] not in nueva:
            nueva.append([n, lista.count(n)])
    return nueva

#A
numeros=[]
nro=int(input("Número: "))
while nro!=0:
    numeros.append(nro)
    nro=int(input("Número: "))
#B
print("Sumatoria de los números:", sumatoria(numeros))
eliminar=int(input("Número a eliminar: "))
#C
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Ese número no está entre los ingresados")
#D
limite=int(input("Filtrar números menores a: "))
for n in numerosMenores(numeros, limite):
    print(n)
#E
print("Frecuencias:")
for tupla in frecuencias(numeros):
    print(tupla[0],"aparece",tupla[1],"veces.")

#2 
# Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas 
# con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), 
# ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, 
# "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. 
# Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), 
# ("Madrid","España")] Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
# -Agregar pasajeros a la lista de viajeros.
# -Agregar ciudades a la lista de ciudades.
# -Dado el DNI de un pasajero, ver a qué ciudad viaja.
# -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
# -Dado el DNI de un pasajero, ver a qué país viaja.
# -Dado un país, mostrar cuántos pasajeros viajan a ese país.
# -Salir del programa.

def agregarPasajeros(pasajeros):
    nombre=input("Nombre -x para cortar: ")
    while nombre!="x":
        dni=int(input("DNI: "))
        destino=input("Ciudad destino: ")
        pasajeros.append((nombre,dni,destino))
        nombre=input("Nombre -x para cortar: ")
    return pasajeros

def agregarCiudades(ciudades):
    ciudad=input("Ciudad -x para cortar: ")
    while ciudad!="x":
        pais=input("País: ")
        ciudades.append((ciudad,pais))
        ciudad=input("Ciudad -x para cortar: ")
    return ciudades

def buscarCiudad(pasajeros, dni):
    for viaje in pasajeros:
        if viaje[1]==dni:
            return viaje[2]
    return ""

def cantidadPasajerosCiudad(pasajeros, ciudad):
    cantidad=0
    for viaje in pasajeros:
        if viaje[2]==ciudad:
            cantidad+=1
    return cantidad

def buscarPaisDestino(pasajeros, ciudades, dni):
    buscada=buscarCiudad(pasajeros, dni)
    for ciudad in ciudades:
        if ciudad[0]==buscada:
            return ciudad[1]
    return ""

def cantidadPasajerosPais(pasajeros, ciudades, pais):
    cantidad=0
    for viaje in pasajeros:
        if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
            cantidad+=1
    return cantidad

#programa principal
pasajeros=[]
ciudades=[]
while True:
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino mediante el DNI")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar país destino mediante DNI")
    print("6. Cantidad de pasajeros que viajan a un país")
    print("7. Salir del programa")
    opcion=int(input("Acción a ejecutar: "))
    if opcion==1:
        print("AGREGAR PASAJEROS")
        pasajeros=agregarPasajeros(pasajeros)
    elif opcion==2:
        print("AGREGAR CIUDADES")
        ciudades=agregarCiudades(ciudades)
    elif opcion==3:
        dni=int(input("DNI: "))
        print("El pasajero viaja a", buscarCiudad(pasajeros, dni))
    elif opcion==4:
        ciudad=input("Ciudad a buscar: ")
        print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad), "pasajeros")
    elif opcion==5:
        dni=int(input("DNI: "))
        print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))
    elif opcion==6:
        pais=input("País: ")
        print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais), "pasajeros")
    elif opcion==7:
        break
    else:
        print("Opción inválida")

#3
# Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, 
# finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, 
# finalizando al ingresar “x”.
# - Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>
# - Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
# -Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

def cargarNombres(alumnos):
   nombre=input("Nombre: ")
   while nombre!="x":
       alumnos.add(nombre)
       nombre=input("Nombre: ")
   return alumnos

primaria=set()
secundaria=set()
print("ALUMNOS DE PRIMARIA")
primaria=cargarNombres(primaria)
print("ALUMNOS DE SECUNDARIA")
secundaria=cargarNombres(secundaria)

print("NOMBRES DE TODOS LOS ALUMNOS:")
for nombre in primaria|secundaria:
   print(nombre)

print("NOMBRES COMUNES:")
for nombre in primaria&secundaria:
   print(nombre)

print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre in primaria-secundaria:
   print(nombre)

#4
# Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, 
# la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). 
# Ejemplo:[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), 
# ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
# ("Jorge Russo", 15, 958, "Mirasol 218")]
# Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente 
# y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. 
# Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que la función 
# debe retornar una estructura que contenga cada domicilio una sola vez.

def direcciones(ventas):
   domicilios=set()
   for venta in ventas:
       domicilios.add(venta[3])
   return domicilios

#5
# Escribir un programa que procese strings ingresados por el usuario. 
# La lectura finaliza cuando se hayan procesado 50 strings. 
# Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. 
# Ejemplo: "r":5, "%":3, "a":8, "9":1.
# ¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, 
# incluyendo el valor 0 para las letras que no aparecieron?

contadores={}
for i in range(50):
   cadena=input("Cadena de caracteres: ")
   for caracter in cadena:
       if caracter not in contadores:
           contadores[caracter]=1
       else:
           contadores[caracter]+=1
print("Frecuencia de cada carácter")
for caracter, cantidad in contadores.items():
   print(caracter, ": ", cantidad)

#Para contabilizar sólo letras (mayúsculas y minúsculas por separado):
contadores={}
alfabeto="abcdefghijklmnñopqrstuvwxyz"
for letra in alfabeto+alfabeto.upper():
    contadores[letra]=0
for i in range(50):
   cadena=input("Cadena de caracteres: ")
   for caracter in cadena:
       if caracter.lower() in alfabeto:
           contadores[caracter]+=1
print("Frecuencia de cada letra")
for caracter, cantidad in contadores.items():
   print(caracter, ": ", cantidad)

#6
# Crear un programa para gestionar datos de los socios de un club, permitiendo:
# -Cargar información de los socios en un diccionario para acceder por número de socio. 
# Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). 
# El programa debe iniciar con los datos de los socios fundadores ya cargados:
# Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
# Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
# Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
# -Informar cantidad de socios del club.
# -Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
# -Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, 
# para indicar que en realidad ingresaron el 14/03/2018.
# -Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
# -Imprimir el listado de socios completo.

def cargarSocios(socios):
   numero=int(input("Número de socio (0 para cortar): "))
   while numero!=0:
       nombre=input("Nombre y apellido: ")
       fecha=input("Fecha de ingreso (DDMMAAAA): ")
       cuota=input("¿Cuota al día? s/n: ")
       socios[numero]=[nombre,fecha,cuota.lower()=="s"]
       numero=int(input("Número de socio (0 para cortar): "))
   return socios

def modificarFecha(socios, fecha_anterior, fecha_nueva):
   for datos in socios.values():
       if datos[1]==fecha_anterior:
           datos[1]=fecha_nueva
   return socios

def numeroSocio(socios, nombre):
   for numero,datos in socios.items():
       if datos[0].lower()==nombre.lower():
           return numero
   return 0

def formatoFecha(fecha):
   return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

def imprimirListado(socios):
   for numero,datos in socios.items():
       print("-Número:",numero)
       print("-Nombre:",datos[0])
       print("-Ingresó:", formatoFecha(datos[1]))
       if datos[2]:
           print("-Cuota al día")
       else:
           print("-En deuda")

socios_activos={1:["Amanda Núñez","17032009",True], 2:["Bárbara Molina","17032009",True], 3:["Lautaro Campos","17032009",True]}

print("***Cargar socios")
socios_activos=cargarSocios(socios_activos)

print("El club tiene", len(socios_activos), "socios")

print("***Registrar pago de cuotas")
numero=int(input("Número de socio: "))
socios_activos[numero][2]=True

print("***Modificando fecha de ingreso...")
socios_activos=modificarFecha(socios_activos, "13032018", "14032018")

print("***Eliminar socio")
nombre=input("Nombre y apellido: ")
numero=numeroSocio(socios_activos, nombre)
if numero in socios_activos:
    del socios_activos[numero]

imprimirListado(socios_activos)

#14 Ejercicios para practicar programación usando estructuras de datos, con Python.

#1 

lista=[1, 2, 3, 4]
for elemento in lista:
  print(elemento)
articulos={ 154:["jabon en polvo", "limpieza", True],
            248: ["talco", "cosmetica", False],
            199: ["cera para pisos","limpieza", True] }
for clave, valor in articulos.items():
  print("Codigo: ", clave)
  print("Descripcion: ", valor[0])
  print("Rubro; ", valor[1])
  if valor[2]:
    print("Hay stock")
  else:
    print("Agotado")
  print("-------------")

#2

lista =[1, 2, 3, 4, 4, 6, 7, 7, 8, 0, 9, 9, 9]

for i in range(len(lista)-1):
  if lista[i]==lista[i+1]:
    print(lista[i])

#3
 
def empleadoExiste(empleados, nombre):
  for datos in empleados.values():
    if datos[0]==nombre:
      return True
  return False

empleados= {100: ["Jorge Millán", "Administracion"],
200:["Oriana López", "Gerencia"],
300:["Guadalupe Ríos", "RR.HH"],
400:["Lionel Campos", "Ventas"]}

nombre = input("Nombre de empleados: ")
if not empleadoExiste(empleados,nombre):
  print("El empleado no se encuentra en la nómina")

#4

alumnos= {"121-5": 42752983,
"243-9":  39234110,
"113-8:": 44922182,
"324-1": 39110245 }

legajo= input("Legajo a buscar: ")
if legajo in alumnos.keys():
  print("El DNI es: ", alumnos[legajo])

#5

def cargarDatos(diccionario):
  dni = int(input("DNI: "))
  while dni != 0:
    nombre = input("Nombre:" )
    domicilio = input("Domicilio:" )
    telefono = int(input("Telefono: " ))
    diccionario[dni]=[nombre, domicilio, telefono]
    dni= int(input("DNI: "))
  return diccionario

def imprimirDatos (diccionario):
  for clave, valor in diccionario.items():
    print ("-DNI:",clave, "-Nombre:", valor[0], "-Domicilio:", valor[1], "-Telefono:", valor[2])

clientes= { 44299132:["Gastón Quinteros", "Los Tilios 412", 582119721],
          38110223:["Valeria Gimenez", "Almendros 192",59912834],
          27918006:["Diego Linares", "Las Fresias 881", 51288390] }
clientes= cargarDatos(clientes)
imprimirDatos(clientes)

#6

def cargarMercaderias(mercaderias):
  articulo=[]
  codigo= int(input("codigo: "))
  while codigo !=0:
    descripcion=input("Descripcion: ")
    articulo.append(descripcion)
    rubro=input("Rubro: ")
    articulo.append(rubro)
    mercaderias[codigo]=articulo
    codigo=int(input("codigo: "))
  return mercaderias

productos={}
productos=cargarMercaderias(productos)
for codigo, datos in productos.items():
  print(codigo, "-Descripcion: ", datos[0], "-Rubro", datos[1])

#7

a=[1, 2, 3, 4]
for i in range(len(a)):
  if i==2:
    del a[3]
  print(a[i])

#8

b={"a": [1, 2, 3], "b": [], "c": [8,6], "d": [], "e": [4]}
for clave in b.keys():
  if b[clave]==[]:
    del b[clave]