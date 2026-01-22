from db_manager import DBManager

# Instanciar
pedidos = DBManager("pedidos_ordenes.db")

# Conectar / crear DB
pedidos.crear_conectar_db()

pedidos.cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    mail TEXT NOT NULL,
    ubicacion TEXT NOT NULL,
    pedidos TEXT NOT NULL,
    timestamp TEXT NOT NULL    
);
""")

# -----------
# Guardamos 
# -----------
pedidos.commit()