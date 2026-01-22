from flask import Flask, request, jsonify
from pedidos_db import pedidos
from logs_db import logs
from tokens import validar_token
from datetime import datetime
import json

# Crear la app de Flask
app = Flask(__name__)

# ----------------------------------
# Ruta POST para recibir datos JSON
# ----------------------------------
@app.route("/orden", methods=["POST"])
def orden():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token no proporcionado"}), 401

    if token.startswith("Bearer "):
        token = token[len("Bearer "):]

    try:
        validar_token(token)  # Si falla, lanza ValueError
    except ValueError:
        return jsonify({"error": "Token inválido"}), 401
    
    # Obtenemos los datos enviados por el cliente en formato JSON
    data = request.get_json()

    # Validación básica
    if not data:
        return jsonify({"error": "No se envió JSON"}), 400

    if "nombre" not in data or "mail" not in data or "ubicacion" not in data or "pedido" not in data:
        logs.crear_log("pedido_service", "orden", "ERROR", "Información incompleta del cliente")
        logs.cargar_log_a_db()
        return jsonify({"error": "Faltan campos obligatorios"}), 400
    
    nombre = data["nombre"]
    mail = data["mail"]
    ubicacion = data["ubicacion"]
    pedido = data["pedido"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # datetime local. # strftime() es para un formato más legible.

    pedidos.cursor.execute(
        "INSERT INTO pedidos (nombre, mail, ubicacion, pedidos, timestamp) VALUES (?, ?, ?, ?, ?)",
        (nombre, mail, ubicacion, json.dumps(pedido), timestamp)
    )
    pedidos.conn.commit()

    logs.crear_log("pedido_service", "orden", "INFO", f"Cliente {mail} ha hecho un pedido")
    logs.cargar_log_a_db()

    return jsonify({
        "success": "Se ha realizo el pedido exitosamente"
    }), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8003, debug=True)