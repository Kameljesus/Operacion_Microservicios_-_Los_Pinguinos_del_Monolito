# -----------------------------
# Importaciones
# -----------------------------

# En FastAPI, los headers se reciben como parámetros de la función del endpoint, usando la clase Header. Así podemos validar tokens como hacíamos en HTTP “puro”.
from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from db_management import DBManager  # Tu clase DBManager
from tokens import validar_token  # Función para validar tokens

# -----------------------------
# Creamos el router
# -----------------------------
router = APIRouter()

# -----------------------------
# Instanciamos DB
# -----------------------------
db = DBManager("Shake_It!.db")  # Nombre de la DB
db.crear_conectar_db()           # Conectamos
db.crear_tabla_logs()            # Nos aseguramos de que la tabla de logs exista

# -----------------------------
# Modelo del pedido
# -----------------------------
class Pedido(BaseModel):
    tragos: list[str]

# -----------------------------
# Endpoint para hacer pedido
# -----------------------------
@router.post("/order")
def make_order(
    pedido: Pedido,                       # Recibimos el pedido en JSON
    authorization: str | None = Header(default=None)  # Header Authorization
):
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
    """
    raise es la palabra clave que usamos para “lanzar” una excepción.
    Cuando lanzás una excepción, interrumpís la ejecución normal del código y le decís a Python: “Ocurrió algo que no puedo manejar aquí, pasalo a quien me llame”.
    """

    # -----------------------------
    # Verificamos que no se superen los 15 tragos por pedido
    # -----------------------------
    if len(pedido.tragos) > 15:
        raise HTTPException(status_code=400, detail="Máximo 15 tragos por pedido")

    try:
        # -----------------------------
        # Creamos log del pedido
        # -----------------------------
        db.crear_log(
            autor="orden_service",
            service="order",
            severity="INFO",
            mensaje=f"Pedido recibido: {pedido.tragos}"
        )
        db.cargar_log_a_db()

        # -----------------------------
        # Retornamos respuesta
        # -----------------------------
        return {"pedido": pedido.tragos, "status": "Recibido"}
    
    except Exception as e:
        # -----------------------------
        # Si ocurre un error, lo logueamos y devolvemos HTTP 500
        # -----------------------------
        db.crear_log(
            autor="orden_service",
            service="order",
            severity="ERROR",
            mensaje=f"Error al procesar el pedido: {e}"
        )
        db.cargar_log_a_db()
        raise HTTPException(status_code=500, detail="Error interno del servidor")