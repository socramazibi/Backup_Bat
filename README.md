# Backup_Bat
    Creado a partir ChatGPT, basado en el modelo GPT-4.
    
    Y luego no se cuantas horas mas preguntando y modificando para dejarlo mas o menos como quería.
    Es un simple script en python, que crea un archivo .bat que realiza copias de carpetas y las comprime en otra ruta.
    Yo el .bat generado lo pongo en el escritorio a los juegos que mas juego y cuando termino de jugar inicio el .bat
    para crear una copia del savegame. Puede hacer varias copias de diferentes carpetas.

    Ejemplo:
            origen=C:\Users\Nombre_Usuario\Documents\Egosoft\X4\99866623
            destino=D:\BACKUP-JUEGOS
            nombre del juego=X4Foundation

    Ejemplo:
            origen1=F:\SteamLibrary\steamapps\common\RisingWorld\Worlds
            origen2=F:\SteamLibrary\steamapps\common\RisingWorld\Blueprints
            destino=D:\BACKUP-JUEGOS
            nombre del juego=RisingWorld
            
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
    5. Una vez generado el archivo .bat, muestra un mensaje de exito y espera a que el
       usuario presione una tecla para salir.

    -He quitado todas las tildes del proyecto porque me daban error y ya me estaba poniendo nervioso.

- Generando el archivo


![imagen](https://github.com/user-attachments/assets/1e4676ac-797f-42dd-b422-7754b46b874c)

![imagen](https://github.com/user-attachments/assets/d09c8e11-3a4d-4a6c-b9a7-9094c33b9797)

![imagen](https://github.com/user-attachments/assets/47d527e2-3d58-4b53-9ae7-f6d8d0ada65a)

![imagen](https://github.com/user-attachments/assets/a1ea2985-41d0-4bbf-86d7-6484b905218f)

![imagen](https://github.com/user-attachments/assets/f1da930f-00e6-4a82-8650-0eecfb0bca20)




- Cuando ejecuto el .Bat

![imagen](https://github.com/user-attachments/assets/f89781b2-a2bb-4f2c-baff-ea25665faf4f)

![imagen](https://github.com/user-attachments/assets/8a3950bb-6026-403c-a6fd-52efb2fe1430)



    
