---
title: Imprimir dos imágenes folio
date: 2024-11-07
category: General
slug: imprimir-dos-imagenes-folio
tags: ['General']
---

# Imprimir dos imágenes folio


> **Pregunta original:**
> 
Como puedo imprmir 2 imagenes en la misma cara de un folio en windows 
> como reinicio el servicio de impresar de windows 11

---


## Respuesta


Para imprimir dos imágenes en la misma cara de un folio en Windows, puedes utilizar varias opciones. Aquí tienes un método utilizando Microsoft Word y otro con el Visor de Fotos de Windows.

### Opción 1: Usando Microsoft Word

1. **Abre Microsoft Word** y crea un nuevo documento.
2. **Inserta las imágenes**:
   - Ve a la pestaña *Insertar* y selecciona *Imágenes*.
   - Elige las dos imágenes que quieres imprimir y añádelas al documento.
3. **Organiza las imágenes**:
   - Ajusta el tamaño de las imágenes para que ambas quepan en la misma página.
   - Puedes moverlas una al lado de la otra, una encima de la otra, o donde prefieras.
4. **Configura la impresión**:
   - Ve a *Archivo* > *Imprimir* y selecciona la impresora.
   - Asegúrate de seleccionar una página por hoja.
5. **Imprime el documento**. Deberías ver ambas imágenes impresas en la misma página del folio.

### Opción 2: Usando el Visor de Fotos de Windows

1. **Selecciona las imágenes**:
   - Encuentra las imágenes que quieres imprimir en el Explorador de Archivos.
   - Selecciona ambas imágenes manteniendo presionada la tecla *Ctrl* mientras haces clic en cada una.
2. **Abrir con el Visor de Fotos**:
   - Haz clic derecho en una de las imágenes seleccionadas, luego elige *Imprimir* en el menú contextual.
3. **Configura la impresión**:
   - En el menú de impresión, elige una opción de *Diseño de impresión* que permita dos imágenes en una sola página, como "2 por página" o "Dos imágenes por hoja".
   - Asegúrate de tener seleccionada la opción de papel adecuada, normalmente *A4* o el tamaño de papel que uses.
4. **Imprime**. Esto imprimirá las dos imágenes en la misma cara del folio.

Ambos métodos te permitirán tener dos imágenes en una sola página. La elección dependerá de si prefieres usar Word para más opciones de personalización o el Visor de Fotos de Windows para un enfoque más directo.
---


Para reiniciar el servicio de impresión en Windows 11, puedes seguir estos pasos:

### Método 1: Usando la herramienta Servicios

1. **Abre la herramienta Servicios**:
   - Presiona `Win + R` para abrir el cuadro de diálogo *Ejecutar*.
   - Escribe `services.msc` y presiona *Enter*.

2. **Busca el servicio de cola de impresión**:
   - En la lista de servicios, busca uno llamado **Cola de impresión** o **Print Spooler**.
   
3. **Reinicia el servicio**:
   - Haz clic derecho en **Cola de impresión** y selecciona *Reiniciar*.
   - Si no ves la opción de *Reiniciar*, selecciona *Detener*, espera unos segundos, y luego selecciona *Iniciar*.

Esto reiniciará el servicio de impresión y, en muchos casos, resolverá problemas de impresión.

### Método 2: Usando el Símbolo del sistema (CMD)

1. **Abre el Símbolo del sistema como administrador**:
   - Escribe "CMD" en la barra de búsqueda de Windows, haz clic derecho sobre el *Símbolo del sistema* y selecciona *Ejecutar como administrador*.

2. **Ejecuta los comandos para reiniciar el servicio**:
   - Escribe el siguiente comando para detener el servicio de cola de impresión y presiona *Enter*:
     ```cmd
     net stop spooler
     ```
   - Luego, escribe este comando para iniciar el servicio nuevamente:
     ```cmd
     net start spooler
     ```

Este método es rápido y útil si prefieres usar la línea de comandos.

### Método 3: Reiniciar desde Configuración de Impresoras

Si estos métodos no resuelven el problema, puedes intentar reiniciar la impresora desde la configuración de Windows:

1. **Abre la Configuración de impresoras**:
   - Ve a *Configuración* > *Bluetooth e impresoras* > *Impresoras y escáneres*.

2. **Selecciona la impresora con problemas** y realiza una prueba de impresión para verificar que el servicio funciona correctamente.

Con cualquiera de estos métodos, podrás reiniciar el servicio de impresión y resolver problemas comunes de impresión en Windows 11.

---
*Generado desde conversación con 4 mensajes.*
*General*
