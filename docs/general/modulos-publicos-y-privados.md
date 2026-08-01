---
title: Módulos públicos y privados
date: 2025-03-24
category: General
slug: modulos-publicos-y-privados
tags: ['General']
---

# Módulos públicos y privados


> **Pregunta original:**
> 
En powershell que diferencias en un modulo privado y otro público

---


## Respuesta


En PowerShell, al hablar de **módulos públicos y privados**, nos referimos principalmente a cómo se organizan y exponen los **comandos (funciones, cmdlets, variables, etc.)** dentro de un módulo. La idea es separar el **código interno (privado)** del **código que quieres que los usuarios del módulo puedan usar (público)**.

---

### 📦 Estructura típica de un módulo PowerShell

Un módulo puede estar organizado así:

```
MiModulo/
│
├── MiModulo.psd1          # Archivo de manifiesto del módulo
├── MiModulo.psm1          # Archivo principal del módulo (puede importar otros archivos)
├── Public/
│   ├── Get-Cosa.ps1
│   └── Set-Cosa.ps1
└── Private/
    ├── Helper.ps1
    └── Interna.ps1
```

---

### 🧭 Diferencias entre Público y Privado

| Característica            | Público                               | Privado                                |
|---------------------------|----------------------------------------|-----------------------------------------|
| **Accesibilidad**         | Accesible para quien importe el módulo | Solo usado internamente por el módulo   |
| **Exportación**           | Se exportan explícitamente             | No se exportan                          |
| **Uso**                   | Funciones útiles para el usuario final | Funciones de soporte o internas         |
| **Ubicación común**       | Carpeta `Public/`                      | Carpeta `Private/`                      |
| **Declaración**           | Se hace `Export-ModuleMember`         | No se incluye en `Export-ModuleMember`  |

---

### 🧪 Ejemplo práctico

**Get-Cosa.ps1 (en Public/):**
```powershell
function Get-Cosa {
    param ($Nombre)

    Validar-Nombre $Nombre  # Función interna (privada)
    return "Cosa: $Nombre"
}

Export-ModuleMember -Function Get-Cosa
```

**Helper.ps1 (en Private/):**
```powershell
function Validar-Nombre {
    param ($Nombre)
    if (-not $Nombre) {
        throw "Nombre no puede estar vacío."
    }
}
```

**MiModulo.psm1:**
```powershell
# Importar funciones privadas
Get-ChildItem -Path "$PSScriptRoot\Private\*.ps1" | ForEach-Object {
    . $_.FullName
}

# Importar funciones públicas
Get-ChildItem -Path "$PSScriptRoot\Public\*.ps1" | ForEach-Object {
    . $_.FullName
}
```

---

### ✅ ¿Por qué separar público y privado?

- **Encapsulamiento**: Ocultas la lógica interna para evitar confusión o mal uso.
- **Mantenibilidad**: Facilita cambios internos sin afectar a los usuarios del módulo.
- **Claridad**: Al mirar la carpeta `Public`, sabes qué funciones puedes usar directamente.

---

¿Te gustaría que te dé una plantilla lista para usar con esta estructura?

---
*Generado desde conversación con 2 mensajes.*
*General*
