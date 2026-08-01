---
title: Implementación Phi-4 en Azure
date: 2025-02-14
category: Azure/Cloud
slug: implementacion-phi-4-en-azure
tags: ['Azure/Cloud', 'azure']
---

# Implementación Phi-4 en Azure


> **Pregunta original:**
> 
PRefiero con REST
> Estoy en Azure AI Foundry. Quiero crear una implementacion de Phi-4

---


## Respuesta


Si prefieres usar **REST API** para implementar **Phi-4 en Azure AI Foundry**, sigue estos pasos:

---

## 🚀 **1. Obtener la URL de Inferencia y Clave de API**
Antes de hacer solicitudes REST, necesitas:

1. **Obtener el endpoint** de tu implementación en Azure AI Foundry.
2. **Clave API** de acceso (en Azure Portal > AI Foundry > Deployment).

---

## 🔗 **2. Enviar una Solicitud REST a Phi-4**
Usaremos `curl` como ejemplo, pero puedes hacerlo en cualquier lenguaje.

### **Ejemplo de Petición REST (cURL)**
```bash
curl -X POST "https://<TU-ENDPOINT>.openai.azure.com/openai/deployments/<NOMBRE-DEPLOY>/chat/completions?api-version=2024-02-01"
-H "Content-Type: application/json"
-H "Authorization: Bearer <TU-CLAVE-API>"
-d '{
  "messages": [
    {
      "role": "system",
      "content": "Eres un asistente útil."
    },
    {
      "role": "user",
      "content": "¿Cuántos planetas hay en el sistema solar?"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 100
}'
```

- Reemplaza:
  - `<TU-ENDPOINT>` con el URL de tu despliegue.
  - `<NOMBRE-DEPLOY>` con el nombre de la implementación en Azure.
  - `<TU-CLAVE-API>` con tu clave de API.

---

## 📝 **3. Implementación en Python (requests)**
Si prefieres hacerlo en **Python**, usa la librería `requests`:

```python
import requests

# Configuración
API_ENDPOINT = "https://<TU-ENDPOINT>.openai.azure.com/openai/deployments/<NOMBRE-DEPLOY>/chat/completions?api-version=2024-02-01"
API_KEY = "<TU-CLAVE-API>"

# Datos de la solicitud
payload = {
    "messages": [
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "¿Cuántos planetas hay en el sistema solar?"}
    ],
    "temperature": 0.7,
    "max_tokens": 100
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Enviar solicitud
response = requests.post(API_ENDPOINT, json=payload, headers=headers)

# Mostrar respuesta
print(response.json())
```

---

## 📌 **Parámetros Opcionales**
Puedes modificar estos parámetros en la solicitud:

| Parámetro      | Descripción |
|---------------|------------|
| `temperature` | Controla la aleatoriedad (0 = respuestas más deterministas, 1 = más creativas). |
| `max_tokens`  | Número máximo de tokens en la respuesta. |
| `top_p`       | Controla la diversidad en la respuesta. |
| `stop`        | Lista de secuencias para detener la generación. |

---

## 🎯 **Conclusión**
🔹 Con esto ya puedes interactuar con **Phi-4 en Azure AI Foundry** usando **REST API**.  
🔹 Funciona en **cualquier lenguaje** que soporte peticiones HTTP.  
🔹 Puedes integrar esto en aplicaciones, chatbots o automatizaciones.

Si necesitas ayuda con algo más, dime. 🚀
---


Para implementar el modelo Phi-4 en Azure AI Foundry, sigue estos pasos:

1. **Despliegue del modelo**: Accede al portal de Azure AI Foundry y selecciona el modelo Phi-4 de la familia de modelos disponibles. Puedes optar por desplegarlo como una API sin servidor con facturación según el uso, o en una infraestructura autogestionada para mayor control. citeturn0search0

2. **Instalación del paquete de inferencia**: Para interactuar con el modelo, instala el paquete `azure-ai-inference` en tu entorno de Python. Asegúrate de tener Python 3.8 o superior y utiliza el siguiente comando para la instalación:

   ```bash
   pip install azure-ai-inference
   ```

3. **Autenticación y configuración del cliente**: Configura las credenciales necesarias y crea un cliente para consumir el modelo. Por ejemplo, utilizando una clave de acceso:

   ```python
   import os
   from azure.ai.inference import ChatCompletionsClient
   from azure.core.credentials import AzureKeyCredential

   client = ChatCompletionsClient(
       endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
       credential=AzureKeyCredential(os.environ["AZURE_INFERENCE_CREDENTIAL"]),
   )
   ```

   Asegúrate de reemplazar las variables de entorno con los valores correspondientes a tu implementación.

4. **Consumo del modelo**: Una vez configurado el cliente, puedes enviar mensajes al modelo para obtener respuestas. Por ejemplo:

   ```python
   from azure.ai.inference.models import UserMessage

   response = client.complete(
       messages=[
           UserMessage(content="¿Cuántos idiomas se hablan en el mundo?"),
       ],
   )
   ```

   Este código envía una pregunta al modelo y recibe una respuesta generada por Phi-4.

Para obtener más detalles y opciones avanzadas, consulta la documentación oficial de Microsoft sobre cómo utilizar los modelos de la familia Phi-4 en Azure. citeturn0search0

Además, puedes obtener más información sobre Phi-4 y su disponibilidad en el siguiente video:

videoMicrosoft Introduces CoreAI and Makes Phi-4 Free for Everyoneturn0search8

---
*Generado desde conversación con 4 mensajes.*
*Azure/Cloud*
