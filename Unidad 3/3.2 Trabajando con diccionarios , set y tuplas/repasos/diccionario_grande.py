# Creación de diccionario con muchos datos

diccionario = {
    "usuarios":[
        {
            "nombre":"victor",
            "edad":"20",
            "mascotas":["perro","gato","loro"],
            "perfil_salud":{
                "sangre":"rh positivo",
                "IMC":"gordito",
                "presion":"alta"
            }
        },
        {
            "nombre":"luciano",
            "edad":"24",
            "mascotas":["leon","elefante","zorro"],
            "perfil_salud":{
                "sangre":"rh negativo",
                "IMC":"flaquito",
                "presion":"baja"
            }

        },
        {
            "nombre":"felipe",
            "edad":"32",
             "mascotas":["raton","jabali","ornitorrinco"],
             "perfil_salud":{
                 "sangre":"otaku",
                "IMC":"normi",
                "presion":"maoma"
             }
        },
        {
            "nombre":"cesar",
            "edad":"29",
             "mascotas":["oso","ballena","rana"],
             "perfil_salud":{
                 "sangre":"otaku",
                "IMC":"morbido",
                "presion":"piola"
             }
        }
        
    ],
    "meta_datos": {
        "id":"12345",
        "fecha":"0234"
    }

    
}

# Filtrando el objeto para que solo traiga los datos de alguien llamado "victor"

for i in range(len(diccionario["usuarios"])):
    if diccionario["usuarios"][i]["nombre"].lower() == "victor":
        print(diccionario["usuarios"][i])