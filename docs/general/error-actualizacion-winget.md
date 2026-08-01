---
title: Error actualización winget
date: 2026-06-09
category: General
slug: error-actualizacion-winget
tags: ['General']
---

# Error actualización winget


> **Pregunta original:**
> 
Crea un comando o script de powershell para revisar si tengo deshabilitado toda la seguridad de  windos y aislamiento  de memoria y todo y el firewall y el defender.

Enteoria sí pero quiero confirmalo 
> esto todo el log seguido :

PowerShell 7.6.2
PS C:\Users\sico> winget update
Error al intentar actualizar el origen: winget
Nombre              Id                                      Versión Disponible Origen
-------------------------------------------------------------------------------------
Raspberry Pi Imager RaspberryPiFoundation.RaspberryPiImager v2.0.7  2.0.8      winget
1 actualizaciones disponibles.
PS C:\Users\sico> winget upgrade -r
Error al intentar actualizar el origen: winget
Nombre              Id                                      Versión Disponible Origen
-------------------------------------------------------------------------------------
Raspberry Pi Imager RaspberryPiFoundation.RaspberryPiImager v2.0.7  2.0.8      winget
1 actualizaciones disponibles.

(1/1) Encontrado Raspberry Pi Imager [RaspberryPiFoundation.RaspberryPiImager] Versión 2.0.8
El propietario de esta aplicación le concede una licencia.
Microsoft no es responsable, ni tampoco concede ninguna licencia de paquetes de terceros.
Descargando https://github.com/raspberrypi/rpi-imager/releases/download/v2.0.8/imager-v2.0.8.exe
  ██████████████████████████████  19.7 MB / 19.7 MB
El hash del instalador se verificó correctamente
Iniciando instalación de paquete...
El instalador solicitará que se ejecute como administrador. Espere una indicación.
Instalado correctamente

PS C:\Users\sico> winget source reset --force
Este comando requiere que se ejecuten privilegios de administrador.
PS C:\Users\sico> winget update
Error al intentar actualizar el origen: winget
El origen 'msstore' requiere que vea los siguientes contratos antes de usarlo.
Terms of Transaction: https://aka.ms/microsoft-store-terms-of-transaction
El origen requiere que la región geográfica de dos letras de la máquina actual se envíe al servicio back-end para que funcione correctamente (por ejemplo, "EE. UU.").

¿Está de acuerdo con todos los términos de los contratos de origen?
[Y] Sí  [N] No: Y
No se encontró ningún paquete que coincida con los criterios de entrada.
PS C:\Users\sico> winget update
Error al intentar actualizar el origen: winget
No se encontró ningún paquete que coincida con los criterios de entrada.
PS C:\Users\sico> winget upgrade
Error al intentar actualizar el origen: winget
No se encontró ningún paquete que coincida con los criterios de entrada.
PS C:\Users\sico>
> PowerShell 7.6.2
PS C:\Users\sico> Get-AppxPackage Microsoft.DesktopAppInstaller | Reset-AppxPackage
PS C:\Users\sico> Get-AppxPackage Microsoft.DesktopAppInstaller | Foreach {
>>     Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppxManifest.xml"
>> }
PS C:\Users\sico> winget source update
Actualizando todos los orígenes...
Actualizando origen: msstore...
Listo
Actualizando origen: winget...
  ██████████████████████████████  100%
Listo
Actualizando origen: winget-font...
  ██████████████████████████████  100%
Listo
PS C:\Users\sico>
> 
> *...y 5 preguntas de seguimiento*


---


## Respuesta


El log da una pista importante:

### Lo que funciona

- Winget encuentra paquetes.
- Winget descarga paquetes.
- Winget instala paquetes.
- La actualización de Raspberry Pi Imager se ha completado correctamente.

Por tanto, **Winget no está roto**.

### Lo que falla

Solo falla la actualización del origen:

```
Error al intentar actualizar el origen: winget
```

pero inmediatamente después sigue consultando ese mismo origen y encuentra paquetes:

```
Origen: winget
```

Eso suele indicar que:

- la caché local del origen está dañada, o
- hay un problema de sincronización con el repositorio, pero Winget puede usar los datos ya almacenados.

### Lo siguiente que haría

Ejecuta estos dos comandos y pega la salida:

```powershell
winget source list
```

```powershell
winget --info
```

Especialmente nos interesa ver:

- versión de Winget
- versión de App Installer
- estado de los orígenes (`winget` y `msstore`)

### Mientras tanto

Abre una consola **como Administrador** y ejecuta:

```powershell
winget source reset --force
```

Si termina correctamente:

```powershell
winget source update
```

y comprueba:

```powershell
winget source list
```

### Valoración

Lo bueno:
- Has podido actualizar Raspberry Pi Imager sin problemas.
- No hay indicios de corrupción grave de Winget.

Lo malo:
- El origen `winget` sigue fallando al refrescarse.
- El problema persistirá hasta reparar el origen o reinstalar App Installer.

Con `winget source list` y `winget --info` podremos saber si merece la pena reparar la instalación de App Installer o simplemente reconstruir los orígenes.
---


La información de `winget --info` parece normal:

- Winget: **1.28.240**
- App Installer: **1.28.240.0**
- Windows: **10.0.26200.8524**
- No hay configuraciones extrañas activadas.
- Los orígenes existen y el `source reset` funcionó.

Lo que resulta extraño es esto:

```text
Error al intentar actualizar el origen: winget
```

pero al mismo tiempo Winget fue capaz de:

- Encontrar Raspberry Pi Imager.
- Descargarlo desde GitHub.
- Verificar el hash.
- Instalarlo.

Eso sugiere que el problema está únicamente en la actualización del índice del repositorio, no en el funcionamiento general de Winget.

### Falta una prueba clave

Ejecuta:

```powershell
winget source update
```

y pega la salida completa.

### También revisaría la conectividad al CDN

Desde PowerShell:

```powershell
Test-NetConnection cdn.winget.microsoft.com -Port 443
```

Debe devolver algo parecido a:

```text
TcpTestSucceeded : True
```

### Ver los logs de Winget

Busca el error exacto:

```powershell
Get-ChildItem "$env:LOCALAPPDATA\Packages\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\LocalState\DiagOutputDir" | Sort-Object LastWriteTime -Descending | Select-Object -First 5
```

Después abre el más reciente:

```powershell
Get-Content "RUTA_DEL_LOG" -Tail 100
```

(o pega el nombre del archivo y te indico el comando exacto).

### Mi valoración

**Lo bueno**
- No parece una instalación dañada.
- App Installer está actualizado.
- Los orígenes están registrados correctamente.
- Las instalaciones y actualizaciones funcionan.

**Lo malo**
- El origen `winget` no está sincronizando correctamente.
- El mensaje persiste incluso después de un `source reset`, por lo que probablemente sea un problema de conectividad al CDN o un error registrado en los logs.

En este momento, `winget source update` y el resultado de `Test-NetConnection` son las dos pruebas más útiles. Si además puedes sacar las últimas líneas del log, probablemente podremos identificar la causa exacta.
---


Lo que veo es que ahora el problema ha cambiado:

- Ya has aceptado las condiciones de `msstore`.
- El error sigue siendo **"Error al intentar actualizar el origen: winget"**.
- Además, `winget update` responde *"No se encontró ningún paquete que coincida con los criterios de entrada"*.

Hay dos detalles importantes:

### 1. `winget update` no es el comando correcto para listar actualizaciones

Prueba:

```powershell
winget upgrade
```

o

```powershell
winget upgrade --include-unknown
```

`upgrade` es el comando estándar para ver paquetes actualizables.

### 2. Necesitamos ver el estado de los orígenes

Ejecuta:

```powershell
winget source list
```

y también:

```powershell
winget --info
```

Pega aquí la salida completa.

### 3. Si el origen `winget` aparece dañado

Abre **PowerShell como Administrador** (no una ventana normal) y ejecuta:

```powershell
winget source reset --force
```

Después:

```powershell
winget source update
```

### 4. Posible causa frecuente

Muchas veces este error aparece porque la aplicación de Windows que contiene Winget está dañada o desactualizada:

urlApp Installer (Microsoft)https://apps.microsoft.com/detail/9NBLGGH4NNS1

Comprueba en:

**Configuración → Aplicaciones → Aplicaciones instaladas → App Installer**

y dime qué versión tienes.

Por ahora, los dos comandos más útiles son:

```powershell
winget source list
```

```powershell
winget --info
```

Con esa salida podremos ver si el origen `winget` falta, está corrupto o simplemente no puede sincronizarse.
---


El mensaje indica dos cosas distintas:

1. **Winget ha detectado una actualización**
   - `Raspberry Pi Imager` está en la versión `2.0.7`.
   - Hay disponible la versión `2.0.8`.

2. **Ha fallado la actualización del origen (source) "winget"**
   - Esto afecta a la sincronización del repositorio de paquetes.
   - No necesariamente impide instalar o actualizar paquetes si la información ya está en caché.

Prueba estos comandos en una consola de PowerShell o Terminal como administrador:

```powershell
winget source reset --force
```

Después:

```powershell
winget source update
```

Y verifica:

```powershell
winget source list
```

Para actualizar el programa directamente:

```powershell
winget upgrade RaspberryPiFoundation.RaspberryPiImager
```

O todas las aplicaciones:

```powershell
winget upgrade --all
```

Si sigue apareciendo **"Error al intentar actualizar el origen: winget"**, ejecuta:

```powershell
winget --info
```

y pega aquí la salida completa. Con esa información se puede determinar si el problema es:
- una caché corrupta de winget,
- el origen `winget` dañado,
- un problema de red/proxy,
- o una instalación defectuosa de **App Installer**.
---


Puedes ejecutar este script en PowerShell **como Administrador**. No modifica nada; solo muestra el estado de las principales protecciones de Windows.

```powershell
Write-Host "`n=== MICROSOFT DEFENDER ===" -ForegroundColor Cyan

try {
    $mp = Get-MpComputerStatus

    [PSCustomObject]@{
        AntivirusEnabled          = $mp.AntivirusEnabled
        RealTimeProtectionEnabled = $mp.RealTimeProtectionEnabled
        BehaviorMonitorEnabled    = $mp.BehaviorMonitorEnabled
        IOAVProtectionEnabled     = $mp.IoavProtectionEnabled
        ScriptScanningEnabled     = $mp.ScriptScanningEnabled
        TamperProtection          = $mp.IsTamperProtected
    } | Format-List
}
catch {
    Write-Host "Defender no disponible o eliminado." -ForegroundColor Yellow
}

Write-Host "`n=== FIREWALL ===" -ForegroundColor Cyan

Get-NetFirewallProfile |
Select-Object Name, Enabled |
Format-Table -AutoSize

Write-Host "`n=== AISLAMIENTO DE MEMORIA (HVCI) ===" -ForegroundColor Cyan

try {
    $hvci = Get-ItemProperty `
        -Path "HKLM:\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity" `
        -Name Enabled -ErrorAction Stop

    if ($hvci.Enabled -eq 1) {
        "Aislamiento de memoria: ACTIVADO"
    }
    else {
        "Aislamiento de memoria: DESACTIVADO"
    }
}
catch {
    "Aislamiento de memoria: NO CONFIGURADO"
}

Write-Host "`n=== VBS / DEVICE GUARD ===" -ForegroundColor Cyan

try {
    $dg = Get-CimInstance Win32_DeviceGuard

    [PSCustomObject]@{
        VBS_Running = ($dg.VirtualizationBasedSecurityStatus -eq 2)
        SecurityServicesRunning = ($dg.SecurityServicesRunning -join ",")
        SecurityServicesConfigured = ($dg.SecurityServicesConfigured -join ",")
    } | Format-List
}
catch {
    Write-Host "No se pudo consultar Device Guard."
}

Write-Host "`n=== WINDOWS SECURITY SERVICES ===" -ForegroundColor Cyan

Get-Service WinDefend,mpssvc,SecurityHealthService -ErrorAction SilentlyContinue |
Select Name, Status, StartType |
Format-Table -AutoSize

Write-Host "`n=== RESUMEN ===" -ForegroundColor Green

$firewallEnabled = (Get-NetFirewallProfile | Where-Object Enabled).Count

if ($firewallEnabled -eq 0) {
    Write-Host "Firewall: DESACTIVADO"
}
else {
    Write-Host "Firewall: ACTIVADO"
}

try {
    $mp = Get-MpComputerStatus

    if (-not $mp.RealTimeProtectionEnabled) {
        Write-Host "Protección en tiempo real: DESACTIVADA"
    }
    else {
        Write-Host "Protección en tiempo real: ACTIVADA"
    }
}
catch {
    Write-Host "Defender: NO DISPONIBLE"
}
```

Si quieres una comprobación más agresiva, que devuelva algo tipo:

```text
Defender ............ OFF
Firewall ............ OFF
Tamper Protection ... OFF
VBS ................. OFF
Memory Integrity .... OFF
SmartScreen ......... OFF
Core Isolation ...... OFF
BitLocker ........... OFF
```

puedo prepararte un script más completo que revise prácticamente todas las capas de seguridad de Windows 11 en una sola pantalla.
---


Ya tenemos la causa.

El error no es de red ni del CDN. La descarga funciona perfectamente:

```text
Download completed.
Result for trust info validation of the msix: 0
```

El fallo ocurre justo después, cuando Windows intenta registrar el paquete descargado:

```text
0x80070005 Acceso denegado
Operation failed: error al abrir el paquete desde la ubicación
Microsoft.Winget.Source_8wekyb3d8bbwe.msix
```

## Diagnóstico

Winget descarga correctamente:

- `Microsoft.Winget.Source_8wekyb3d8bbwe.msix`
- `Microsoft.Winget.Fonts.Source_8wekyb3d8bbwe.msix`

Pero Windows devuelve:

```text
0x80070005 = E_ACCESSDENIED
```

Esto suele deberse a uno de estos motivos:

1. Permisos incorrectos en el perfil de usuario.
2. Algún antivirus o protección antiransomware bloqueando la instalación de MSIX.
3. Registro corrupto de App Installer.
4. Algún problema con los servicios de despliegue de paquetes AppX.

## Lo primero que probaría

Abre PowerShell **como Administrador** y ejecuta:

```powershell
Get-AppxPackage Microsoft.DesktopAppInstaller | Reset-AppxPackage
```

Si tu versión de Windows no reconoce `Reset-AppxPackage`, usa:

```powershell
Get-AppxPackage Microsoft.DesktopAppInstaller | Foreach {
    Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppxManifest.xml"
}
```

Después:

```powershell
winget source update
```

## Comprobar si hay antivirus interfiriendo

¿Usas únicamente Microsoft Defender o tienes algo como:

- Bitdefender
- ESET
- Avast
- Kaspersky
- Malwarebytes

instalado?

El patrón de tu log encaja bastante con software de seguridad bloqueando la instalación temporal del MSIX descargado.

## Otra comprobación rápida

Ejecuta:

```powershell
Get-Service AppXSvc,ClipSVC | Select Name,Status
```

Deberías obtener algo parecido a:

```text
Name     Status
----     ------
AppXSvc  Running
ClipSVC  Running
```

## Lo que sabemos con certeza

**Bien:**

- Winget funciona.
- Las actualizaciones funcionan.
- El CDN responde.
- Los certificados son válidos.
- La descarga es correcta.

**Mal:**

- Windows rechaza registrar los paquetes `Microsoft.Winget.Source` y `Microsoft.Winget.Fonts`.
- El error exacto es `0x80070005 (Access Denied)` durante el despliegue AppX/MSIX.

El siguiente paso más útil es que me pegues la salida de:

```powershell
Get-Service AppXSvc,ClipSVC | Select Name,Status
```

y me digas si tienes algún antivirus de terceros instalado. Con eso probablemente podamos aislar la causa definitiva.
---


Perfecto. Ya está identificado y resuelto.

El problema era que el paquete de Winget/App Installer estaba registrado de forma inconsistente. El síntoma en el log era:

```text
0x80070005 Acceso denegado
Microsoft.Winget.Source_8wekyb3d8bbwe.msix
```

Al ejecutar:

```powershell
Get-AppxPackage Microsoft.DesktopAppInstaller | Foreach {
    Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppxManifest.xml"
}
```

has vuelto a registrar correctamente **App Installer**, y ahora:

```text
Actualizando origen: winget...      Listo
Actualizando origen: winget-font... Listo
```

confirma que los paquetes `Microsoft.Winget.Source` y `Microsoft.Winget.Fonts` ya pueden instalarse y actualizarse.

Haz una última comprobación:

```powershell
winget upgrade
```

Lo esperado es:

- que no aparezca ya el mensaje:
  ```text
  Error al intentar actualizar el origen: winget
  ```
- y que simplemente liste actualizaciones o indique que no hay ninguna.

En resumen:

| Estado | Antes | Ahora |
|----------|----------|----------|
| Descarga desde CDN | ✔ | ✔ |
| Actualización de paquetes | ✔ | ✔ |
| Actualización de origen winget | ✘ | ✔ |
| Actualización de winget-font | ✘ | ✔ |
| Error 0x80070005 | ✘ | Resuelto |

El comando que ha solucionado el problema es el re-registro de **Microsoft.DesktopAppInstaller**. Si vuelve a ocurrir tras una actualización de Windows Insider (tu compilación `26200` sugiere que estás en un canal de pruebas), ya sabes cuál es la reparación rápida.
---


Esto es una buena señal:

```text
winget source reset --force
Restableciendo todos los orígenes...Listo
```

Ahora el comando se ha ejecutado correctamente y los orígenes existen:

```text
msstore
winget
winget-font
```

Eso descarta que el origen esté desaparecido o corrupto de forma grave.

Lo que todavía falta comprobar es si después del reset sigue fallando la sincronización. Ejecuta:

```powershell
winget source update
```

y después:

```powershell
winget upgrade
```

Si vuelve a aparecer:

```text
Error al intentar actualizar el origen: winget
```

necesito ver también:

```powershell
winget --info
```

porque en ese punto el problema suele estar en uno de estos sitios:

1. **App Installer desactualizado o dañado** (lo más frecuente).
2. Proxy/VPN/firewall bloqueando el acceso a:
   - `cdn.winget.microsoft.com`
3. Caché local dañada pese al reset.
4. Un bug concreto de la versión de Winget instalada.

De momento, lo positivo es que:

- Has actualizado Raspberry Pi Imager correctamente.
- El reset de orígenes ha funcionado.
- Winget sigue siendo plenamente utilizable para instalar y actualizar paquetes.

Lo negativo es que todavía no sabemos si el error de actualización del origen ha desaparecido tras el reset, porque falta ver el resultado de:

```powershell
winget source update
```

y de:

```powershell
winget --info
```

Pega ambas salidas completas.

---
*Generado desde conversación con 16 mensajes.*
*General*
