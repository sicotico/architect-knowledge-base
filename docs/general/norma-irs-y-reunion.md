---
title: Norma IRs y Reunión
date: 2024-11-21
category: General
slug: norma-irs-y-reunion
tags: ['General']
---

# Norma IRs y Reunión


> **Pregunta original:**
> 
Que dice Azure sobre la funcion de los Integration Runtime
> Traduce la a ingles por favor 
> Resumelo en 3 lineas
> 
> *...y 2 preguntas de seguimiento*


---


## Respuesta


Azure define el **Integration Runtime (IR)** como la infraestructura de proceso utilizada por Azure Data Factory y Azure Synapse para proporcionar capacidades de integración de datos en diferentes entornos de red. Sus principales funciones incluyen:

- **Movimiento de datos**: Copiar datos entre almacenes en redes públicas o privadas, ya sean locales o en redes virtuales. citeturn0search0

- **Flujos de datos**: Ejecutar flujos de datos en un entorno de proceso administrado por Azure. citeturn0search0

- **Distribución de actividades**: Despachar y supervisar actividades de transformación que se ejecutan en diversos servicios de proceso, como Azure Databricks, Azure HDInsight, Azure SQL Database y SQL Server. citeturn0search0

- **Ejecución de paquetes SSIS**: Ejecutar de forma nativa paquetes de SQL Server Integration Services (SSIS) en un entorno de proceso administrado por Azure. citeturn0search0

Azure ofrece tres tipos de Integration Runtime:

1. **Azure Integration Runtime**: Proporciona un proceso completamente administrado y sin servidor en Azure, ideal para mover datos entre almacenes en la nube de forma segura y eficiente. citeturn0search0

2. **Integration Runtime autohospedado**: Permite ejecutar actividades de copia entre almacenes de datos en la nube y almacenes en redes privadas, así como distribuir actividades de transformación en recursos de proceso locales o en Azure Virtual Network. citeturn0search0

3. **Azure-SSIS Integration Runtime**: Facilita la ejecución nativa de paquetes SSIS en un entorno de proceso administrado por Azure, permitiendo migrar cargas de trabajo SSIS existentes a la nube. citeturn0search0

La elección del tipo de Integration Runtime adecuado depende de las necesidades específicas de integración de datos y de los requisitos del entorno de red de su organización.
---


It is the infrastructure that enables data integration across different environments, providing data movement, flow execution, distributed activities, and SSIS package execution.

Its location impacts network connections and performance.
---


### Resumen para Diapositiva

- **Situación Actual**:  
  - No existe una norma definida para la ubicación y administración de los IRs.  
  - Los IRs proveen acceso a recursos y capacidad de cómputo.

- **Acciones Realizadas**:  
  - Inicio de un *assessment* para evaluar el estado actual.  
  - Desarrollo de una propuesta *To-Be* en proceso.

- **Próximos Pasos**:  
  - Reunión agendada por la TO para la próxima semana.  
  - Participantes: Escalona, Luis Soler y Arquitectura de Migración.  
  - Objetivo: Revisión y discusión de la propuesta presentada.
---


El **Integration Runtime (IR)** en Azure es la infraestructura que permite integrar datos en distintos entornos, proporcionando movimiento de datos, ejecución de flujos, actividades distribuidas y ejecución de paquetes SSIS. Hay tres tipos: **Azure IR** (administrado y sin servidor), **Self-hosted IR** (para redes privadas y locales), y **Azure-SSIS IR** (para ejecutar paquetes SSIS). La elección depende de los requisitos de red e integración.
---


### Slide Summary

- **Current Situation**:  
  - No defined standard for the location and management of IRs.  
  - IRs provide access to resources and computing capacity.

- **Actions Taken**:  
  - Initiated an assessment to evaluate the current state.  
  - Development of a *To-Be* proposal in progress.

- **Next Steps**:  
  - TO has scheduled a meeting for next week.  
  - Participants: Escalona, Luis Soler, and Migration Architecture.  
  - Objective: Review and discuss the presented proposal.

---
*Generado desde conversación con 10 mensajes.*
*General*
