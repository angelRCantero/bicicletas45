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

def verificacion_entrada():
    marca = "MORENO", "SPECIALIZED", "SCOTT", "TREK", "GIANT", "CANYON", "CANNONDALE", "ORBEA", "BMC", "PINARELLO", "BIANCHI"

    tipo = "MONTANIA", "PASEO", "COMPETICION", "EXPOSICION", "ENTRENAMIENTO"

    rodado = "XS", "S", "M", "M2"

    color = "ROJO", "VERDE", "AZUL", "AMARILLO", "NEGRO", "BLANCO"
    while True: # GENERO EL BUCLE DEL PROGRAMA DESDE LA LINEA '41' HASTA LA LINEA '95' MEDIANTE WHILE TRUE/BREAK/CONTINUE
         
        while True:
                marca = input('ingrese marca')#COMENZAMOS AGRUPANDO TODAS LAS VARIABLES CON LAS QUE FUE DECLARADA LA ENTRADA 'marca' 
                #CON UNA ETIQUETA DE TIPO 'and' EN VEZ DE EL 'or'
                #ESTO ES SOLAMENTE POSIBLE SI SE LLAMA A LA ACCION PREVIAMENTE MARCADA DENTRO DEL 'if' CADA VEZ QUE SE USE EL AND EN ESTE CASO
                #'IF MARCA != VAR ACEPTADA 'and' IF MARCA != VAR ACEPTADA NUEVAMENTE' 
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
#APOYANDOME EN EL TRABAJO DE MI COMPAÑERO BERNARDO USO SU SINTAXIS PARA EL MENÚ DEL BUCLE DEL PROGRAMA
#POR MEDIO DEL MENÚ LLAMO A LAS VARIABLES CON EL USO DEL ' print + var ' POR EJEMPLO ' print(su msj) + marca '            
        print("Has elegido la bicicleta ")
        print(("de la marca:  ") + (marca))
        print(("del tipo:  ") + (tipo))
        print(("rodado: ") + rodado)
        print(("de color: ") + color)
        print("Si la bicicleta elegida es correcta presione 1")
        print("De no ser correcta presione 0")
        paso_1 = int(input("Desea continuar ")) #EL PASO 1 ESTÁ DELIVERANDO LA CONTINUIDAD DE LA EJECUCIÓN DEL PROGRAMA
        if paso_1 == 0:
            print("Vuelva a seleccionar el bulón")        
        else: #COMO SIGUIENTE PASO LLAMA A UNA NUEVA VARIABLE EN ESTE CASO LA VARIABLE ' cantRequerida ' QUE DEFINIREMOS EN LA LINEA '98'
            cantRequerida
            break
        continue
    
def cantidad_requerida():
    while True:#LA CANTIDAD REQUERIDA CONSTA DE UN BUCLE PARA PODER VALIDAR EL DATO DE ENTRADA E INTEGRÁR TANTO EL STOCK DE LA TIENDA
        global cantRequerida #COMO ASI TAMBIÉN EL CARRITO DE COMPRA,PUDIENDO ASI,HACER MAS DE UNA COMPRA DENTRO DEL PROGRAMA ACTIVO
        try:
            cantRequerida = int(input("Introduzca la cantidad requerida: "))
        except ValueError:
            print("Debes escribir un numero")
            continue
        if cantRequerida > 0:
            continuarComprando()#ESTA OPERACIÓN LLAMA A LA SIGUIENTE VARIABLE PARA PODER CONTINUAR COMPRANDO
        else:#LA VARIABLE 'continuarComprando' DEFINIDA EN LA LINEA (113)
            print("Debe colocar un numero positivo")
            break
        continue         
    
def continuarComprando ():
    while True:#MEDIANTE WHILE TRUE SE GENERA UN SUB-MENÚ QUE DA OPCIONES DE COMO CONTINUAR
        print("Desea seguir comprando?: ")
        print("1:Continuar comprando")
        print("2:Finalizar compra")
        continuarONo = int(input("Introduzca Respuesta "))
        if continuarONo == 1:#AL CONTINUAR SE DEBERÁ SEGUIR CON LAS SIGUIENTES SUBRRUTINAS YA ADENTRANDONOS EN LA LOCAL DE NUESTRO PROGRAMA
            Superb45()#POR MEDIO DE UN SUPERDESCRIPTOR HACEMOS USO DE BUSQUEDAS MAS ÁGILES PERO RESTA DEFINIRLO
            agregarAlCarrito() #RESTA DEFINIR EL CARRITO CON SU ESTRUCTURA IMPORTANDO LOS DATOS DEL EXCEL
        else:
            Superb45()
            verficarStock()#RESTA DEFINIR EL STOCK DISPONIBLE PARA ASÍ MODIFICAR NUESTRA LOCAL Y HACER CAMBIOS MEDIANTE LA 
            break# ENTRADA DEL USUARIO Y DAR UNA RESPUESTA NEGATIVA EN CASO DE NO HABER DISPONIBILIDAD DE DICHA BICI
        continue
    

            
 
 #IMPORTAR EL EXCEL MEDIANTE PANDA
 #OP: GENERAR SUPERDESCRIPTOR IMPORTADO DESDE EL EXCEL Y CARGAR DE DATOS AL MISMO
 

    