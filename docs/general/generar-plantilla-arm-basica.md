---
title: Generar plantilla ARM básica
date: 2025-02-18
category: General
slug: generar-plantilla-arm-basica
tags: ['General']
---

# Generar plantilla ARM básica


> **Pregunta original:**
> 
Eres un especialista de azure y estas trabajando con plantillas de ARM. Quieres generar un plantilla ARM pero que no contenga más que los nombre, obviando los id 

---


## Respuesta


Aquí tienes una plantilla ARM mínima que solo contiene los nombres de los recursos, sin incluir los IDs:

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "resources": [
    {
      "type": "Microsoft.Resources/resourceGroups",
      "apiVersion": "2021-04-01",
      "name": "[parameters('resourceGroupName')]",
      "location": "[parameters('location')]"
    },
    {
      "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2021-09-01",
      "name": "[parameters('storageAccountName')]",
      "location": "[parameters('location')]",
      "kind": "StorageV2",
      "sku": {
        "name": "Standard_LRS"
      }
    },
    {
      "type": "Microsoft.Compute/virtualMachines",
      "apiVersion": "2022-08-01",
      "name": "[parameters('vmName')]",
      "location": "[parameters('location')]",
      "properties": {
        "hardwareProfile": {
          "vmSize": "Standard_B1s"
        }
      }
    }
  ],
  "parameters": {
    "resourceGroupName": {
      "type": "string"
    },
    "location": {
      "type": "string"
    },
    "storageAccountName": {
      "type": "string"
    },
    "vmName": {
      "type": "string"
    }
  }
}
```

Esta plantilla incluye solo los nombres de los recursos, omitiendo los IDs completos. Se definen parámetros para los nombres y ubicaciones, lo que permite mayor flexibilidad al desplegar la plantilla.

---
*Generado desde conversación con 2 mensajes.*
*General*
