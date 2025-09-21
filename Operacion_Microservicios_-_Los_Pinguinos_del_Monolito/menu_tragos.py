from fastapi import APIRouter, HTTPException, Header
from db_management import DBManager  # Tu clase DBManager
from tokens import validar_token     # Función para validar tokens

# -----------------------------
# Creamos la app de FastAPI
# -----------------------------
router = APIRouter()

# -----------------------------
# Instanciamos nuestro manager de DB
# -----------------------------
db = DBManager("Shake_It!.db")  # Nombre de tu DB
db.crear_conectar_db()              # Conectamos
db.crear_tabla_logs()               # Nos aseguramos de que la tabla exista

# -----------------------------
# Endpoint para obtener el menú
# -----------------------------
@router.get("/menu")
def get_menu(authorization: str | None = Header(default=None)):
    # -----------------------------
    # Validamos token
    # -----------------------------
    if not authorization or not authorization.startswith("Token "):
        raise HTTPException(status_code=401, detail="Token faltante o formato inválido")

    token_real = authorization.split(" ")[1]

    try:
        validar_token(token_real)  # Si el token no es válido, lanza ValueError
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
    try:
        # -----------------------------
        # Obtener tragos de la DB
        # -----------------------------
        cursor = db.conn.cursor()
        cursor.execute("SELECT nombre, available FROM tragos")
        tragos = cursor.fetchall()

        # -----------------------------
        # Formatear la respuesta
        # -----------------------------
        menu = []
        for nombre, available in tragos:
            estado = "Available" if available == 1 else "Not Available"
            menu.append(f"{nombre}, Available: {estado}")

        # -----------------------------
        # Crear log del evento
        # -----------------------------
        db.crear_log(
            autor="menu_service",
            service="menu",
            severity="INFO",
            mensaje="Cliente solicitó el menú"
        )
        db.cargar_log_a_db()

        return {"menu": menu}

    except Exception as e:
            # -----------------------------
            # Si ocurre un error, loguearlo y devolver HTTP 500
            # -----------------------------
            db.crear_log(
                autor="menu_service",
                service="menu",
                severity="ERROR",
                mensaje=f"Error al obtener el menú: {e}"
            )
            db.cargar_log_a_db()
            raise HTTPException(status_code=500, detail="Error interno del servidor")