import sqlite3

# Conexión a la base de datos
base_de_datos = sqlite3.connect("Shake_It!.db")
cursor = base_de_datos.cursor()

# Creación de tablas:
# Tabla Logs:
cursor.execute("""
CREATE TABLE IF NOT EXISTS eventos_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    autor TEXT NOT NULL,
    timestamps TEXT NOT NULL,
    services TEXT NOT NULL,
    severity TEXT NOT NULL,
    messages TEXT NOT NULL,
    received_at TEXT
);
""")

# Tabla Tragos:
cursor.execute("""
CREATE TABLE IF NOT EXISTS tragos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    available BOOLEAN NOT NULL
);
""")

# Lista de 30 tragos
tragos = [
    "Old Fashioned", "Negroni", "Daiquiri", "Piña Colada", "Whisky Sour",
    "Pisco Sour", "Mojito", "Caipirinha", "Manhattan", "Gin Tonic",
    "Dry Martini", "Dirty Martini", "Carajillo", "Irish Coffee", "Aperol Spritz",
    "Singapur", "Cosmopolitan", "Aviation", "Sidecar", "Whisky Fix",
    "Bee's Knees", "Sangría", "Mai Tai", "Sex On The Beach", "Penicillin",
    "Margarita", "Moscow Mule", "Paloma", "Tequila Sunrise", "Long Island Iced Tea"
]

# Insertar tragos en la tabla (todos disponibles por defecto)
for trago in tragos:
    cursor.execute("INSERT INTO tragos (nombre, available) VALUES (?, ?)", (trago, True))

# Guardar cambios y cerrar conexión
base_de_datos.commit()
base_de_datos.close()

print("Base de datos creada y tragos insertados con éxito.")