# Operación Microservicios – Los Pingüinos del Monolito

Proyecto de **arquitectura de microservicios** en Python.  
Se simula un sistema compuesto por **tres microservicios independientes**, cada uno con su propia base de datos, conectado a una base de datos central de logs.  

El diseño garantiza que **si un microservicio se cae, el sistema completo sigue funcionando**, demostrando **tolerancia a fallos y escalabilidad**.

---

## 🧠 Objetivo del proyecto

- Implementar **microservicios como APIs REST** usando **Flask**  
- Cada microservicio tiene su propia base de datos y responsabilidades:
  - Gestión de clientes
  - Gestión de pedidos
  - Gestión de menú
- Centralizar logs en una **base de datos de logs**  
- Implementar **cliente HTTP** que interactúa con los microservicios  
- Mostrar flujo de comunicación entre servicios y persistencia de datos

---

## 🛠️ Tecnologías y herramientas

- Python 3  
- Flask para microservicios
- `requests` para enviar HTTP requests desde el cliente 
- SQLite para bases de datos individuales y de logs  
- Autenticación básica mediante tokens (`tokens.py`) 

---

## 📂 Estructura del proyecto

Archivos principales:

- `client.py` — Cliente principal que interactúa con los microservicios  
- `server.py` — Servidor central que orquesta los microservicios y logs  
- `db_manager.py` — Funciones de conexión y gestión de bases de datos  
- `logs_db.py` — Persistencia de logs centralizados  
- `registros_db.py` — Funciones específicas para logs de eventos  
- `menu_db.py` — Base de datos de menú de productos  
- `pedidos_db.py` — Base de datos de pedidos  
- `orden_del_pedido.py` — Lógica de creación y gestión de pedidos  
- `registro.py` — Registro de clientes o eventos  
- `mostrar_menu.py` — Funciones para mostrar el menú  
- `defs_cliente.py` — Constantes y definiciones de cliente  
- `tokens.py` — Diccionario de tokens válidos para autenticación  
- `notas_de_aprendizaje.md` — Apuntes y explicaciones teóricas del proyecto  

---

## 🚀 Cómo usar el proyecto

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Kameljesus/Operacion_Microservicios_-_Los_Pinguinos_del_Monolito.git
cd Operacion_Microservicios_-_Los_Pinguinos_del_Monolito
```

### 2️⃣ Instalar Flask (si no lo tenés)

```bash
pip install flask requests
```

### 3️⃣ Iniciar server

```bash
python server.py
```

### 4️⃣ Ejecutar cliente

```bash
python client.py
```

El cliente envía requests HTTP a los microservicios, crea pedidos, registra clientes y consulta el menú.
