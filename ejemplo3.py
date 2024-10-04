

"""

- os.listdir():Devuelve una lista con los nombres de los archivos y carpetas en el directorio especificado. Si no se proporciona un argumento, se usará el directorio actual.
Ejemplo: os.listdir(".") te devolverá los archivos en el directorio actual.

- os.getcwd():Retorna una cadena que representa el directorio de trabajo actual (Current Working Directory).
Ejemplo: os.getcwd() devuelve el directorio en el que se está ejecutando el script.

- os.mkdir():Crea un nuevo directorio con el nombre que se le pase como argumento.
Ejemplo: os.mkdir("nueva_carpeta") creará una carpeta llamada "nueva_carpeta" en el directorio actual.

- os.path.exists():Devuelve True si la ruta especificada (archivo o directorio) existe, de lo contrario devuelve False.
Ejemplo: os.path.exists("archivo.txt") te dirá si "archivo.txt" existe en el sistema.

- os.rename():Renombra un archivo o directorio. Recibe dos argumentos: el nombre actual y el nuevo nombre.
Ejemplo: os.rename("archivo.txt", "nuevo_nombre.txt") renombrará "archivo.txt" a "nuevo_nombre.txt".

- os.remove():Elimina (borra) un archivo. No se puede usar para eliminar directorios.
Ejemplo: os.remove("archivo.txt") eliminará el archivo "archivo.txt".

- os.rmdir():Elimina un directorio vacío. Si el directorio no está vacío, lanzará un error.
Ejemplo: os.rmdir("carpeta_vacia") eliminará la carpeta si no tiene contenido.

- os.system():Ejecuta un comando del sistema operativo desde un programa en Python. El comando debe pasarse como una cadena.
Ejemplo: os.system("ls") (en Linux/macOS) o os.system("dir") (en Windows) listará los archivos del directorio actual.

- os.name:Devuelve una cadena que indica el nombre del sistema operativo en el que se está ejecutando Python. Normalmente será 'posix' para sistemas Unix-like (Linux, macOS) o 'nt' para Windows.
Ejemplo: os.name devolverá 'nt' en Windows o 'posix' en sistemas basados en Unix.
"""
