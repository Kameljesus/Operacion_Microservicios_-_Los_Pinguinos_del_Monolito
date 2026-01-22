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
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token no proporcionado"}), 401

    if token.startswith("Bearer "):
        token = token[len("Bearer "):]

    try:
        # -----------------------------
        # Obtener tragos de la DB
        # -----------------------------
        menu.cursor.execute("SELECT nombre, available FROM tragos")
        tragos = menu.cursor.fetchall()

        # -----------------------------
        # Formatear la respuesta
        # -----------------------------
        # Filtrar solo los disponibles
        menu_disponible = [
            nombre for nombre, available in tragos if available == 1
        ]

        # Log de éxito
        logs.crear_log("menu_service", "menu", "INFO", "Cliente solicitó el menú")
        logs.cargar_log_a_db()

        return jsonify({"menu": menu_disponible}), 200

    except Exception as e:
        print(f"🔥 Error interno: {e}")  # <-- debug en consola
        logs.crear_log("menu_service", "menu", "ERROR", f"Error al obtener el menú: {e}")
        logs.cargar_log_a_db()
        return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8002, debug=True)