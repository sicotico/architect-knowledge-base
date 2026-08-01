---
title: Extensiones para dev containers
date: 2025-09-21
category: IA/ML
slug: extensiones-para-dev-containers
tags: ['IA/ML']
---

# Extensiones para dev containers


> **Pregunta original:**
> 
Tengo un vscode y quiero usar dev containers. ¿cuales son las extensiones minimas que tengo que tener en el vscode de mi desktop?
> Necesito que lo afines a un MacOS 15

---


## Respuesta


Para trabajar con **Dev Containers** en VS Code desde tu máquina **local (desktop)** no necesitas instalar demasiadas extensiones, lo mínimo es:  

### Extensiones mínimas en tu VS Code local:
1. **Dev Containers**  
   - ID: `ms-vscode-remote.remote-containers`  
   - Esta es la extensión principal que permite abrir carpetas/proyectos dentro de un contenedor definido por un `devcontainer.json`.

---

### Opcionales (dependiendo de tu flujo):
- **Docker**  
  - ID: `ms-azuretools.vscode-docker`  
  - Útil para visualizar, manejar contenedores e imágenes desde VS Code, aunque no es obligatorio si ya manejas Docker desde la terminal.  
- **Remote Explorer**  
  - ID: `ms-vscode.remote-explorer`  
  - Facilita ver los entornos remotos, incluidos los dev containers.  

---

### Requisitos fuera de VS Code:
- Tener **Docker Desktop** (Windows/Mac) o **Docker Engine** (Linux) funcionando en tu máquina.  
- Si usas **WSL2** en Windows, necesitas que Docker esté configurado para integrarse con WSL2.  

---

👉 Con solo **Dev Containers** + **Docker funcionando en tu sistema**, ya puedes abrir proyectos con `Reopen in Container`.  

¿Quieres que te arme un ejemplo mínimo de `devcontainer.json` para arrancar tu primer entorno?
---


Si estás usando **macOS** (digamos versión 15 o cercana), para trabajar bien con Dev Containers en VS Code, te conviene tener una configuración mínima específica. Aquí lo afinamos para ese entorno:

---

## 🖥️ Requisitos mínimos en macOS

| Componente | Detalles |
|---|---|
| **macOS** | Cualquiera compatible con Docker Desktop 2.0+ (documentado para macOS) citeturn0search1turn0search0 |
| **Docker** | Tener instalado y corriendo **Docker Desktop** para Mac. Versión 2.0+ como mínimo. citeturn0search1turn0search0 |
| **VS Code** | Tener la versión reciente (uno de los builds estables, idealmente actualizado) → para evitar incompatibilidades con extensiones/remotos. |
| **Extensión Dev Containers** | La extensión oficial de Microsoft: `ms-vscode-remote.remote-containers` (o el nombre nuevo si ha cambiado, pero esa sigue siendo la identificada). citeturn0search0turn0search1 |

---

## 🔌 Extensiones mínimas extra útiles en macOS

Aunque lo estrictamente necesario es lo anterior, hay algunas extensiones adicionales que te ayudan mucho en macOS:

- **Docker** (ms-azuretools.vscode-docker) → para ver contenedores, imágenes, logs desde el UI de VS Code.  
- **Remote Explorer** → para gestionar remotamente los contenedores, explorar VPS, etc.  
- Posiblemente extensiones de lenguajes que uses (Python, Node, Go, etc.), ya que dentro del contenedor quizá quieras que ciertas extensiones estén instaladas automáticamente.

---

## ⚙️ Consideraciones específicas para macOS

- **Performance del disco**: Montar volúmenes del sistema de archivos local a contenedores en macOS puede ser lento. Docker Desktop tiene mecanismos para mejorar esto (por ejemplo, uso de volúmenes, exclusiones de paths, etc.). citeturn0search0turn0search4  
- **Compatibilidad de arquitecturas**: Si tu Mac es con chip ARM (Apple Silicon), asegúrate de que los contenedores que uses soportan ARM64, o que Docker pueda emular/usar imágenes compatibles. Algunos contenedores prehechos pueden estar sólo para x86_64.  
- **Recursos asignados en Docker**: RAM y CPU suficientes para los contenedores que uses. En Docker Desktop puedes ajustar recursos (“Settings → Resources”) si los builds o ejecución se tornan lentos.

---

Si quieres, puedo darte un checklist concreto para un MacOS 15, con versiones recomendadas y configuración del Docker Desktop para que todo vaya fluido. ¿Te lo preparo?

---
*Generado desde conversación con 4 mensajes.*
*IA/ML*
