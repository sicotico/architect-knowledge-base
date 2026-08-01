---
title: Codium vs VS Code
date: 2025-02-08
category: Comparativas
slug: codium-vs-vs-code
tags: ['Comparativas']
---

# Codium vs VS Code


> **Pregunta original:**
> 
Que diferencia hay en codium y vscode
> Como s epuede deshabilitar la tlemetria de VS Code

---


## Respuesta


### Diferencias entre **Codium** y **VS Code**:

1. **Código Fuente y Licencia**:
   - **Codium**: Es una bifurcación de **Visual Studio Code** sin telemetría y completamente de código abierto bajo la licencia MIT.
   - **VS Code**: Aunque su código fuente es abierto (repositorio de Microsoft en GitHub), la versión binaria oficial incluye componentes propietarios y telemetría.

2. **Telemetría y Privacidad**:
   - **Codium**: No incluye rastreo ni recopilación de datos por parte de Microsoft.
   - **VS Code**: Incluye telemetría que envía datos a Microsoft a menos que se desactive manualmente.

3. **Extensiones y Marketplace**:
   - **Codium**: No tiene acceso directo a la tienda de extensiones de Microsoft, pero puede usar **Open VSX Registry**, una alternativa libre.
   - **VS Code**: Usa el marketplace oficial de Microsoft, con más extensiones disponibles.

4. **Compatibilidad y Soporte**:
   - **Codium**: Es compatible con la mayoría de las extensiones de VS Code, aunque algunas dependen de servicios de Microsoft y podrían no funcionar.
   - **VS Code**: Totalmente compatible con todas las extensiones del marketplace de Microsoft.

5. **Actualizaciones y Distribución**:
   - **Codium**: Se actualiza con cada nueva versión de VS Code, pero sin el branding y los servicios de Microsoft.
   - **VS Code**: Microsoft lanza actualizaciones regulares con soporte oficial.

### **¿Cuál elegir?**
- **Codium** es ideal para quienes buscan **privacidad y código 100% abierto**.
- **VS Code** es mejor si necesitas **todas las extensiones del marketplace de Microsoft** y no te importa la telemetría.

Si prefieres un entorno más libre y sin telemetría, **Codium** es una excelente opción. Si necesitas el soporte completo de Microsoft y su ecosistema, **VS Code** es la mejor elección. 🚀
---


Para **deshabilitar la telemetría** en **VS Code**, sigue estos pasos:

---

### 🔹 **Método 1: Desde la Configuración de VS Code**
1. **Abrir VS Code**.
2. **Ir a la configuración**:
   - En Windows/Linux: `Ctrl + ,`
   - En macOS: `Cmd + ,`
3. **Buscar "telemetry"** en la barra de búsqueda.
4. **Deshabilitar la opción**:  
   - Encuentra `telemetry.telemetryLevel` y selecciona `"off"`.

---

### 🔹 **Método 2: Editando settings.json**
1. Abre la paleta de comandos con:
   - Windows/Linux: `Ctrl + Shift + P`
   - macOS: `Cmd + Shift + P`
2. Escribe: **"Preferences: Open Settings (JSON)"** y selecciona la opción.
3. Agrega o edita la siguiente línea:
   ```json
   "telemetry.telemetryLevel": "off"
   ```
4. Guarda y cierra el archivo.

---

### 🔹 **Método 3: Usando la Línea de Comandos**
Si prefieres hacerlo desde la terminal, ejecuta:
```sh
code --disable-telemetry
```
Esto desactiva la telemetría solo en esa sesión.

---

### 🔹 **Método 4: Bloquear los Servidores de Telemetría**
Si quieres asegurarte de que VS Code no envíe datos, puedes **bloquear los dominios de Microsoft** en tu archivo `hosts`:

1. Abre el archivo **hosts**:
   - Windows: `C:\Windows\System32\drivers\etc\hosts`
   - Linux/macOS: `/etc/hosts`
2. Agrega estas líneas al final:
   ```
   0.0.0.0 vortex.data.microsoft.com
   0.0.0.0 vscode-telemetry.azurewebsites.net
   ```
3. Guarda los cambios y reinicia tu computadora.

---

Con estos pasos, la telemetría de **VS Code quedará completamente desactivada**. 🚀🔒

---
*Generado desde conversación con 4 mensajes.*
*Comparativas*
