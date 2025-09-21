# -----------------------------
# Lista de tokens válidos
# -----------------------------
TOKENS_VALIDOS = [
    "TOKEN_SUPER_SECRETO_1",
    "TOKEN_SUPER_SECRETO_2",
    # Podés agregar más tokens aquí
]

# -----------------------------
# Función para validar un token
# -----------------------------
def validar_token(token: str):
    """
    Verifica si un token recibido está dentro de los TOKENS_VALIDOS.
    Lanza ValueError si el token no es válido.
    """
    if token not in TOKENS_VALIDOS:
        raise ValueError("Token inválido")