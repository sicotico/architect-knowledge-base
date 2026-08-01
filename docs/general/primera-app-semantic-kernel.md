---
title: Primera app Semantic Kernel
date: 2025-02-08
category: General
slug: primera-app-semantic-kernel
tags: ['General']
---

# Primera app Semantic Kernel


> **Pregunta original:**
> 

Este es el error completo:

(venv) luis@mini4 semantic_kernel_app % python main.py
Traceback (most recent call last):
  File "/Users/luis/Documents/semantic_kernel_app/main.py", line 20, in <module>
    import semantic_kernel as sk
  File "/Users/luis/Documents/semantic_kernel_app/venv/lib/python3.9/site-packages/semantic_kernel/__init__.py", line 3, in <module>
    from semantic_kernel.kernel import Kernel
  File "/Users/luis/Documents/semantic_kernel_app/venv/lib/python3.9/site-packages/semantic_kernel/kernel.py", line 10, in <module>
    from semantic_kernel.connectors.ai.prompt_execution_settings import PromptExecutionSettings
  File "/Users/luis/Documents/semantic_kernel_app/venv/lib/python3.9/site-packages/semantic_kernel/connectors/ai/__init__.py", line 3, in <module>
    from semantic_kernel.connectors.ai.prompt_execution_settings import PromptExecutionSettings
  File "/Users/luis/Documents/semantic_kernel_app/venv/lib/python3.9/site-packages/semantic_kernel/connectors/ai/prompt_execution_settings.py", line 5, in <module>
    from semantic_kernel.kernel_pydantic import KernelBaseModel
  File "/Users/luis/Documents/semantic_kernel_app/venv/lib/python3.9/site-packages/semantic_kernel/kernel_pydantic.py", line 9, in <module>
    from pydantic.networks import Url
ImportError: cannot import name 'Url' from 'pydantic.networks' (/Users/luis/Documents/semantic_kernel_app/venv/lib/python3.9/site-packages/pydantic/networks.py)
> Estoy en MacOS con Python 3,9 , como lo actualizo ?
> Eres profesor de programación en python. y especialista en IA. Estas impartiendo un curo con semantic kernel. Tus alumnos usa MAcOS 15 y codium Quiero hacer mi primera aplicación con sematic kernes y python. ¿Cual es el primer paso? 
> 
> *...y 4 preguntas de seguimiento*


---


## Respuesta


El problema ahora es que **Semantic Kernel 0.9.6b1** requiere **Pydantic 2.x**, pero previamente intentamos instalar **Pydantic 1.x**. Esto significa que **Semantic Kernel ya es compatible con Pydantic 2**, y simplemente hay que **asegurarnos de tener la versión correcta**.

---

## **Solución Paso a Paso**
### **1. Desinstalar Semantic Kernel y Pydantic**
Primero, elimina las versiones instaladas para evitar conflictos:

```sh
pip uninstall semantic-kernel pydantic -y
```

---

### **2. Instalar la Última Versión Correcta**
Ahora instala la versión más reciente compatible de **Pydantic 2.x** y **Semantic Kernel**:

```sh
pip install pydantic semantic-kernel --upgrade
```

Esto instalará:

✅ **Pydantic 2.x** (compatible con Semantic Kernel 0.9.6b1)  
✅ **Semantic Kernel** en su versión más reciente  

---

### **3. Verificar la Instalación**
Para asegurarte de que tienes las versiones correctas, ejecuta:

```sh
pip show semantic-kernel pydantic
```

Debe mostrar algo como:

```
Name: semantic-kernel
Version: 0.9.6b1
---
Name: pydantic
Version: 2.x.x  (donde x.x es la última versión estable)
```

---

### **4. Probar el Código Nuevamente**
Ahora, ejecuta tu aplicación:

```sh
python main.py
```

Esto debería funcionar sin errores. 🚀

---

🔹 **¿Por qué pasó esto?**  
Semantic Kernel **actualizó su compatibilidad a Pydantic 2.x**, pero antes intentamos usar Pydantic 1.x debido a una versión más antigua. Ahora simplemente hemos alineado las versiones correctamente.

¡Prueba y dime si ya funciona! 😊
---


Si estás utilizando **Phi-4** en un servidor local y no necesitas una clave de API, entonces puedes conectarlo a **Semantic Kernel** usando una configuración de servicio local.

Aquí te dejo un código de ejemplo para configurar **Semantic Kernel** con **Phi-4** ejecutándose en un servidor local:

---

### **1. Instalar Dependencias**
Asegúrate de tener instalado **Semantic Kernel**:

```sh
pip install semantic-kernel
```

Si **Phi-4** está ejecutándose en un servidor **local** con **llama-cpp-python** o un API similar, también necesitarás:

```sh
pip install llama-cpp-python
```

---

### **2. Código para Conectar Semantic Kernel con Phi-4 en Local**
Crea un archivo `main.py` y copia este código:

```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

# Configurar el Kernel
kernel = sk.Kernel()

# Configurar el servicio de Phi-4 en un servidor local
local_api_url = "http://localhost:8000/v1"  # Ajusta al puerto donde corre tu servidor

# Conectar Phi-4 con Semantic Kernel
kernel.add_text_completion_service(
    service_id="phi-4",
    service=OpenAIChatCompletion(model_id="phi-4", api_key="", endpoint=local_api_url)
)

# Crear y ejecutar una función en Semantic Kernel
async def main():
    function = kernel.create_function("Hola, ¿cómo estás?")
    respuesta = await function.invoke()
    print(respuesta)

import asyncio
asyncio.run(main())
```

---

### **3. Explicación del Código**
1. **`local_api_url = "http://localhost:8000/v1"`**  
   - Si usas **llama-cpp-python** o cualquier **API compatible con OpenAI**, normalmente se ejecuta en el puerto `8000`.
   - Cambia el puerto si tu servidor usa otro.

2. **`api_key=""`**  
   - Como **Phi-4** corre en local, **no necesitas clave API**.

3. **`model_id="phi-4"`**  
   - Debes asegurarte de que **tu servidor reconoce este modelo**. A veces el nombre varía según cómo cargaste Phi-4.

---

### **4. Iniciar el Servidor de Phi-4**
Si estás usando **llama-cpp-python** para correr **Phi-4**, inícialo con:

```sh
python3 -m llama_cpp.server --model /ruta/al/modelo/phi-4.gguf
```

---

### **5. Ejecutar la Aplicación**
Corre el código en tu terminal:

```sh
python main.py
```

---

### **Próximos Pasos**
✅ Si necesitas **instrucciones más avanzadas** (como cargar funciones personalizadas o integración con memoria), dime y te ayudo a mejorarlo 🚀
---


Parece que el problema persiste debido a la incompatibilidad de **Pydantic 2.x** con el código actual de **Semantic Kernel**. El error indica que **Semantic Kernel todavía intenta importar `Url` desde `pydantic.networks`**, lo cual **ya no existe en Pydantic 2.x**.

---

## **Solución Definitiva**
Debemos asegurarnos de que **Semantic Kernel esté completamente actualizado** y que **Pydantic 2.x** esté correctamente instalado.

### **1. Verificar las Versiones Instaladas**
Ejecuta estos comandos para comprobar qué versiones tienes instaladas:

```sh
pip show semantic-kernel pydantic
```

Si **Pydantic es 2.x**, pero **Semantic Kernel sigue fallando**, entonces probablemente tu instalación esté corrupta.

---

### **2. Limpiar e Instalar la Última Versión Compatible**
Ejecuta los siguientes pasos para limpiar el entorno y reinstalar las versiones correctas.

#### **2.1 Desinstalar Todo**
```sh
pip uninstall semantic-kernel pydantic -y
```

#### **2.2 Instalar Pydantic 2.x Primero**
```sh
pip install "pydantic>=2.0"
```

#### **2.3 Instalar Semantic Kernel (Última Beta)**
```sh
pip install --upgrade semantic-kernel
```

Esto forzará la instalación de la última versión **oficial y compatible** de **Semantic Kernel** con **Pydantic 2**.

---

### **3. Verificar la Instalación**
Después de instalar, revisa que tienes **Pydantic 2.x** y **Semantic Kernel 0.9.6 o superior**:

```sh
pip show semantic-kernel pydantic
```

Debe mostrar algo como:

```
Name: semantic-kernel
Version: 0.9.6b1  (o una versión más nueva)
---
Name: pydantic
Version: 2.x.x  (donde x.x es la última versión estable)
```

Si todo está bien, **prueba de nuevo tu código**:

```sh
python main.py
```

---

### **¿Por qué ocurre este problema?**
- **Pydantic 2.x eliminó `pydantic.networks.Url`**, lo que rompe algunos módulos que lo importan directamente.
- **Semantic Kernel ya es compatible con Pydantic 2**, pero si se instala una versión más antigua o corrupta, puede intentar usar código viejo que no es compatible.
- **Al limpiar e instalar las versiones correctas**, evitamos dependencias rotas.

Prueba esto y dime si ya funciona. 🚀
---


Para actualizar **Python 3.9** en **MacOS** a una versión más reciente (como **Python 3.10 o 3.11**), sigue estos pasos:

---

## **1️⃣ Verificar la Versión de Python**
Ejecuta en la terminal:

```sh
python3 --version
```

Si te muestra algo como:

```
Python 3.9.x
```

Entonces necesitas actualizarlo.

---

## **2️⃣ Instalar la Última Versión de Python**
En **MacOS**, la mejor forma de instalar la versión más reciente de Python es usando **Homebrew**.

### **Si No Tienes Homebrew, Instálalo** (si ya lo tienes, sáltate este paso)
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

### **2.1 Instalar o Actualizar Python con Homebrew**
Ejecuta:

```sh
brew install python
```

Si ya tienes Python instalado con Homebrew y solo quieres actualizar:

```sh
brew upgrade python
```

Después de esto, revisa la versión instalada:

```sh
python3 --version
```

Debe mostrar algo como:

```
Python 3.11.x
```

---

## **3️⃣ Verificar y Configurar Python por Defecto**
Si después de la instalación sigues viendo **Python 3.9**, ejecuta:

```sh
which python3
```

Si muestra algo como:

```
/usr/bin/python3
```

Significa que todavía estás usando la versión del sistema. Para asegurarte de usar la nueva versión de Homebrew, ejecuta:

```sh
brew link --overwrite python
```

Luego, confirma de nuevo:

```sh
python3 --version
```

---

## **4️⃣ (Opcional) Cambiar el `python` Predeterminado**
Si `python3` sigue apuntando a la versión vieja, puedes forzarlo a usar la nueva:

```sh
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Si usas **bash** en lugar de **zsh**:

```sh
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

## **5️⃣ Verificar el `venv`**
Después de actualizar Python, es recomendable **eliminar y recrear tu entorno virtual**:

```sh
rm -rf venv  # Borra el entorno virtual antiguo
python3 -m venv venv  # Crea un nuevo entorno virtual
source venv/bin/activate  # Activa el nuevo entorno virtual
pip install --upgrade pip  # Actualiza pip
pip install semantic-kernel pydantic  # Reinstala dependencias
```

---

✅ **Listo**, ahora deberías tener **Python actualizado y compatible con Semantic Kernel**.

### **🔹 Próximo Paso**
Prueba ejecutar tu código nuevamente:

```sh
python main.py
```

¡Avísame si necesitas más ayuda! 🚀
---


El error:

```
ImportError: cannot import name 'Url' from 'pydantic.networks'
```

indica un problema de compatibilidad entre **Semantic Kernel** y la versión de **Pydantic** que tienes instalada. 

---

### **Solución Paso a Paso**

#### **1. Verificar la Versión de Pydantic**
Ejecuta este comando dentro de tu entorno virtual:

```sh
pip show pydantic
```

Si ves que la versión es `2.x`, es probable que **Semantic Kernel** esté esperando `pydantic 1.x`.

#### **2. Desinstalar Pydantic**
Para corregir el problema, desinstala `pydantic`:

```sh
pip uninstall pydantic -y
```

#### **3. Instalar la Versión Correcta**
Ahora instala **Pydantic 1.10.13**, que es compatible con Semantic Kernel:

```sh
pip install "pydantic<2"
```

Esto instalará **Pydantic 1.10.13**, que es la versión estable usada en proyectos como **Semantic Kernel**.

#### **4. Verificar la Instalación**
Vuelve a ejecutar:

```sh
pip show pydantic
```

Debe mostrar algo como:

```
Name: pydantic
Version: 1.10.13
```

#### **5. Probar la Aplicación**
Ahora intenta ejecutar de nuevo tu código:

```sh
python main.py
```

---

### **¿Por qué ocurre esto?**
Semantic Kernel aún no es 100% compatible con **Pydantic 2.x**, y trata de importar `Url` desde un módulo que ha cambiado en Pydantic 2. La solución es mantener **Pydantic 1.x** hasta que **Semantic Kernel** lo actualice.

¡Prueba y dime si funciona! 🚀
---


Si te aparece el error:

```
ModuleNotFoundError: No module named 'semantic_kernel'
```

significa que **Semantic Kernel** no está instalado en tu entorno virtual, o que no estás ejecutando el código dentro del entorno virtual correcto.

---

### **1. Verificar si estás en el Entorno Virtual**
Antes de revisar los módulos instalados, asegúrate de que estás dentro de tu **entorno virtual**.

Ejecuta en la terminal:

```sh
which python
```

Si estás en un entorno virtual, debería mostrar una ruta similar a:

```
/ruta/al/proyecto/venv/bin/python
```

Si no, activa el entorno virtual:

```sh
source venv/bin/activate  # Para Mac/Linux
```

---

### **2. Verificar los Módulos Instalados**
Una vez dentro del entorno virtual, revisa los módulos instalados con:

```sh
pip list
```

Esto mostrará todos los paquetes instalados. Busca `semantic-kernel`.

Si no aparece, instálalo con:

```sh
pip install semantic-kernel
```

---

### **3. Reintentar la Ejecución**
Después de instalar el módulo, intenta ejecutar el script de nuevo:

```sh
python main.py
```

Si el problema persiste, dime qué muestra el comando `pip list` y te ayudaré a corregirlo. 🚀
---


¡Genial! Para comenzar con tu primera aplicación usando **Semantic Kernel** en **Python** en **MacOS 15** con **VSCodium**, sigue estos pasos:

---

### **Paso 1: Configurar el Entorno de Desarrollo**

#### **1.1 Instalar Python**
Verifica que tienes Python 3.8 o superior instalado. Abre la terminal y ejecuta:

```sh
python3 --version
```

Si no está instalado, descárgalo desde [python.org](https://www.python.org/) o instálalo con:

```sh
brew install python
```

#### **1.2 Instalar VSCodium**
Si no tienes **VSCodium**, descárgalo e instálalo desde [VSCodium](https://vscodium.com/).

Luego, abre la terminal y configura Python en VSCodium:

```sh
codium .
```

Instala la extensión **Python** desde la pestaña de extensiones (`Cmd + Shift + X`).

---

### **Paso 2: Crear un Entorno Virtual**
Para evitar conflictos entre librerías, usa un entorno virtual:

```sh
mkdir semantic_kernel_app && cd semantic_kernel_app
python3 -m venv venv
source venv/bin/activate
```

---

### **Paso 3: Instalar Semantic Kernel**
Ahora instala **Semantic Kernel** y dependencias necesarias:

```sh
pip install semantic-kernel openai
```

Si deseas soporte para Azure OpenAI:

```sh
pip install semantic-kernel[azure]
```

---

### **Paso 4: Crear tu Primera Aplicación**
Crea un archivo **main.py** en tu carpeta del proyecto:

```sh
touch main.py
```

Edita `main.py` en VSCodium y escribe este código base para usar **Semantic Kernel** con OpenAI:

```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

# Configurar el Kernel
kernel = sk.Kernel()

# Configurar OpenAI API
api_key = "TU_OPENAI_API_KEY"
kernel.add_text_completion_service("gpt-3.5-turbo", OpenAIChatCompletion("gpt-3.5-turbo", api_key))

# Definir una función con Semantic Kernel
async def main():
    function = kernel.create_function("Hola, ¿cómo te llamas?")
    respuesta = await function.invoke()
    print(respuesta)

import asyncio
asyncio.run(main())
```

---

### **Paso 5: Obtener una Clave de OpenAI**
Para usar **GPT**, necesitas una API Key de OpenAI:

1. Ve a [OpenAI](https://platform.openai.com/signup/) y crea una cuenta.
2. Obtén tu API Key en la sección de **API Keys**.
3. Reemplaza `"TU_OPENAI_API_KEY"` en el código con tu clave.

---

### **Paso 6: Ejecutar tu Aplicación**
Ejecuta el código con:

```sh
python main.py
```

Si todo está bien, deberías ver una respuesta generada por **GPT-3.5** 🎉.

---

### **Siguientes Pasos**
- Explora los **Plugins y Skills** de Semantic Kernel.
- Prueba con **memoria** y **planificación** en Semantic Kernel.
- Integra con APIs externas.

¿Te gustaría que haga una demostración en código más avanzada? 🚀

---
*Generado desde conversación con 14 mensajes.*
*General*
