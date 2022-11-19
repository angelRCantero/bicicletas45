#########################################
# Primer commit main Bici45-prueba
# *Subir a Github
# ejecutable.exe
# release: 26/10/2022
# developes: Cantero Angel Rafael
#########################################

#main-resources

marca = "MORENO", "SPECIALIZED", "SCOTT", "TREK", "GIANT", "CANYON", "CANNONDALE", "ORBEA", "BMC", "PINARELLO", "BIANCHI"

tipo = "MONTANIA", "PASEO", "COMPETICION", "EXPOSICION", "ENTRENAMIENTO"

rodado = "XS", "S", "M", "M2"

color = "ROJO", "VERDE", "AZUL", "AMARILLO", "NEGRO", "BLANCO"

#index

#marca = input ( "seleccione marca")
#print (" usted selecciono, " + marca )

#tipo = input ( "seleccione tipo")
#print (" usted selecciono, " + tipo )

#rodado = input ( "seleccione rodado")
#print (" usted selecciono, " + rodado )

#color = input ( "seleccione color")
#print (" usted selecciono, " + color )

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
            
            
 #GENERAR WHILE TRUE GENERAL PARA ASI DARLE BUCLE AL PROGRAMA DESDE SU INICIO
 #IMPORTAR EL EXCEL MEDIANTE PANDA
 #DEFINIR VALIDACIONES DE DATOS MEJOR ORGANIZADAS
 #OP: GENERAR SUPERDESCRIPTOR IMPORTADO DESDE EL EXCEL Y CARGAR DE DATOS AL MISMO
 #CREAR INTERFAZ O MENU INTUITIVO PARA EL USUARIO CONTENIENDO ESTE BUCLE Y OPCIONES DE STOCK NEGATIVO

    