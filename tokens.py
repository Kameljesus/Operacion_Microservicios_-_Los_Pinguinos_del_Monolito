from registros_db import registrados

# -------------------------------
# Función para validar un token
# -------------------------------
def validar_token(token):
    # Obtenemos todos los tokens de clientes
    registrados.cursor.execute("SELECT token FROM clientes")
    tokens_de_los_clientes = registrados.cursor.fetchall()
    
    for (token_del_cliente,) in tokens_de_los_clientes:  # desempaquetamos la tupla
        if token_del_cliente == token:
            return  # válido

    # Si ningún token coincide:
    raise ValueError("Token inválido")