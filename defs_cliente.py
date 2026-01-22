import re
# re es un módulo de Python que sirve para trabajar con expresiones regulares (regex). Las expresiones regulares son patrones que te permiten buscar, validar o manipular texto de forma muy precisa.
import requests
import sys

def ingreso_nombre():
    while True:
        nombre = input("Por favor ingrese su nombre: ").strip()
        print()

        # Letras (mayúsculas/minúsculas), tildes, ñ y espacios.
        if re.fullmatch(r"[A-Za-zÁÉÍÓÚÜáéíóúüÑñ ]+", nombre):
            print(f"Bienvenido {nombre}")
            return nombre
        
        else:
            print("❌ Nombre inválido. Solo se permiten letras y espacios")



def ingreso_mail():
    while True:
        mail = input("Por favor ingrese su mail: ") #.not spaces ni antes de en medio
        print()

        if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", mail):
            print("Mail ingresado correctamente")
            print()
            return mail
        
        else:
            print("❌ Mail inválido. Ingrese su mail correctamente")
            print()



def ingreso_ubicacion():
    while True:
        ubicacion = input("Por favor, ingrese su ubicación para el pedido: ")
        print()

        if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ]+", ubicacion): # re.fullmatch(patrón, texto) verifica que todo el texto coincida con el patrón.
            print("Ubicación ingresada correctamente")
            print()
            return ubicacion
        else:
            print("❌ Ubicación inválida. Solo se permiten letras, números y espacios.")
            print()



def registrarse(nombre, mail, ubicacion):
    try:
        response = requests.post(
            "http://127.0.0.1:8001/registro",
            json={
                "nombre": nombre,
                "mail": mail,
                "ubicacion": ubicacion
            }
        )

        if response.status_code == 200:
            data = response.json()

            # Caso: error explícito desde la API
            if "error" in data:
                print(f"❌ {data['error']}")
                sys.exit(1)

            # Caso: el usuario ya estaba registrado
            elif "info" in data:
                token = data.get("token")
                if token:
                    print(f"Bienvenido de vuelta {nombre}")
                    print()
                    return token
                else:
                    print("❌ No se pudo recuperar el token. Saliendo.")
                    sys.exit(1)

            # Caso: registro exitoso
            elif "success" in data:
                token = data.get("token")
                if token:
                    print("✅ Se ha registrado exitosamente")
                    print()
                    return token
                else:
                    print("❌ Respuesta inválida del servidor (falta token).")
                    sys.exit(1)

            else:
                # Caso: respuesta inesperada
                print("❌ Respuesta desconocida del servidor.")
                sys.exit(1)

        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        sys.exit(1)



def obtener_menu(token):
    try:
        response = requests.get(
            "http://127.0.0.1:8002/menu",
            headers={"Authorization": f"Bearer {token}"}  # token en headers
        )

        # Verificamos si la respuesta fue exitosa
        if response.status_code == 200:
            data = response.json()
            menu = [trago.split(",")[0] for trago in data.get("menu", [])]  # extraemos solo los nombres

            # Recorremos la lista y mostramos uno por línea
            print("🍹 Menú disponible:")
            for trago in menu:
                print(trago)
            print()
            return menu  # devolvemos la lista de nombres para usar en la orden

        else:
            # Si hay error, mostramos mensaje amable
            print("❌ Ahora mismo, no contamos con esta opción.")
            print("Estamos trabajando para poder brindarle un servicio mejor. Muchas gracias.")

    except requests.exceptions.RequestException as e:
            # Error de conexión
            print("❌ Ahora mismo, no contamos con esta opción.")
            print("Estamos trabajando para poder brindarle un servicio mejor. Muchas gracias.")



def hacer_una_orden(nombre, mail, ubicacion, token):
    menu_disponible = obtener_menu(token)
    print()
    if not menu_disponible:
        return  # Si no hay menú, salimos

    pedido = []
    print("Ingrese los nombres de los tragos que desea pedir (máximo 15).")
    print("Escriba 'fin' para terminar su pedido.")

    while len(pedido) < 15:
        trago = input(f"Trago {len(pedido)+1}: ").strip()
        if trago.lower() == "fin":
            break
        elif trago not in menu_disponible:
            print()
            print("❌ Ese trago no está en el menú. Elija uno disponible.")
            print()
        elif trago in pedido:
            print()
            print("Trago repetido.")
            print('Puede elegir otro trago distinto o terminar su pedido con "fin"')
            print()
        else:
            pedido.append(trago)
    
    if not pedido:
        print("No se agregó ningún trago al pedido. Operación cancelada.")
        return

    # Mostrar el pedido antes de enviarlo
    print("Su pedido será:")
    for trago in pedido:
        print("-", trago)
    print()

    # Enviar la orden a la API
    try:
        response = requests.post(
            "http://127.0.0.1:8003/orden",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "nombre": nombre,
                "mail": mail,
                "ubicacion": ubicacion,
                "pedido": pedido
            }
        )

        if response.status_code == 200:
            print("✅ Pedido enviado correctamente:")
            print()
            
        else:
            print("❌ Ahora mismo, no contamos con esta opción.")
            print("Estamos trabajando para poder brindarle un servicio mejor. Muchas gracias.")

    except requests.exceptions.RequestException:
        print("❌ Ahora mismo, no contamos con esta opción.")
        print("Estamos trabajando para poder brindarle un servicio mejor. Muchas gracias.")