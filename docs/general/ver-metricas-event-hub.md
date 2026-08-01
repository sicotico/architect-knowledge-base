---
title: Ver métricas Event Hub
date: 2025-02-11
category: General
slug: ver-metricas-event-hub
tags: ['General']
---

# Ver métricas Event Hub


> **Pregunta original:**
> 
Como monitorizo un azure eventhub
> Quiero ver las graficas de Eventhub en el portal de azure
> eventhub tiene un limite de almacenamiento de m ensajes ?

---


## Respuesta


Sí, Azure Event Hubs tiene límites de almacenamiento de mensajes que varían según el nivel de servicio que utilices. A continuación, se detallan los límites principales:

1. **Período de retención de datos**:
   - **Nivel Básico**: Los eventos se retienen hasta por **1 día**.
   - **Nivel Estándar**: Los eventos se retienen hasta por **7 días**.
   - **Niveles Premium y Dedicado**: Los eventos se retienen hasta por **90 días**.

2. **Almacenamiento de eventos para retención**:
   - **Nivel Básico y Estándar**: **84 GB por Unidad de Rendimiento (TU)**.
   - **Nivel Premium**: **1 TB por Unidad de Procesamiento (PU)**.
   - **Nivel Dedicado**: **10 TB por Unidad de Capacidad (CU)**.

Es importante tener en cuenta que, aunque puedes configurar el período de retención dentro de estos límites, el almacenamiento disponible para la retención de eventos está sujeto a las capacidades mencionadas anteriormente. Si el almacenamiento asignado se llena antes de que se alcance el período de retención configurado, los eventos más antiguos se eliminarán para dar espacio a los nuevos.

Para almacenar eventos más allá del período de retención permitido o para análisis a largo plazo, puedes utilizar la característica **Event Hubs Capture**. Esta funcionalidad permite capturar automáticamente los datos de transmisión de Event Hubs y guardarlos en una cuenta de Azure Blob Storage o Azure Data Lake Storage para almacenamiento y análisis posteriores. citeturn0search2

Para obtener información más detallada sobre las cuotas y límites de Azure Event Hubs, puedes consultar la documentación oficial de Microsoft. citeturn0search0
---


Para monitorear un Azure Event Hub de manera efectiva, puedes utilizar Azure Monitor, que ofrece una variedad de herramientas para supervisar y analizar el rendimiento y la actividad de tus recursos en Azure. A continuación, se detallan los pasos y consideraciones clave para el monitoreo de Event Hubs:

1. **Recolección de datos de monitoreo**:
   - **Métricas de plataforma**: Azure Monitor recopila automáticamente métricas básicas como el número de mensajes entrantes, el rendimiento de entrada y salida, y la latencia. Estas métricas te permiten evaluar el rendimiento general de tu Event Hub.
   - **Logs de recursos**: Para obtener información más detallada sobre las operaciones y eventos dentro de tu Event Hub, puedes habilitar los logs de recursos. Esto incluye registros de auditoría de runtime y métricas de aplicaciones que proporcionan una visión más profunda de las interacciones y el estado de tus aplicaciones cliente.

2. **Análisis de métricas y logs**:
   - **Azure Monitor Metrics Explorer**: Utiliza esta herramienta para visualizar y analizar las métricas recopiladas. Puedes aplicar filtros y segmentar las métricas por dimensiones como el nombre de la entidad para obtener información más específica.
   - **Azure Monitor Logs (Log Analytics)**: Configura una configuración de diagnóstico para enviar los logs de recursos a Log Analytics. Esto te permitirá realizar consultas detalladas utilizando el lenguaje Kusto Query Language (KQL) para identificar patrones, anomalías y obtener información detallada sobre el comportamiento de tu Event Hub.

3. **Configuración de alertas**:
   - Establece alertas en función de métricas o logs específicos para recibir notificaciones proactivas cuando se cumplan ciertas condiciones. Por ejemplo, puedes configurar alertas para cuando la utilización de la CPU supere un umbral determinado o cuando el número de mensajes entrantes caiga por debajo de un valor específico.

4. **Integración con herramientas externas**:
   - Si utilizas herramientas de terceros para el monitoreo o análisis de logs, Azure Monitor te permite enrutar datos a través de Azure Event Hubs a estas herramientas. Esto es útil para integraciones con sistemas SIEM u otras plataformas de análisis.

Para una guía más detallada sobre cómo implementar estas prácticas, puedes consultar la documentación oficial de Microsoft: citeturn0search0

Además, este video proporciona una introducción completa a Azure Event Hubs y sus capacidades de monitoreo:

videoAzure Event Hub Tutorial | Big data message streaming serviceturn0search3
---


​Para visualizar las gráficas de métricas de un Azure Event Hub en el portal de Azure, sigue estos pasos:

1. **Acceder al recurso Event Hub**:
   - Inicia sesión en el [portal de Azure](https://portal.azure.com/).
   - En el menú de la izquierda, selecciona "Grupos de recursos" y elige el grupo que contiene tu Event Hub.
   - Dentro del grupo de recursos, selecciona el namespace de tu Event Hub y luego el Event Hub específico que deseas monitorear.

2. **Visualizar las métricas**:
   - En la página de tu Event Hub, en el menú de la izquierda, haz clic en "Métricas".
   - Aquí podrás ver las métricas predeterminadas como "Mensajes entrantes", "Rendimiento de entrada" y "Rendimiento de salida".
   - Para personalizar las gráficas, utiliza las opciones de filtrado y agrupación según tus necesidades.

3. **Configurar alertas (opcional)**:
   - Si deseas recibir notificaciones basadas en ciertas métricas, ve a la sección "Alertas" en el menú de la izquierda.
   - Configura reglas de alerta según los umbrales que consideres importantes para el monitoreo de tu Event Hub.

Para una guía más detallada sobre cómo habilitar y configurar la captura de eventos en Event Hubs, puedes consultar la documentación oficial de Microsoft:

Además, este video proporciona una introducción completa a Azure Event Hubs y sus capacidades de monitoreo:

videoAzure Event Hubs ejemplo prácticoturn0search2

---
*Generado desde conversación con 6 mensajes.*
*General*
