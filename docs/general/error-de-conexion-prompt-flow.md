---
title: Error de conexión Prompt Flow
date: 2025-02-28
category: General
slug: error-de-conexion-prompt-flow
tags: ['General']
---

# Error de conexión Prompt Flow


> **Pregunta original:**
> 
Ya he arreglado la conexión, gracias. Ahora me sale este:
chat : OpenAI API hits exception: TypeError: chat() missing 1 required positional argument: 'deployment_name'
> Estoy promt flow , en la web de Azure AI foundry . ME ha salido este error después de desplegar la plantilla de promtflow chat:
Tool load failed in 'chat': (GetConnectionError) Get connection '' for node 'chat' error: Connection '' not found in dict connection provider. Available keys are [].

---


## Respuesta


El error que mencionas en **Azure AI Foundry** con **Prompt Flow** sugiere que hay un problema con la conexión a un recurso necesario para ejecutar el flujo de chat. Aquí te dejo algunos pasos para solucionarlo:

### 🔍 **Causas del Error**
1. **No se ha configurado correctamente la conexión**: Parece que el flujo está intentando acceder a una conexión que no está definida.
2. **Falta de permisos o credenciales**: Puede que la conexión exista, pero el servicio no tenga los permisos adecuados para acceder a ella.
3. **El recurso no está disponible**: Si el flujo usa un servicio externo (como OpenAI, Azure OpenAI o Cognitive Services), puede que el recurso no esté bien configurado.

---

### ✅ **Pasos para Solucionarlo**

#### 1️⃣ **Revisar la configuración de la conexión en Prompt Flow**
1. Ve a **Azure AI Studio > Prompt Flow**.
2. Abre tu flujo y revisa la configuración del nodo `chat`.
3. Busca si hay una conexión especificada en la sección de **conexiones**.
4. Si falta, intenta asignarle una conexión válida.

---

#### 2️⃣ **Verificar las Conexiones Disponibles**
Dado que el error menciona *"Available keys are []"*, parece que no hay conexiones registradas. Para verificarlo:
1. Ve a **Azure AI Studio > Connections**.
2. Comprueba si hay alguna conexión disponible.
3. Si no hay ninguna, agrega una nueva.

Para agregar una conexión manualmente:
- Si usas **Azure OpenAI**, agrega una conexión a ese recurso.
- Si usas **OpenAI API**, configura una conexión con la clave de API.
- Si usas otro servicio, verifica qué tipo de conexión se necesita.

---

#### 3️⃣ **Reasignar la Conexión en el Flujo**
1. Abre el nodo `chat` en el flujo.
2. Busca el campo **Connection**.
3. Selecciona una conexión disponible en la lista.
4. Guarda los cambios y vuelve a desplegar.

---

#### 4️⃣ **Verificar Permisos y Configuración del Recurso**
Si el problema persiste:
- Asegúrate de que la conexión tiene las **credenciales correctas**.
- Comprueba que el recurso en **Azure OpenAI** o **Cognitive Services** está activo y accesible.

---

### 🚀 **Conclusión**
El error se debe a que el nodo `chat` está intentando acceder a una conexión inexistente. Debes **verificar, configurar y asignar una conexión válida** en el flujo de Prompt Flow.

Si después de estos pasos el error persiste, dime qué tipo de conexión estás usando y revisamos juntos la configuración. 😉
---


El nuevo error que mencionas en **Prompt Flow en Azure AI Foundry** indica que la función `chat()` necesita un argumento obligatorio llamado **`deployment_name`** y no lo está recibiendo. Este argumento es crucial porque Azure OpenAI usa **deployments** en lugar de modelos directos.

---

### ✅ **Pasos para Solucionarlo**
1. **Verificar la configuración del nodo `chat` en Prompt Flow**  
   - Ve a **Azure AI Studio > Prompt Flow**.
   - Abre tu flujo y localiza el nodo `chat`.
   - Asegúrate de que hay un campo para `deployment_name` y que contiene el nombre correcto de tu despliegue de Azure OpenAI.

2. **Obtener el nombre correcto del deployment en Azure**  
   - Ve a **Azure Portal > Azure OpenAI**.
   - Entra en el recurso de **Azure OpenAI** que usas.
   - En la sección de "Deployments", revisa el nombre exacto del deployment (por ejemplo, `gpt-4-turbo` o `chat-gpt-35-turbo`).
   - Usa **este nombre exacto** en la configuración del flujo.

3. **Añadir `deployment_name` en el flujo manualmente (si es necesario)**  
   Si el error persiste, puedes editar la configuración del nodo `chat` y asegurarte de que el `deployment_name` está presente en la llamada a la API.

   🔹 **Ejemplo correcto en JSON o YAML (si usas configuraciones personalizadas)**:
   ```json
   {
     "type": "chat",
     "connection": "mi-conexion-openai",
     "deployment_name": "gpt-4-turbo",
     "model": "gpt-4"
   }
   ```

4. **Guardar y volver a ejecutar el flujo**  
   - Guarda los cambios en Prompt Flow.
   - Vuelve a desplegar y ejecutar el flujo.

---

### 🚀 **Conclusión**
Este error se debe a que la API de OpenAI en Azure requiere un **deployment_name**, y no se ha pasado correctamente en el nodo `chat`. Configurarlo correctamente con el nombre exacto de tu deployment debería resolver el problema.

Si sigues teniendo problemas, dime qué configuración tienes en el nodo `chat` y lo revisamos juntos. 😊

---
*Generado desde conversación con 4 mensajes.*
*General*
