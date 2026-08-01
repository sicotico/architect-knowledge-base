---
title: Arquitectura Azure Hub-Spoke
date: 2025-05-22
category: Azure/Cloud
slug: arquitectura-azure-hub-spoke
tags: ['Azure/Cloud', 'azure']
---

# Arquitectura Azure Hub-Spoke


> **Pregunta original:**
> 
El resultado formatealo en markdown
> Es un diagrama de arquitectura sobre Azure. Se basa en Hub and Spoke. Eres un arquitecto con mucha experiencia en cloud y sobre todo en Azure, Dynamics365 y Databricks. En el spoke se utiliza DNS resolver m Databricks , diferentes storages account y todos ellos con private links. Salvo Databricks que utiliza en Service point para reducir costes ya que el almacenamiento de Dynamics365 (Dataverse) se ubica en otro tenent.  Hemos solucionado el problema de la resolución DNS, la necesaria par los usuarios es diferente a la que necesita Databricks y Services end points. Lo usuarios utiliza Privat links. t por tanto se registra en los DNS de la CRossZone o Hub y Databricks necesita FQDN con ip pública para acceder al Service EndPoint, este ya trata el trafico vía backbone de Azure.

Con todo esto necesito que generes la documentacion técnica de arquitectura.

---


## Respuesta


Gracias por la información y el diagrama. A continuación, te presento la **documentación técnica de arquitectura** basada en el diseño que has compartido y la explicación proporcionada. Este documento está estructurado para cumplir estándares profesionales, siendo útil para revisión técnica, auditorías y traspasos.

---

# 📘 Documentación Técnica de Arquitectura – Plataforma de Datos en Azure

## 🔹 Resumen Ejecutivo

La solución implementa un modelo **Hub-and-Spoke** sobre Microsoft Azure, orientado a una arquitectura escalable, segura y optimizada para integración de datos entre servicios como **Dataverse (Dynamics 365)**, **Azure Data Lake**, **Databricks** y sistemas externos. Se ha dado especial atención a la resolución de nombres DNS diferenciada, conectividad privada mediante **Private Links**, y optimización de costes con **Service Endpoints** en los casos necesarios.

---

## 🔹 Diseño General

### Modelo de Red: Hub-and-Spoke

- **Hub**: Nodo central que alberga la conectividad de red, controladores de dominio, Azure Firewall y servicios comunes como Azure DNS, Private Resolver, y Data Gateways.
- **Spokes**:
  - **Spoke de Identidad y Networking**
  - **Spoke de Servicios Comunes (ODB Spoke)**
  - **Spoke de Datos (E-AUTO77-dt-PRO)**
  - **Spoke de Dataverse (Tenant externo: Ferrovial)**

### Principales Servicios Utilizados:

| Servicio Azure              | Función Principal                                                      |
|----------------------------|------------------------------------------------------------------------|
| Azure Firewall             | Control de acceso y tráfico entre spoke y servicios externos           |
| Azure Private Link         | Conectividad privada con recursos (Data Lake, Key Vault, etc.)         |
| Azure DNS & Private Resolver | Resolución DNS diferenciada para usuarios y servicios internos        |
| Azure Storage Account      | Almacenamiento de datos estructurados y no estructurados               |
| Azure Databricks           | Plataforma analítica para tratamiento y modelado de datos              |
| Azure Synapse Link         | Integración directa entre Dataverse y Azure Data Lake                  |
| Azure Event Hub            | Ingesta de eventos desde sistemas distribuidos                         |

---

## 🔹 Detalles Técnicos por Componente

### 🔸 Resolución DNS

- **Usuarios Finales**:
  - Utilizan **Private Endpoints**, cuyos FQDN son resueltos mediante **Azure DNS Zones privadas** publicadas en el **Hub**.
  - Se garantiza el aislamiento de tráfico dentro del backbone de Azure.

- **Databricks y Service Endpoints**:
  - Requieren resolución de **FQDN públicos**, ya que Service Endpoints exigen IP pública.
  - Se ha configurado el **Private DNS Resolver** en el Spoke de datos con reglas específicas para que esta resolución no interfiera con los endpoints privados de usuarios.

### 🔸 Conectividad

- **Private Link**:
  - Se utiliza en todos los recursos críticos de almacenamiento (Data Lake, Storage Accounts, Key Vault) y para la integración segura con Dataverse.

- **Service Endpoints**:
  - Exclusivamente usados por Databricks para acceso a **almacenamiento ubicado en otro Tenant (Ferrovial)**, optimizando costes y manteniendo la conectividad dentro del Azure Backbone.

### 🔸 Seguridad y Gobernanza

- Todo el tráfico está auditado a través de **Azure Firewall**.
- Las zonas privadas de DNS impiden fugas de información y garantizan resolución segura.
- **Role-Based Access Control (RBAC)** se aplica estrictamente en los recursos y suscripciones.
- Uso de **Private Resolver Inbound/Outbound** para control total de tráfico DNS hacia/desde Azure.

---

## 🔹 Integración con Dataverse (Dynamics 365)

- **Synapse Link** permite la sincronización continua de datos entre Dataverse y Azure Data Lake Gen2 (ubicado en spoke E-AUTO77-dt-PRO).
- El Dataverse se encuentra en **otro tenant (Ferrovial)**, y la comunicación se realiza a través de **Service Endpoints y Private Links**, permitiendo mantener el flujo de datos seguro y optimizado.

---

## 🔹 Arquitectura Visual

Referencia al diagrama compartido:  
**Archivo**: `I77 Data-Arq Data I77 - PROD.jpeg`

El diagrama refleja la segmentación en Hub and Spoke, con todos los flujos, servicios y relaciones de red adecuadamente representados.

---

## 🔹 Consideraciones de Rendimiento y Costes

- **Uso de Service Endpoints en Databricks** evita el sobrecoste del uso de Private Link entre tenants.
- **DNS Resolver personalizado** elimina conflictos de resolución entre usuarios y servicios internos.
- **Optimización de tráfico** al mantener la mayoría de la comunicación dentro del backbone de Azure.

---

## 🔹 Recomendaciones Futuras

- Migrar todos los endpoints públicos restantes a Private Link si el tenant origen se encuentra en control del equipo.
- Considerar el uso de Azure Policy para forzar el uso de Private Endpoints en todos los nuevos recursos.
- Incorporar Azure Monitor y Sentinel para visibilidad y respuesta ante incidentes de seguridad.

---

¿Deseas que esta documentación se exporte a formato Word o PDF? También puedo ayudarte a generar diagramas adicionales o versiones más detalladas para cada spoke.
---


Claro, aquí tienes la documentación técnica formateada en **Markdown** lista para incluir en tu repositorio, Wiki o documentación interna:

---

```markdown
# 📘 Documentación Técnica de Arquitectura – Plataforma de Datos en Azure

## 🔹 Resumen Ejecutivo

La solución implementa un modelo **Hub-and-Spoke** sobre Microsoft Azure, orientado a una arquitectura escalable, segura y optimizada para la integración de datos entre servicios como **Dataverse (Dynamics 365)**, **Azure Data Lake**, **Databricks** y sistemas externos. Se ha dado especial atención a la resolución de nombres DNS diferenciada, conectividad privada mediante **Private Links**, y optimización de costes con **Service Endpoints** en los casos necesarios.

---

## 🔹 Diseño General

### Modelo de Red: Hub-and-Spoke

- **Hub**: Nodo central con conectividad de red, Azure Firewall, Data Gateways y servicios comunes como Azure DNS y Private Resolver.
- **Spokes**:
  - Spoke de Identidad y Networking
  - Spoke de Servicios Comunes (ODB Spoke)
  - Spoke de Datos (E-AUTO77-dt-PRO)
  - Spoke de Dataverse (Tenant externo: Ferrovial)

### Servicios Principales

| Servicio Azure         | Función Principal                                                         |
|------------------------|----------------------------------------------------------------------------|
| Azure Firewall         | Control de tráfico entre spokes y hacia servicios externos                |
| Azure Private Link     | Conectividad privada con recursos como Storage, Key Vault, Event Hubs     |
| Azure DNS + Resolver   | Resolución DNS diferenciada por tipo de consumidor (usuario o servicio)   |
| Azure Storage Account  | Almacenamiento estructurado/no estructurado, lago de datos                |
| Azure Databricks       | Plataforma de procesamiento analítico y machine learning                  |
| Azure Synapse Link     | Integración de datos desde Dataverse a Data Lake Gen2                     |
| Azure Event Hub        | Ingesta de datos de eventos de sistemas externos o IoT                    |

---

## 🔹 Detalles Técnicos

### 🔸 Resolución DNS

- **Usuarios Finales**:
  - Usan **Private Endpoints** con FQDN registrados en **Azure DNS Private Zones** dentro del Hub.
  - Resolución gestionada desde el **Azure Private DNS Resolver** del Hub.

- **Databricks & Service Endpoints**:
  - Requieren resolución de **FQDN públicos**.
  - Se ha configurado el **Private DNS Resolver** en el spoke de datos con reglas de reenvío adecuadas para permitir ambas resoluciones de forma paralela.

### 🔸 Conectividad

- **Private Link**:
  - Empleado para todos los recursos de almacenamiento, Key Vaults y Event Hubs.
  - Garantiza la privacidad y la conectividad segura sin exposición pública.

- **Service Endpoints**:
  - Utilizados exclusivamente por **Azure Databricks** para conectarse a **almacenamiento externo en otro tenant (Ferrovial)**.
  - Permite ahorrar costes manteniendo tráfico dentro del backbone de Azure.

### 🔸 Seguridad y Gobernanza

- **Azure Firewall** filtra todo el tráfico entre on-premise, spoke y servicios públicos.
- **RBAC** aplicado por recurso y suscripción.
- **Zonas DNS privadas** garantizan resolución segura y controlada.
- **Private DNS Resolver** con reglas de reenvío específicas para soportar resoluciones múltiples.

---

## 🔹 Integración con Dataverse (Dynamics 365)

- **Azure Synapse Link** sincroniza datos entre **Dataverse (Ferrovial, otro tenant)** y **Azure Data Lake Gen2 (Spoke E-AUTO77-dt-PRO)**.
- La comunicación se realiza mediante combinación de **Private Links** y **Service Endpoints** para mantener la eficiencia, seguridad y minimizar costes.

---

## 🔹 Diagrama de Arquitectura

El diagrama utilizado se encuentra en el archivo:

```
I77 Data-Arq Data I77 - PROD.jpeg
```

Refleja las relaciones de red, servicios conectados, configuración de DNS y caminos de conectividad entre los distintos elementos del entorno.

---

## 🔹 Costes y Rendimiento

- **Uso de Service Endpoints** en Databricks evita el uso innecesario de Private Link entre tenants, reduciendo costes.
- **DNS Resolver personalizado** asegura resolución eficiente y sin conflictos.
- **Optimización del tráfico**: todos los flujos viajan dentro del backbone de Azure.

---

## 🔹 Recomendaciones Futuras

- Migrar cualquier conexión pública restante hacia **Private Link** si el tenant lo permite.
- Aplicar **Azure Policy** para forzar el uso de Private Endpoints en nuevos recursos.
- Integrar con **Azure Monitor** y **Microsoft Sentinel** para supervisión de seguridad y cumplimiento.
- Evaluar el uso de **Azure Managed Identities** para simplificar la gestión de credenciales en todos los recursos.

---
```

---

¿Te gustaría que lo exporte directamente a un archivo `.md` o lo prepare como documento de Word o PDF también?

---
*Generado desde conversación con 4 mensajes.*
*Azure/Cloud*
