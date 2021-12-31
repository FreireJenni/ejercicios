# Nombre: Bryan Javier Flor Esparza

# Tipos de Datos y Acciones elementales 
#Ejercicio º1

li = ("Hola mundo", "" , "Verdadero", "1", "c", "256", "8>19" )
print(li)

#Ejercicio º2

#ejemplo
resp = 2 *(4 - 10 + 8)/2* 36 *(1/2)
print(resp)
print(type(resp))

#Ejercicio º4

numero1 = 5
numero2 = 7

suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
divi = numero1 / numero2
modulo = numero1 % numero2

print(suma)
print(resta)
print(multi)
print(divi)
print (modulo)

#Ejercicio º5
from math import sqrt
c = 20
d = 6
e = 9
c1 = 0
c2 = 0
if ((d**2)-4*c*e) < 0:
     print("Solución de la ecuación contiene numeros complejos")
else:
    c1 = (-d+sqrt(d**2-(4*c*e)))/(2*c)
    c2 = (-d-sqrt(d**2-(4*c*e)))/(2*c)
    print("Las soluciones de la ecuación son:")
    print(c1)
    print(c2)

print("Soluciones: ", c1 , c2)

#Ejercicio º6
import math

ca1 = float(input("Introducir el cateto 1: "))
ca1 = float(input("Introducir el cateto 2: "))

hipo = math.sqrt((ca1**2) + (ca1**2))
print("Hipotenusa es igual a: ", hipo)

#Ejercicio º7

n = int(input("Ingrese un número: "))
if n % 2 == 0:
    print("0")
else:
    print("1")

#Ejercicio º9

lista=[]
for v in range(4):
    val=int(input("Ingrese un valor entero: "))
    lista.append(val)

rep = lista.count(1)
if rep % 2 == 0:
    print("El codigo de paridad es 1")
else:
    print("El codigo de paridad es 0")

#Ejercio º10

valor_binario = '1010'

num_decimal = 0

for posicion, digito_string in enumerate(valor_binario[::-1]):
	num_decimal += int(digito_string) * 2 ** posicion

print(f'El número decimal que buscamos es {num_decimal}')

#Ejercicio º11

nume = int(input("Ingrese un numero entero de 4 cifras: "))
unidad_mil = nume / 1000
t = nume % 1000

cen = t / 100
t = t % 100

dec = t / 10
uni = t % 10

print("Unidades de mil : %i" % unidad_mil)
print("Centenas: %i" % cen)
print ("Decenas: %i" % dec)
print("Unidades: %i" % uni)

#Estructuras de Control de Flujo de Datos

#Ejercicio º1

año = 0
lis_1 = []
def string_int(mi_infor):
    for a in mi_infor:
        lis_1.append(int(a))
p_fecha = input("Ingrese la fecha en formato (ddmmaaaa): ")
string_int(p_fecha)

m = lis_1
n = lis_1[6]
o = lis_1[5]
p = lis_1[4]

if año % 4 != 0:
    print(" El año No es bisiesto")
elif año % 4 == 0 and año % 100 != 0:
    print(" El año Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
    print("El año No es bisiesyo")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    print("El año Es bisiesto")

#Ejercicio º2 

lis_2 = []

def string_int(mi_infor):
    for a in mi_infor:
        lis_2.append(int(a))

p_num = input("Ingrese un numero entero de 5 digitos: ")
string_int(p_num)

m = lis_2[0]
n = lis_2[1]
o = lis_2[2]
p = lis_2[3]
q = lis_2[4]

if m == q:
    if n == p:
        print("El número ingresado es capicúa")
    else:
        print("El número ingresado NO es capicúa")
else:
    print("El número ingresado no es capicúa")

#Ejercicio º3

hora = int(input("Ingrese la cantidad de horas: "))
min= int(input("Ingrrese la cantidad de minutos: "))

h_a_s = hora * (3600)
m_a_s = min *(60)
total_seg = h_a_s +m_a_s

print("El total de segundos es: ", total_seg)

#Ejercicio º4

s = int(input("Ingrese la cantidad de segundos: "))

if s > 0 :
    m = s / 60
    h = s / 3600
    dias = s / 86400

    print("\n La cantidad de minutos es: ", m)
    print("\n La cantidad de horas es: ", h)
    print("\n La cantidad de dias es: ", dias)
else:
    print("Ingrese una cantidad de segundos validos")

#Ejercicio º5

A = int(input("Ingrese el primer numero entero positivo: "))

if A > 0 :
    B = int(input("Ingrese el el segundor numero entero positivo: "))
    if B > 0 :
        C = int(input("Ingrese el Tercer numero entero positivo: "))
        if C > 0:
            if A > B and A > C:
                print("\n El numero mayor es: ", A)
                if B > C:
                    print("\n El segundo mayor es: ", B)
                else:
                    print("\n El segundo mayor es: ", C)
            elif B > A and B > C:
                print("\n EL numero mayor es: ", B)
                if A > C:
                    print("\n El segundo mayor es: ", A)
                else:
                    print("\n El segundo mayor es: ", C)
            elif C > A and C > B:   
                print("\n EL numero mayor es: ", C)
                if A > B:
                    print("\n El segundo mayor es: ", A)
                else:
                    print("\n El segundo mayor es: ", B)
            else:
                print("No se ha podido deteerminar el mayor de los 3 numeros")                
        else:
            print("Por favor ingrese un numero entero positivo")  
    else:
        print("Por favor ingrese un numero entero positivo")          
else:
    print("Por favor ingrese un numero entero positivo") 

#Ejercicio º6

H_e = int(input("Ingrese de hora en formato de 12 en la que se estaciono: "))
if H_e >= 0 and H_e <= 12:   
    M_e = int(input("Ingrese el o los minutos en la que se estaciono: "))   
    if M_e >= 0 and M_e < 60: 
        AM_PM_e  = input("SI usted se estaciono en la mañana ingrese la letra A y si ingreso pasado del medio dìa ingrese la letra P: ") 
        if AM_PM_e == "A" or AM_PM_e == "P" :
            H_s = int(input("Ingrese la hora en formato de 12 en la que sale del estacionamiento: "))
            if H_s >= 0 and H_s <= 12:
                M_s= int(input("Ingrese la hora en la que sale del estacionamiento: ")) 
                if M_s >= 0 and M_s < 60:
                    AM_PM_s = input("SI usted sale del estacionamiento en la mañana ingrese la letra A y si salio pasado del medio dìa ingrese la letra P: ")
                    if AM_PM_s == "A" or AM_PM_s == "P" :
                        if AM_PM_e == "A" and AM_PM_s == "A" or AM_PM_e == "A" and AM_PM_s == "P" or AM_PM_e == "P" and AM_PM_s == "P":
                            if AM_PM_e == "A" and AM_PM_s == "A" or AM_PM_e == "P" and AM_PM_s == "P":
                                resta_H = H_e - H_s
                                Total_H = resta_H * 4
                                resta_M = M_e - M_s
                                Total_M = resta_M/30
                                Total_M_2 = 0
                                if Total_M < 0 :
                                    Total_M_2 = 2.50
                                    Total_T = Total_H + Total_M_2
                                    print("El Valor a pagar es: Bs", Total_T)
                            elif AM_PM_e == "A" and AM_PM_s == "P":
                                H_s+=12
                                resta_H = H_e - H_s
                                Total_H = resta_H * 4
                                resta_M = M_e - M_s
                                Total_M = resta_M/30
                                Total_M_2 = 0
                                if Total_M < 0 :
                                    Total_M_2 = 2.50
                                    Total_T = Total_H + Total_M_2
                                    print("El Valor a pagar es: Bs", Total_T)
                        else:
                            print("Los datos de entrada y salida no coinciden")
                    else:
                        print("Ingrese una Letra Valida")
                else:
                    print("Ingrese unos minutos de salida valido")        
            else:
                print("Ingrese una hora de salida valida")
        else:
            print("Ingrese una letra valida")    
    else:
        print("Ingrese una cantidad de minutos valido")   
else:
    print("Ingrese una hora de entrada valida")

#Ejercicio º7

L = float(input("Ingrese su peso en Libras: "))
C = int(input("Ingrese su Altura en Centimetros: "))

P = L*0.453592
A = C /100

prom = P/(A * A)

print("Su peso en Kg es: ", P)
print("Su altura en Metros es: ", A)
print("Su promedio es: ", prom)

if prom < 16 :
    print("Su categoria es Criterio de ingreso.")
elif prom >= 16 and prom <= 16.9:
    print("Su categoria es infra peso.")
elif prom >= 17 and prom <= 18.4:
    print("Su categoria es bajo peso.")
elif prom >= 18.5 and prom <= 24.9:
    print("Su categoria es peso normal.")
elif prom >= 25 and prom <= 29.9:
    print("Su categoria es sobrepeso.")
elif prom >= 30 and prom <= 34.9:
    print("Su categoria es obesidad pre-mórbida.")
elif prom >= 40 and prom <= 45:
    print("Su categoria es obesidad mórbida.")
elif prom > 45 :
    print("Su categoria es obesidad híper-mórbida.")


#Ejercicio º8

d = int(input("Ingrese un dia correspondiente al 2014: "))
if d > 0 and d < 31:
    m = int(input("Ingrese un numero de mes correspondiente al 2014: "))
    if m > 0 and m <=12 :
        dias_Mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        i = 0
        acum = 0
        while i <= m - 1:
            acum = acum + dias_Mes[i]
            i = i + 1
        total = acum + d
        print("\n EL total de dias que han transcurrido desde el 1 de enero del 20154 hasta la fecha que solicito es: ", total)

#Ejercicio º9

m = int(input("Ingrese un numero entre el 1 y el 12: "))
if m > 0 and m <= 12 :
    if m == 1 :
        print("Enero")
    elif m ==2 :
        print("Febrero")
    elif m ==3 :
        print("Marzo")
    elif m ==4 :
        print("Abril")
    elif m ==5 :
        print("Mayo")
    elif m ==6 :
        print("Junio")
    elif m ==7 :
        print("Julio")
    elif m ==8 :
        print("Agosto")
    elif m ==9 :
        print("Septiembre")
    elif m ==10 :
        print("Octubre")
    elif m ==11:
        print("Noviembre")
    elif m ==12 :
        print("Diciembre")       
else:
    print("Ingrese un numero valido")

#Ejercicio º10 

c = float(input("Ingrese la cantidad a pagar en el almacen: "))

if c > 1000:
    total = c * 0.80
    print("SU total a pagar aplicando el descuento de la tienda es de: Bs", total)
else:
    print("Su total a pagar es de: Bs", c)

#Estructuras Iterativas

#Ejercicio º1

import math
n = int(input("ingrese un numero entero: "))
if n > 0:
    dig = int(math.log10(n))+1
    print(dig)
elif n == 0:
    dig = 1
    print(dig)
elif n < 0:
    print("Ingrese un numero valido")

#Ejercicio º2

def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero

def capicua(numero):
    return numero == invertir_numero(numero)

numeros = [11, 20, 123, 9889, 2811, 1801, 777, 12321, ]

for numero in numeros:
    es_capicua = capicua(numero)
    print(f"El número {numero} es capicúa? {es_capicua}")

#Ejercicio º3

def es_primo(num):
    con = 0

    for i in range(1, num+1):
        if num % i == 0:
            con += 1
    
    if con == 2:
        print("Es un numero primo")
        return True
    else:
        print("No es un numero primo")
        return False
n = int(input("Ingrese un numero primo positico: "))
if n > 0:
    print(es_primo(n))  

#Ejercicio º4:

n = int(input("Ingrese un numero entero: "))
if n >= 0 :
    x = 1
    f = 1
    while x <= n:
        f = f *x 
        x += 1
    print("El factorial de ",n," es: ",f)
else:
    print("No se pudo calcular el factorial")

#Ejercicio º5:

def validar(valor):
    	return False

valido = 0
while not valido:
    contraseña = input("Introduzca una contraseña con al menos 10 digitos: ")
    valido = len(contraseña) >= 10
print("\n Felicidades has ingresado una contraseña valida")

#Ejercicio º6
#Ejercicio º7

def secuencia(self):
            edad=[18,24,25,30,35,36]
            p=[40,50,60,70,80]
            esta=[1.40,1.45,1.50,1.55,1.60,1.70]
            p_edad=(sum())/len()
            p_peso=(sum(p))/len(p)
            p_es=(sum(p))/len(esta)
            c=0
            x=0
            while c<8:
                x+=(p_edad.count(18+c))
                c+=1  
            c=1
            mayores_36=0  
            while c<150:
                mayores_36+=(p_edad.count(36+c))
                c+=1
            c=0
            freire=0
            while c<36:
                freire=[i for i,x in enumerate(p_edad) if x>=18 and x<=35]
                c+=1
            suma=0
            c=0
            while c<len(freire):
                suma+=p[freire[0+c]]
                c+=1
            print(freire)
            print("promedio de la edad :", p_edad)
            print("promedioa del peso : ", p_peso)
            print("promedio de la  estatura : " ,p_es)
            print("un rango entre 18 y 25 : ", x)
            print("personas mayores : " , mayores_36)
            print("promedio de pesos de todas las personas : " , suma/len(freire))

#Ejercicio º8

def algoritmo(self):
        for w in range (10):
            print("tabla de mult: "+str(w+1))
            for v in range (12):
                print(str(+1)+"*"+str(v+1)+"="+str(w+1)* (v+1))
                print ("\n")  

#ejercicio 9 y 10
def fichas(self):
        for o in range(0,7):
            for e in range(0, o+1):
                print("|" + str(o) + "|" + str(e) + "|")

def numeros_positivos(self):
        c=0
        numeros_posi=0
        while True:
            nume=int(input("Ingrese  números positivos: "))
            if nume==0:
                break
            elif nume > 1:
                numeros_posi+=nume
                c+=1
                prome1=numeros_posi/c
            print("serie promedio : " ,prome1 )       

#Prodecimientos (Acciones y Funciones)

#Ejercicio º1

def edades_usuarios(self):
        c=0
        e_ma=0
        while True:
            print("presione [enter] para dejar de ingresar notas!")
            edades=(input("ingrese las edades a promediar:"))
            if edades=='':
                break
            elif edades >= "18":
                edades=int(edades)
                e_ma+=edades
                c+=1
                pro=e_ma/c
        return pro

#Ejercicio º2

def Eleva(self):
    ba=int(input("ingrese la base: "))
    exponente=int(input("ingrese el exponente: "))
    exponente= 2
    result=ba**exponente
    print(f"El resultado es: {result} ")

#Ejercicio º3

def peri(self):
    lado=float(input("Ingrese el valor de uno de los lados del pentágono:"))
    perimetro=5*lado
    return perimetro

#Ejercicio º4
#Ejercicio º5

def horas(self):
        def MillasAKilometros(mi):
            kilome=mi*1.60935
            return kilome
        ci=['']*12
        xyz=['A','B','','C','D','','F','G','','H','I']
        ind=0
        while ind<=11:
            if ind==0 or ind==1 or ind==3 or ind==4 or ind==6 or ind==7 or ind==9 or ind==10:
                while ci[ind]<='':
                    ci[ind]=input(f"Ingrese ciudad {xyz[0+ind]}: ")
                ind+=1
            else:
                while ci[ind]<='':
                    ci[ind]=input(f"Ingrese distancia entre ciudades en millas: ")
                ind+=1
        print(f"\nEntre {ci[0]} y {ci[1]}, hay {MillasAKilometros(int(ci[2])):.2f} Km de distancia\n")
        print(f"Entre {ci[3]} y {ci[4]}, hay {MillasAKilometros(int(ci[5])):.2f} Km de distancia\n")
        print(f"Entre {ci[6]} y {ci[7]}, hay {MillasAKilometros(int(ci[8])):.2f} Km de distancia\n")
        print(f"Entre {ci[9]} y {ci[10]}, hay {MillasAKilometros(int(ci[11])):.2f} Km de distancia\n")


