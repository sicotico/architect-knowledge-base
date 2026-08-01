---
title: Uso de Codex gratis
date: 2026-04-29
category: Programación
tags: ['Programación']
slug: uso-de-codex-gratis
---

# Uso de Codex gratis

> **Pregunta original:** como lo configguro en opencode ?...


Primero aclaro algo importante: **“Codex” como producto separado ya no se configura igual que antes**. Hoy en día, lo que usas en herramientas como OpenCode es básicamente un **modelo de código de OpenAI vía API** (por ejemplo, GPT-4.x / GPT-5 con capacidades de programación), no el Codex clásico como tal.

Dicho eso, para configurarlo en OpenCode, el proceso estándar es este:

---

## 1. Consigue tu API key de entity["company","OpenAI","AI company"]
1. Ve a: https://platform.openai.com
2. Inicia sesión
3. Genera una **API key**

⚠️ Esto es clave:
- La **versión gratuita de ChatGPT NO incluye API gratis**
- La API se paga aparte (aunque tengas ChatGPT gratis o Plus)

---

## 2. Configura OpenCode
En OpenCode (o cualquier herramienta similar), busca la sección de:

- **Providers / Model Providers**
- Añade un proveedor tipo: `OpenAI`

Introduce:

- **API Key** → la que generaste
- **Base URL** → normalmente:
  ```
  https://api.openai.com/v1
  ```

---

## 3. Elige el modelo correcto
En vez de “codex”, usa un modelo actual, por ejemplo:

- `gpt-4.1`
- `gpt-4o`
- o equivalentes más nuevos disponibles

💡 Muchos tutoriales antiguos usan:
- `code-davinci-002` → ❌ ya obsoleto

---

## 4. Ejemplo de configuración (genérico)
Algo así suele funcionar:

```json
{
  "provider": "openai",
  "apiKey": "TU_API_KEY",
  "model": "gpt-4.1"
}
```

---

## Problemas comunes
- ❌ “No funciona con mi cuenta gratis”
  → Normal: necesitas saldo en la API
- ❌ “No veo Codex”
  → Porque ya no se usa ese nombre como antes
- ❌ “Error 401”
  → API key mal copiada o sin permisos

---

## Resumen claro
- No configuras “Codex” directamente
- Configuras **OpenAI API + modelo moderno**
- Necesitas **API de pago**, no basta ChatGPT gratis

---

Si quieres, dime exactamente qué es *OpenCode* en tu caso (hay varias herramientas con ese nombre) o pégame tu configuración y te la reviso línea por línea.

Sí, **pero con matices importantes**.

👉 A día de hoy (2026), la versión gratuita de ChatGPT **sí puede usar Codex**, pero:

- Es un acceso **limitado o de prueba** citeturn0search2
- OpenAI lo ha incluido en el plan gratis **“por tiempo limitado”** citeturn0search0turn0search3
- Tiene **menos capacidad, menos mensajes y más restricciones** que los planes de pago citeturn0search2

### En resumen
- ✅ **Gratis**: puedes probar Codex (con límites)
- 💰 **Plus / Pro / etc.**: uso mucho más amplio y potente

💡 Traducción rápida:
Con la versión gratuita te dejan “catarlo”, pero si quieres usarlo en serio (proyectos grandes, muchas ejecuciones, etc.), necesitarás un plan de pago.

Si quieres, dime qué quieres hacer con Codex (programar, automatizar cosas, etc.) y te digo si con el plan gratis te alcanza o no 👍

---
*Generado desde conversación con 5 mensajes.*
*Categoría: Programación*
