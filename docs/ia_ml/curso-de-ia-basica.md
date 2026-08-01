---
title: Curso de IA Básica
date: 2024-10-16
category: IA/ML
slug: curso-de-ia-basica
tags: ['IA/ML']
---

# Curso de IA Básica


> **Pregunta original:**
> 
Eres un profesor con muchos años de experiencia en didáctica. Quiero un Curso de IA, con principal orientación a ejecutar en local.
Hoy empieza con los conceptos básicos 
> El siguiente capítulo quiero lo básico para entender los tipos de modelos (huggface), la herramientas para ejecutar los LLMs en local


---


## Respuesta


### Curso de Inteligencia Artificial (IA) – Módulo 1: Conceptos Básicos de IA

---

### Introducción al Curso
Este curso tiene como objetivo enseñar los conceptos fundamentales de la Inteligencia Artificial (IA), con un enfoque en cómo ejecutar algoritmos y aplicaciones de IA de manera local, es decir, en tu propia computadora o servidor, sin depender necesariamente de servicios en la nube.

A lo largo de las sesiones, aprenderás los principios básicos de la IA, explorarás algoritmos clave y técnicas de Machine Learning, y pondrás en práctica tus conocimientos implementando tus propios modelos de IA utilizando herramientas y bibliotecas ampliamente utilizadas como Python, TensorFlow, PyTorch, y otros.

---

### **Clase 1: Conceptos Fundamentales de la Inteligencia Artificial**

---

#### **1. ¿Qué es la Inteligencia Artificial?**
La **Inteligencia Artificial (IA)** es el campo de la informática que se enfoca en la creación de sistemas capaces de realizar tareas que normalmente requieren inteligencia humana. Estas tareas incluyen el reconocimiento de voz, la toma de decisiones, la resolución de problemas, la comprensión del lenguaje, la percepción visual, entre otras.

Hay tres tipos de IA:

1. **IA Débil o IA Específica**: Diseñada para realizar tareas específicas (por ejemplo, asistentes de voz, software de reconocimiento facial).
2. **IA Fuerte o IA General**: Especulativa en este momento, se refiere a sistemas con capacidad cognitiva general, similar a la humana.
3. **Superinteligencia Artificial**: Hipotética, se refiere a una IA que supera la inteligencia humana en todos los aspectos.

---

#### **2. Áreas Principales dentro de la IA**
Dentro de la IA, existen varias áreas clave:

- **Machine Learning (ML)**: Rama de la IA que permite a las máquinas aprender a partir de datos sin ser programadas explícitamente.
- **Deep Learning (DL)**: Subcampo del ML que usa redes neuronales profundas para modelar datos de alta complejidad.
- **Procesamiento del Lenguaje Natural (NLP)**: Permite a las máquinas comprender y generar lenguaje humano.
- **Visión por Computadora (Computer Vision)**: Habilidad de los sistemas para interpretar y comprender imágenes y videos.
- **Sistemas Expertos**: Programas diseñados para tomar decisiones en un área específica basados en conocimientos expertos.

---

#### **3. Componentes Clave de la IA**
Para desarrollar sistemas de IA, es esencial comprender algunos de los conceptos clave que permiten que estos funcionen:

1. **Datos**: La IA se alimenta de datos. Cuanto más diversos y numerosos sean, más preciso será el modelo.
   
2. **Algoritmos**: Son las reglas y operaciones que procesan los datos para hacer predicciones o clasificaciones. Los algoritmos de Machine Learning aprenden de los datos y ajustan sus parámetros para mejorar su precisión.
   
3. **Modelos**: Un modelo es el resultado de entrenar un algoritmo en un conjunto de datos. Un modelo entrenado puede hacer predicciones sobre nuevos datos.

4. **Entrenamiento y Evaluación**: Entrenar un modelo implica alimentar datos al algoritmo para que ajuste sus parámetros. Luego, el modelo es evaluado en datos no vistos para medir su rendimiento.

---

#### **4. IA en Local vs. en la Nube**
Ejecutar IA en **local** significa que el procesamiento y entrenamiento de modelos ocurre en tu propia máquina, en lugar de depender de servicios externos (como Google Colab, AWS, etc.). Ejecutar IA en local ofrece varias ventajas:

- **Control total** sobre los datos y el proceso.
- **Mayor privacidad**, ya que los datos no se envían a servicios externos.
- **Personalización**: Puedes ajustar el entorno de trabajo según tus necesidades específicas.

Sin embargo, puede requerir **recursos computacionales** significativos, como GPU, CPU potentes, y suficiente memoria RAM.

---

#### **5. Requisitos para Correr IA en Local**
Antes de empezar a ejecutar proyectos de IA en tu propio sistema, es importante preparar el entorno de trabajo. Aquí están los requisitos fundamentales:

1. **Lenguaje de Programación**: 
   - **Python** es el lenguaje más común en IA por su simplicidad y la gran cantidad de bibliotecas disponibles para Machine Learning (ML) y Deep Learning (DL).
   
2. **Entorno de Desarrollo**:
   - Tener instalado **Python** en tu sistema.
   - Usar **Jupyter Notebook** o **Visual Studio Code** como entornos de desarrollo interactivos.
   
3. **Bibliotecas Esenciales**:
   - **NumPy** y **Pandas**: Para el manejo de datos.
   - **Matplotlib** y **Seaborn**: Para la visualización de datos.
   - **Scikit-learn**: Para Machine Learning clásico.
   - **TensorFlow** o **PyTorch**: Para Deep Learning.

4. **Hardware**:
   - Para tareas básicas de ML, una **CPU** moderna suele ser suficiente.
   - Para Deep Learning, especialmente si usas redes neuronales profundas, una **GPU** (preferentemente Nvidia con CUDA) puede ser necesaria para reducir los tiempos de entrenamiento.

---

#### **6. Herramientas Clave para Ejecutar IA en Local**
Aquí tienes algunas herramientas que instalaremos y utilizaremos a lo largo del curso:

- **Anaconda**: Distribución que facilita la gestión de paquetes y entornos Python.
- **Jupyter Notebooks**: Un entorno interactivo para escribir y ejecutar código Python.
- **Pip/Conda**: Gestores de paquetes para instalar las bibliotecas necesarias.

En la próxima clase configuraremos el entorno de trabajo local paso a paso, instalando Python, configurando Anaconda y preparando las bibliotecas clave.

---

### **Tarea para la próxima clase:**
1. **Instalación de Anaconda**: Ve a la página oficial de Anaconda y descarga el instalador correspondiente a tu sistema operativo ([enlace](https://www.anaconda.com/products/individual)).
2. **Familiarízate con Python**: Si no has trabajado antes con Python, trata de completar algunos ejercicios básicos para familiarizarte con la sintaxis.
3. **Reflexión sobre IA en tu entorno**: Piensa en alguna aplicación de IA que te gustaría implementar en tu entorno local. Esto puede ser un sistema de clasificación, una predicción o incluso un sistema de recomendación. Discutiremos estas ideas en la próxima sesión.

---

Con esto hemos cubierto los conceptos básicos de la IA y hemos sentado las bases para empezar a trabajar en local. En la próxima sesión, profundizaremos en cómo configurar el entorno y comenzar a construir modelos simples de Machine Learning.
---


### Curso de Inteligencia Artificial (IA) – Módulo 2: Modelos de Lenguaje y Herramientas para Ejecutar LLMs en Local

---

### **Clase 2: Introducción a los Modelos de Lenguaje y Herramientas para Ejecutar LLMs en Local**

---

En esta sesión, vamos a explorar dos áreas clave que forman la base del trabajo con **modelos de lenguaje de gran tamaño (LLMs, por sus siglas en inglés)**:

1. **Entender los tipos de modelos de lenguaje** y su arquitectura, en especial los que puedes encontrar en plataformas como **Hugging Face**.
2. **Herramientas para ejecutar estos modelos en tu máquina local**, de manera eficiente, considerando los recursos computacionales.

---

### **1. ¿Qué son los Modelos de Lenguaje (LLMs)?**

Los **Modelos de Lenguaje de Gran Escala (LLMs)** son una clase de modelos de Inteligencia Artificial diseñados para comprender y generar texto basado en patrones aprendidos a partir de grandes volúmenes de datos textuales. Algunos de los ejemplos más conocidos incluyen **GPT (Generative Pre-trained Transformer)** y **BERT (Bidirectional Encoder Representations from Transformers)**.

#### **Arquitectura Transformer**
La mayoría de los LLMs modernos están construidos sobre la **arquitectura Transformer**, que ha demostrado ser especialmente efectiva para manejar secuencias largas de texto. Los transformadores utilizan mecanismos de **autoatención** que permiten al modelo enfocarse en diferentes partes de la secuencia de entrada de manera simultánea, a diferencia de modelos anteriores que dependían de secuencias más lineales.

---

#### **2. Tipos de Modelos Populares de Lenguaje**

Aquí te explico algunos de los modelos más conocidos que encontrarás en plataformas como **Hugging Face**:

1. **GPT (Generative Pre-trained Transformer)**:
   - Desarrollado por OpenAI, **GPT** es un modelo autoregresivo que genera texto palabra por palabra, prediciendo cada palabra en función del contexto anterior. Se utiliza principalmente para generación de texto, chatbots, entre otras aplicaciones.
   
   - Ejemplos: GPT-3, GPT-4.

2. **BERT (Bidirectional Encoder Representations from Transformers)**:
   - **BERT** es un modelo bidireccional, lo que significa que tiene en cuenta el contexto de una palabra desde ambas direcciones (antes y después de la palabra). Esto lo hace ideal para tareas como clasificación de texto, análisis de sentimientos, y extracción de información.
   
   - Ejemplos: BERT, RoBERTa, DistilBERT.

3. **T5 (Text-to-Text Transfer Transformer)**:
   - **T5** convierte todas las tareas de procesamiento del lenguaje en problemas de conversión de texto a texto. Esto permite que un solo modelo maneje múltiples tareas como traducción, resumen, y generación de texto.

4. **StableLM y BLOOM**:
   - Modelos abiertos diseñados para replicar parte del éxito de GPT, pero con acceso público y licencias más flexibles. Se enfocan en ser más ligeros y menos costosos de entrenar o ejecutar en local.

5. **Whisper**:
   - Un modelo de reconocimiento de voz desarrollado por OpenAI que también se usa para transcribir texto y realizar tareas de comprensión de lenguaje a partir de audio.

---

#### **3. Hugging Face: El Repositorio de Modelos**

**Hugging Face** es una plataforma que ofrece una colección de miles de modelos preentrenados para tareas de procesamiento de lenguaje natural (NLP) y visión por computadora. Aquí, puedes descargar modelos listos para usar y ajustarlos a tus necesidades específicas.

- **Transformers**: Biblioteca principal de Hugging Face para trabajar con modelos de lenguaje basados en Transformers. Puedes cargar y ejecutar modelos como GPT-2, BERT, y otros con solo unas pocas líneas de código.
- **Datasets**: Además de los modelos, también ofrece una vasta colección de datasets para entrenar y evaluar modelos.

##### **Cómo empezar con Hugging Face**:
```bash
pip install transformers datasets
```

Con esta instalación, ya puedes comenzar a utilizar modelos preentrenados y datasets para tus propios proyectos.

---

### **4. Herramientas para Ejecutar LLMs en Local**

Ahora que entiendes los diferentes tipos de modelos, es importante aprender a ejecutarlos en tu propia máquina. A continuación, presentamos algunas de las herramientas clave para ejecutar estos LLMs en local.

#### **A. Hardware para Ejecutar LLMs**
Antes de pasar a las herramientas, es esencial conocer el tipo de hardware que necesitarás:

1. **CPU**: Es posible ejecutar LLMs pequeños en CPU, pero puede ser lento. Modelos más grandes requieren tiempo considerable para procesamiento.
2. **GPU (Unidad de Procesamiento Gráfico)**: Para modelos grandes, el uso de una GPU con soporte para **CUDA** (Nvidia) es altamente recomendado, ya que acelera los cálculos de forma significativa.
3. **TPU (Tensor Processing Unit)**: En casos más avanzados, Google ofrece TPUs para acelerar el entrenamiento y ejecución de LLMs, pero esto suele estar disponible en la nube.

#### **B. Herramientas para Ejecutar LLMs en Local**

1. **Transformers de Hugging Face**:
   - Esta es la biblioteca principal para trabajar con modelos preentrenados de Hugging Face. Puedes descargar modelos de su repositorio e integrarlos fácilmente en tu propio flujo de trabajo local.
   - La ventaja es que permite cargar modelos de diferentes tamaños y ajustar los parámetros según los recursos de tu máquina.

   Ejemplo básico para cargar un modelo:
   ```python
   from transformers import pipeline

   # Cargamos un pipeline para generar texto con GPT-2
   generador = pipeline('text-generation', model='gpt2')
   result = generador("Hoy es un buen día para", max_length=50)
   print(result)
   ```

2. **PEFT (Parameter-Efficient Fine-Tuning)**:
   - Esta es una técnica desarrollada para permitir la **sintonización fina de modelos grandes en local** sin necesidad de recursos masivos. En lugar de ajustar todos los parámetros del modelo, PEFT ajusta solo un subconjunto pequeño, lo que reduce significativamente los requisitos de hardware.

   - **LoRA (Low-Rank Adaptation)**: Un ejemplo de PEFT, LoRA permite entrenar modelos grandes con solo una fracción de los recursos necesarios para entrenar el modelo completo.

3. **BitsAndBytes**:
   - Esta herramienta permite ejecutar **modelos de lenguaje a menor precisión (8-bit, 4-bit)**, lo que reduce los requisitos de memoria y potencia computacional.
   - Ideal para personas que no cuentan con acceso a GPU potentes, pero quieren probar modelos de gran tamaño.

   Instalación y uso:
   ```bash
   pip install bitsandbytes
   ```

4. **Accelerate (Hugging Face)**:
   - Una herramienta de Hugging Face diseñada para **optimizar la ejecución de modelos grandes en hardware local**. Automáticamente ajusta el uso de CPU o GPU para maximizar el rendimiento y acelerar el procesamiento.
   
   Ejemplo de uso con Accelerate:
   ```bash
   pip install accelerate
   ```

5. **llama.cpp y GPTQ-for-llama**:
   - **llama.cpp** es una implementación ligera para ejecutar modelos LLaMA (desarrollado por Meta) en CPU de forma eficiente. Esta herramienta permite correr estos modelos con una sobrecarga mínima de recursos y ha ganado popularidad entre desarrolladores que desean ejecutar IA en local sin depender de GPU.
   - **GPTQ-for-llama**: Esta técnica permite cuantizar modelos GPT en precisiones más bajas (4-bit) para reducir el consumo de memoria y hacer factible su ejecución en máquinas con hardware limitado.

---

### **5. Preparación del Entorno Local**

Antes de comenzar a ejecutar modelos grandes en tu máquina, es importante asegurarse de que tienes todo configurado adecuadamente. Aquí tienes una lista de verificación básica:

1. **Instalar Python 3.8+** (si no lo has hecho ya).
2. **Instalar Hugging Face Transformers** y **Accelerate**.
3. **Tener los drivers de GPU actualizados** (si usas una GPU Nvidia).
4. **Instalar CUDA Toolkit y cuDNN** (para que PyTorch o TensorFlow puedan utilizar la GPU).
5. **Usar ambientes virtuales** como los que ofrece Anaconda o venv para manejar dependencias y aislar proyectos.

---

### **Tarea para la próxima clase:**
1. **Descarga e instala Hugging Face Transformers** y familiarízate con la documentación de Hugging Face.
2. **Ejecuta un modelo preentrenado en tu entorno local**. Si no tienes GPU, empieza con modelos más pequeños como DistilBERT o GPT-2.
3. **Investiga sobre LoRA o BitsAndBytes**: Explora cómo puedes usarlas para reducir la carga computacional de los modelos y ejecutarlos en hardware menos potente.

---

Con esto hemos cubierto los fundamentos de los modelos de lenguaje (LLMs) y las herramientas necesarias para ejecutarlos en local. En la próxima sesión, veremos cómo ajustar modelos para tareas específicas y cómo optimizar el rendimiento en entornos locales.

---
*Generado desde conversación con 4 mensajes.*
*IA/ML*
