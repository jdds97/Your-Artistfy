from marvel import Marvel

marvel = Marvel(PUBLIC_KEY="6c6852c85207adba9e725a4d7e5de26e", PRIVATE_KEY="ed1eb9958e767573a19ff94480cd0cb8c55b6ea9")

personajes = marvel.characters
nombre_personaje_favorito = input("Dime tu nombre de personaje favorito: ")

todosPersonajes = personajes.all(name=nombre_personaje_favorito)

def aparicionesPersonajeComic():
    for personaje in todosPersonajes:
        if nombre_personaje_favorito==personaje["id"]["name"]:
            print(f"El nombre del personaje es {personaje['name']} y aparece en la serie {personaje['series'][0]['name']}")

aparicionesPersonaje()
        if personajes
        print(f"El nombre del personaje es {personaje['name']} y aparece en la serie {personaje['series