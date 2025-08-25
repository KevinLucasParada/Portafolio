# condicionales.py

# Condicional simple
edad = 18
if edad >= 18:
    print("Eres mayor de edad")

# Condicional con else
nota = 5.5
if nota >= 4.0:
    print("Aprobado")
else:
    print("Reprobado")

# Condicional con elif
temperatura = 30

if temperatura < 10:
    print("Hace frío")
elif temperatura < 25:
    print("Clima agradable")
else:
    print("Hace calor")

# Condicional anidado
usuario = "admin"
conectado = True

if usuario == "admin":
    if conectado:
        print("Admin conectado")
    else:
        print("Admin no conectado")
else:
    print("Usuario desconocido")
