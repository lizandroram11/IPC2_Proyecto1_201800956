import os
from xml_ET import XMLManager

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Cargar archivo")
    print("2. Procesar archivo (F y Fp)")
    print("3. Escribir archivo de salida (reducción)")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica (pendiente)")
    print("6. Salir")
    print("==========================")

def main():
    gestor = XMLManager()
    archivo_cargado = False

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ruta = input("Ingrese la ruta del archivo (ej: C:/Users/.../): ").strip()
            nombre = input("Ingrese el nombre del archivo (ej: entradas.xml): ").strip()
            archivo = os.path.join(ruta, nombre)
            try:
                gestor.cargar_archivo(archivo)
                archivo_cargado = True
            except Exception as e:
                print(f"❌ No se pudo cargar el archivo: {e}")

        elif opcion == "2":
            if not archivo_cargado:
                print("⚠️ Primero debe cargar un archivo.")
            else:
                print("🔄 Procesando archivo...")
                gestor.procesar_archivo()
                gestor.generar_patrones()

        elif opcion == "3":
            if not archivo_cargado:
                print("⚠️ Primero debe cargar un archivo.")
            else:
                ruta = input("Ingrese la ruta donde guardar el archivo: ").strip()
                nombre = input("Ingrese el nombre del archivo de salida (ej: salida.xml): ").strip()
                archivo_salida = os.path.join(ruta, nombre)
                grupos = gestor.reducir_estaciones()
                gestor.escribir_salida(archivo_salida, grupos)

        elif opcion == "4":
            print("\n👨‍💻 Datos del estudiante:")
            print("Nombre : Tu Nombre Aquí")
            print("Carnet : 201800956")
            print("Curso  : Introducción a la Programación y Computación 2")
            print("Carrera: Ingeniería en Ciencias y Sistemas")
            print("Semestre: 4to")
            print("Repositorio: https://github.com/usuario/IPC2_Proyecto1_201800956")

        elif opcion == "5":
            if not archivo_cargado:
                print("⚠️ Primero debe cargar un archivo.")
            else:
                print("📊 Generando gráfica con Graphviz (por implementar)...")

        elif opcion == "6":
            print("👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
