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

marca = input ( "seleccione marca")
print (" usted selecciono, " + marca )

tipo = input ( "seleccione tipo")
print (" usted selecciono, " + tipo )

rodado = input ( "seleccione rodado")
print (" usted selecciono, " + rodado )

color = input ( "seleccione color")
print (" usted selecciono, " + color )

while True:
        marca = input('ingrese marca')
        if marca != "SCOTT":
            print("Pone una marca valida")
        else:
            print("Genial!")
            break
        continue

while True:
        tipo = input('ingrese tipo')
        if tipo != "MONTANIA":
            print("elija un tipo valido")
        else:
            print("Bien!")
            break
        continue
   
while True:
        rodado = input('ingrese tipo')
        if rodado != "XS":
            print("elija un rodado valido")
        else:
            print("Perfecto!")
            break
        continue