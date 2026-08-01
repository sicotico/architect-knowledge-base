---
title: Conversión de texto a markdown
date: 2024-09-21
category: General
slug: conversion-de-texto-a-markdown
tags: ['General']
---

# Conversión de texto a markdown


> **Pregunta original:**
> 
Falta la imagen adjunta al problema, l puedes mostrar ?
> Quiero que obtengas el texto y lo conviertas a markdown desde la pregunta 220


---


## Respuesta


I have found the information related to "Pregunta 220". Here is the corresponding text in markdown format:

---

### Pregunta 220

**Escenario:** Requisitos de seguridad:

- Todos los secretos utilizados por los servicios de Azure deben almacenarse en Azure Key Vault.
- Los servicios que requieren credenciales deben tener las credenciales vinculadas a la instancia del servicio. Las credenciales no deben compartirse entre servicios.

#### Solución recomendada:

- **Box 1:** Una identidad administrada asignada por el sistema  
  Nadie conoce las credenciales de las identidades administradas. Las identidades administradas existen en dos formatos:
  - Asignada por el sistema: en este escenario, la identidad está vinculada a un solo recurso de Azure, por ejemplo, una máquina virtual, una aplicación lógica, una cuenta de almacenamiento, una aplicación web, función, etc. Además, viven con el recurso de Azure, lo que significa que se eliminan cuando el recurso de Azure se elimina.
  - **Identidad administrada asignada por el usuario (incorrecto para esta pregunta)**, lo que significa que primero se debe crear como un recurso independiente de Azure y luego se puede vincular a varios recursos de Azure.

- **Box 2:** Una política de acceso  
  Configurar una política de acceso para la identidad administrada asignada por el sistema.

  **Nota:** Conceder acceso:  
  La identidad administrada debe tener acceso para leer el secreto que se almacenará en el Key Vault.

  **Pasos:**
  1. Navegar a tu Key Vault recién creado.
  2. Seleccionar "Access Policy" desde el menú en el lado izquierdo.
  3. Seleccionar "Add Access Policy".
  4. Continuar con la configuración.

#### Referencias:

- [Managed identities for Azure resources](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/tutorial-windows-vm-access-nonaad)
- [Service principals and managed identities](https://devblogs.microsoft.com/devops/demystifying-service-principals-managed-identities/)

--- 

This is the formatted content for question 220 from the document. Let me know if you need further changes or more details.
---


It seems I couldn't find the image associated with question 220 in the document. However, if you can provide a description or if there is a way to upload a screenshot or other parts of the document, I'd be happy to assist further.

---
*Generado desde conversación con 4 mensajes.*
*General*
