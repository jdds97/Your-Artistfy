import json
import base64
import os
from dotenv import load_dotenv
from requests import post,get

load_dotenv()

cliente_id = os.getenv("CLIENTE_ID")
cliente_secreto = os.getenv("CLIENTE_SECRETO")

print(cliente_id, cliente_secreto)


def obtener_token():
    auth_string = f"{cliente_id}:{cliente_secreto}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic" + auth_base64,
        "Content-Type ": "application/x-www-form-urlencoded",
    }
    data = {"grant-type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Autorizathion": "Bearer" + token}

nombre="ACDC"
def buscar_artista(nombre):
    token = get_token()
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    parametros = {"q": nombre, "type": "artist", "limit": 1}
    parametros_url = url + parametros
    resultado = get(parametros_url, headers=headers)
    resultado_json = json.loads(resultado.content)
    print(resultado_json)

    """
    if name == resultado_json:
        
        return id_artista
    """


token = get_token()

'''
def obtenerTopTracksPorId(id_artista):
    topTracks = f"https://api.spotify.com/v1/artists/{id_artista}/top-tracks"
    headers = get_auth_header(token)
    parametros = {"market": "ES"}
    result = post(topTracks, headers=headers, data=parametros)
    json_result = json.loads(result.content)
    return json_result["tracks"]


def crearListaReproducción():
    salir = False
    while salir == False:
        listaReproduccion = ""
        nombre_artista = input("Dime el nombre de tus artista")
        listaReproduccion += obtenerTopTracksPorId(
            id_artista=buscar_artista(nombre_artista)
        )
        salir = input("¿Has terminado con tus artistas?" + "\n" + "1.Si" + "2.No").lower
        if salir == "si" or salir == "1":
            salir == True
        else:
            artistas_favoritos += [nombre_artista]
    return listaReproduccion


listaReproduccion = crearListaReproducción()

print(listaReproduccion)

"""'





PAÍS=input("Si quieres dime de qué país quieres")
if PAÍS ==" " or ==
urlPaís=f"https://restcountries.com/v3.1/name/{PAÍS}"

with open(urlPaís, "w") as j:
    fichero = json.load(j)


for INFO_PAÍS in fichero:
    print(INFO_PAÍS[''])
"""
'''