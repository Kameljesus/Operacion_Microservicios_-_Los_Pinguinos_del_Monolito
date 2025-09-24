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

            # Revisar si hubo error pero el usuario ya estaba registrado
            if "error" in data:
                print(f"❌ {data['error']}")
                print(f"Token actual del usuario: {data.get('token')}")
            else:
                print(f"✅ {data['success']}")
                print(f"Token generado: {data.get('token')}")

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
            headers={"Authorization": token}  # token en headers
        )

        # Verificamos si la respuesta fue exitosa
        if response.status_code == 200:
            print(f"{response.json()}")   # devolvemos el JSON (el menú)

        else:
            # Si tu API falla con un error que no devuelva JSON (por ejemplo un 500 que devuelve HTML de Flask), tu línea:
            try:
                error_data = response.json()
            except ValueError:
                error_data = response.text  # si no es JSON, devolvemos texto plano
            
            print(f"❌ Error {response.status_code}: {error_data}")
            sys.exit(1)

    except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API: {e}")
            sys.exit(1)