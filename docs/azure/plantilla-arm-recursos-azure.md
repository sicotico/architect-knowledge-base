---
title: Plantilla ARM recursos Azure
date: 2025-01-23
category: Azure/Cloud
slug: plantilla-arm-recursos-azure
tags: ['Azure/Cloud', 'azure']
---

# Plantilla ARM recursos Azure


> **Pregunta original:**
> 
¿Se puede tener un plantilla de Azure Arm con todos los recursos?

---


## Respuesta


Sí, es posible tener una plantilla de Azure Resource Manager (ARM) que incluya todos los recursos necesarios para una solución específica. Las plantillas ARM son documentos JSON que definen los recursos y configuraciones que deseas implementar en Azure.

Sin embargo, incluir **todos** los recursos disponibles de Azure en una sola plantilla no es práctico porque:

1. **Especificidad de los recursos:** Cada recurso tiene configuraciones específicas y dependencias únicas.
2. **Complejidad:** Una plantilla con todos los recursos posibles sería inmanejable y difícil de utilizar, ya que contendría configuraciones genéricas o vacías para recursos innecesarios.
3. **Escalabilidad:** Las plantillas deben diseñarse para soluciones concretas o grupos de recursos que trabajen en conjunto.

### Buenas prácticas para plantillas ARM:
1. **Modularidad:** Divide tus recursos en varias plantillas según su función o propósito (por ejemplo, red, almacenamiento, bases de datos, aplicaciones).
2. **Reutilización:** Usa **plantillas enlazadas** o **plantillas anidadas** para separar los recursos lógicamente.
3. **Parámetros y variables:** Haz uso de parámetros para permitir configuraciones dinámicas y variables para simplificar la lógica.
4. **Outputs:** Utiliza la sección `outputs` para exponer información útil (como conexiones o claves generadas) que pueda ser usada por otras plantillas.

### Ejemplo básico de una plantilla ARM
Aquí tienes un ejemplo que incluye varios recursos comunes: una máquina virtual, una cuenta de almacenamiento y una red virtual.

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "location": {
      "type": "string",
      "defaultValue": "East US",
      "metadata": {
        "description": "Ubicación de los recursos"
      }
    },
    "vmName": {
      "type": "string",
      "defaultValue": "miVM"
    }
  },
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2022-09-01",
      "name": "[concat('storage', uniqueString(resourceGroup().id))]",
      "location": "[parameters('location')]",
      "sku": {
        "name": "Standard_LRS"
      },
      "kind": "StorageV2",
      "properties": {}
    },
    {
      "type": "Microsoft.Network/virtualNetworks",
      "apiVersion": "2022-07-01",
      "name": "miVNet",
      "location": "[parameters('location')]",
      "properties": {
        "addressSpace": {
          "addressPrefixes": ["10.0.0.0/16"]
        }
      }
    },
    {
      "type": "Microsoft.Compute/virtualMachines",
      "apiVersion": "2022-03-01",
      "name": "[parameters('vmName')]",
      "location": "[parameters('location')]",
      "properties": {
        "hardwareProfile": {
          "vmSize": "Standard_DS1_v2"
        },
        "osProfile": {
          "computerName": "[parameters('vmName')]",
          "adminUsername": "adminuser",
          "adminPassword": "ContraseñaSegura123!"
        },
        "storageProfile": {
          "imageReference": {
            "publisher": "MicrosoftWindowsServer",
            "offer": "WindowsServer",
            "sku": "2019-Datacenter",
            "version": "latest"
          },
          "osDisk": {
            "createOption": "FromImage"
          }
        },
        "networkProfile": {
          "networkInterfaces": [
            {
              "id": "[resourceId('Microsoft.Network/networkInterfaces', 'miNIC')]"
            }
          ]
        }
      },
      "dependsOn": [
        "[resourceId('Microsoft.Network/virtualNetworks', 'miVNet')]"
      ]
    }
  ]
}
```

### ¿Quieres una plantilla personalizada?
Si necesitas una plantilla ARM diseñada para un caso específico, puedo ayudarte a generarla según tus requerimientos (por ejemplo, un clúster de AKS, aplicaciones web, bases de datos, etc.). Solo indícame qué necesitas. 😊

---
*Generado desde conversación con 2 mensajes.*
*Azure/Cloud*
