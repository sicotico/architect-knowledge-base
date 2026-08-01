---
title: RAG en LM Studio
date: 2025-02-09
category: General
slug: rag-en-lm-studio
tags: ['General']
---

# RAG en LM Studio


> **Pregunta original:**
> 
Describe el RAG de LM Studio

---


## Respuesta


La Generación Aumentada por Recuperación (RAG, por sus siglas en inglés) es una técnica que mejora las capacidades de los Modelos de Lenguaje de gran tamaño (LLMs) al permitirles acceder a información externa relevante durante el proceso de generación de texto. Esto se logra recuperando fragmentos pertinentes de documentos extensos o múltiples fuentes y proporcionándolos al modelo como referencia, lo que enriquece y contextualiza sus respuestas. citeturn0search3

En LM Studio, a partir de la versión 0.3.0, se ha incorporado la funcionalidad de RAG para facilitar la interacción con documentos. Al adjuntar archivos en formatos como `.docx`, `.pdf` o `.txt` a una sesión de chat, el modelo puede utilizarlos como contexto adicional. Si el documento es lo suficientemente breve y cabe en la ventana de contexto del modelo, LM Studio incluirá el contenido completo en la conversación. Para documentos más extensos, se emplea RAG para extraer y proporcionar al modelo las secciones más relevantes del texto. citeturn0search1

Para optimizar el uso de RAG en LM Studio, es recomendable que las consultas incluyan términos, ideas y palabras clave presentes en el material fuente relevante. Esta práctica aumenta la probabilidad de que el sistema proporcione al modelo el contexto más útil y pertinente. La experimentación es clave para determinar las estrategias más efectivas según el caso de uso específico. citeturn0search1

Para una guía visual sobre cómo utilizar RAG en LM Studio, puedes consultar el siguiente tutorial:

videoTutorial sobre RAG en LM Studioturn0search2

---
*Generado desde conversación con 2 mensajes.*
*General*
