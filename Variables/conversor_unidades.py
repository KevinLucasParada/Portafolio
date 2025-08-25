# conversor_unidades.py

def convertir_unidades(valor, unidad_origen, unidad_destino):
    # Todas las unidades se convierten primero a metros
    factores = {
        'km': 1000,
        'm': 1,
        'mi': 1609.34  # 1 milla ≈ 1609.34 metros
    }

    if unidad_origen not in factores or unidad_destino not in factores:
        return None

    # Convertimos a metros y luego a la unidad deseada
    valor_metros = valor * factores[unidad_origen]
    resultado = valor_metros / factores[unidad_destino]
    return resultado

print("Conversor de unidades: km, m, mi")
valor = float(input("Ingrese el valor a convertir: "))
origen = input("Unidad de origen (km/m/mi): ").lower()
destino = input("Unidad de destino (km/m/mi): ").lower()

resultado = convertir_unidades(valor, origen, destino)

if resultado is not None:
    print(f"{valor} {origen} = {resultado:.2f} {destino}")
else:
    print("Unidades inválidas.")
