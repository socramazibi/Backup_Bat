import os
import unidecode  # Librería para eliminar tildes

# Funcion para mostrar una explicacion del funcionamiento del script
def mostrar_explicacion(version):
    print(f"""
    Este script (Version {version}) genera un archivo .bat que realiza una copia de seguridad de los archivos 
    de guardado de un juego y los comprime en un archivo ZIP.

    Funcionamiento:
    1. Solicita al usuario las rutas de las carpetas de savegame (pueden ser varias).
    2. Solicita la ruta donde se guardará la copia de seguridad.
    3. Solicita el nombre del juego, que se usará para nombrar la carpeta de backup y el archivo .bat.
    4. Genera un archivo .bat que:
       - Crea una carpeta con el nombre del juego seguido de "_Backup".
       - Dentro de esa carpeta, genera un archivo ZIP con la fecha y hora actuales.
       - Comprime los archivos de guardado en el ZIP.
    5. Una vez generado el archivo .bat, muestra un mensaje de éxito y espera a que el
       usuario presione una tecla para salir.
    6. Pulsa Ctrl+C para cancelar este proceso en cualquier punto.
    """)
    input("Presiona Enter para continuar...")

# Función para quitar tildes de un texto
def quitar_tildes(texto):
    return unidecode.unidecode(texto)

def crear_script_backup():
    version = "1.1.0"
    
    mostrar_explicacion(version)
    
    rutas_origen = []
    while True:
        origen = input("Ingresa la ruta del savegame (o deja vacío para finalizar): ").strip()
        if not origen:
            break
        rutas_origen.append(origen)
    
    if not rutas_origen:
        print("ERROR: No se ingresaron rutas de savegame. El archivo .bat no será creado.")
        input("Presiona Enter para salir...")
        return
    
    destino = input("Ingresa la ruta de destino del backup: ").strip()
    if not destino:
        print("ERROR: No se ingresó una ruta de destino. El archivo .bat no será creado.")
        input("Presiona Enter para salir...")
        return
    
    nombre_juego = input("Ingresa el nombre del juego: ").strip()
    if not nombre_juego:
        print("ERROR: No se ingresó el nombre del juego. El archivo .bat no será creado.")
        input("Presiona Enter para salir...")
        return
    
    # Limpiar texto
    nombre_juego = quitar_tildes(nombre_juego)
    destino = quitar_tildes(destino)

    nombre_archivo = f"{nombre_juego}_Backup_v{version}.bat"

    with open(nombre_archivo, "w", encoding="utf-8") as bat:
        bat.write(f"REM Version del script: {version}\n\n")
        bat.write("@echo off\n")
        bat.write("setlocal enabledelayedexpansion\n\n")
        bat.write(f'set "destino={destino}\\{nombre_juego}_Backup"\n')
        bat.write("mkdir \"!destino!\" 2>nul\n\n")
        
        bat.write("REM Obtener fecha y hora en formato DD-MM-YYYY_HH-MM-SS\n")
        bat.write("for /f \"tokens=2 delims==\" %%I in ('wmic os get localdatetime /value') do set fechaHora=%%I\n")
        bat.write("set \"fechaHora=!fechaHora:~6,2!-!fechaHora:~4,2!-!fechaHora:~0,4!_!fechaHora:~8,2!-!fechaHora:~10,2!-!fechaHora:~12,2!\"\n\n")
        
        bat.write("set \"archivoZIP=!destino!\\Backup_!fechaHora!.zip\"\n\n")

        for i, origen in enumerate(rutas_origen, 1):
            origen = quitar_tildes(origen)
            bat.write(f'set "origen{i}={origen}"\n')
        
        bat.write("\n")
        for i in range(1, len(rutas_origen) + 1):
            bat.write(f'if not exist "!origen{i}!" (\n')
            bat.write(f'    echo ERROR: La carpeta de origen {i} "!origen{i}!" no existe.\n')
            bat.write("    pause\n")
            bat.write("    exit /b\n")
            bat.write(")\n\n")
        
        bat.write("echo.\n")
        bat.write("echo Creando copia de seguridad en ZIP: \"!archivoZIP!\"...\n")
        bat.write("echo.\n")

        # Usar PowerShell con rutas entre comillas simples para evitar errores por espacios
        bat.write("powershell -NoProfile -Command \"Compress-Archive -Path ")
        bat.write(",".join([f"'!origen{i}!'" for i in range(1, len(rutas_origen)+1)]))
        bat.write(" -DestinationPath '!archivoZIP!' -Force\"\n\n")
        
        bat.write("if %errorlevel% equ 0 (\n")
        bat.write("    echo.\n")
        bat.write("    echo Copia de seguridad creada con éxito en \"!archivoZIP!\"\n")
        bat.write("    echo.\n")
        bat.write(") else (\n")
        bat.write("    echo.\n")
        bat.write("    echo ERROR: No se pudo completar la copia de seguridad.\n")
        bat.write("    echo.\n")
        bat.write(")\n\n")
        bat.write("pause\n")

    print(f"\n✅ Archivo '{nombre_archivo}' creado con éxito.")
    input("Presiona Enter para salir...")

if __name__ == "__main__":
    crear_script_backup()
