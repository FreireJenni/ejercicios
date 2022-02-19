import os
class ficha :
    def init(self):
        pass

    def menu(self,opciones):
        
        print("===================> MENU DE FICHA PERSONAL <========================")
        for opcion in opciones:
            print(opcion)

        opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
        return opc

help=ficha()
Lista=["1. Pila","2. Cola","3. Lista","4. Salir"]

opcion =" "

while opcion != "4":
    
    os.system("cls")
    
    if opcion=="1":
        class Menu :
            def init(self):
                pass
        
            def menu(self,opciones):
                

                print("================> Se ingresó el menú Pila <================ ")
                for opcion in opciones:
                    print(opcion)

                opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
                return opc
                
            milis=[]
                # for x in milis:
                # milis_edd = print(milis)
            print("================> Se ingresó el menú Pila <================ ")
            print("cuantos elementos se requiere ")
            cant=int(input())
            os.system("cls")
            i=0
            if cant <8:
                    print("La lista está vacía")
                    
            while i<cant:
                        print("Ingresar")
                        nom=input()
                        milis.append(nom)
                        i+=1
                        
                        print("La Pila esta vacía")
                        # lista2=["si","no"]
                        # lista2=input("desea agg otro nombre si o no : ")


                        # if lista2 == "si":
                        #     nom2=input("agg otro nombre : ")
                        #     milis.append(nom2)

                        #     print(f"el segundo nombre que se agg fue {nom2}")

                        # else:
                        #     print("ok")
                        
                        
                        os.system("cls")
                        print(milis)
                    
            else:
                    print("La lista está llena")

            print("La lista es: ",milis)

            na=milis.pop(-1)
            print("El elemento que va a salir es : ",na)

            print(milis)

        print("=====================================================")
        print()
        
    elif opcion=="2":
        class ficha :
            def init(self):
                pass
        
            def menu(self,opciones):
                
                print("================> Se ingreso al menú Cola <================ ")
                for opcion in opciones:
                    print(opcion)

                opc=input("Digitar la ficha personal [1...{}]: ".format(len(opciones)))
                return opc             
            milis=[]
                # for x in milis:
                # milis_edd = print(milis)
            print("================> Se ingresó al menú cola <================ ")
            print("Cuantos elementos desea ")
            cant=int(input())
            os.system("cls")
            i=0
            if cant <8:
                    print("La lista está vacía")
                    
            while i<cant:
                        print("Ingrese")
                        nom=input()
                        milis.append(nom)
                        i+=1
                        
                        print("La Pila está vacía")
                                    
                        os.system("cls")
                        print(milis)
                    
            else:
                 print("La lista está llena")

            print("La lista es ",milis)

            na=milis.pop(0)
            print("El elemento que se va a salir es : ",na)
            
            print(milis)

        print("=====================================================")
        print()
    elif opcion=="3":
        class ficha :
            def init(self):
                pass

            def menu(self,opciones):
            
                print("================> Se ingresó al mení Lista <================ ")
                for opcion in opciones:
                    print(opcion)

                opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
                return opc                 
            milis=[]
                # for x in milis:
                # milis_edd = print(milis)
            print("================> Se ingresó al menú Lista <================ ")
            print("Cuantos elementos desea ")
            cant=int(input())
            os.system("cls")
            i=0
            if cant <8:
                    print("La lista estña vacía")
                
            while i<cant:
                        print("Ingresar")
                        nom=input()
                        milis.append(nom)
                        i+=1
                        
                        print("La lista está vacía")
                        os.system("cls")
                        print(milis)
                    
            else:
                    print("La lista está llena")

            sacar=input("Que elemento desea sacar : ")
                    
            os.system("cls")
            for x in range(len(milis)-1,-1,-1):
                        if milis[x]== sacar:
                            print(milis.pop(x))
            print(milis)

            sa=input("Desea averiguar en que posicion esta su elemento : ")
            
            print("Posicion : ",milis.index(sa))
    else:
            print()
    opcion=help.menu(Lista)
print("GRACIAS POR VISITAR NUESTRO SITIO")