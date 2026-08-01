---
title: Funciones GitHub PRs
date: 2026-07-28
category: General
slug: funciones-github-prs
tags: ['General']
---

# Funciones GitHub PRs


> **Pregunta original:**
> 
@GitHub Inspect PRs, triage issues, debug failing checks, and prepare code changes for review

---


## Respuesta


Ese texto es la descripción del complemento de GitHub que tienes disponible en esta conversación. En la práctica significa que puedo interactuar directamente con tus repositorios de GitHub (si la aplicación tiene permisos sobre ellos), no solo darte instrucciones.

Las capacidades principales son:

| Función | Qué puedo hacer |
|--------|------------------|
| **Inspect PRs** | Leer Pull Requests, revisar el diff, analizar el código, resumir cambios y detectar problemas. |
| **Triage issues** | Buscar, crear, etiquetar, asignar, cerrar o actualizar Issues. |
| **Debug failing checks** | Inspeccionar ejecuciones de GitHub Actions, leer logs, localizar el fallo y proponer o aplicar la corrección. |
| **Prepare code changes** | Crear o modificar archivos, hacer commits, crear ramas y abrir Pull Requests. |
| **Code review** | Revisar un PR como un revisor humano, dejar comentarios o solicitar cambios. |

En tu caso concreto, para el repositorio **architect-knowledge-base**, esto significa que puedo, por ejemplo:

- Crear automáticamente la estructura del proyecto.
- Crear el `README.md`.
- Añadir `mkdocs.yml`.
- Crear toda la documentación inicial.
- Hacer commits directamente en una rama.
- Abrir un Pull Request listo para revisar.
- Si falla GitHub Pages, inspeccionar los logs y corregirlos.

### Lo que todavía necesito

Aunque el complemento esté disponible, **solo puedo operar sobre repositorios para los que la aplicación de GitHub tenga autorización**.

La forma más rápida de comprobarlo es que me digas:

> **"Lista mis repositorios disponibles"**

o

> **"Busca el repositorio architect-knowledge-base"**

Si aparece, ya podremos trabajar directamente sobre él sin que tengas que copiar y pegar archivos. Si no aparece, significará que la aplicación de GitHub todavía no tiene acceso a ese repositorio y habrá que concedérselo.

---
*Generado desde conversación con 2 mensajes.*
*General*
