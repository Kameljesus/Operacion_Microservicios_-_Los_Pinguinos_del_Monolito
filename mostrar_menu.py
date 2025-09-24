from flask import Flask, request, jsonify
from menu_db import menu
from logs_db import logs
from tokens import validar_token  # Función para validar tokens

# Crear la app de Flask
app = Flask(__name__)

# ----------------------------------
# Ruta GET para recibir datos JSON
# ----------------------------------
@app.route("/menu", methods=["GET"])
def get_menu():
    # -----------------------------
    # Validamos token desde headers
    # -----------------------------
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token no proporcionado"}), 401

    try:
        validar_token(token)  # Si no es válido, lanza ValueError
    except ValueError as e:
        return jsonify({"error": str(e)}), 401

    try:
        # -----------------------------
        # Obtener tragos de la DB
        # -----------------------------
        menu.cursor.execute("SELECT nombre, available FROM tragos")
        tragos = menu.cursor.fetchall()

        # -----------------------------
        # Formatear la respuesta
        # -----------------------------
        menu_disponible = []
        for nombre, available in tragos:
            estado = "Available" if available == 1 else "Not Available"
            menu_disponible.append(f"{nombre}, Available: {estado}")

        # -----------------------------
        # Crear log del evento
        # -----------------------------
        logs.crear_log(
            autor="menu_service",
            service="menu",
            severity="INFO",
            mensaje="Cliente solicitó el menú"
        )
        logs.cargar_log_a_db()

        return jsonify({"menu": menu_disponible})

    except Exception as e:
        # -----------------------------
        # Si ocurre un error, loguearlo y devolver HTTP 500
        # -----------------------------
        logs.crear_log(
            autor="menu_service",
            service="menu",
            severity="ERROR",
            mensaje=f"Error al obtener el menú: {e}"
        )
        logs.cargar_log_a_db()
        return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8002, debug=True)