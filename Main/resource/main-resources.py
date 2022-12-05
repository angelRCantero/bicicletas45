#########################################
# Primer commit main Bici45-prueba
# *Subir a Github
# ejecutable.exe
# release: 26/10/2022
# developes: Cantero Angel Rafael
#########################################

#main-resources

#marca = "MORENO", "SPECIALIZED", "SCOTT", "TREK", "GIANT", "CANYON", "CANNONDALE", "ORBEA", "BMC", "PINARELLO", "BIANCHI"

#tipo = "MONTANIA", "PASEO", "COMPETICION", "EXPOSICION", "ENTRENAMIENTO"

#rodado = "XS", "S", "M", "M2"

#color = "ROJO", "VERDE", "AZUL", "AMARILLO", "NEGRO", "BLANCO"

#index

#marca = input ( "seleccione marca")
#print (" usted selecciono, " + marca )

#tipo = input ( "seleccione tipo")
#print (" usted selecciono, " + tipo )

#rodado = input ( "seleccione rodado")
#print (" usted selecciono, " + rodado )

#color = input ( "seleccione color")
#print (" usted selecciono, " + color )

import openpyxl
from openpyxl import workbook
from openpyxl import load_workbook



def verificacion_entrada():
    marca = "MORENO", "SPECIALIZED", "SCOTT", "TREK", "GIANT", "CANYON", "CANNONDALE", "ORBEA", "BMC", "PINARELLO", "BIANCHI"

    tipo = "MONTANIA", "PASEO", "COMPETICION", "EXPOSICION", "ENTRENAMIENTO"

    rodado = "XS", "S", "M", "M2"

    color = "ROJO", "VERDE", "AZUL", "AMARILLO", "NEGRO", "BLANCO"

while True:
    
        while True:
                marca = input('ingrese marca') 
                if marca != "SCOTT" and marca !="MORENO" and marca != "SPECIALIZED" and marca != "SCOTT" and marca != "TREK" and marca != "GIANT"and marca != "CANYON" and marca != "CANNONDALE" and marca != "ORBEA" and marca != "BMC" and marca != "PINARELLO" and marca != "BIANCHI":
                    print("Pone una marca valida")
                else:
                    print("Genial!")
                    break
                continue

        while True:
                tipo = input('ingrese tipo')
                if tipo != "MONTANIA" and tipo != "PASEO" and tipo != "COMPETICION" and tipo != "EXPOSICION" and tipo != "ENTRENAMIENTO":
                    print("elija un tipo valido")
                else:
                    print("Bien!")
                    break
                continue
            
        while True:
                rodado = input('ingrese rodado')
                if rodado != "XS" and rodado != "S" and rodado != "M" and rodado != "M2":
                    print("elija un rodado valido")
                else:
                    print("Perfecto!")
                    break
                continue
            
        while True:
                color = input('ingrese color')
                if color != "ROJO" and color != "VERDE" and color != "AZUL" and color != "AMARILLO" and color != "NEGRO" and color != "BLANCO":
                    print('elija entre:"ROJO", "VERDE", "AZUL", "AMARILLO", "NEGRO", "BLANCO" ')
                else:
                    print("Excelente!")
                    break
                continue
                        
        print("Has elegido la bicicleta ")
        print(("de la marca:  ") + (marca))
        print(("del tipo:  ") + (tipo))
        print(("rodado: ") + rodado)
        print(("de color: ") + color)
        print("Si la bicicleta elegida es correcta presione 1")
        print("De no ser correcta presione 0")
        paso_1 = int(input("Desea continuar ")) 
        if paso_1 == 0:
            print("Vuelva a seleccionar la bicicleta")
        elif paso_1 == 1:
            cantRequerida()      
        else: 
            print("ingrese una opcion valida")
            paso_1
            break
        continue
    
def cantRequerida():
    while True:
        global cantRequerida
        try:
            cantRequerida = int(input("Introduzca la cantidad requerida: "))
        except ValueError:
            print("Debes escribir un numero")
            continue
        if cantRequerida <= 0:
            print("coloca un numero valido") 
        else:
            finalizarCompra()
            break
        continue
    
def finalizarCompra ():
    while True:
        print("Desea seguir comprando?: ")
        print("2:Continuar comprando")
        print("1:Finalizar compra")
        finalizarCompra = input("Introduzca Respuesta ")
        if finalizarCompra == 1:
            print("Gracias por visitarnos!!")
        else:
            continuarComprando()
            break
        
def continuarComprando():
        while True:
            print("seguimos comprando? ")
            print("1:seguimos!: ")
            print("2:No, gracias!: ")
            if continuarComprando ==1:
                print("sigamos comprando!!")
                verificacion_entrada()
            else:
                print("gracias por tu visita!!")
            break
            
print("Hola!! Bienvenidos a Bicicletas45")
print("Seleccione que bicicleta desea comprar")

verificacion_entrada()
finalizarCompra()

            
 
 #PROBLEMA AL EJECUTAR EL BUCLE POR SEGUNDA VEZ SE ROMPE EL PROGRAMA NI TAMPOCO CIERRA BIEN EL BUCLE INICIAL

    