from db_manager import DBManager

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

# -----------
# Guardamos 
# -----------
registrados.commit()