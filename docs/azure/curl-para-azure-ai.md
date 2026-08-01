---
title: Curl para Azure AI
date: 2025-02-14
category: Azure/Cloud
slug: curl-para-azure-ai
tags: ['Azure/Cloud', 'azure']
---

# Curl para Azure AI


> **Pregunta original:**
> 
¿Se puede usar AI Foudry para crear aplicaciones corporativas con cientos de usuarios?
> Tengoun modelo en Azure y me han dado estos dato: 

Punto de conexión
URI de destino
https://Phi-3-mini-4k-instruct-ttnlt.swedencentral.models.ai.azure.com

Clave
Mg2HGIrWQljlvHKvSaqpZJ2WtKCJYSf9


Tipo de proceso
Consumption
URI de Swagger
https://Phi-3-mini-4k-instruct-ttnlt.swedencentral.models.ai.azure.com/swagger.json

Rutas de API


Azure AI model inference: Chat Completion
https://Phi-3-mini-4k-instruct-ttnlt.swedencentral.models.ai.azure.com/chat/completions

phi3-mini-4k: Chat Completion
https://Phi-3-mini-4k-instruct-ttnlt.swedencentral.models.ai.azure.com/v1/chat/completions

Como puedo hacer un curl para probarlo ??
> Hazme un diagra de la estructura de AI Foundry 
> 
> *...y 2 preguntas de seguimiento*


---


## Respuesta


Aquí tienes un diagrama de la estructura de **AI Foundry**, mostrando los componentes clave y sus relaciones. Si necesitas ajustes o detalles adicionales, dime y lo mejoramos. 🚀
---


Para hacer una solicitud `curl` a tu modelo en Azure, sigue estos pasos:

### 1️⃣ **Prepara tu API Key y Endpoint**
Tu API requiere autenticación con la clave proporcionada. En este caso, la clave es:
```
Mg2HGIrWQljlvHKvSaqpZJ2WtKCJYSf9
```
Y el endpoint de inferencia para chat completions es:
```
https://Phi-3-mini-4k-instruct-ttnlt.swedencentral.models.ai.azure.com/v1/chat/completions
```

### 2️⃣ **Construye la solicitud `curl`**
Ejecuta el siguiente comando en tu terminal:

```sh
curl -X POST "https://Phi-3-mini-4k-instruct-ttnlt.swedencentral.models.ai.azure.com/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer Mg2HGIrWQljlvHKvSaqpZJ2WtKCJYSf9" \
  -d '{
    "messages": [
      {"role": "system", "content": "Eres un asistente útil."},
      {"role": "user", "content": "¿Cuál es la capital de Francia?"}
    ],
    "temperature": 0.7,
    "max_tokens": 100
  }'
```

### 3️⃣ **Explicación del comando:**
- `-X POST`: Indica que estamos enviando una solicitud POST.
- `-H "Content-Type: application/json"`: Especifica que enviamos datos en formato JSON.
- `-H "Authorization: Bearer TU_CLAVE"`: Se usa la clave de API como token de autenticación.
- `-d '{ ... }'`: Es el cuerpo de la solicitud en JSON. Incluye:
  - `messages`: Lista de mensajes en el formato requerido por OpenAI/Azure.
  - `temperature`: Controla la creatividad de la respuesta (0.7 es un valor típico).
  - `max_tokens`: Límite de tokens en la respuesta.

### 4️⃣ **Ejecuta la solicitud**
Copia y pega el comando en la terminal y presiona **Enter**. Si todo está bien configurado, deberías recibir una respuesta JSON con el resultado de la inferencia del modelo.

Si tienes problemas con la autenticación, es posible que necesites usar un `API Key` en lugar de un `Bearer Token`. En ese caso, prueba con:

```sh
-H "api-key: Mg2HGIrWQljlvHKvSaqpZJ2WtKCJYSf9"
```
en lugar de la cabecera `Authorization`.

¿Necesitas más ayuda o quieres probar con otro modelo? 🚀
---


iturn0image0turn0image2turn0image8turn0image9Azure AI Foundry es una plataforma integral diseñada para que desarrolladores y científicos de datos construyan, evalúen y desplieguen modelos de inteligencia artificial de manera eficiente. A continuación, se presenta un diagrama que ilustra su arquitectura:

![Diagrama de la arquitectura de Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/media/concepts/architecture/architecture-diagram.png)

**Componentes principales de Azure AI Foundry:**

1. **Azure OpenAI**: Proporciona acceso a los modelos más recientes de OpenAI, permitiendo la creación de implementaciones seguras, pruebas en entornos controlados, ajuste fino de modelos, filtros de contenido y ejecución de tareas en lote.

2. **Centro de Gestión**: Facilita la gobernanza y administración de recursos dentro de Azure AI Foundry, incluyendo hubs, proyectos, recursos conectados y despliegues.

3. **Hub de Azure AI Foundry**: Es el recurso principal que ofrece configuración de seguridad, recursos de cómputo para desarrollo interactivo, ajuste fino, despliegue de modelos de código abierto y conexiones a otros servicios de Azure como Azure OpenAI y Azure AI Search.

4. **Proyecto de Azure AI Foundry**: Un contenedor dentro del hub que proporciona herramientas de desarrollo para construir y personalizar aplicaciones de IA, componentes reutilizables como conjuntos de datos y modelos, y conexiones específicas del proyecto para acceder a datos y recursos.

5. **Conexiones**: Permiten que los hubs y proyectos accedan a recursos de otros servicios de Azure, como cuentas de almacenamiento, servicios de Azure OpenAI y otros servicios de Azure AI.

Esta estructura modular y escalable de Azure AI Foundry permite a las organizaciones desarrollar y desplegar aplicaciones de inteligencia artificial de manera segura y eficiente, aprovechando la amplia gama de servicios y recursos que ofrece Azure.

Para obtener más detalles sobre la arquitectura de Azure AI Foundry, puedes consultar la documentación oficial de Microsoft: citeturn0search0

Además, si deseas una guía práctica sobre cómo utilizar Azure AI Foundry en tus aplicaciones de IA, te recomiendo el siguiente video:

videoUsando el SDK de Azure AI Foundry para tus aplicaciones de IAturn0search2
---


Sí, Azure AI Foundry está diseñado para crear y gestionar aplicaciones de inteligencia artificial a escala empresarial, permitiendo su uso por cientos o incluso miles de usuarios simultáneamente. La plataforma ofrece una infraestructura escalable y flexible que facilita el desarrollo, despliegue y gestión de aplicaciones de IA generativa y copilotos personalizados. citeturn0search0

Además, Azure AI Foundry se integra con herramientas de desarrollo populares como GitHub y Visual Studio, proporcionando un entorno unificado para diseñar, personalizar y administrar aplicaciones de IA de manera eficiente. Esta integración permite a los desarrolladores trabajar en sus entornos preferidos, facilitando la colaboración y acelerando el ciclo de desarrollo. citeturn0search0

La plataforma también garantiza la seguridad y privacidad de los datos, heredando las políticas de seguridad de Azure para asegurar que los datos de la organización se mantengan privados y no sean utilizados para mejorar los modelos sin consentimiento. citeturn0search3

En resumen, Azure AI Foundry es una solución robusta y escalable para desarrollar aplicaciones corporativas de IA que pueden atender a una gran cantidad de usuarios, asegurando al mismo tiempo la seguridad y eficiencia en su implementación.
---


En Azure, los costos de los modelos de inteligencia artificial varían según su complejidad, capacidad y proveedor. Recientemente, Microsoft ha integrado el modelo R1 de DeepSeek en su plataforma Azure AI Foundry, destacando por su eficiencia y menor costo en comparación con otros modelos líderes. citeturn0news15

Además, Azure ofrece una gama de modelos de código abierto a través de su servicio "Modelos como Servicio" (MaaS). Esta oferta permite a los desarrolladores acceder y utilizar diversos modelos sin necesidad de aprovisionar hardware especializado, pagando únicamente por el número de tokens utilizados durante la inferencia y la cantidad de datos empleados para el ajuste fino. Los precios específicos varían según el modelo y la región, y se pueden consultar en Azure Marketplace. citeturn0search0

Para obtener una estimación precisa de los costos asociados a cada modelo y seleccionar la opción más económica que se ajuste a tus necesidades, se recomienda utilizar la calculadora de precios de Azure disponible en su sitio web oficial. citeturn0search5

Ten en cuenta que los precios pueden variar según la región y las configuraciones específicas del modelo, por lo que es esencial revisar la información más actualizada directamente en las fuentes oficiales de Azure.

---
*Generado desde conversación con 10 mensajes.*
*Azure/Cloud*
