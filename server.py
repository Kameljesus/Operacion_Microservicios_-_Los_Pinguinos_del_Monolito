import subprocess
import sys
import time

# Lista de tus microservicios (archivo, puerto, nombre amigable)
SERVICIOS = [
    ("registro.py", 8001, "Registro"),
    ("mostrar_menu.py", 8002, "Menú"),
    ("orden_del_pedido.py", 8003, "Ordenes"),  # tu archivo es "orden_del_pedido.py"
]

def main():
    procesos = []

    try:
        for archivo, puerto, nombre in SERVICIOS:
            print(f"🚀 Iniciando {nombre} en http://127.0.0.1:{puerto}")
            # Ejecuta cada API como subproceso
            p = subprocess.Popen([sys.executable, archivo])
            procesos.append(p)
            time.sleep(1)  # un poco de respiro para evitar choques

        print("✅ Todos los servicios están corriendo")
        print("Usa CTRL+C para detenerlos todos")

        # Mantener el script vivo
        for p in procesos:
            p.wait()

    except KeyboardInterrupt:
        print("🛑 Deteniendo todos los servicios...")
        for p in procesos:
            p.terminate()
        print("✅ Todos los servicios han sido detenidos.")

if __name__ == "__main__":
    main()