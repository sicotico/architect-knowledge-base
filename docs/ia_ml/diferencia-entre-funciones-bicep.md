---
title: Diferencia entre funciones Bicep
date: 2025-02-19
category: IA/ML
slug: diferencia-entre-funciones-bicep
tags: ['IA/ML']
---

# Diferencia entre funciones Bicep


> **Pregunta original:**
> 
En las plantillas de Bicep , ¿Que difirencia hay entre subscriptionResourceId() y resourceID()?

---


## Respuesta


En Bicep, tanto `subscriptionResourceId()` como `resourceId()` se utilizan para construir identificadores de recursos (IDs de Azure Resource Manager, o ARNs). Sin embargo, tienen diferencias clave en su propósito y uso:

### 1. **`subscriptionResourceId()`**
   - Se usa para construir el **ID de un recurso a nivel de suscripción**.
   - Se aplica cuando los recursos **no están dentro de un grupo de recursos (resource group), sino directamente en la suscripción**.
   - Su sintaxis es:
     ```bicep
     subscriptionResourceId(resourceType, resourceName)
     ```
   - Ejemplo:
     ```bicep
     var policyId = subscriptionResourceId('Microsoft.Authorization/policyDefinitions', 'myPolicy')
     ```
   - Esto genera un ID como:
     ```
     /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/myPolicy
     ```
   - Útil para definir recursos como **políticas, roles o directivas que operan a nivel de suscripción**.

---

### 2. **`resourceId()`**
   - Se usa para construir el **ID de un recurso dentro de un grupo de recursos (resource group)**.
   - Se usa cuando los recursos están dentro de un **Resource Group** y no directamente en la suscripción.
   - Su sintaxis básica es:
     ```bicep
     resourceId(resourceType, resourceName)
     ```
   - O si está en un grupo de recursos diferente:
     ```bicep
     resourceId(resourceGroupName, resourceType, resourceName)
     ```
   - Ejemplo:
     ```bicep
     var storageAccountId = resourceId('Microsoft.Storage/storageAccounts', 'mystorageaccount')
     ```
   - Esto genera un ID como:
     ```
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Storage/storageAccounts/mystorageaccount
     ```

---

### **Diferencias clave**
| Función                   | Nivel de recurso | Ubicación en la jerarquía de Azure | Ejemplo de salida |
|---------------------------|-----------------|----------------------------------|------------------|
| `subscriptionResourceId()` | Suscripción     | `/subscriptions/{subscriptionId}/providers/...` | `/subscriptions/123/providers/Microsoft.Authorization/policyDefinitions/myPolicy` |
| `resourceId()`            | Grupo de recursos | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/...` | `/subscriptions/123/resourceGroups/myRG/providers/Microsoft.Storage/storageAccounts/mystorageaccount` |

### **¿Cuándo usar cada una?**
- **Usa `subscriptionResourceId()`** cuando el recurso **existe a nivel de suscripción**, como políticas, roles o suscripciones a eventos.
- **Usa `resourceId()`** cuando el recurso **existe dentro de un grupo de recursos**, como máquinas virtuales, bases de datos o redes.

En resumen, la elección entre `subscriptionResourceId()` y `resourceId()` depende de dónde esté alojado el recurso en la jerarquía de Azure. 🚀

---
*Generado desde conversación con 2 mensajes.*
*IA/ML*
