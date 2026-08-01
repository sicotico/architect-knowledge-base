---
title: Comando agregar PATH Windows
date: 2026-05-14
category: General
slug: comando-agregar-path-windows
tags: ['General']
---

# Comando agregar PATH Windows


> **Pregunta original:**
> 
 To run "pi", add the global bin folder to $PATH:

C:\\Users\\sico\\.bun\\bin

dame el comando para hacer esto en windows 111

---


## Respuesta


En Windows 11 tienes dos formas habituales: temporal (solo para la terminal actual) o permanente.

## Temporal (solo sesión actual de PowerShell)

```powershell
$env:Path += ";C:\Users\sico\.bun\bin"
```

## Permanente para tu usuario (recomendado)

### Desde PowerShell

```powershell
[Environment]::SetEnvironmentVariable(
  "Path",
  $env:Path + ";C:\Users\sico\.bun\bin",
  "User"
)
```

Después:

1. Cierra la terminal.
2. Abre una nueva ventana de PowerShell o CMD.
3. Comprueba:

```powershell
echo $env:Path
```

o:

```powershell
pi --version
```

## Alternativa desde CMD

```cmd
setx PATH "%PATH%;C:\Users\sico\.bun\bin"
```

Limitaciones de `setx`:
- A veces recorta variables PATH muy largas.
- No actualiza la sesión actual; necesitas abrir otra terminal.

En Windows 11 normalmente es más seguro usar PowerShell con `SetEnvironmentVariable`.

---
*Generado desde conversación con 2 mensajes.*
*General*
