import json
import base64
import webbrowser
import os
from dotenv import load_dotenv
from requests import post, get
import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()


def obtener_token():
    """
    Función para obtener el TOKEN de acceso a Spotify para solamente crear la lista de spotify si el usuario es premium
    """
    cliente_id = os.getenv("CLIENTE_ID")
    cliente_secreto = os.getenv("CLIENTE_SECRETO")
    auth_string = f"{cliente_id}:{cliente_secreto}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    resultado = post(url, headers=headers, data=data, timeout=5)
    resultado_json = json.loads(resultado.content)
    token = resultado_json["access_token"]
    return token


def obtener_autentificacion_header(token):
    """
    Función para obtener el header de autenticación
    """
    return {"Authorization": "Bearer " + token}


def buscar_artista(token, nombre):
    """
    Función para buscar un artista en Spotify
    """
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": "Bearer " + token}
    parametros = f"?q={nombre}&type=artist&limit=1"
    parametros_url = url + parametros
    resultado = get(parametros_url, headers=headers, timeout=5)
    resultado_json = json.loads(resultado.content)["artists"]["items"]
    if len(resultado_json)>0:
        id_artista = resultado_json[0]['id']
        return id_artista
    print("No se encontró ningún artista con el nombre indicado.")
    return None


def obtener_top_tracks_por_id(token, id_artista):
    """
    Función para obtener las top tracks de un artista por su ID
    """
    top_tracks = f"https://api.spotify.com/v1/artists/{id_artista}/top-tracks?country=ES"
    headers = obtener_autentificacion_header(token)
    resultado = get(top_tracks, headers=headers, timeout=5)
    canciones = json.loads(resultado.content)["tracks"]
    lista_canciones = ""
    for num, cancion in enumerate(canciones):
        lista_canciones += f"{num+1} - {cancion['name']}\n"
    return lista_canciones, [track["uri"] for track in canciones]


def crear_lista_canciones(token, nombre_artista):
    """
    Función para crear una lista de reproducción de un artista
    """
    id_artista = buscar_artista(token, nombre_artista)
    lista_reproduccion = []
    lista_reproduccion.append(f"Lista de reproduccion de {nombre_artista}")
    lista_reproduccion.append(
        f"Top 10 Mejores éxitos de {nombre_artista}\n\n{obtener_top_tracks_por_id(token, id_artista)}"
    )
    return lista_reproduccion


def crear_lista_reproduccion(token):
    """
    Función para crear una lista de reproducción de varios artistas
    """
    scope = "playlist-modify-private playlist-modify-public"
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("CLIENTE_ID"),
            client_secret=os.getenv("CLIENTE_SECRETO"),
            redirect_uri="http://localhost:8888/callback",
            scope=scope,
            open_browser=True,
        )
    )
    listas_reproduccion = []
    encabezado = input("Dime cómo quieres que se llame la playlist\n")
    listas_reproduccion.insert(0, encabezado)
    uri_canciones_total = []
    salir = False
    while not salir:
        nombre_artista = input("Dime el nombre de tu artista\n")
        lista_reproduccion, uri_canciones = obtener_top_tracks_por_id(
            token, buscar_artista(token, nombre_artista)
        )
        listas_reproduccion.append(
            f"Top 10 Mejores éxitos de {nombre_artista}\n\n{lista_reproduccion}"
        )
        uri_canciones_total.extend(uri_canciones)
        final = input(
            "¿Has terminado con tus artistas?" + "\n" + "1.Si\n" + "2.No\n"
        ).lower()
        salir = bool(final == "si")
    playlist = sp.user_playlist_create(user=sp.me()['id'], name=encabezado, public=True)
    sp.playlist_add_items(playlist_id=playlist["id"], items=uri_canciones_total)
    return listas_reproduccion, playlist['uri']


def main():
    """
    Esta función obtiene un token de Spotify, crea una lista de reproducción, imprime los elementos de la lista y abre el enlace de la lista en un navegador web.
    """
    TOKEN = obtener_token()
    lista_reproduccion, uri_lista = crear_lista_reproduccion(TOKEN)
    for lista in lista_reproduccion:
        print(lista)
    playlist_link = f"https://open.spotify.com{uri_lista.replace('spotify:playlist:', '/playlist/')}"
    webbrowser.open(playlist_link)

#Se utiliza para ejecutar la funcion main cuando el archivo index.py es el archivo principal a ejecutar
if __name__ == "__main__":
    main()
