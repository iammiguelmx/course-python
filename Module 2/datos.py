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

# Iteracion de estudiantes 👀
for estudiante in estudiantes: 
    print("Name 👀: ", estudiante["nombre"])
    print("edad 👀: ", estudiante["edad"])
    if estudiante["sexo"] == 'F':
        print("Sexo mujer ")
    else:
         print("Sexo Men")
    print("Superhero")
    for sh in estudiante["sh"]:
        print(" - ", sh)
    print()

