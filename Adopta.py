Afirmacion = True
print("Bienvenido al centro de adopción de mascotas")
print("Por favor, responde las siguientes preguntas para encontrar la mascota ideal para ti.")

Lista =("""
|----------------------------------------------------|
|                                                    |
|              Adopta tu compañero de vida           |
|                                                    |
|----------------------------------------------------|
|                                                    |
|              1. ¿Qué estás buscando?               |
|              2. ¿Qué mascotas tenemos para ti?     |
|              3. ¿Adoptarías esta mascota?          |
|              4. Salir                              |
|                                                    |
|----------------------------------------------------|
""")


mascotas = [
    {"nombre": "Luna", "especie": "perro", "edad": 3, "energia": "alta", "niños": "sí"},
    {"nombre": "Milo", "especie": "gato", "edad": 5, "energia": "media", "niños": "no"},
    {"nombre": "Bella", "especie": "conejo", "edad": 2, "energia": "baja", "niños": "sí"},
    {"nombre": "Rocky", "especie": "perro", "edad": 6, "energia": "media", "niños": "sí"},
    {"nombre": "Simba", "especie": "gato", "edad": 1, "energia": "alta", "niños": "sí"},
    {"nombre": "Nube", "especie": "conejo", "edad": 4, "energia": "baja", "niños": "no"},
    {"nombre": "Max", "especie": "perro", "edad": 2, "energia": "alta", "niños": "sí"},
    {"nombre": "Lola", "especie": "gato", "edad": 3, "energia": "media", "niños": "sí"},
    {"nombre": "Coco", "especie": "conejo", "edad": 5, "energia": "baja", "niños": "sí"},
    {"nombre": "Toby", "especie": "perro", "edad": 4, "energia": "media", "niños": "no"},
    {"nombre": "Mimi", "especie": "gato", "edad": 2, "energia": "alta", "niños": "sí"},
    {"nombre": "Pipo", "especie": "conejo", "edad": 1, "energia": "baja", "niños": "no"},
]


preferencias = []
resultado = []

def obtener_preferencias():
    especie = input("¿Prefieres perro, gato o conejo?: ")
    edad = int(input("¿Qué edad te gustaría que tuviera?: "))
    energia = input("¿Quieres que sea de energía alta, media o baja?: ")
    niños = input("¿Tienes niños en casa? (sí/no): ")
    preferencias.clear()
    preferencias.extend([especie, edad, energia, niños])

def filtrar_mascotas():
    global resultado
    resultado = []
    especie, edad, energia, niños = preferencias
    for mascota in mascotas:
        if mascota["especie"] == especie and mascota["edad"] == edad and mascota["energia"] == energia and mascota["niños"] == niños:
            resultado.append(mascota)

def mostrar_mascotas():
    global Afirmacion
    if not resultado:
        print("No se encontraron mascotas compatibles con tus preferencias.")
    else:
        mascota = resultado[0]
        print("Nombre:", mascota["nombre"])
        print("Especie:", mascota["especie"])
        print("Edad:", mascota["edad"])
        print("Energía:", mascota["energia"])
        print("Compatible con niños:", mascota["niños"])
        opcion = input("¿Te gustaría adoptar esta mascota? (si/no/salir): ")
        if opcion == "si":
            print("¡Felicidades! Adoptaste a", mascota["nombre"])
        elif opcion == "salir":
            print("Has decidido salir del programa.")
            Afirmacion = False
        else:
            print("Seguir buscando...")

while Afirmacion:
    print(Lista)
    opt = input("Seleccione una opción: ")
    
    if opt == "1":
        obtener_preferencias()
    
    elif opt == "2":
        filtrar_mascotas()
        mostrar_mascotas()
    
    elif opt == "3":
        mostrar_mascotas()
    
    elif opt == "4":
        print("Gracias por visitarnos")
        print("¡Esperamos que encuentres a tu compañero ideal pronto!")
        print("Hasta pronto")
        Afirmacion = False  
    
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")



