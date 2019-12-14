
# DICIONARIO
cat =  {
    "nombre": "Marie",
    "edad": 2,
    "raza": "Angora"
}

print(cat)
print(cat["edad"])

cat["owner"] = "Liz"

print(cat)


###########################################################################################

estudiantes = [
    {
        "nombre": "Luis",
        "edad": 22,
        "sexo": "M",
        "sh": ["Iron Man","Spider Man","Batman"]
    },
    {
        "nombre": "Liz",
        "edad": 22,
        "sexo": "F",
        "sh": ["Hulk","Spider Man","Chapulin colodado"]
    },
     {
        "nombre": "Marie",
        "edad": 22,
        "sexo": "F",
        "sh": ["Yo","Yo","Yo x3"]
    }
]

# Aqui trae solo la lista de la posicion 2
print(estudiantes[2])
# Aqui trae solo la lista de la posicion 2, y trae el objeto de la posicion
print(estudiantes[2]["nombre"])

print(estudiantes[0]["sh"][1])