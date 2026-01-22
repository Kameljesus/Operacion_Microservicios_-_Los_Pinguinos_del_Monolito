from defs_cliente import ingreso_nombre, ingreso_mail, ingreso_ubicacion, registrarse, obtener_menu, hacer_una_orden

# ------------------------------------
# Obtención de datos para el ingreso:
# ------------------------------------

nombre = ingreso_nombre()
mail = ingreso_mail()
ubicacion = ingreso_ubicacion()

token = registrarse(nombre, mail, ubicacion)  # guardamos el token
print("Bienvenido a Shake It!:")
print()

def ciclo_de_apis(token):
    while True:
        print("Para pedir el menú disponible, presione: 1")
        print("Para hacer una orden, presione: 2")
        print('Para salir, escriba "salir"')
        print()
        pregunta = (input("Qué desea hacer?: "))
        print()

        if pregunta == "1":
            obtener_menu(token)  # ahora pasamos el token
        
        elif pregunta == "2":
            hacer_una_orden(nombre, mail, ubicacion, token)

        elif pregunta == "salir":
            print("Muchas gracias, lo esperamos de vuelta.")
            break

        else:
            print("Respuesta no válida:")
            print("Disculpe, no lo he entendido.")
            print()


ciclo_de_apis(token)