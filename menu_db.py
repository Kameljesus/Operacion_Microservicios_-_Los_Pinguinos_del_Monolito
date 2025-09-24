from db_manager import DBManager

# Instanciar
menu = DBManager("tragos_menu.db")

# Conectar / crear DB
menu.crear_conectar_db()

menu.cursor.execute("""
CREATE TABLE IF NOT EXISTS tragos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,     -- Aseguramos que no haya tragos duplicados
    available BOOLEAN NOT NULL
);
""")

# ----------------------------
# Lista de tragos a insertar
# ----------------------------
tragos = [
    "Old Fashioned", "Negroni", "Daiquiri", "Piña Colada", "Whisky Sour",
    "Pisco Sour", "Mojito", "Caipirinha", "Manhattan", "Gin Tonic",
    "Dry Martini", "Dirty Martini", "Carajillo", "Irish Coffee", "Aperol Spritz",
    "Singapur", "Cosmopolitan", "Aviation", "Sidecar", "Whisky Fix",
    "Bee's Knees", "Sangría", "Mai Tai", "Sex On The Beach", "Penicillin",
    "Margarita", "Moscow Mule", "Paloma", "Tequila Sunrise", "Long Island Iced Tea"
]

# ----------------------------------------
# Insertamos tragos (solo si no existen)
# ----------------------------------------

for trago in tragos:
    menu.cursor.execute("SELECT id FROM tragos WHERE nombre = ?", (trago,))
    existe = menu.cursor.fetchone()
    if not existe:  # Si no existe, lo insertamos
        menu.cursor.execute("INSERT INTO tragos (nombre, available) VALUES (?, ?)", (trago, True))

# ----------------------
# Guardamos y cerramos
# ----------------------
menu.commit()
menu.cerrar_db()

print("✅ Base de datos creada y tragos insertados con éxito.")