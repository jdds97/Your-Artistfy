import json
import os
import base64
from requests import post




client_id = "2672e0ae0aa5490790c100b875539755"
client_secret ="4f963dea4f53423abc1d4dc1ada3a108"

print(client_id,client_secret)

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes=auth_string.encode("utf-8")
    auth_base64=str(base64.b64encode(auth_bytes),"utf-8")
    
    url="https://accounts.spotify.com/api/token"
    headers={
        "Authorization" :"Basic" +auth_base64,
        "Content-Type ":"application/x-www-form-urlencoded"
    }
    data={"grant_type" : "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result=json.loads(result.content)
    token=json_result["access_token"]
    return token

token=get_token()
print(token)
def get_auth_header(token):
    return{"Autorizathion" :"Bearer" +token}

def buscar_artista(nombre):
    url="https://api.spotify.com/v1/search"
    headers=get_auth_header(token)
    parametros={
        "q":nombre,
        "type":"artist",
        "limit":1
    }
    if name == resultado_json:
        
        return id_artista

def obtenerTopTracksPorId(id_artista):    
    topTracks=f"https://api.spotify.com/v1/artists/{id_artista}/top-tracks"
    headers=get_auth_header(token)
    parametros={
        "market":"ES"
    }
    result = post(topTracks, headers=headers, data=parametros)
    json_result=json.loads(result.content)
    return json_result["tracks"]
salir=False

def crearListaReproducción(){
while salir==False:
    nombre_artista=input("Dime el nombre de tus artista")
    listaReproduccion+=obtenerTopTracksPorId(id_artista=buscar_artista(nombre_artista))
    salir=input("¿Has terminado con tus artistas?"+"\n"+"1.Si"+"2.No").lower
    if salir=="si" or salir=="1":
        salir==True
    else:
        artistas_favoritos+=[nombre_artista]
    return listaReproduccion
}
    
print(listaReproduccion)

''''





PAÍS=input("Si quieres dime de qué país quieres")
if PAÍS ==" " or ==
urlPaís=f"https://restcountries.com/v3.1/name/{PAÍS}"

with open(urlPaís, "w") as j:
    fichero = json.load(j)


for INFO_PAÍS in fichero:
    print(INFO_PAÍS[''])
'''