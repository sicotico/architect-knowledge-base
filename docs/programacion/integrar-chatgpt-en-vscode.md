---
title: Integrar ChatGPT/OpenAI en VSCode y Zed Editor: Guía Completa
date: 2024-12-01
category: Programación
slug: integrar-chatgpt-en-vscode
tags: ['IA', 'VSCode', 'OpenAI', 'ChatGPT', 'API']
author: 'Piconocimiento'
reading_time: 12
---

# Integrar ChatGPT/OpenAI en VSCode y Zed Editor: Guía Completa

## 🎯 Contexto

> **Pregunta original:** *"No entiendo cómo funciona la API key de ChatGPT. Yo tengo uno personal y desde la web me funciona, pero por API no tengo posibilidad de usarlo. Actualmente tengo una cuenta de ChatGPT y quiero utilizarla en Visual Studio Code."*

Este artículo explica las diferencias entre **ChatGPT (Web)** y **OpenAI API**, y cómo integrar inteligencia artificial directamente en tu editor de código favorito.

## 🔑 Diferencia Fundamental: ChatGPT vs OpenAI API

### ⚠️ Lo Más Importante

**Tu suscripción a ChatGPT Plus NO te da acceso a la API.** Son servicios separados:

| Característica | ChatGPT (Web) | OpenAI API |
|----------------|---------------|------------|
| **Acceso** | Tu cuenta personal | Clave API (API Key) |
| **Costo** | $20/mes (Plus) | Pago por uso (tokens) |
| **Uso** | Interfaz web | Programática/API |
| **Modelos** | GPT-4, GPT-4o | GPT-3.5, GPT-4, GPT-4o, etc. |
| **Créditos** | Incluidos en suscripción | Créditos separados |

### ¿Por Qué Son Diferentes?

```
ChatGPT Plus → Interfaz web → Tu cuenta → $20/mes
                                                  ↓
OpenAI API   → Clave API  → Programática → $ por token
```

**Para usar IA en VSCode, necesitas una clave API de OpenAI**, no tu suscripción a ChatGPT.

## 📋 Pasos para Configurar OpenAI API

### 1. Obtener una Clave API

1. Ve a [OpenAI Platform](https://platform.openai.com/)
2. Inicia sesión con tu cuenta
3. Navega a **API Keys** (panel izquierdo)
4. Haz clic en **"Create new secret key"**
5. **Copia la clave inmediatamente** (no podrás verla de nuevo)

```
⚠️ ADVERTENCIA: Guarda tu API Key en un lugar seguro.
   Si alguien la obtiene, usará tus créditos.
```

### 2. Añadir Créditos a Tu Cuenta

1. Ve a [Billing](https://platform.openai.com/account/billing)
2. Añade un método de pago
3. Los primeros $5 son gratis (crédito promocional)

## 🛠️ Integración en Editores de Código

### Opción A: GitHub Copilot (Recomendado para VSCode)

El camino más sencillo si usas VSCode:

```bash
# 1. Instalar extensión GitHub Copilot en VSCode
#   - Abre VSCode → Extensiones (Ctrl+Shift+X)
#   - Busca "GitHub Copilot"
#   - Instala y autentica con tu cuenta GitHub

# 2. Configurar créditos API
#   - GitHub Copilot usa su propio sistema de facturación
#   - Plan gratuito: limitaciones
#   - Plan pago: $10/mes (incluye ChatGPT Plus)
```

### Opción B: Directamente con OpenAI API + Python

```python
import os
import openai

# Configurar API Key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Ejemplo: Generar código
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Eres un experto en desarrollo Python"},
        {"role": "user", "content": "Escribe una función para conectar a Azure Blob Storage"}
    ],
    max_tokens=500,
    temperature=0.2
)

print(response.choices[0].message.content)
```

### Opción C: Zed Editor con OpenAI

Zed tiene un panel de asistente integrado:

```markdown
# Configurar Zed Editor con OpenAI

1. Abre Zed → Settings (Cmd+,)
2. Busca "assistant"
3. Configura:
   - provider: openai
   - api_key: tu_clave_api_aqui
   - model: gpt-4o
```

## 💻 Ejemplos Prácticos por Lenguaje

### Python + OpenAI

```python
from openai import OpenAI

client = OpenAI(api_key="tu_api_key")

# Generar documentación de una función
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": """
        Documenta esta función en Google format:
        
        def connect_to_azure_storage(account_url, credential):
            from azure.storage.blob import BlobServiceClient
            return BlobServiceClient(account_url, credential)
        """}
    ]
)

print(response.choices[0].message.content)
```

### C# + OpenAI

```csharp
using OpenAI;
using OpenAI.Chat;

var client = new ChatClient("gpt-4", "tu_api_key");

var request = new ChatCompletionOptions
{
    Temperature = 0.2f,
    MaxTokens = 500
};

var messages = new List<ChatMessage>()
{
    new SystemChatMessage("Eres experto en C# y Azure"),
    new UserChatMessage("Genera un ejemplo de conexión a Azure SQL Database")
};

var response = await client.GetCompletionAsync(messages, request);

foreach (var update in response)
{
    Console.Write(update.Content);
}
```

### PowerShell + OpenAI

```powershell
# Instalar módulo
Install-Module -Name OpenAI -Scope CurrentUser

# Configurar API Key
$env:OPENAI_API_KEY = "tu_api_key"

# Generar código PowerShell
$result = Get-OpenAICompletion -Model gpt-4 -Prompt @"
Escribe un script PowerShell para listar todas las VMs en Azure
"@

Write-Output $result.Choices[0].Message.Content
```

## 📊 Costos Estimados OpenAI API

| Modelo | Precio por 1K tokens | Uso típico en VSCode |
|--------|---------------------|---------------------|
| **GPT-3.5-turbo** | $0.003 | Código sugerido |
| **GPT-4** | $0.03 | Análisis complejo |
| **GPT-4o** | $0.015 | Asistente general |

### Ejemplo de Costo Mensual

```
Uso diario: 100 solicitudes × 500 tokens = 50K tokens/día
Mes: 50K × 30 = 1.5M tokens

Costo GPT-3.5-turbo: $4.50/mes
Costo GPT-4: $45.00/mos
```

## 🔒 Buenas Prácticas de Seguridad

### 1. Nunca Commit API Keys

```bash
# .gitignore
.env
*.key
config/secrets.yml
```

### 2. Usar Variables de Entorno

```bash
# Linux/Mac
export OPENAI_API_KEY="tu_clave"

# Windows
setx OPENAI_API_KEY "tu_clave"

# En código
import os
api_key = os.environ["OPENAI_API_KEY"]
```

### 3. Usar .env Files (con python-dotenv)

```python
from dotenv import load_dotenv
load_dotenv()  # Carga variables desde .env

import os
api_key = os.environ["OPENAI_API_KEY"]
```

## ⚡ Tips de Productividad

### Prompt Templates para VSCode

```markdown
# Template: Documentar Código
"Documenta este código en formato {formato}:
{código}"

# Template: Generar Tests
"Escribe tests unitarios para esta función:
{función}"

# Template: Optimizar Código
"Optimiza este código manteniendo la funcionalidad:
{código}"
```

### Atajos Útiles

| Acción | Atajo | Editor |
|--------|-------|--------|
| Copiar línea | Ctrl+Shift+C | VSCode |
| Duplicar línea | Ctrl+D | VSCode |
| Comentar código | Ctrl+/ | Todos |
| Mover línea arriba | Alt+↑ | Todos |

## 📚 Recursos Adicionales

- [Documentación OpenAI API](https://platform.openai.com/docs/api-reference)
- [GitHub Copilot Docs](https://docs.github.com/copilot)
- [Zed Editor Assistant](https://zed.dev/docs/assistant)
- [VSCode Extensions IA](https://marketplace.visualstudio.com/search?term=ai&category=All%20categories)

## ✅ Resumen Final

| Paso | Acción | Costo |
|------|--------|-------|
| 1 | Crear cuenta OpenAI Platform | Gratis |
| 2 | Generar API Key | Gratis |
| 3 | Añadir créditos (opcional) | Desde $5 |
| 4 | Instalar extensión en editor | Gratis |
| 5 | Configurar API Key | - |

**Recuerda**: ChatGPT Plus ($20/mes) ≠ OpenAI API (pago por uso). Son servicios separados.

---
*Artículo mejorado a partir de conversación sobre integración de IA en editores.*
*Categoría: Programación*
