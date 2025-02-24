# Backup_Bat
    Este script (Version {version}) genera un archivo .bat que realiza una copia de seguridad de los archivos de guardado de un juego y los comprime en un archivo ZIP.

    Funcionamiento:
    1. Solicita al usuario las rutas de las carpetas de savegame (pueden ser varias).
    2. Solicita la ruta donde se guardará la copia de seguridad.
    3. Solicita el nombre del juego, que se usará para nombrar la carpeta de backup y el archivo .bat.
    4. Genera un archivo .bat que:
       - Crea una carpeta con el nombre del juego seguido de "_Backup".
       - Dentro de esa carpeta, genera un archivo ZIP con la fecha y hora actuales.
       - Comprime los archivos de guardado en el ZIP.
    5. Una vez generado el archivo .bat, muestra un mensaje de exito y espera a que el
       usuario presione una tecla para salir.
    6. Pulsa Ctrl+c para cancelar este proceso en cualquier punto.
