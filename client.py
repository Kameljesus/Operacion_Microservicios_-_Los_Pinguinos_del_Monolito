from defs_cliente import ingreso_nombre, ingreso_mail, ingreso_ubicacion, registrarse, obtener_menu

# ------------------------------------
# Obtención de datos para el ingreso:
# ------------------------------------

nombre = ingreso_nombre()
mail = ingreso_mail()
ubicacion = ingreso_ubicacion()

registrarse(nombre, mail, ubicacion)

obtener_menu()