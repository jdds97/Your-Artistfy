# Your Artistfy
## Aplicación de Python que utiliza la API de Spotify para crear una lista de reproducción de los mejores éxitos de uno o más de tus artistas favoritos. 

# Requisitos previos:
## Instalación 
### Instalamos git en la terminal con git 

### Instalamos docker en el dispositivo 

### Creamos un usuario en github

Una vez tengamos instalado docker, git y creado el usuario en github haremos lo siguiente:

1.Abrimos una consola de comandos y creamos un directorio en el sistema operativo y desde la carpeta vacía que tienes abres un terminal o te vas en una terminal con $cd /rutadirectorio

2.Clonamos el repositorio de github con el comando $git clone https://github.com/jdds97/Your-Artistfy.git

3.Te pedirá tu usuario en github y tu contraseña

4.Procedemos con la creación de un contenedor en docker:

## Creación de contenedor en  Docker

1.Creamos la aplicación con la imagen estando en el directorio YourArtistfy directorio con el siguiente comando 
$docker build -t your-artistfy ./Your-Artistfy IMPORTANTE PONER EL PUNTO BARRA PARA QUE SE META EN EL DIRECTORIO DE ./Your-Artistfy  


2.Creamos un nuevo contenedor con la imagen que hemos creado anteriormente con el siguiente comando

$ docker run -it --name your-artistfy your-artistfy


# Y ya iniciará el programa :
1. Te preguntará:
Dime cómo quieres que se llame la playlist
Aquí tienes que poner el nombre por teclado 

2.Te volverá a preguntar lo siguiente:
¿Has terminado con tus artistas?
1.Si
2.No
Aquí tienes que contestar 1 si has terminado y 2 si ya has terminado con tu playlist

# Y ya tendrías tu lista de reproducción con tus artista/s favoritos!

# Funcionamiento del programa interno

1.Primero, se importan los módulos necesarios, como `json`, `base64` y `os`. También se importan los módulos `load_dotenv` y `post` y `get` de la biblioteca `requests`. 

2.Luego, se carga el archivo `.env` para obtener las credenciales de autenticación del cliente de Spotify. Estas credenciales se utilizan para obtener un token de acceso a la API de Spotify. 

3.La función `obtener_token()` se encarga de obtener el token de acceso. Para ello, se codifican las credenciales de autenticación en base64 y se envían en una solicitud POST a la API de Spotify. El token de acceso se devuelve como una cadena. 

4.La función `obtener_autentificacion_header()` se utiliza para crear un encabezado de autenticación que se utiliza en las solicitudes a la API de Spotify. 

5.La función `buscar_artista()` se utiliza para buscar un artista en la API de Spotify. Se envía una solicitud GET a la API de Spotify con el nombre del artista como parámetro de consulta. Si se encuentra un artista, se devuelve su ID. 

6.La función `obtenerTopTracksPorId()` se utiliza para obtener los mejores éxitos de un artista. Se envía una solicitud GET a la API de Spotify con el ID del artista como parámetro de consulta. Se devuelve una lista de las mejores canciones del artista. 

7.La función `crearListaCanciones()` se utiliza para crear una lista de reproducción de los mejores éxitos de un artista. Se llama a la función `buscar_artista()` para obtener el ID del artista y luego se llama a la función `obtenerTopTracksPorId()` para obtener los mejores éxitos del artista. 

8.La función `crearListaReproduccion()` se utiliza para crear una lista de reproducción de los mejores éxitos de varios artistas. Se llama a la función `obtenerTopTracksPorId()` para cada artista y se agrega a la lista de reproducción. 

9.Finalmente, se llama a la función `crearListaReproduccion()` para crear la lista de reproducción y se imprime en la consola.
