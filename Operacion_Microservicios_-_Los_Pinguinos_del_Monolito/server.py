# -----------------------------
# Archivo principal que levanta el servidor FastAPI
# -----------------------------

from fastapi import FastAPI
from db_management import DBManager

# Importamos routers
import menu_tragos
import orden_tragos

# -----------------------------
# Creamos la app principal
# -----------------------------
app = FastAPI(title="Shake It! API", version="1.0")

# -----------------------------
# Instanciamos y preparamos la DB
# -----------------------------
db = DBManager("Shake_It!.db")
db.crear_conectar_db()
db.crear_tabla_logs()

# -----------------------------
# Incluimos routers
# -----------------------------
app.include_router(menu_tragos.router)
app.include_router(orden_tragos.router)

# -----------------------------
# Endpoint de prueba del server
# -----------------------------
@app.get("/")
def root():
    return {"message": "Bienvenido a Shake It! API 🍹"}