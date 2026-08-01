---
title: Reducir logs en Azure
date: 2024-10-24
category: Azure/Cloud
slug: reducir-logs-en-azure
tags: ['Azure/Cloud', 'azure']
---

# Reducir logs en Azure


> **Pregunta original:**
> 
donde se definen las DCR
> Como reducir los logs almacenados en logs analitucs de azure

---


## Respuesta


Las **Data Collection Rules (DCR)** en Azure se definen y gestionan dentro del servicio de **Azure Monitor**, específicamente a través de la configuración de recolección de datos. Las DCR permiten controlar qué datos se recogen y de qué fuentes, brindando más flexibilidad para la gestión de datos.

### Pasos para definir y gestionar las DCR:

1. **Acceder a Azure Monitor**:
   - Inicia sesión en el portal de Azure.
   - Navega hacia **Azure Monitor**, que es el servicio donde se gestionan la mayoría de las configuraciones de recopilación de datos.

2. **Crear o gestionar una Data Collection Rule (DCR)**:
   - Dentro de Azure Monitor, busca la opción **Data Collection Rules** en la sección de "Configuración".
   - Si no tienes una DCR existente, selecciona **Crear** para empezar a configurar una nueva regla de recolección.
   
3. **Seleccionar el origen de los datos**:
   - Las DCR permiten seleccionar varias fuentes de datos, como máquinas virtuales, contenedores, servicios PaaS, o cualquier recurso de Azure que produzca logs.
   - Define desde qué fuentes quieres recopilar datos (por ejemplo, Windows Event Logs, Syslog, o métricas de rendimiento).

4. **Definir las condiciones y filtros de recopilación**:
   - Puedes filtrar los datos en base a criterios específicos como el tipo de evento o nivel de gravedad (por ejemplo, recolectar solo errores o advertencias). Esto ayuda a optimizar el volumen de datos recolectados.
   - Configura las transformaciones de datos si necesitas modificar o reducir la cantidad de datos antes de que lleguen al Workspace de Log Analytics.

5. **Especificar los destinos de datos**:
   - Define a qué destino se enviarán los datos recogidos. Los destinos pueden ser:
     - **Log Analytics Workspace** (para análisis y monitoreo avanzado).
     - **Azure Monitor Metrics** (para recopilación de métricas).
     - **Azure Storage** (para almacenamiento a largo plazo).
     - **Event Hub** (para integrar con otros servicios o aplicaciones).
  
6. **Asignar las DCR a los recursos**:
   - Las DCR se pueden asociar a recursos individuales o a grupos de recursos. Al definir una DCR, selecciona los recursos o grupos de recursos donde quieres que esta regla aplique.

### Detalles adicionales:
- **Compatibilidad con agentes**: Las DCR son compatibles con el **Azure Monitor Agent (AMA)**, el agente más reciente para la recolección de datos, que reemplaza a los antiguos **Log Analytics Agents (MMA)**. Esto permite definir reglas específicas y más granulares de recolección de datos.
  
- **Transformaciones Kusto (KQL)**: Puedes incluir consultas Kusto para filtrar y transformar los datos a medida que se recopilan. Esto permite realizar una selección avanzada de los datos antes de enviarlos al destino.

### Ubicación de las DCR en Azure:
- Para revisar las reglas ya existentes, ve a **Azure Monitor** > **Data Collection Rules**.
- Desde ahí, puedes ver todas las DCR configuradas, crear nuevas, o editar las actuales para ajustar los parámetros de recolección.

Las **DCR** son esenciales para reducir y optimizar los datos que se envían a Log Analytics o a otros destinos, controlando de manera precisa qué información es realmente relevante para el monitoreo y análisis.
---


Para reducir la cantidad de logs almacenados en Azure Log Analytics, es importante optimizar tanto la recolección de datos como el tiempo de retención de los mismos. Aquí tienes varias estrategias para reducir la cantidad de logs almacenados:

### 1. **Optimización de la recopilación de datos:**

#### Filtrar los datos de entrada
- **Configuración de recolección de datos**: En lugar de capturar todos los logs posibles, asegúrate de estar capturando solo los datos necesarios. Esto se puede hacer ajustando los **Data Collection Rules (DCR)** o configurando **agentes** de Log Analytics.
  - En las fuentes de datos, como Azure Monitor, diagnósticos de recursos de Azure, o máquinas virtuales, limita el tipo de datos que realmente necesitas, como métricas críticas y logs importantes.

- **Custom logs**: Si tienes logs personalizados, asegúrate de que solo se recojan los campos que son realmente útiles, para evitar capturar información innecesaria.

#### Definir reglas de filtrado (Kusto Queries)
- Utiliza **queries Kusto** en Azure Monitor o Log Analytics para filtrar y seleccionar únicamente los datos que necesites monitorear.
  
  Un ejemplo de esto podría ser crear una consulta KQL que filtre los registros no relevantes y solo muestre los logs de errores críticos:
  ```kql
  AzureDiagnostics
  | where Level == "Error"
  ```

### 2. **Reducir el tiempo de retención de logs:**

Azure Log Analytics ofrece opciones para definir el período de retención de los datos. La reducción de este período es una forma directa de reducir el almacenamiento utilizado:

- **Cambiar la retención de datos**: En las configuraciones de Log Analytics Workspace, puedes ajustar el período de retención de datos. Si no necesitas conservar los logs durante el período predeterminado (30 días), puedes reducir el tiempo de retención a algo más adecuado, como 7 o 14 días.
  - Dirígete a tu **Log Analytics Workspace** > **Usage and estimated costs** > **Data Retention** y ajusta el número de días.

### 3. **Utilizar tarifas por niveles y políticas de archivo**

- **Niveles de precios**: Revisa los niveles de precios de Log Analytics. En algunos casos, cambiar a un nivel con políticas de almacenamiento más adaptadas puede ayudar a reducir costos, como usar los niveles de **Retención a largo plazo** o **Archivo** para datos que no necesitas en tiempo real.
  
- **Políticas de archivado**: Usa el archivado para mover datos antiguos a un almacenamiento más económico que todavía esté disponible para consultas si es necesario. Los datos archivados son mucho más baratos de almacenar que los datos en caliente.

### 4. **Uso de Event Hub o Storage Account para logs no críticos:**
Si tienes logs que no necesitas consultar frecuentemente pero deseas almacenarlos por cumplimiento, puedes configurarlos para ser enviados a un **Azure Storage Account** o **Event Hub** en lugar de almacenarlos en Log Analytics. De esta forma, podrás reducir el volumen de logs enviados directamente al Workspace de Log Analytics.

### 5. **Optimizar la frecuencia de recolección de logs:**

- Ajusta la **frecuencia de recopilación de logs**. Algunos recursos generan datos a intervalos muy cortos, lo cual puede no ser necesario para ciertos escenarios. Ajustar la frecuencia de recolección puede disminuir considerablemente el volumen de datos.

### 6. **Monitorear el uso de espacio y ajustar reglas según el análisis:**

Monitorea el uso de datos regularmente para entender qué fuentes están generando la mayoría de los logs y ajusta las configuraciones en consecuencia.

En resumen, la clave está en configurar de forma precisa qué datos necesitas recolectar, reducir el período de retención, y considerar el uso de almacenamiento alternativo para logs menos críticos o archivados. Esto reducirá la cantidad de logs en Log Analytics, optimizando costos y eficiencia.

---
*Generado desde conversación con 4 mensajes.*
*Azure/Cloud*
