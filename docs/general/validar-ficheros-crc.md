---
title: Validar ficheros CRC
date: 2024-12-21
category: General
slug: validar-ficheros-crc
tags: ['General']
---

# Validar ficheros CRC


> **Pregunta original:**
> 
En Jdownloder tengo ficheros que ha fallado el CRC. ¿Como puedo validar esos fichero para tenerlos?


---


## Respuesta


Cuando los ficheros descargados con JDownloader fallan en la verificación de CRC, es posible que estén incompletos o corruptos. Aquí tienes algunas estrategias para validar y, en algunos casos, recuperar estos ficheros:

---

### **1. Revisar la configuración de JDownloader**
- **Verifica las descargas incompletas:** En el panel de descargas, identifica los archivos con errores CRC y asegúrate de que las descargas no estén pausadas o incompletas.
- **Reintentar la descarga:** Haz clic derecho en el archivo con error y selecciona "Reintentar descarga". Esto puede corregir el error si el problema es temporal.

---

### **2. Comprobar archivos con WinRAR o 7-Zip**
Si el archivo descargado es un archivo comprimido (por ejemplo, `.rar` o `.zip`):
1. **Abrir el archivo:**
   - Abre el archivo con un gestor como **WinRAR** o **7-Zip**.
   - Intenta extraer los archivos. Si hay errores, el programa te notificará.
2. **Reparar el archivo:**
   - En **WinRAR**, usa la opción "Reparar archivo" desde el menú "Herramientas".
   - Esto intentará recuperar datos de archivos dañados.
3. **Extraer datos parcialmente:**
   - En WinRAR, activa la casilla de "Mantener archivos dañados" para extraer cualquier parte del archivo que sea legible.

---

### **3. Validar con la suma de verificación**
Si el archivo tiene un archivo de verificación asociado (por ejemplo, `.sfv`, `.md5`, `.sha1`):
1. Usa una herramienta como **QuickSFV** o **HashCheck** para comparar el archivo descargado con la suma de verificación proporcionada.
2. Si el archivo no coincide, vuelve a descargar las partes corruptas o inténtalo desde otra fuente.

---

### **4. Reparar partes corruptas con PAR2**
- Si los archivos están acompañados de archivos de corrección **PAR2**, puedes usar herramientas como **QuickPar** para reparar las partes corruptas.
- Abre el archivo `.par2` con QuickPar y este analizará los ficheros. Si los bloques necesarios están presentes, podrá reparar el archivo.

---

### **5. Descargar las partes corruptas nuevamente**
En JDownloader:
1. Haz clic derecho en el archivo con error CRC.
2. Selecciona "Forzar descarga" para volver a descargar las partes corruptas.
3. Si usaste un enlace contenedor (como un `.dlc`), verifica que los enlaces aún estén activos.

---

### **6. Verificar los registros de JDownloader**
- En la interfaz de JDownloader, ve a la pestaña "Registro" o busca en la carpeta `logs`.
- Analiza el registro para entender por qué falló el CRC y qué partes del archivo están afectadas.

---

### **Consejos adicionales**
- **Cambia de servidor:** Si el archivo tiene múltiples fuentes, cambia a un servidor alternativo para descargar las partes corruptas.
- **Revisar almacenamiento:** Asegúrate de que tu disco duro no tenga sectores defectuosos, ya que esto puede causar errores en la descarga.

¿Tienes algún detalle adicional sobre el tipo de archivo o error? ¡Puedo ayudarte más!

---
*Generado desde conversación con 2 mensajes.*
*General*
