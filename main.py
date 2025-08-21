import xml_elementtree as xmlet 
import xml_minidom as xmldom

def menu():
    print("------------------------------------------")
    print("************  MENU  **********************")
    print("------------------------------------------")
    print("1.- Cargar archivo               *********")
    print("2.- Procesar archivo             *********")
    print("3.- Escribir archivo salida      *********")
    print("4.- Mostrar datos del estudiante *********")
    print("5.- Generar gráfica              *********")
    print("6.- Salir                        *********")
    print("------------------------------------------")

    opcion = int(input('Ingresa una opción: '))
    return opcion

if __name__ == "__main__":

    campos_agricolas = []

    while True:
        opc = menu()
        if opc == 1: #Leer archivo xml con ElementTree
            ruta = input('Ingresa la ruta origen del archivo: ') 
            nombre_archivo = input('Ingresa el nombre del archivo: ')
            xmlet.leer_archivo(ruta + nombre_archivo, campos_agricolas)
            print('')
        elif opc == 2: #Procesar Archivo
            pass

        elif opc == 3: #Escribir Archivo de salida
            for campo in campos_agricolas:
                '''
                #Mostrar campos Agricolas
                print('====================================')
                print(campo.get_nombre())
                print('====================================')
                for estacion in campo.estaciones:
                    print(estacion.get_nombre())   
                print('')'''

        elif opc == 4: #Mostrar datos del Estudiante
            '''
            #Escribir archivo xml con ElementTree
            ruta = input('Ingresa la ruta destino del archivo: ') 
            nombre_archivo = input('Ingresa el nombre del archivo: ')
            xmlet.escribir_archivo(ruta + nombre_archivo, campos_agricolas)
            print('')'''

            print("Hugo Lizandro Ramirez Siquinajay")
            print("201800956")
            print("Introducción a la Programación y Computación 2")
            print("Seccion N")
            print("Ingenieria en Ciencias y Sistemas")
            print("4to Semestre")

        elif opc == 5: #Generar Grafica
            '''
            #Escribir archivo xml con Mini
            ruta = input('Ingresa la ruta destino del archivo: ') 
            nombre_archivo = input('Ingresa el nombre del archivo: ')
            xmldom.escribir_inventario(ruta + nombre_archivo, campos_agricolas)
            print('')'''
        elif opc == 6:
            print('Programa finalizado')
            break
        else:
            print('Opción no válida\n')