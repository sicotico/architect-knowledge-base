---
title: Consultar servicios Azure en uso
date: 2024-12-16
category: Azure/Cloud
slug: consultar-servicios-azure-en-uso
tags: ['Azure/Cloud', 'azure']
---

# Consultar servicios Azure en uso


> **Pregunta original:**
> 
Utilizando Azure Resource Graph quiero que solo me salgan el tipo de recursos. y una sola vez
> Estoy en el portal de azure, como puedo consultar todos los servicios en uso. Necesito un listado de los productos de azure que estamos usando


---


## Respuesta


Para consultar todos los servicios de Azure en uso en tu suscripción y obtener un listado de los productos que estás utilizando, puedes seguir estos pasos desde el portal de Azure:

---

### **1. Revisión general en el portal de Azure:**
1. **Accede al portal de Azure**: Inicia sesión en [Azure Portal](https://portal.azure.com/).
2. **Ir al apartado "Cost Management + Billing"**:
   - En el menú izquierdo, busca y selecciona **"Cost Management + Billing"**.
   - En la sección **"Cost Analysis"**, puedes identificar los servicios con costos asociados. Esto te da una idea de los productos en uso.
3. **Usa el menú de "Recursos"**:
   - Ve a **"All Resources"** o **"Todos los recursos"** desde el menú principal.
   - Aquí verás una lista de todos los recursos activos en tu suscripción.
   - Puedes filtrar por tipo de recurso (máquinas virtuales, bases de datos, redes, etc.) o exportar la lista.

---

### **2. Exportar la lista de recursos:**
Si necesitas un listado para análisis o documentación:
1. Ve a **"Todos los recursos" (All Resources)**.
2. En la parte superior, haz clic en el botón **"Exportar"**.
3. Selecciona el formato de exportación, como **CSV**.
4. El archivo contendrá detalles como el nombre del recurso, tipo, grupo de recursos, ubicación, etc.

---

### **3. Uso de Azure Resource Graph (Opcional para consultas avanzadas):**
Si necesitas un análisis más profundo:
1. Ve al servicio **"Resource Graph Explorer"** en el portal de Azure.
2. Ejecuta la siguiente consulta para obtener todos los recursos:
   ```kusto
   Resources
   | project name, type, resourceGroup, location, subscriptionId
   ```
3. Puedes ajustar la consulta para filtrar servicios específicos o agruparlos por tipo.

---

### **4. Uso de Azure CLI o PowerShell:**
Para automatizar la consulta de servicios en uso:

#### **Azure CLI:**
Ejecuta este comando desde una terminal con la CLI de Azure configurada:
```bash
az resource list --output table
```

#### **PowerShell:**
Ejecuta este comando en PowerShell:
```powershell
Get-AzResource | Select-Object Name, ResourceType, ResourceGroupName, Location
```

---

### **5. Consultar productos asociados a costos (si aplica):**
1. Ve a **"Cost Management" > "Cost Analysis"**.
2. Analiza los costos por servicio para entender qué productos de Azure están generando actividad.

---

Estas herramientas te permiten tener una visión clara de los servicios en uso y documentar los productos activos en tu suscripción. Si necesitas más detalles sobre un paso en particular, avísame.
---


Para listar únicamente los tipos de recursos utilizados en tu suscripción y asegurarte de que cada tipo aparezca solo una vez, puedes usar una consulta en **Azure Resource Graph**. 

Aquí está la consulta que necesitas:

```kusto
Resources
| summarize count() by type
| project type
```

### **Explicación**:
1. **`Resources`**: Hace referencia a todos los recursos en tu suscripción.
2. **`summarize count() by type`**: Agrupa los recursos por su tipo y cuenta cuántos existen de cada uno (aunque en este caso, no necesitamos el número).
3. **`project type`**: Selecciona únicamente la columna `type`, eliminando los demás datos para mostrar un listado único.

### **Pasos para ejecutarla en Azure Resource Graph Explorer**:
1. Ve al portal de Azure y busca **"Resource Graph Explorer"** en la barra de búsqueda.
2. Crea una nueva consulta y pega el código proporcionado.
3. Haz clic en **"Run Query"** (Ejecutar consulta).
4. Si quieres exportar el resultado, usa la opción **"Export"** (Exportar) en la parte superior derecha.

El resultado será una lista única de todos los tipos de recursos que estás utilizando en tu suscripción. Si necesitas más personalización, házmelo saber. 😊

---
*Generado desde conversación con 4 mensajes.*
*Azure/Cloud*
