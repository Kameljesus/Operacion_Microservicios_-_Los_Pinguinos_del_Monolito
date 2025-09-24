from flask import Flask, request, jsonify
from db_manager import DBManager
from logs_db import logs
import uuid  # para generar tokens seguros

# Instanciar
registrados = DBManager("clientes_registrados.db")

# Conectar / crear DB
registrados.crear_conectar_db()

registrados.cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    mail TEXT NOT NULL,
    ubicacion TEXT NOT NULL,
    token TEXT NOT NULL
);
""")

# Crear la app de Flask
app = Flask(__name__)

# ----------------------------------
# Ruta POST para recibir datos JSON
# ----------------------------------
@app.route("/registro", methods=["POST"])
def registro():
    # Obtenemos los datos enviados por el cliente en formato JSON
    data = request.get_json()

    # Validación básica
    if not data:
        return jsonify({"error": "No se envió JSON"}), 400
    
    if "nombre" not in data or "mail" not in data or "ubicacion" not in data:
        logs.crear_log("registro_service", "registro", "ERROR", "Información incompleta del cliente")
        logs.cargar_log_a_db()
        return jsonify({"error": "Faltan campos obligatorios"}), 400
    
    nombre = data["nombre"]
    mail = data["mail"]
    ubicacion = data["ubicacion"]

    # Revisar si el usuario ya está registrado
    registrados.cursor.execute("SELECT token FROM clientes WHERE mail = ?", (mail,))
    token_del_cliente = registrados.cursor.fetchone()

    if token_del_cliente:
        logs.crear_log("registro_service", "registro", "INFO", f"Intento repetido de registro por parte del cliente: {mail}")
        logs.cargar_log_a_db()
        return jsonify({
            "error": "Usted ya está registrado en la Web",
            "token": token_del_cliente[0]
        }), 200
    
    # Generar token único
    token = uuid.uuid4().hex

    registrados.cursor.execute(
        "INSERT INTO clientes (nombre, mail, ubicacion, token) VALUES (?, ?, ?, ?)", (nombre, mail, ubicacion, token)
    )
    registrados.conn.commit()

    logs.crear_log("registro_service", "registro", "INFO", f"Cliente nuevo registrado: {mail}")
    logs.cargar_log_a_db()

    return jsonify({
        "success": "Se ha registrado exitosamente",
        "token": token
    }), 200
        
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001, debug=True)