## Qué es FastAPI?:

FastAPI es un framework web para Python, que sirve para crear APIs REST (interfaces que permiten que programas se hablen entre sí) de forma rápida, simple y eficiente.

👉 Su nombre lo dice: Fast porque es muy rápido (usa async por debajo) y API porque está pensado para construir APIs.

# 🛠️ Analogía: Restaurante:

Imaginá que tenés un restaurante:

- FastAPI es como la cocina del restaurante: organiza todo lo que entra (pedidos) y todo lo que sale (platos listos).
- El cliente (tu navegador o app móvil) manda un pedido: "Quiero la pizza N°5" → eso sería un request HTTP GET.
- FastAPI recibe ese pedido, busca la receta (la función en tu código), la prepara y devuelve la pizza (la respuesta JSON).
- Si el cliente pide algo más complejo (ejemplo: registrar usuario, mandar logs, generar un token), FastAPI se encarga de que tu código maneje esos pedidos correctamente.

# 📌 Ventajas de FastAPI:

1. Rápido y moderno → usa async y está construido sobre Starlette (para lo web) y Pydantic (para validación de datos).
2. Documentación automática → apenas levantas tu API, ya tenés documentación en Swagger UI (http://localhost:8000/docs).
3. Facilita seguridad → integración con JWT, OAuth2, etc.
4. Validación de datos integrada → no necesitás validar a mano, FastAPI lo hace por vos.

👉 En resumen: FastAPI es el puente entre tu código en Python y el mundo exterior (navegadores, apps, otros servicios).


## 📌 Qué significa async?:

En Python, async es una forma de programar tareas que pueden esperar sin bloquear todo el programa.
Se combina con await y sirve para manejar operaciones lentas (como leer de una base de datos, esperar respuesta de un servidor, leer un archivo grande) sin que el programa se quede "congelado".

# 🛠️ Analogía: Restaurante otra vez 🍽️:

- Imaginá que tenés un solo mozo en un restaurante.
- Si el mozo va a la cocina, pide una pizza y se queda esperando sin hacer nada hasta que salga, los demás clientes quedan esperando. Eso sería el código normal (síncrono).
- En cambio, si el mozo pide la pizza y mientras espera atiende otras mesas, cuando la pizza está lista, la trae. Eso es código asíncrono (async).

👉 El mozo nunca se queda parado, aprovecha el tiempo para hacer otras tareas mientras espera.

# 📌 En FastAPI:

FastAPI usa async porque:

- Muchas veces hace llamadas lentas (a bases de datos, APIs externas, etc.).
- Con async, mientras espera esas respuestas, el servidor puede atender a otros clientes.


## 📌 Qué es httpx?:

httpx es una librería de Python para hacer solicitudes HTTP, muy parecida a requests (si lo conocés), pero con soporte nativo para async.

- HTTP = el protocolo que usan los navegadores y APIs para hablar entre sí.
- httpx nos permite que nuestro cliente Python hable con nuestro servidor FastAPI.

# 🛠️ Analogía: Correo entre microservicios ✉️:

- Imaginá que tu microservicio de Pedidos quiere avisarle al microservicio de Pagos que alguien hizo un pedido.
- httpx es como el cartero digital que lleva la carta (request) de un servicio a otro y trae la respuesta.
- Puede enviar cartas sin bloquear el escritorio (async), o de manera simple (síncrona).


## Qué es un router en FastAPI?:

Un router es un conjunto de endpoints agrupados que podés definir en un archivo separado y luego “enchufar” a tu app principal de FastAPI.

- Sirve para organizar el código cuando la app crece.
- Evita tener un solo archivo gigante con todos los endpoints.

Cada router puede tener:

- Sus propios endpoints (get, post, etc.)
- Sus propios prefix (prefijo de ruta)
- Sus propios tags (para documentación automática)

# Ventaja real

Si después agregás /order o /hacer_pedido, cada uno puede tener su router:

- orden_router.py
- pedido_router.py

Todo esto se centraliza en server.py y tu app queda limpia y escalable.

💡 Resumen:

Router = “mini-FastAPI” dentro de un archivo, que luego se conecta a la app principal.
No es obligatorio, pero es muy recomendable para apps con varios endpoints.

## Qué hace que una API sea RESTful

Una API se considera RESTful si cumple con ciertos principios de REST (Representational State Transfer):

1. Uso de métodos HTTP según la operación:
    
    - GET → obtener datos
    - POST → crear datos
    - PUT/PATCH → actualizar datos
    - DELETE → eliminar datos

2. URLs limpias y recursos bien definidos:

Ejemplo: /registro es un recurso “cliente” donde se crea un registro.

3. Sin estado en el servidor (stateless):

Cada request incluye toda la información necesaria (como tu token).

4. Uso de JSON o XML para representar los datos:

Tu API devuelve JSON, perfecto