from db_manager import DBManager

# Instanciar
logs = DBManager("logs.db")

# Conectar / crear DB
logs.crear_conectar_db()

# Crear tabla si no existe
logs.crear_tabla_logs()