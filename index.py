import json
import base64
import os
#Módulo para importar variables de entorno
from dotenv import load_dotenv
#Módulo para importar preguntas a un servidor
from requests import post,get

load_dotenv()

cliente_id = os.getenv("CLIENTE_ID")
cliente_secreto = os.getenv("CLIENTE_SECRETO")

#Función para obtener el token para que nos de acceso a spotify 
def obtener_token():
    auth_string = f"{cliente_id}:{cliente_secreto}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")


    url = "https://accounts.spotify.com/api/token"
    headers = {
    "Authorization": "Basic " + auth_base64,
    "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    resultado = post(url, headers=headers, data=data)
    resultado_json = json.loads(resultado.content)
    token = resultado_json["access_token"]
    return token

token=obtener_token()
print(token)

def obtener_autentificacion_header(token):
    return {"Authorization": "Bearer " + token}





def buscar_artista(token,nombre):
    url = "https://api.spotify.com/v1/search"
    headers = obtener_autentificacion_header(token)
    parametros = f"?q={nombre}&type=artist&limit=1"
    parametros_url = url + parametros
    resultado = get(parametros_url, headers=headers)
    resultado_json = json.loads(resultado.content)["artists"]["items"][0]["id"]
    if len(resultado_json)==0:
        print("No existe ningún artista con el nombre indicado ")
        return None
    return resultado_json




def obtenerTopTracksPorId(token,id_artista):
    top_Tracks = f"https://api.spotify.com/v1/artists/{id_artista}/top-tracks?country=ES"
    headers = obtener_autentificacion_header(token)
    resultado = get(top_Tracks, headers=headers)
    canciones = json.loads(resultado.content)["tracks"]
    listaCanciones=""
    for num,cancion in enumerate(canciones):
        listaCanciones+=f"{num+1} - {cancion['name']}\n"
    return listaCanciones



def crearListaReproducción(token):
    salir = False
    
    while not salir:
        listaReproduccion = ""
        nombre_artista = input("Dime el nombre de tus artista\n")
            
        listaReproduccion +=f"Top 10 Mejores éxitos de {nombre_artista}\n\n{obtenerTopTracksPorId(token,id_artista=buscar_artista(token,nombre_artista))}"
            
        salir = input("¿Has terminado con tus artistas?" + "\n" + "1.Si " +"\n" "2.No\n").lower
        if salir == "si" or salir == "1":
            salir == True
        else:
            salir == False
    
    return listaReproduccion




print(crearListaReproducción(token))

'''
PAÍS=input("Si quieres dime de qué país quieres")

if PAÍS ==" " or ==
urlPaís=f"https://restcountries.com/v3.1/name/{PAÍS}"

with open(urlPaís, "w") as j:
    fichero = json.load(j)


for INFO_PAÍS in fichero:
    print(INFO_PAÍS[''])
'''