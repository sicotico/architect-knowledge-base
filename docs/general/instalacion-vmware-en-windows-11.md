---
title: Instalación VMware en Windows 11
date: 2026-06-08
category: General
slug: instalacion-vmware-en-windows-11
tags: ['General']
---

# Instalación VMware en Windows 11


> **Pregunta original:**
> 
Es un equipo que no uso WSL ni Docker , en GNS3 voy a usar todo libre, OPNsense , OpenWRT y algún cliente alpine 
>  Get-CimInstance -ClassName Win32_DeviceGuard | Format-List *
Get-CimInstance: La clase especificada no existe.
PS C:\Users\Luis> Get-CimInstance Win32_DeviceGuard | Select-Object *
Get-CimInstance: La clase especificada no existe.
PS C:\Users\Luis>

 reg query "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard"

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard
    CachedDrtmAuthIndex    REG_DWORD    0x0
    RequireMicrosoftSignedBootChain    REG_DWORD    0x1
    WasEnabledBy    REG_DWORD    0x1
    EnableVirtualizationBasedSecurity    REG_DWORD    0x1
    HyperVVirtualizationBasedSecurityOptout    REG_DWORD    0x0

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios
> estoy instaldo vmware workstation en windows 11 y me sale este mensaje , el cual no entiendo  
> 
> *...y 10 preguntas de seguimiento*


---


## Respuesta


Si te vuelve a salir **exactamente el mismo mensaje que mostraste al principio**, entonces VMware sigue detectando un hipervisor de Windows activo.

Eso encaja con lo que vimos en `systeminfo`:

```text
Seguridad basada en virtualización: Estado: En ejecución
Services Running:
    Credential Guard
```

Por tanto, a día de hoy tu sistema **no está limpio de VBS/Credential Guard**.

## Lo bueno

Ese mensaje es una **advertencia**, no un bloqueo.

Puedes instalar VMware, importar la GNS3 VM y probablemente funcionará.

## Lo malo

No estamos en la configuración óptima para GNS3:

- Algo más de sobrecarga.
- Menor rendimiento en escenarios grandes.
- Posibles problemas con virtualización anidada.
- Mayor consumo de CPU al ejecutar varias appliances simultáneamente.

## Lo que haría ahora

No perdería más tiempo intentando eliminar VBS hasta comprobar si realmente te afecta.

1. Termina la instalación.
2. Importa la GNS3 VM.
3. Arráncala.
4. Comprueba que GNS3 detecta correctamente la VM.

Dentro de GNS3:

```text
Edit → Preferences → GNS3 VM
```

Debería aparecer:

```text
GNS3 VM is running
```

en verde.

## Prueba importante

Cuando la GNS3 VM arranque, abre la consola de la VM y ejecuta:

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

Si devuelve un número mayor que 0 (por ejemplo 4, 8, 12...), la VM está viendo las extensiones de virtualización del procesador.

Eso es mucho más relevante para GNS3 que el mensaje del instalador.

---

Mi sospecha es que estás ante una instalación moderna de Windows 11 donde Credential Guard sigue activo por diseño. Antes de entrar en cambios más agresivos (políticas locales, BIOS, Secure Launch, etc.), comprobaría primero si la GNS3 VM funciona correctamente. Si arranca y ve VT-x, probablemente no merece la pena seguir peleando con Windows.
---


Perfecto. Los cambios se han aplicado correctamente.

Ahora lo importante es:

1. **Reiniciar el equipo.**
2. Abrir una consola después del reinicio.
3. Ejecutar:

```cmd
systeminfo
```

y comprobar si siguen apareciendo estas líneas:

```text
Seguridad basada en virtualización: Estado: En ejecución
```

y

```text
Se detectó un hipervisor.
```

### Si desaparecen

Has eliminado correctamente VBS/Credential Guard y VMware podrá usar VT-x/AMD-V directamente, que es lo que interesa para GNS3.

### Si siguen apareciendo

Habrá que revisar si el Latitude tiene alguna configuración de BIOS/UEFI relacionada con:

- Virtualization Based Security (VBS)
- Credential Guard
- Secure Launch
- Dell SafeBIOS / herramientas corporativas

Pero primero merece la pena comprobar el resultado tras este reinicio, porque en muchos casos estos dos cambios de registro son suficientes.

Cuando vuelvas a arrancar, pégame únicamente estas dos secciones de `systeminfo`:

```text
Seguridad basada en virtualización
```

y

```text
Requisitos Hyper-V
```

Con eso sabremos inmediatamente si el sistema ya está listo para VMware + GNS3 VM.
---


En ese caso, **sí desactivaría Hyper-V y las funciones relacionadas**.

Tu escenario es bastante favorable:

- No usas WSL2.
- No usas Docker Desktop.
- Vas a ejecutar GNS3 VM en VMware.
- Las máquinas previstas (OPNsense, OpenWrt, Alpine Linux) se benefician de una virtualización más directa y con menos capas.

## Lo que haría

### 1. Desactivar características de Windows

Ve a:

**Panel de control → Programas → Activar o desactivar las características de Windows**

Desmarca:

- Hyper-V
- Windows Hypervisor Platform
- Virtual Machine Platform
- Windows Sandbox (si está activado)

Reinicia.

### 2. Desactivar Integridad de memoria

Ve a:

**Seguridad de Windows → Seguridad del dispositivo → Aislamiento del núcleo**

Desactiva:

- Integridad de memoria

Reinicia nuevamente.

### 3. Verificar que Hyper-V ya no está cargado

Abre una consola como administrador:

```cmd
systeminfo
```

Ya no debería aparecer el mensaje:

```text
Se ha detectado un hipervisor.
```

### 4. Confirmar en VMware

Una vez instalado VMware y creada la GNS3 VM, en:

**VM → Settings → Processors**

Deberías poder activar opciones como:

```text
Virtualize Intel VT-x/EPT or AMD-V/RVI
```

sin advertencias relacionadas con Hyper-V.

---

## Ventajas para tu laboratorio

Con OPNsense, OpenWrt y Alpine no vas a necesitar una máquina extremadamente potente, pero sí te interesa:

- Menor consumo de CPU.
- Menor latencia entre nodos.
- Arranque más rápido de las VMs.
- Menos problemas al usar interfaces virtuales y redes complejas de GNS3.

La diferencia puede no ser enorme en un laboratorio pequeño, pero ya que no dependes de WSL2 ni Docker, no hay prácticamente ninguna razón para mantener Hyper-V activo.

## Un método rápido (línea de comandos)

Si quieres desactivar el hipervisor sin tocar demasiadas opciones, abre CMD como administrador:

```cmd
bcdedit /set hypervisorlaunchtype off
```

y reinicia.

Para volver a activarlo en el futuro:

```cmd
bcdedit /set hypervisorlaunchtype auto
```

Es una forma rápida de probar antes de hacer cambios más profundos.

Mi recomendación para un equipo dedicado a GNS3 con VMware y appliances como OPNsense/OpenWrt es: **instala VMware, desactiva Hyper-V y trabaja con VMware usando VT-x/AMD-V directamente.** Es la configuración que suele dar menos problemas.
---


Perfecto. Entonces estás usando **VMware Workstation Pro 26H1**, que es la versión más reciente de la rama actual. VMware introdujo varios cambios importantes en esta versión, incluyendo una transición completa a binarios de 64 bits para Windows y mejoras en la detección del entorno de virtualización del host. citeturn0search0turn0search12

Dado todo lo que hemos visto:

- Hyper-V clásico está deshabilitado (`hypervisorlaunchtype Off`).
- HVCI está deshabilitado.
- Las claves habituales de Credential Guard están desactivadas o ausentes.
- Sin embargo Windows sigue reportando VBS/Credential Guard en ejecución.

Yo dejaría de perseguir el problema desde Windows por el momento y haría una prueba real con VMware.

## Prueba que nos sacará de dudas

1. Termina de instalar VMware 26H1.
2. Importa la GNS3 VM.
3. Arranca la GNS3 VM.
4. Comprueba si aparece alguno de estos mensajes:
   - "VMware is running with Hyper-V enabled"
   - "Windows Hypervisor Platform is active"
   - "User Level Monitor Mode"
   - "Virtualized Intel VT-x/EPT is not supported"

5. En VMware abre:

```text
VM > Settings > Processors
```

y revisa si puedes activar opciones relacionadas con:

```text
Virtualize Intel VT-x/EPT
```

sin errores.

## Qué espero en tu caso

Con un Dell Latitude 5420, VMware 26H1 y Windows 11 Pro reciente, es posible que `systeminfo` siga mostrando un hipervisor activo aunque VMware funcione correctamente con aceleración por hardware. VMware ha mejorado mucho la convivencia con las características de seguridad modernas de Windows. citeturn0search0turn0search19

Por tanto, el siguiente dato realmente útil ya no es `systeminfo`, sino:

- ¿La GNS3 VM arranca?
- ¿Qué mensaje muestra VMware al arrancarla?
- ¿Qué aparece en la pestaña **Processors**?

Cuando tengas VMware instalado y la GNS3 VM creada, envíame una captura de cualquier advertencia o de la ventana **Processors** y podremos confirmar si el entorno está listo para OPNsense, OpenWrt y Alpine.
---


Bien. Ahora sabemos que **no era simplemente Hyper-V ni la clave principal de Device Guard**.

Lo relevante es:

```text
Seguridad basada en virtualización: Estado: En ejecución
Services Running:
    Credential Guard
```

y además:

```text
App Control for Business policy: Forzado
```

Eso sugiere que Windows sigue aplicando una política de seguridad adicional. En equipos Dell corporativos o instalaciones que provienen de una imagen empresarial, esto no es raro.

## Vamos a localizar exactamente qué queda activo

Ejecuta estos comandos y pega la salida:

### 1. Estado de LSA

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa"
```

### 2. Estado de Credential Guard

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\CredentialGuard"
```

### 3. Estado de HVCI

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity"
```

---

## Mientras tanto: una observación práctica

Aunque `systeminfo` siga mostrando el hipervisor, **instala VMware Workstation y prueba la GNS3 VM**.

Lo que realmente nos interesa es si VMware muestra mensajes como:

- "VMware is running in User Level Monitor Mode"
- "Windows Hypervisor Platform is active"
- "VMware Workstation and Hyper-V are not compatible"

o si por el contrario detecta VT-x/EPT normalmente.

Hay casos en Windows 11 recientes donde `systeminfo` sigue reportando un hipervisor activo, pero VMware 17 funciona correctamente con aceleración por hardware.

Por tanto, haría ambas cosas en paralelo:

1. Instalar VMware y comprobar qué dice.
2. Revisar las tres claves del registro anteriores.

Con esas salidas podremos determinar si queda únicamente Credential Guard o si también hay HVCI/App Control manteniendo VBS activo.
---


La salida confirma que **todavía tienes el hipervisor de Windows activo**.

Las líneas clave son:

```text
Seguridad basada en virtualización: Estado: En ejecución
Services Running:
    Credential Guard
```

y

```text
Requisitos Hyper-V:
Se detectó un hipervisor.
```

Por tanto, aunque hayas desactivado Hyper-V y ejecutado:

```cmd
bcdedit /set hypervisorlaunchtype off
```

algo sigue forzando la carga del hipervisor, concretamente **Credential Guard / VBS (Virtualization-Based Security)**.

## Comprueba primero el valor actual

Abre CMD como administrador:

```cmd
bcdedit
```

Busca la línea:

```text
hypervisorlaunchtype
```

Debería aparecer:

```text
hypervisorlaunchtype    Off
```

Si aparece `Auto`, el cambio no se aplicó.

---

## Lo más probable en Windows 11 Pro

Windows puede volver a activar VBS aunque Hyper-V esté desmarcado.

Abre:

```text
gpedit.msc
```

Ve a:

```text
Configuración del equipo
 └ Plantillas administrativas
    └ Sistema
       └ Device Guard
```

Abre:

```text
Activar seguridad basada en virtualización
```

y selecciona:

```text
Deshabilitada
```

Aplica y reinicia.

---

## Método rápido para verificar

Abre PowerShell como administrador:

```powershell
Get-CimInstance Win32_DeviceGuard
```

Pégame el resultado.

Con ese comando puedo ver exactamente qué componente de VBS sigue activo (Credential Guard, HVCI, Device Guard, etc.) y decirte qué falta por deshabilitar para que VMware use VT-x/AMD-V directamente.
---


Los resultados son interesantes porque descartan varias cosas:

### Ya sabemos que NO es

- Hyper-V clásico → deshabilitado (`hypervisorlaunchtype Off`).
- HVCI / Memory Integrity → deshabilitado (`Enabled = 0`).
- Credential Guard configurado mediante la clave habitual → la clave ni siquiera existe.
- LsaCfgFlags → está a `0`.

Sin embargo Windows sigue diciendo:

```text
Seguridad basada en virtualización: Estado: En ejecución
Services Running:
    Credential Guard
```

Eso apunta a que tu Windows 11 está usando el **nuevo mecanismo de Credential Guard por defecto** (Microsoft ha cambiado bastante esto en versiones recientes de Windows 11).

## Mi recomendación práctica

Antes de seguir persiguiendo el último resto de VBS:

### Instala VMware Workstation

Después mira qué ocurre al arrancar una VM.

En VMware ve a:

```text
Help → About VMware Workstation
```

y comprueba que sea VMware 17.x.

Luego arranca cualquier VM (o la GNS3 VM) y revisa si aparece algún mensaje relacionado con:

- Hyper-V
- Windows Hypervisor Platform
- User Level Monitor Mode

### Verifica desde VMware

Dentro de VMware:

```text
VM → Settings → Processors
```

Si ves opciones como:

```text
Virtualize Intel VT-x/EPT
```

y no aparecen advertencias, probablemente estés bien.

---

## Por qué digo esto

Tu salida de Windows es inconsistente:

| Componente | Estado |
|------------|---------|
| Hyper-V | Desactivado |
| HVCI | Desactivado |
| LsaCfgFlags | 0 |
| CredentialGuard key | No existe |
| systeminfo | Dice que Credential Guard corre |

Eso me hace pensar que estás en una compilación moderna de Windows 11 donde parte de VBS permanece activa por diseño.

La pregunta importante ya no es "¿queda algo de VBS?" sino:

> ¿VMware está usando la virtualización por hardware correctamente?

Porque para GNS3 eso es lo que realmente importa.

## Siguiente paso

Instala VMware Workstation y dime:

1. La versión exacta (17.5.x, 17.6.x, etc.).
2. Si durante la instalación vuelve a salir el mensaje de Hyper-V.
3. Si la GNS3 VM arranca sin advertencias.

Con eso podremos determinar si merece la pena seguir eliminando VBS o si el sistema ya está en un estado perfectamente válido para tu laboratorio.
---


Has encontrado la pista importante.

La clave es esta:

```text
EnableVirtualizationBasedSecurity    REG_DWORD    0x1
```

Ese valor significa que **VBS (Virtualization Based Security) sigue activado**, aunque la directiva local aparezca como "No configurada".

Además:

```text
WasEnabledBy    REG_DWORD    0x1
```

indica que fue habilitado anteriormente por Windows, una política o alguna herramienta de endurecimiento de seguridad.

## Lo extraño

El error:

```text
Get-CimInstance: La clase especificada no existe.
```

no es normal en Windows 11 Pro. No es grave para nuestro objetivo, pero impide usar ese método de diagnóstico.

## Lo que haría ahora

Abre CMD como administrador y ejecuta:

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard" /v EnableVirtualizationBasedSecurity /t REG_DWORD /d 0 /f
```

Luego:

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v LsaCfgFlags /t REG_DWORD /d 0 /f
```

Después reinicia.

## Tras el reinicio

Vuelve a ejecutar:

```cmd
systeminfo
```

y revisa estas dos líneas:

```text
Seguridad basada en virtualización
```

y

```text
Requisitos Hyper-V
```

### Resultado esperado

Lo ideal sería algo parecido a:

```text
Seguridad basada en virtualización: No habilitada
```

o

```text
Estado: No habilitada
```

y que desaparezca:

```text
Se detectó un hipervisor.
```

## Si sigue apareciendo

En equipos Dell corporativos a veces intervienen además:

- Credential Guard persistente
- Secure Launch
- Configuraciones UEFI/BIOS relacionadas con VBS

Pero antes de tocar BIOS, probaría el cambio de registro porque es la solución más frecuente cuando ya has deshabilitado Hyper-V y las características de Windows.

Por cierto, veo que es un **Dell Latitude 5420**. Para GNS3 con OPNsense, OpenWrt y Alpine, ese equipo debería ir razonablemente bien con 16 GB de RAM, pero te recomendaría asignar inicialmente a la GNS3 VM:

- 4 vCPU
- 6–8 GB RAM

y dejar el resto para Windows. Con varios routers/firewalls simultáneos notarás más limitación por memoria que por CPU.
---


Ya está claro: **Hyper-V sigue activo a través de VBS/Credential Guard**, no por la característica Hyper-V clásica.

Las pruebas son concluyentes:

- `hypervisorlaunchtype Off` ✅
- `Seguridad basada en virtualización: Estado: En ejecución` ❌
- `Services Running: Credential Guard` ❌
- `Se detectó un hipervisor` ❌

Eso significa que Windows está arrancando un hipervisor para soportar Credential Guard.

## Lo que falta comprobar

Ejecuta PowerShell como administrador:

```powershell
Get-CimInstance -ClassName Win32_DeviceGuard | Format-List *
```

o

```powershell
Get-CimInstance Win32_DeviceGuard | Select-Object *
```

Necesito ver especialmente los campos:

- `SecurityServicesConfigured`
- `SecurityServicesRunning`
- `VirtualizationBasedSecurityStatus`

## Mientras tanto, revisa esto

Abre:

```text
gpedit.msc
```

y ve a:

```text
Configuración del equipo
 └ Plantillas administrativas
    └ Sistema
       └ Device Guard
```

Mira el estado de:

```text
Activar seguridad basada en virtualización
```

Si aparece:

- Habilitada → ese es el problema.
- No configurada → hay otra fuente activándola.
- Deshabilitada → hay otra política o configuración persistente.

## Otra comprobación rápida

Abre una consola de administrador:

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard"
```

y pega el resultado.

---

### Sobre GNS3

Aunque VMware probablemente funcione así, para un laboratorio de redes con:

- OPNsense
- OpenWrt
- Alpine Linux

yo intentaría dejar el sistema sin VBS ni Credential Guard. En un Latitude 5420 con 16 GB de RAM cada recurso cuenta, y VMware suele comportarse mejor cuando tiene acceso directo a VT-x/EPT sin la capa de virtualización de Windows.

Pásame la salida de `Get-CimInstance Win32_DeviceGuard | Format-List *` y localizamos exactamente qué componente está manteniendo vivo el hipervisor.
---


Perfecto. El valor:

```text
hypervisorlaunchtype    Off
```

indica que **tu comando se aplicó correctamente**.

Sin embargo, hay una contradicción:

- `bcdedit` dice que el hipervisor no debe arrancar.
- `systeminfo` dice que hay un hipervisor activo y que **Credential Guard** está ejecutándose.

Esto suele ocurrir cuando Windows ha dejado activa la **Seguridad basada en virtualización (VBS)** mediante una política o configuración que no se deshabilitó completamente.

## Lo siguiente que comprobaría

Abre PowerShell como administrador y ejecuta:

```powershell
Get-CimInstance -ClassName Win32_DeviceGuard
```

o bien:

```powershell
Get-CimInstance Win32_DeviceGuard | Format-List *
```

Pégame la salida completa.

### Lo que espero encontrar

Alguno de estos componentes seguirá activo:

- Credential Guard
- Hypervisor-Enforced Code Integrity (HVCI)
- Device Guard
- VBS

Una vez vea esa salida podré decirte exactamente qué falta por desactivar.

## Mientras tanto

Si acabas de hacer los cambios y **solo has reiniciado una vez**, también existe la posibilidad de que Windows todavía no haya terminado de aplicar todas las modificaciones.

Haz una comprobación rápida:

1. Reinicia una segunda vez.
2. Ejecuta:

```cmd
systeminfo
```

Si sigue apareciendo:

```text
Se detectó un hipervisor.
```

entonces tendremos la confirmación de que VBS/Credential Guard sigue activo y necesitaremos revisar la salida de `Get-CimInstance Win32_DeviceGuard`.

Por ahora, no instalaría la GNS3 VM hasta verificar esto, porque merece la pena dejar VMware limpio de Hyper-V antes de empezar.
---


Correcto. Hacer **todos los cambios y luego un único reinicio** es lo más eficiente.

Después del reinicio, te recomiendo verificar tres cosas:

### 1. Comprobar que el hipervisor ya no está activo

Abre una consola y ejecuta:

```cmd
systeminfo
```

Si todo ha salido bien, **no debería aparecer** la línea:

```text
Se ha detectado un hipervisor.
```

### 2. Verificar VMware

Instala o abre VMware Workstation y comprueba que no aparezcan mensajes como:

- "VMware Workstation and Hyper-V are not compatible"
- "Running with Windows Hypervisor Platform"

Si no aparecen, buena señal.

### 3. Verificar la GNS3 VM

Cuando importes la GNS3 VM:

- En VMware → **Settings → Processors**
- Comprueba que VMware detecta correctamente la virtualización por hardware.
- Asigna recursos razonables:
  - 2 vCPU y 4 GB RAM para laboratorios pequeños.
  - 4 vCPU y 8 GB RAM si vas a tener varias instancias de OPNsense/OpenWrt simultáneamente.

---

Si después del reinicio ejecutas:

```cmd
systeminfo
```

y me pegas las últimas 15-20 líneas de la salida, puedo confirmar si Hyper-V ha quedado realmente desactivado o si todavía queda alguna característica de virtualización basada en Windows activa.
---


Para **GNS3 VM**, mi recomendación suele ser distinta que para un uso normal de VMware.

## Recomendación: desactivar Hyper-V

GNS3 VM suele funcionar mejor cuando VMware tiene acceso directo a las extensiones de virtualización del procesador (**Intel VT-x** o **AMD-V**) y no depende del hipervisor de Windows.

**Ventajas de desactivar Hyper-V para GNS3:**
- Mejor rendimiento general.
- Menos problemas con dispositivos Cisco, Juniper, Fortinet, etc.
- Mejor compatibilidad con virtualización anidada.
- Menos errores al arrancar appliances pesadas (IOSv, IOS-XRv, CSR1000v, vMX, vSRX, etc.).

## Antes de desactivarlo, revisa si realmente está activo

Abre PowerShell como administrador y ejecuta:

```powershell
systeminfo
```

Al final busca algo parecido a:

```text
Se ha detectado un hipervisor.
```

o

```text
A hypervisor has been detected.
```

Si aparece, Windows está usando Hyper-V.

## Qué desactivar

En **Activar o desactivar características de Windows**:

- Hyper-V
- Virtual Machine Platform
- Windows Hypervisor Platform
- Windows Sandbox (si no la usas)

Y en:

**Seguridad de Windows → Seguridad del dispositivo → Aislamiento del núcleo**

- Integridad de memoria = Desactivada

Después reinicia.

## Si también usas WSL2 o Docker

Aquí aparece el inconveniente:

| Función | Requiere Hyper-V |
|----------|----------|
| WSL2 | Sí |
| Docker Desktop | Sí |
| GNS3 VM en VMware (máximo rendimiento) | Mejor sin Hyper-V |

Si utilizas mucho WSL2 o Docker, hay que valorar el compromiso.

## Mi criterio práctico

- **PC dedicado a laboratorios de redes (GNS3/EVE-NG/CML):** desactiva Hyper-V.
- **PC para desarrollo con Docker y WSL2:** prueba primero con Hyper-V activado; si GNS3 va lento o da problemas, entonces desactívalo.

Indícame:
- Modelo de CPU (por ejemplo, i7-12700H, Ryzen 7 5800X, etc.).
- VMware Workstation 17 Pro o Player.
- Qué imágenes vas a correr en GNS3 (IOSv, CSR1000v, FortiGate, vMX, etc.).

Y te digo si merece la pena desactivar Hyper-V en tu caso concreto.
---


Ese mensaje no es un error. VMware te está informando de cómo va a funcionar en tu equipo.

El texto dice:

> "El instalador detectó que el host tiene habilitado Hyper-V o Device/Credential Guard. Las máquinas virtuales se iniciarán mediante Windows Plataforma de Hipervisor."

### ¿Qué significa?

En tu Windows 11 está activada alguna de estas características:

- **Hyper-V**
- **Windows Hypervisor Platform**
- **Virtual Machine Platform**
- **Credential Guard**
- **Core Isolation / Integridad de memoria**

Cuando VMware detecta eso, no puede usar directamente su propio motor de virtualización tradicional (VT-x/AMD-V), así que utiliza el hipervisor de Windows.

### ¿Es un problema?

**No necesariamente.**

**Ventajas:**
- VMware funcionará igualmente.
- No necesitas cambiar nada para usar máquinas virtuales básicas.

**Desventajas:**
- El rendimiento puede ser algo inferior.
- Algunas funciones avanzadas pueden no estar disponibles o funcionar peor.
- Algunas VM exigentes (laboratorios, virtualización anidada, etc.) pueden rendir menos.

### ¿Qué debes hacer?

Si solo quieres instalar VMware y ejecutar Windows o Linux dentro de una VM:

➡️ Pulsa **"Siguiente"** y continúa con la instalación.

### ¿Y si quiero el máximo rendimiento?

Tendrías que desactivar Hyper-V y algunas funciones de seguridad de Windows, por ejemplo:

- Hyper-V
- Virtual Machine Platform
- Windows Hypervisor Platform
- Credential Guard
- Integridad de memoria (Aislamiento del núcleo)

Pero esto puede afectar otras funciones de Windows (WSL2, Docker Desktop, seguridad basada en virtualización, etc.).

### Recomendación

Instala VMware normalmente y prueba una máquina virtual. Solo si notas problemas de rendimiento merece la pena plantearse desactivar Hyper-V.

Si me dices:
- La versión de VMware (17 Pro, 16, etc.)
- Tu procesador (Intel o AMD y modelo)
- Qué sistema operativo quieres virtualizar

puedo decirte si te conviene dejar Hyper-V activado o desactivarlo.

---
*Generado desde conversación con 26 mensajes.*
*General*
