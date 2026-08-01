---
title: Problemas GNS3 Windows 11
date: 2026-06-01
category: General
slug: problemas-gns3-windows-11
tags: ['General']
---

# Problemas GNS3 Windows 11


> **Pregunta original:**
> 
GNS3 en Windows 11, hice un proyecto y ahor ano me aprece para cargarlo y tamco me inicia la GNS3 VM 
> he dado 2blockick al fchero gns3

---


## Respuesta


Si en **GNS3 para Windows 11** te han desaparecido proyectos y además la **GNS3 VM no arranca**, pueden ser dos problemas relacionados o independientes.

## 1. Verifica si el proyecto sigue en disco

Primero revisa dónde guarda GNS3 los proyectos:

- Abre GNS3.
- Ve a **Edit > Preferences > General > Project directory**.
- Comprueba la ruta configurada.

Normalmente suele ser algo parecido a:

```text
C:\Users\TU_USUARIO\GNS3\projects
```

o

```text
Documents\GNS3\projects
```

Mira con el Explorador de Windows si allí siguen existiendo carpetas con el nombre de tu proyecto.

Si encuentras la carpeta:

1. En GNS3 selecciona **File > Open Project**.
2. Busca el archivo `.gns3` dentro de esa carpeta.

Si no aparece ningún proyecto, puede que la ruta de proyectos haya cambiado después de una actualización o reinstalación.

---

## 2. Comprueba si la GNS3 VM existe todavía

¿Qué hipervisor usas?

- VMware Workstation
- VirtualBox
- Hyper-V

Abre el hipervisor directamente y verifica si sigue existiendo una máquina llamada algo similar a:

- **GNS3 VM**
- **GNS3 VM 2.x**

Si no aparece, GNS3 no podrá iniciarla.

---

## 3. Revisa la configuración de la VM en GNS3

En GNS3:

**Edit > Preferences > GNS3 VM**

Comprueba:

- "Enable the GNS3 VM" activado.
- Hipervisor correcto seleccionado.
- Nombre de la VM correcto.

Si aparece un error al arrancar, dime el mensaje exacto.

---

## 4. Conflicto típico en Windows 11

Windows 11 suele causar problemas con VMware y VirtualBox cuando están activados:

- Hyper-V
- Windows Hypervisor Platform
- Virtual Machine Platform
- WSL2

Si usas VMware o VirtualBox y la VM dejó de arrancar tras una actualización de Windows, revisa:

**Panel de control > Programas > Activar o desactivar características de Windows**

y dime cuáles de estas opciones tienes marcadas:

- Hyper-V
- Virtual Machine Platform
- Windows Hypervisor Platform
- Windows Sandbox

---

## 5. Recuperar proyectos aunque la VM no arranque

Los proyectos de GNS3 suelen ser simplemente carpetas con:

```text
nombre_proyecto.gns3
project-files\
```

Aunque la GNS3 VM esté rota, normalmente los proyectos siguen estando en disco y pueden recuperarse.

---

Para identificar la causa exacta, dime:

1. Qué versión de GNS3 tienes.
2. Si usas VMware, VirtualBox o Hyper-V.
3. Qué error aparece al arrancar la GNS3 VM.
4. Si la carpeta de tu proyecto sigue existiendo en el disco.
---


La captura muestra claramente el problema:

```text
Client version 2.2.54 is not the same as server (controller) version 2.2.59
```

y además:

```text
Cannot open a .gns3 file on a remote server
```

## Qué ha ocurrido

Has hecho doble clic sobre un archivo `.gns3` y GNS3 ha intentado abrirlo usando un **servidor/controlador 2.2.59**, mientras que tu cliente gráfico es **2.2.54**.

Tienes una instalación mezclada:

| Componente | Versión |
|------------|----------|
| Cliente GNS3 (GUI) | 2.2.54 |
| Controller/Server | 2.2.59 |

GNS3 exige que ambas versiones coincidan.

---

## Solución 1 (la más probable)

Actualiza el cliente GNS3 a la misma versión que el servidor.

Ve a:

**Help → About**

y confirma las versiones.

Después instala la versión **2.2.59** completa.

---

## Solución 2: revisar qué servidor está arrancando

A veces queda un servidor antiguo ejecutándose.

Cierra GNS3 completamente.

Abre PowerShell y ejecuta:

```powershell
taskkill /F /IM gns3server.exe
taskkill /F /IM gns3.exe
```

Luego vuelve a abrir GNS3.

---

## Solución 3: abrir el proyecto correctamente

El mensaje:

```text
Cannot open a .gns3 file on a remote server
```

indica que has abierto directamente el fichero `.gns3` desde Windows Explorer.

En lugar de eso:

1. Inicia GNS3.
2. File → Open Project.
3. Selecciona la carpeta del proyecto.

o

1. File → Open Recent.
2. Busca el proyecto.

---

## Verifica dónde está tu proyecto

Busca el archivo `.gns3` que abriste.

Normalmente estará en algo parecido a:

```text
C:\Users\TU_USUARIO\GNS3\projects\
```

Si la carpeta existe, el proyecto no está perdido.

---

## Sobre la GNS3 VM

Todavía no sabemos si la VM está rota o simplemente no puede comunicarse por el conflicto de versiones.

Haz una captura de:

**Edit → Preferences → GNS3 VM**

o dime:

- ¿Usas VMware Workstation?
- ¿Usas VirtualBox?
- ¿Usas Hyper-V?

Con esa información puedo indicarte exactamente cómo volver a enlazar la GNS3 VM y recuperar el proyecto.

---
*Generado desde conversación con 4 mensajes.*
*General*
