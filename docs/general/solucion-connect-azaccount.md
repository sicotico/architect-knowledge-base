---
title: Solución Connect-AzAccount
date: 2025-03-24
category: General
slug: solucion-connect-azaccount
tags: ['General']
---

# Solución Connect-AzAccount


> **Pregunta original:**
> 
como lo soluciono ?

---


## Respuesta


El error que ves:

```
Connect-AzAccount: The term 'Connect-AzAccount' is not recognized as a name of a cmdlet...
```

significa que PowerShell no reconoce el comando `Connect-AzAccount` porque el módulo **Az** no está instalado todavía.

### 🔧 Solución

Sigue estos pasos desde PowerShell (`pwsh`):

1. **Instala el módulo Az:**

   ```powershell
   Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force
   ```

   Esto instalará el módulo completo que incluye `Connect-AzAccount`.

2. **Importa el módulo (opcional, normalmente se carga solo):**

   ```powershell
   Import-Module Az
   ```

3. **Prueba el comando nuevamente:**

   ```powershell
   Connect-AzAccount -UseDeviceAuthentication -TenantId 6fafb374-8df1-44da-9bc8-9b174edc67ea
   ```

---

### 📝 Notas

- Si es la primera vez que usas PowerShell con módulos externos, puede que te pregunte si quieres confiar en el repositorio (di que sí).
- El parámetro `-Scope CurrentUser` evita que necesites permisos de administrador.

¿Quieres que revise si ya tienes el módulo instalado antes de que lo intentes?

---
*Generado desde conversación con 2 mensajes.*
*General*
