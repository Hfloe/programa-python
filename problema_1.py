# Matriz de datos
# Formato: [ID Cliente, Duración, Clics]

sesiones = [
    ["C001", 250, 12],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 300, 15],
    ["C005", 80, 1]
]

# Función para clasificar el compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Mostrar informe final
print("INFORME DE COMPROMISO DE CLIENTES")
print("---------------------------------")

for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente)
    print("Clasificación:", clasificacion)
    print("----------------------------")