# Your Artistfy
## Aplicación de Python que utiliza la API de Spotify para crear una lista de reproducción de los mejores éxitos de uno o más de tus artistas favoritos. 

# Despliegue

# Requisitos previos:
## Instalación 
### Instalamos git en la terminal 
### Creamos un usuario en github
### Instalamos python en nuestro sistema operativo y el paquete pip para instalar.
Si tienes instalado python en windows o en linux vete directamente al paso de creación entorno virtual

###Instalación de Python y pip en Windows:

Visita el sitio web oficial de Python en python.org.
Descarga la última versión estable de Python para Windows.
Ejecuta el instalador y asegúrate de marcar la opción "Add Python X.X to PATH" durante la instalación.
Verificar la Instalación:

Abre la línea de comandos (cmd) y escribe python --version para verificar que Python se ha instalado correctamente.
Luego, verifica que pip esté instalado usando pip --version.

### Instalación de Python y pip en Linux:
En la mayoría de las distribuciones de Linux, Python viene preinstalado. Sin embargo, si necesitas instalar pip, puedes hacerlo utilizando el administrador de paquetes de tu distribución. Por ejemplo, en Ubuntu y otras distribuciones basadas en Debian, puedes usar apt:
sudo apt update
sudo apt install python3 python3-pip
Para verificar la instalación, ejecuta:

python3 --version
pip3 --version


# Despliegue en entorno virtual 

1.Abrimos una consola de comandos y creamos un directorio en el sistema operativo y desde la carpeta vacía que tienes abres un terminal o te vas en una terminal con $cd /rutadirectorio

2.Clonamos el repositorio de github con el comando $git clone https://github.com/jdds97/Your-Artistfy.git

3.Te pedirá tu usuario en github y tu contraseña

4.Escribimos en la consola de comandos haciendo 
$cd Your-Artistfy

5.Escribimos el siguiente comando para crear un entorno virtual
$python3 -m venv entorno-virtual

6.Entonces para activar el entorno virtual que está en este directorio ponemos en la terminal estando en /Your-Artistfy 
$source entorno-virtual/bin/activate

7.Estará entonces el entorno virtual activado si nos sale (entorno-virtual) en la consola de comandos para instalar las dependencias que nos hacen falta y entonces pondremos en la consola de comandos:
$pip install -r requirements.txt  

8.A continuación ejecutaremos el archivo donde está el programa estando en el directorio /Your-Artistfy introduciremos el siguiente comando para ejecutar el código:
$python o python3 index.py 

9.Interacción con el programa

# Despliegue en docker 
### Instalamos docker en el dispositivo 
Una vez tengamos instalado docker haremos lo siguiente:

1.Abrimos una consola de comandos y creamos un directorio en el sistema operativo y desde la carpeta vacía que tienes abres un terminal o te vas en una terminal con $cd /rutadirectorio

2.Clonamos el repositorio de github con el comando $git clone https://github.com/jdds97/Your-Artistfy.git

3.Te pedirá tu usuario en github y tu contraseña

4.Procedemos con la creación de un contenedor en docker:

## Creación de contenedor en  Docker

1.Creamos la aplicación con la imagen estando en el directorio YourArtistfy directorio con el siguiente comando 
$docker build -t your-artistfy ./Your-Artistfy 
IMPORTANTE PONER EL PUNTO BARRA PARA QUE SE META EN EL DIRECTORIO DE ./Your-Artistfy  


2.Creamos un nuevo contenedor con la imagen que hemos creado anteriormente con el siguiente comando

$ docker run -it --name your-artistfy your-artistfy

3.Interacción con el programa
# Interacción con el programa 
1.Te preguntará:

<p>
Dime cómo quieres que se llame la playlist
Aquí tienes que poner el nombre por teclado 
</p>

2.Te volverá a preguntar lo siguiente:

<p>¿Has terminado con tus artistas?
1.Si
2.No

Aquí tienes que contestar 1 si has terminado y 2 si ya has terminado con tu playlist
</p>
Entonces se te abrirá en tu navegador la web de spotify con la playlist creada si eres spotify premium y si no lo eres la podrás seguir!
# Y ya tendrías tu lista de reproducción con tus artista/s favoritos!

# Funcionamiento del programa interno

1. El programa importa varios módulos de Python, incluyendo json, base64, webbrowser, os, dotenv, requests y spotipy.

2. La función 'obtener_token' se encarga de obtener un token de acceso a la API de Spotify. Este token se utiliza para realizar solicitudes a la API de Spotify.

3. La función 'buscar_artista' se encarga de buscar un artista en Spotify utilizando el nombre del artista proporcionado por el usuario.

4. La función 'obtener_top_tracks_por_id' se encarga de obtener las mejores canciones de un artista utilizando su ID.

5. La función 'crear_lista_canciones' se encarga de crear una lista de reproducción de un artista utilizando su nombre.

6. La función 'crear_lista_reproduccion' se encarga de crear una lista de reproducción de varios artistas utilizando la función 'crear_lista_canciones'.

7. La función 'main' se encarga de ejecutar el programa. Primero, obtiene un token de acceso a la API de Spotify utilizando la función 'obtener_token'.

8. Luego, utiliza la función 'crear_lista_reproduccion' para crear una lista de reproducción de varios artistas.

9.  Finalmente, imprime los elementos de la lista de reproducción y abre el enlace de la lista en un navegador web.


En resumen, este programa utiliza la API de Spotify para crear una lista de reproducción de los mejores éxitos de varios artistas.
