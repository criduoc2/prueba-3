import json
def agregar():
    with open("biblioteca.json",mode="r")as archivo:
        json.load(archivo)
        AutorID=input("ingresar id autor: ")
        nombre=input("ingresar nombre de autor:  ")
        autor= [{
            "id":AutorID,
           "nombre_aut":nombre    
        }]
        autor.append(AutorID)
        autor.append(nombre)


id =input("buscar id")
for i in id :
    print(id)