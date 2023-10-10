from marvel import Marvel
import openai
openai.api_key="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"
marvel = Marvel(PUBLIC_KEY="6c6852c85207adba9e725a4d7e5de26e", PRIVATE_KEY="ed1eb9958e767573a19ff94480cd0cb8c55b6ea9")

personajes = marvel.characters
''''
todosPersonajes = personajes.all(name=nombre_personaje_favorito)
class Equipo ():
    def nombre():
        for personaje in todosPersonajes:
            if nombre_personaje_favorito==personaje["id"]["name"]:
                equipo.append(personaje)



'''

nombre_personaje_favorito = input("Dime tu nombre de personaje favorito: ")
nombreProtagonista=input("Ahora dime tu nombre ")
pregunta=openai.Completion.create(engine="text-davinci-003",prompt="Creame una historia de batalla con el "+str(nombreProtagonista),max_tokens=2048)
print(pregunta.choices[0].text)
image_resp = openai.Image.create(prompt="Resultado de la batalla ", n=4, size="512x512")
'''
aparicionesPersonaje()
        if personajes
        print(f"El nombre del personaje es {personaje['name']} y aparece en la serie {personaje['series
'''