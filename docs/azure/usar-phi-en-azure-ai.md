---
title: Usar Phi en Azure AI
date: 2025-02-14
category: Azure/Cloud
slug: usar-phi-en-azure-ai
tags: ['Azure/Cloud', 'azure']
---

# Usar Phi en Azure AI


> **Pregunta original:**
> 
Como puedo usar Phi en Azure AI
> Par ahcer un RAG merece la pena OpenAI o con Phi ya obtienes buenos resultados 

---


## Respuesta


Para construir un sistema **RAG (Retrieval-Augmented Generation)**, la elección entre **OpenAI (GPT-4)** y **Phi (Phi-2 o Phi-3)** depende de varios factores clave:

---

### **Comparación entre OpenAI (GPT-4) y Phi (Phi-3) para RAG**
| Factor | OpenAI (GPT-4) | Phi (Phi-3) |
|--------|--------------|------------|
| **Calidad de Generación** | ✅ Alta calidad, comprende contexto complejo | 🔹 Más ligero, pero menos sofisticado |
| **Costo** | ❌ Más caro por token | ✅ Más barato y eficiente |
| **Velocidad** | ⚖️ Depende de la carga en la API | ✅ Ligero y rápido |
| **Integración en Azure AI** | ✅ Soporte completo | ✅ Disponible, pero más reciente |
| **Contexto permitido** | ✅ Más tokens en entrada | ❌ Menor capacidad en comparación |

---

### **¿Cuándo usar OpenAI GPT-4 en RAG?**
✅ Si necesitas:
- Respuestas detalladas y precisas en consultas complejas
- Un modelo robusto para comprender contexto extenso
- Alta capacidad de razonamiento lógico

❌ **Desventaja:** Mayor costo y latencia.

---

### **¿Cuándo usar Phi-3 en RAG?**
✅ Si buscas:
- **Eficiencia y bajo costo**
- **Velocidad en generación**
- Un modelo que aún responde bien en dominios específicos

❌ **Desventaja:** Puede perder contexto en textos largos o complejos.

---

### **¿Qué opción merece más la pena?**
Si estás **probando un RAG con un presupuesto limitado**, **Phi-3** puede ser suficiente.  
Si necesitas **máxima precisión y comprensión de contexto**, OpenAI GPT-4 sigue siendo la mejor opción.

🔹 **Recomendación:** Puedes empezar con **Phi-3** y si ves que las respuestas no son lo suficientemente precisas, cambiar a **GPT-4**. También puedes hacer **un pipeline híbrido** donde Phi-3 filtra información antes de pasar a GPT-4 para la respuesta final. 🚀
---


Para utilizar los modelos Phi en Azure AI, puedes seguir estos pasos:

1. **Acceder a Azure AI Foundry**:
   - Inicia sesión en el portal de Azure AI Foundry.

2. **Seleccionar el modelo Phi deseado**:
   - En el catálogo de modelos, busca "Phi" y elige el modelo que mejor se adapte a tus necesidades.

3. **Implementar el modelo**:
   - Tienes dos opciones para la implementación:
     - **API sin servidor**: Ideal para consumir el modelo como una API sin necesidad de alojarlo en tu suscripción.
     - **Proceso administrado autohospedado**: Te permite personalizar y controlar todos los detalles sobre cómo se sirve el modelo.

4. **Ajuste fino del modelo (opcional)**:
   - Si deseas personalizar el modelo para tareas específicas, puedes realizar un ajuste fino:
     - Selecciona la opción "Ajuste fino" en la página del modelo.
     - Proporciona un nombre para el modelo ajustado.
     - Configura los parámetros de entrenamiento según tus necesidades.
     - Inicia el proceso de ajuste fino.

5. **Evaluar el modelo ajustado**:
   - Es recomendable evaluar la seguridad y el rendimiento del modelo ajustado para asegurarte de que cumple con los estándares deseados.

Para una guía visual sobre la implementación de un modelo Phi, puedes consultar el siguiente video:

videoImplementación de Phi-3.5 Mini en Azure AI Studioturn0search5

---
*Generado desde conversación con 4 mensajes.*
*Azure/Cloud*
