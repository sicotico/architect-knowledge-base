---
title: Consultas KQL y Diagramas
date: 2025-03-13
category: IA/ML
slug: consultas-kql-y-diagramas
tags: ['IA/ML']
---

# Consultas KQL y Diagramas


> **Pregunta original:**
> 
Eres un especialista de Azure cloud. Tienes acceso a Resource Explorer y te piden generar los diagramas de infraestructura y networking. Que consultas haría con KQL y que herramienta utilizaria spara convertirlos en diagramas?

---


## Respuesta


Para generar diagramas de infraestructura y networking en Azure utilizando **Resource Explorer** y **KQL (Kusto Query Language)**, seguiría estos pasos:

---

### **1. Consultas en KQL para obtener recursos clave**

#### **A. Infraestructura general (Máquinas virtuales, bases de datos, etc.)**
```kql
Resources
| where type =~ 'Microsoft.Compute/virtualMachines' or
        type =~ 'Microsoft.Sql/servers' or
        type =~ 'Microsoft.Storage/storageAccounts'
| project name, type, resourceGroup, location, properties.hardwareProfile.vmSize
```
- Esta consulta obtiene todas las VM, bases de datos SQL y cuentas de almacenamiento.

#### **B. Recursos de Networking (VNETs, Subnets, NICs, NSGs, etc.)**
```kql
Resources
| where type startswith 'Microsoft.Network'
| project name, type, resourceGroup, location, properties
```
- Filtra todos los recursos de red, como VNETs, subredes, NICs, y NSGs.

#### **C. Relaciones entre recursos (Para dependencias y conexiones)**
```kql
ResourceGraphResources
| where type == 'microsoft.resources/links'
| project sourceResourceId, targetResourceId
```
- Obtiene las relaciones entre los recursos para trazar conexiones en los diagramas.

#### **D. Identificar los Load Balancers y sus backends**
```kql
Resources
| where type == 'Microsoft.Network/loadBalancers'
| extend backendPools = properties.backendAddressPools
| project name, type, backendPools
```
- Extrae los Load Balancers y las IPs de sus backends.

---

### **2. Herramientas para convertir los datos en diagramas**
Después de obtener la información con KQL, usaría herramientas como:

✅ **Azure Resource Visualizer (en el portal de Azure)**  
  - Se puede visualizar automáticamente la infraestructura dentro de una suscripción.  

✅ **Diagrams-as-Code (Terraform, Mermaid, PlantUML, etc.)**  
  - Para diagramas más detallados y personalizables, podría exportar los datos en formato JSON y usar **MermaidJS o Draw.io** para generar diagramas automáticos.  
  - Un script en Python podría convertir los datos en un formato compatible con **Graphviz (DOT)** para generar grafos.

✅ **Azure Workbooks**  
  - Se pueden construir dashboards con Workbooks para visualizar los recursos y sus dependencias.

---

### **3. Automatización del Proceso**
Para hacer este proceso más eficiente, podríamos:

1. **Exportar los datos desde Azure Resource Graph a un JSON o CSV.**
2. **Utilizar Python con Diagram (https://diagrams.mingrammer.com/) para generar diagramas automáticamente.**
3. **Automatizar con Azure Logic Apps o Azure Functions** para generar y actualizar diagramas periódicamente.

---

### **Conclusión**
Las consultas KQL permiten extraer la información necesaria de la infraestructura y networking. Luego, herramientas como **Azure Resource Visualizer, Draw.io, MermaidJS y Python Diagrams** pueden ayudar a convertir esos datos en diagramas visuales. La elección depende de la necesidad de personalización y automatización.

¿Quieres ayuda con un script en Python para automatizarlo? 🚀

---
*Generado desde conversación con 2 mensajes.*
*IA/ML*
