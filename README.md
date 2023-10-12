# Proyecto Python
 Proyecto creado para crear tu propia playlist de Spotify según tus artistas favoritos.
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
