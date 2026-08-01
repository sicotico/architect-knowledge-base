---
title: Exportar Markdown a PDF/Word
date: 2025-01-16
category: General
slug: exportar-markdown-a-pdf-word
tags: ['General']
---

# Exportar Markdown a PDF/Word


> **Pregunta original:**
> 
Tengo un markdown  con imágenes en escode. Quiero exportarlo en PDF o word. ¿Como puedo hacerlo?

---


## Respuesta


Para exportar un archivo Markdown con imágenes a PDF o Word, tienes varias opciones. A continuación, te detallo las más comunes:

---

### **1. Exportar a PDF**
#### **Usando un editor de Markdown como VSCode**
1. **Extensiones necesarias:**
   - Instala la extensión **Markdown PDF** en Visual Studio Code.
2. **Pasos:**
   - Abre tu archivo Markdown en VSCode.
   - Haz clic derecho en el archivo y selecciona `Markdown PDF: Export (pdf)`.
   - El archivo será renderizado con las imágenes y convertido a PDF.

#### **Usando herramientas de línea de comandos**
- **Pandoc**: 
  - Si tienes Pandoc instalado, puedes usarlo para convertir tu Markdown a PDF:
    ```bash
    pandoc archivo.md -o archivo.pdf
    ```
  - Asegúrate de tener un sistema de renderizado como **LaTeX** instalado (por ejemplo, `TeX Live`, `MikTeX`, o `MacTeX`).
    
- **Typora**:
  - Typora es un editor de Markdown que permite exportar directamente a PDF con las imágenes incluidas.

#### **Usando herramientas en línea**
- Usa servicios en línea como [Dillinger](https://dillinger.io) o [Markdown to PDF](https://markdowntopdf.com), que soportan imágenes.

---

### **2. Exportar a Word**
#### **Usando Pandoc**
Puedes convertir el Markdown a un archivo Word (.docx) usando Pandoc:
```bash
pandoc archivo.md -o archivo.docx
```

#### **Usando Typora**
1. Abre el archivo Markdown en Typora.
2. Ve al menú `Archivo > Exportar > Word`.
3. Guarda el archivo .docx.

#### **Usando herramientas en línea**
- Usa un conversor como [Markdown to Word](https://www.markdowntoword.com) para generar un archivo Word directamente.

---

### **Consideraciones importantes**
- **Rutas de las imágenes**: Asegúrate de que las imágenes referenciadas en tu archivo Markdown tengan rutas correctas (absolutas o relativas al archivo Markdown).
- **Formato**: Si usas Pandoc y quieres personalizar el estilo del archivo Word o PDF, puedes usar plantillas de diseño.

¿Te gustaría que te ayude con un ejemplo práctico o configurando Pandoc?

---
*Generado desde conversación con 2 mensajes.*
*General*
