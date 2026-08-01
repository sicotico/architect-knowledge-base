---
title: Python y entornos virtuales
date: 2026-06-15
category: Programación
slug: python-y-entornos-virtuales
tags: ['Programación']
---

# Python y entornos virtuales


> **Pregunta original:**
> 
Voy a empezar con Python en Ubuntu server y lo env me están liando un poco, ¿cómo funciona o se tienen que instalar y porque Python y PyTorch?

---


## Respuesta


En Python, **“env”** suele referirse a dos cosas distintas:

1. **Variables de entorno**: valores del sistema como `PATH`, `CUDA_HOME`, `HF_TOKEN`, etc.
2. **Entornos virtuales**: carpetas aisladas donde instalas paquetes Python para un proyecto concreto.

Por tu pregunta, seguramente te está liando lo segundo: **entornos virtuales**.

## 1. Qué es un entorno virtual

Un entorno virtual es una instalación aislada de paquetes Python.

Sin entorno virtual, si instalas algo con:

```bash
pip install torch
```

puedes acabar modificando el Python global del sistema. En Ubuntu Server eso suele ser mala idea, porque algunas herramientas del sistema también dependen de Python.

Con entorno virtual, haces algo así:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install torch
```

Y todo lo que instales queda dentro de la carpeta:

```bash
.venv/
```

No afecta al resto del sistema.

## 2. Por qué se usan

Porque cada proyecto puede necesitar versiones diferentes.

Ejemplo:

```text
proyecto-a necesita numpy 1.x
proyecto-b necesita numpy 2.x
proyecto-c necesita torch con CUDA
proyecto-d necesita torch solo CPU
```

Si instalas todo globalmente, tarde o temprano rompes algo.

Con entornos virtuales:

```text
proyecto-a/.venv
proyecto-b/.venv
proyecto-c/.venv
```

Cada uno vive separado.

## 3. Se tienen que instalar

Sí, pero depende de lo que venga en tu Ubuntu.

Comprueba si tienes Python:

```bash
python3 --version
```

Comprueba si tienes `venv`:

```bash
python3 -m venv --help
```

Si falla, instala esto:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

Luego dentro de tu proyecto:

```bash
mkdir mi-proyecto
cd mi-proyecto
python3 -m venv .venv
source .venv/bin/activate
```

Cuando el entorno está activo, normalmente verás algo así:

```bash
(.venv) usuario@server:~/mi-proyecto$
```

Para salir:

```bash
deactivate
```

## 4. Qué papel tiene `pip`

`pip` es el instalador de paquetes Python.

Con el entorno activado:

```bash
pip install requests
pip install numpy
pip install torch
```

Eso instala paquetes dentro de `.venv`.

Para ver lo instalado:

```bash
pip list
```

Para guardar dependencias:

```bash
pip freeze > requirements.txt
```

Para reinstalarlas en otro servidor:

```bash
pip install -r requirements.txt
```

## 5. Por qué Python y PyTorch son cosas distintas

**Python** es el lenguaje.

**PyTorch** es una librería escrita para Python, muy usada en machine learning, deep learning, IA, redes neuronales, GPUs, tensores, etc.

Analogía rápida:

```text
Python = idioma
PyTorch = herramienta especializada escrita en ese idioma
```

Instalar Python no instala PyTorch.

Tú puedes usar Python para:

```text
scripts
automatización
APIs
web
procesamiento de datos
IA
administración de servidores
```

Pero solo necesitas PyTorch si vas a hacer cosas como:

```text
modelos de IA
redes neuronales
inferencia con modelos
entrenamiento
Stable Diffusion
LLMs
visión artificial
procesamiento tensorial en GPU
```

## 6. Instalación típica de PyTorch

### CPU solamente

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install torch torchvision torchaudio
```

Comprueba:

```bash
python -c "import torch; print(torch.__version__)"
```

### Con NVIDIA GPU

Aquí hay más riesgo de lío.

Necesitas:

```text
driver NVIDIA correcto
versión de PyTorch compatible con CUDA
entorno virtual limpio
```

Normalmente no instalas “CUDA completo” manualmente para empezar. PyTorch suele traer los binarios CUDA necesarios, pero el **driver NVIDIA del sistema sí debe estar bien instalado**.

Comprueba GPU:

```bash
nvidia-smi
```

Si eso funciona, luego instalas PyTorch con el comando recomendado por la web oficial de PyTorch según tu CUDA/driver. No conviene copiar comandos antiguos de tutoriales.

## 7. Flujo recomendado en Ubuntu Server

Para empezar limpio:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

Crear proyecto:

```bash
mkdir ~/python-test
cd ~/python-test
python3 -m venv .venv
source .venv/bin/activate
```

Actualizar herramientas básicas:

```bash
python -m pip install --upgrade pip setuptools wheel
```

Instalar algo simple:

```bash
pip install requests
```

Crear archivo:

```bash
nano app.py
```

Contenido:

```python
import requests

r = requests.get("https://example.com")
print(r.status_code)
```

Ejecutar:

```bash
python app.py
```

## 8. Errores comunes

### Usar `sudo pip install`

Evítalo casi siempre.

Malo:

```bash
sudo pip install torch
```

Mejor:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install torch
```

### Confundir `python`, `python3`, `pip`, `pip3`

En Ubuntu a veces `python` no apunta a Python 3.

Mejor usar:

```bash
python3 -m pip install paquete
```

o dentro del entorno virtual:

```bash
python -m pip install paquete
```

Así te aseguras de instalar en el Python correcto.

### Olvidar activar el entorno

Si no activas:

```bash
source .venv/bin/activate
```

puede que instales paquetes en otro sitio.

Comprueba:

```bash
which python
which pip
```

Deberías ver algo como:

```text
/home/usuario/mi-proyecto/.venv/bin/python
/home/usuario/mi-proyecto/.venv/bin/pip
```

## 9. Resumen práctico

Para trabajar bien en Ubuntu Server:

```bash
sudo apt install python3 python3-venv python3-pip
mkdir proyecto
cd proyecto
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install paquete
python script.py
```

Y para PyTorch:

```text
Python primero
entorno virtual después
PyTorch dentro del entorno
GPU solo si realmente la necesitas
```

Lo bueno de los entornos virtuales: evitan romper el sistema y hacen tus proyectos reproducibles.

Lo malo: al principio añaden comandos extra y es fácil olvidar si estás dentro o fuera del entorno.

---
*Generado desde conversación con 2 mensajes.*
*Programación*
