---
title: Disponibilidad TS en Go
date: 2026-06-17
category: General
slug: disponibilidad-ts-en-go
tags: ['General']
---

# Disponibilidad TS en Go


> **Pregunta original:**
> 
Cuando estará disponble electro con el compilar de TS en Go ? 

---


## Respuesta


Voy a verificar a qué proyecto se refiere exactamente, porque “electro” podría ser un typo de **Electron** u otro paquete. La parte del compilador de TypeScript en Go sí apunta a cambios recientes del equipo de TypeScript.
---


Si te refieres a **Electron + TypeScript**, no hay una “versión de Electron con el compilador de TS en Go”. Electron no compila TypeScript: normalmente usas `tsc`, Vite, esbuild, webpack, etc. El cambio está en **TypeScript**, no en Electron.

## Estado actual

El compilador nativo de TypeScript en Go ya está disponible en **preview** como:

```bash
npm install -D @typescript/native-preview
```

y se ejecuta con:

```bash
npx tsgo
```

Microsoft anunció las previews nativas el **22 de mayo de 2025**. También hay una extensión preview para VS Code. citeturn739693search0

Además, **TypeScript 7.0 Beta** fue anunciado el **21 de abril de 2026**. En esa beta, sigue usándose el paquete `@typescript/native-preview` y el binario `tsgo`; la versión estable de TypeScript 7.0 debería publicarse bajo el paquete normal `typescript` y usar `tsc`. citeturn739693search1

## Entonces, ¿cuándo estará “disponible”?

| Caso | Estado |
|---|---|
| Probarlo hoy en proyectos Electron | **Ya puedes**, usando `@typescript/native-preview` / `tsgo` |
| Usarlo como reemplazo estable de `tsc` | **Aún no completamente estable**; eso llega con TypeScript 7.0 estable |
| Que Electron lo traiga integrado | **No aplica**; Electron no debería “traer” el compilador TS |

## Lo bueno

- Prometen grandes mejoras de rendimiento; Microsoft habló de hasta **10x** en muchos proyectos. citeturn739693search3
- Puede ayudar bastante en proyectos Electron grandes, donde el type-checking de TS se vuelve lento.
- La preview ya permite validar compatibilidad sin reemplazar todo tu toolchain.

## Lo malo / cuidado

- Sigue siendo transición: si tu build depende de plugins, transformers, tooling raro o integración profunda con `tsserver`, puede haber diferencias.
- Para producción, yo no lo pondría como único compilador sin comparar primero contra `tsc`.
- Electron no se beneficia automáticamente: tienes que cambiar tu pipeline de TypeScript.

Para probarlo sin romper tu proyecto Electron:

```bash
npm install -D @typescript/native-preview
npx tsgo --noEmit
```

Eso te permite comparar errores y tiempo contra:

```bash
npx tsc --noEmit
```

---
*Generado desde conversación con 3 mensajes.*
*General*
