---
title: Instalar PowerShell en macOS
date: 2025-03-24
category: General
slug: instalar-powershell-en-macos
tags: ['General']
---

# Instalar PowerShell en macOS


> **Pregunta original:**
> 
como instalo powershell en MacOS 

---


## Respuesta


¡Claro! Instalar PowerShell en macOS es bastante sencillo. Aquí tienes las opciones más comunes para hacerlo:

---

### ✅ Opción recomendada: **Instalación con Homebrew**

1. **Abre Terminal**
2. Asegúrate de tener **Homebrew** instalado. Si no lo tienes, instálalo con:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. Luego, instala PowerShell:

   ```bash
   brew install --cask powershell
   ```

4. Una vez instalado, puedes ejecutarlo escribiendo:

   ```bash
   pwsh
   ```

---

### 🔄 Alternativa: **Instalación manual desde GitHub**

1. Ve a la página oficial de PowerShell en GitHub:  
   👉 [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)

2. Descarga el paquete `.pkg` más reciente para macOS.

3. Ábrelo e instala como cualquier otro paquete de instalación en macOS.

4. Luego, puedes abrir PowerShell desde Spotlight buscando `pwsh`.

---

### ✅ Verifica la instalación

Una vez instalado, abre Terminal y escribe:

```bash
pwsh
```

Deberías entrar en la consola de PowerShell. Para salir, simplemente escribe:

```powershell
exit
```

---

¿Quieres ayuda para configurar PowerShell como tu shell por defecto o instalar módulos útiles?

---
*Generado desde conversación con 2 mensajes.*
*General*
