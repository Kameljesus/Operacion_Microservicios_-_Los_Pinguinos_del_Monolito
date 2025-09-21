# -----------------------------
# Este script representa al CLIENTE que quiere hacer un pedido de tragos
# Se conecta al servidor FastAPI en http://127.0.0.1:8000/order
# -----------------------------

import requests  # Librería para hacer requests HTTP a la API

# -----------------------------
# Token de autenticación del cliente
# (debe existir en tokens.py en el servidor)
# -----------------------------
TOKEN = "TOKEN_SUPER_SECRETO_1"  

# -----------------------------
# Pedido del cliente
# Es un diccionario con la lista de tragos
# -----------------------------
pedido = {
    "tragos": ["Mojito", "Caipirinha", "Daiquiri"]
}

# -----------------------------
# Hacemos el POST al endpoint /order
# -----------------------------
try:
    response = requests.post(
        "http://127.0.0.1:8000/order",   # Endpoint del servidor FastAPI
        json=pedido,                     # El pedido en formato JSON
        headers={"Authorization": f"Token {TOKEN}"}  # Token en el header
    )

    # -----------------------------
    # Mostramos la respuesta del servidor
    # -----------------------------
    if response.status_code == 200:
        print("✅ Pedido enviado con éxito!")
        print("Respuesta del servidor:", response.json())
    else:
        print(f"❌ Error {response.status_code}: {response.json()}")

except Exception as e:
    print("Error al conectarse al servidor:", e)