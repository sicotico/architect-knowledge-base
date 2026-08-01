---
title: Server-Sent Events SSE
date: 2025-04-15
category: General
slug: server-sent-events-sse
tags: ['General']
---

# Server-Sent Events SSE


> **Pregunta original:**
> 
Server-Sent Events
> Y promesa JS
> Respecto de webhooks

---


## Respuesta


**Server-Sent Events (SSE)** is a technology that allows a server to push real-time updates to the client over HTTP. It's part of the HTML5 standard and is often used when you want **unidirectional communication** (server → client), like for:

- Real-time feeds (e.g., stock tickers, news)
- Chat messages (if one-way)
- Notifications or alerts

---

### 🧩 How it works:

1. The client opens a connection to the server via the `EventSource` API.
2. The server responds with an HTTP stream using a `Content-Type: text/event-stream`.
3. The server keeps the connection open and sends updates as new lines of text.
4. The client listens and reacts as events arrive.

---

### 📄 Basic Client Example:

```html
<script>
  const source = new EventSource('/events');

  source.onmessage = function(event) {
    console.log('New message:', event.data);
  };

  source.onerror = function(error) {
    console.error('EventSource failed:', error);
  };
</script>
```

---

### 🔧 Server Example (Node.js + Express):

```js
const express = require('express');
const app = express();

app.get('/events', (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');

  setInterval(() => {
    res.write(`data: ${new Date().toISOString()}\n\n`);
  }, 1000);
});

app.listen(3000, () => console.log('Server listening on port 3000'));
```

---

### ✅ Pros:
- Simple to use with native browser support (no external libraries).
- Efficient for real-time updates.
- Automatically handles reconnection.

### ❌ Cons:
- Only unidirectional (can’t send client → server messages over the same channel).
- Doesn’t work well with some older browsers or proxies.
- Not ideal for high-frequency or bi-directional data (use WebSockets instead).

---

Want a comparison with WebSockets or a deeper dive into handling custom events or reconnections?
---


¡Perfecto! Vamos con **webhooks**, que son otro mecanismo muy usado para comunicación entre servicios, pero funcionan de forma muy diferente a Server-Sent Events (SSE).

---

## 🔁 ¿Qué es un Webhook?

Un **webhook** es una **notificación HTTP** enviada por un servidor a otro **cuando ocurre un evento específico**. En lugar de que el cliente esté preguntando constantemente si hay novedades (como con polling), el servidor **"empuja"** (push) la información en cuanto sucede algo.

---

### 📦 ¿Cómo funciona?

1. Tú (como cliente) registras una URL en el sistema de un tercero (por ejemplo, Stripe, GitHub, etc.).
2. Cuando ocurre un evento (ej: nuevo pago, push en GitHub), el sistema hace una petición HTTP `POST` a tu URL.
3. Tu servidor recibe el dato y puede reaccionar: guardar en la base de datos, enviar un email, actualizar un dashboard, etc.

---

### 🔧 Ejemplo simple (Node.js + Express):

```js
const express = require('express');
const app = express();

app.use(express.json());

app.post('/webhook', (req, res) => {
  const event = req.body;
  console.log('Webhook recibido:', event);

  // Procesar el evento
  res.status(200).send('OK');
});

app.listen(3000, () => console.log('Esperando webhooks en /webhook'));
```

---

### 🧠 Comparación rápida: SSE vs Webhooks

| Aspecto        | SSE                          | Webhooks                      |
|----------------|------------------------------|-------------------------------|
| Dirección      | Servidor → Cliente (navegador) | Servidor → Servidor           |
| Uso común      | Interfaces en tiempo real     | Integración entre sistemas    |
| Inicio         | Cliente inicia conexión       | Servidor hace POST            |
| Persistencia   | Conexión mantenida            | Peticiones independientes     |
| Bi-direccional | No                            | No                            |
| Ejemplo típico | Noticias en vivo              | Notificación de pago          |

---

¿Te gustaría que te arme un diagrama, una demo más completa o ver cómo se manejan temas como **verificación de autenticidad** en webhooks?
---


¡Genial! Vamos con **promesas en JavaScript** — una de las piezas clave para manejar código **asíncrono** de forma limpia.

---

## 📦 ¿Qué es una Promesa?

Una **Promesa** es un objeto que representa un valor que **aún no está disponible**, pero lo estará **en el futuro** (o fallará).

Es como decirle a JS:  
_"No lo tengo ahora, pero cuando lo tenga (o si algo sale mal), te aviso."_

---

### 🧠 Tres estados de una promesa:

1. **Pending** – está en proceso, esperando.
2. **Fulfilled** – se resolvió exitosamente.
3. **Rejected** – hubo un error.

---

### 🔧 Ejemplo básico:

```js
const promesa = new Promise((resolve, reject) => {
  setTimeout(() => {
    const exito = true;

    if (exito) {
      resolve("¡Todo salió bien!");
    } else {
      reject("Algo falló.");
    }
  }, 1000);
});

promesa
  .then(resultado => console.log("✅", resultado))
  .catch(error => console.error("❌", error));
```

---

### ⛓️ Encadenamiento (`then`):

```js
hacerAlgo()
  .then(resultado1 => hacerOtraCosa(resultado1))
  .then(resultado2 => console.log('Final:', resultado2))
  .catch(error => console.error('Error en la cadena:', error));
```

---

### ⏱️ Promesas con funciones `async/await`:

Desde ES2017, puedes usar `async/await` para escribir promesas como si fueran código sincrónico:

```js
async function ejecutar() {
  try {
    const resultado = await promesa;
    console.log("✅", resultado);
  } catch (error) {
    console.error("❌", error);
  }
}

ejecutar();
```

---

### 🧩 Casos de uso comunes:

- Fetch de datos (`fetch()`)
- Esperar a que se resuelvan varias promesas (`Promise.all`)
- Timeouts, animaciones, operaciones asincrónicas

---

¿Querés ver cómo usar promesas con `fetch`, o cómo manejar varios procesos al mismo tiempo con `Promise.all()` o `Promise.race()`?

---
*Generado desde conversación con 6 mensajes.*
*General*
