# YourArtistfy
## Aplicación de Python que utiliza la API de Spotify para crear una lista de reproducción de los mejores éxitos de uno o más de tus artistas favoritos. 

1.Primero, se importan los módulos necesarios, como `json`, `base64` y `os`. También se importan los módulos `load_dotenv` y `post` y `get` de la biblioteca `requests`. 

2.Luego, se carga el archivo `.env` para obtener las credenciales de autenticación del cliente de Spotify. Estas credenciales se utilizan para obtener un token de acceso a la API de Spotify. 

3.La función `obtener_token()` se encarga de obtener el token de acceso. Para ello, se codifican las credenciales de autenticación en base64 y se envían en una solicitud POST a la API de Spotify. El token de acceso se devuelve como una cadena. 

4.La función `obtener_autentificacion_header()` se utiliza para crear un encabezado de autenticación que se utiliza en las solicitudes a la API de Spotify. 

5.La función `buscar_artista()` se utiliza para buscar un artista en la API de Spotify. Se envía una solicitud GET a la API de Spotify con el nombre del artista como parámetro de consulta. Si se encuentra un artista, se devuelve su ID. 

6.La función `obtenerTopTracksPorId()` se utiliza para obtener los mejores éxitos de un artista. Se envía una solicitud GET a la API de Spotify con el ID del artista como parámetro de consulta. Se devuelve una lista de las mejores canciones del artista. 

7.La función `crearListaCanciones()` se utiliza para crear una lista de reproducción de los mejores éxitos de un artista. Se llama a la función `buscar_artista()` para obtener el ID del artista y luego se llama a la función `obtenerTopTracksPorId()` para obtener los mejores éxitos del artista. 

8.La función `crearListaReproduccion()` se utiliza para crear una lista de reproducción de los mejores éxitos de varios artistas. Se llama a la función `obtenerTopTracksPorId()` para cada artista y se agrega a la lista de reproducción. 

9.Finalmente, se llama a la función `crearListaReproduccion()` para crear la lista de reproducción y se imprime en la consola.

# Crear contenedor en  Docker

## Crea la aplicación con la imagen estando en este mismo directorio con el siguiente comando 
$docker build --tag artistfy . IMPORTANTE PONER EL PUNTO!


## Nuevo contenedor con la imagen de python

$docker run artistfy

## Ejecuta el contenedor con la imagen de python

$docker exec -it artistfy bash


# Desarrollo en VS Code

## Instala las Extensiones de VS Code*:

1.Instala la extensión "Remote - Containers" de Visual Studio Code. Esta extensión permite abrir cualquier carpeta o proyecto en un contenedor, incluyendo tu proyecto Python en un contenedor Docker.

2.Instala la extensión "Python" de Microsoft para obtener soporte completo de Python en VS Code.

## Abre tu Proyecto en VS Code:
1.Abre VS Code y abre la carpeta de tu proyecto Python en el editor.

2.En la raíz de tu proyecto, crea un directorio llamado .devcontainer.

3.Dentro de .devcontainer, crea un archivo llamado devcontainer.json y configúralo para usar la imagen de Docker y las configuraciones del contenedor.

4.Configura el Archivo .devcontainer/devcontainer.json
