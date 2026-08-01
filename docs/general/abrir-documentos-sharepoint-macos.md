---
title: Abrir documentos SharePoint MacOS
date: 2024-12-02
category: General
slug: abrir-documentos-sharepoint-macos
tags: ['General']
---

# Abrir documentos SharePoint MacOS


> **Pregunta original:**
> 
Estoy en MacOS con la web de Sharepint y quiero abrir documentos con aplicaciones instaladas en el equipo.
Safari no me abre aplicaciones de escritorio asociadas al tipo de archivos, me devuelve este erro:

Safari no puede abrir la página porque la dirección no es válida.

> Como puedo decirle al Safari que los archivo de MArkdaw se abran coin una aplicación 

---


## Respuesta


El error que mencionas en Safari se debe a que las aplicaciones web como SharePoint intentan usar un protocolo específico para abrir aplicaciones de escritorio (como `ms-word:` o `ms-excel:`), pero Safari puede bloquear o no reconocer correctamente estas solicitudes. Para resolver este problema y abrir documentos desde SharePoint con las aplicaciones de escritorio en tu Mac, puedes seguir estos pasos:

---

### **Soluciones posibles**

1. **Asegúrate de tener instalado Office para Mac:**
   - Descarga e instala Microsoft Office si no lo tienes. Necesitas Word, Excel o la aplicación específica para abrir los documentos.

2. **Usa Microsoft Edge o Google Chrome en lugar de Safari:**
   - Microsoft Edge y Google Chrome manejan mejor los enlaces de protocolo personalizados (`ms-word:`, `ms-excel:`, etc.) que SharePoint usa para abrir documentos.
   - Puedes descargar Microsoft Edge desde [su sitio oficial](https://www.microsoft.com/edge).

3. **Habilita los complementos en Safari:**
   - Abre Safari y ve a **Preferencias** > **Extensiones**.
   - Asegúrate de que cualquier extensión relacionada con Office o SharePoint esté habilitada.

4. **Configura SharePoint para abrir documentos en aplicaciones de escritorio:**
   - Ve al documento en SharePoint.
   - Haz clic en los tres puntos al lado del documento o selecciona **Abrir en aplicación de escritorio** (a menudo es una opción directamente en el menú de SharePoint).
   - Esto debería intentar abrir el documento en la aplicación de escritorio asociada.

5. **Habilita los protocolos personalizados para Safari (si corresponde):**
   - Safari a veces no permite los enlaces `ms-word:` o `ms-excel:`. Puedes intentar forzarlo siguiendo estos pasos:
     - Asegúrate de que Safari esté actualizado a la última versión.
     - Ve a **Preferencias** > **Seguridad** y desactiva cualquier bloqueo relacionado con enlaces no estándar (esto es raro, pero puede ser un problema en configuraciones específicas).

6. **Verifica los permisos de SharePoint y tu cuenta:**
   - Asegúrate de que tu cuenta tenga los permisos necesarios para abrir documentos con las aplicaciones de escritorio.
   - Si SharePoint no tiene configurada la apertura de documentos en aplicaciones de escritorio, pídele al administrador que revise las configuraciones de la biblioteca de documentos.

7. **Usa la aplicación de OneDrive:**
   - Si tienes OneDrive configurado en tu Mac, sincroniza los archivos desde SharePoint y ábrelos localmente desde la carpeta de OneDrive.

---

Si después de probar estas soluciones sigues teniendo problemas, avísame, y exploraremos ajustes más avanzados o específicos de tu configuración.
---


Safari, al igual que otros navegadores, no tiene una configuración directa para abrir archivos de un tipo específico con una aplicación instalada. Sin embargo, puedes lograrlo combinando algunas configuraciones en macOS y ajustes específicos para Safari. Aquí te explico cómo hacerlo:

---

### **1. Asignar la aplicación predeterminada para archivos Markdown**
Esto asegura que macOS sepa qué aplicación usar al abrir archivos `.md` desde cualquier lugar.

1. **Selecciona un archivo Markdown (.md):**
   - Encuentra un archivo Markdown en tu Mac.

2. **Haz clic derecho sobre el archivo y selecciona "Obtener información":**
   - O presiona `Cmd + I` con el archivo seleccionado.

3. **Configura la aplicación predeterminada:**
   - En la sección "Abrir con", selecciona la aplicación que quieres usar (por ejemplo, Visual Studio Code, Obsidian, o cualquier editor que tengas instalado).
   - Haz clic en el botón **Cambiar todo...** para aplicar esta configuración a todos los archivos `.md`.

---

### **2. Configurar Safari para manejar archivos Markdown**
Safari no abre directamente archivos con aplicaciones externas, pero puedes hacer que descargue los archivos en lugar de mostrarlos en el navegador. Una vez descargados, macOS usará la aplicación predeterminada configurada.

1. **Ve a las preferencias de Safari:**
   - Abre Safari y ve a **Safari > Preferencias > General**.

2. **Configura las descargas automáticas:**
   - En la opción **Guardar archivos descargados en**, selecciona una carpeta (por ejemplo, Descargas).

3. **Permite que Safari descargue archivos Markdown:**
   - Intenta abrir un archivo Markdown desde una web. Si Safari muestra el contenido directamente, haz clic derecho y selecciona **Descargar archivo enlazado**.
   - Si quieres automatizarlo, puedes crear un script para que macOS abra automáticamente los archivos descargados.

---

### **3. Usar una extensión de navegador (opcional)**
Si trabajas con Markdown frecuentemente y necesitas más control sobre cómo se abren los archivos:

1. Instala una extensión de navegador como [Open in Default App](https://apps.apple.com) o cualquier otra extensión que permita redirigir enlaces.
2. Configura la extensión para que identifique archivos `.md` y los abra automáticamente con la aplicación seleccionada.

---

### **4. Crear un flujo de trabajo con Automator (opcional)**
Si quieres más automatización, puedes usar Automator para forzar la apertura de archivos descargados:

1. Abre Automator y crea un nuevo **Flujo de trabajo de carpeta**.
2. Selecciona la carpeta donde se descargan los archivos (por ejemplo, Descargas).
3. Añade la acción **Abrir archivo** y selecciona la aplicación que quieras para los archivos `.md`.
4. Guarda el flujo de trabajo.

Cuando descargues un archivo Markdown, Automator lo abrirá automáticamente con la aplicación configurada.

---

Con estas opciones, puedes lograr que Safari maneje los archivos Markdown de la manera que prefieres, ya sea descargándolos automáticamente o abriéndolos con la aplicación correspondiente. Si necesitas ayuda para implementar alguno de estos pasos, no dudes en pedírmelo.

---
*Generado desde conversación con 4 mensajes.*
*General*
