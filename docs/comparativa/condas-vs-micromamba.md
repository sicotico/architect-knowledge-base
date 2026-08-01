---
title: Condas vs Micromamba
date: 2026-07-10
category: Comparativas
slug: condas-vs-micromamba
tags: ['Comparativas']
---

# Condas vs Micromamba


> **Pregunta original:**
> 
estoy compilando llama.cpp en ubuntu para CUDA y me solicita microbamab  y no se porque  
> <pre>nvidia-smi 
Fri Jul 10 17:15:40 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.71.05              Driver Version: 595.71.05      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 5060 Ti     Off |   00000000:01:00.0 Off |                  N/A |
|  0%   33C    P8              4W /  180W |       2MiB /  16311MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
</pre>
> que es micromamaba/conda 
> 
> *...y 1 preguntas de seguimiento*


---


## Respuesta


Con esos datos, **tu driver 595.71.05 es compatible con CUDA Toolkit 13.x mediante compatibilidad menor**. NVIDIA fija para CUDA 13.x un driver mínimo de la rama 580, así que **CUDA 13.3 debería poder ejecutar `llama.cpp` con tu driver 595.71.05**. citeturn660327search2turn660327search8

Hay dos matices:

- `nvidia-smi` mostrando **CUDA Version: 13.2** no significa que solo puedas usar Toolkit 13.2; indica el nivel CUDA anunciado por el driver.
- CUDA 13.3 se distribuye con un driver 610.43.02, pero ese no es necesariamente el mínimo absoluto gracias a la compatibilidad menor de CUDA 13.x. citeturn660327search0turn660327search2

## Recomendación práctica

No eliminaría todavía el entorno CUDA 13.3. Primero intentaría compilar y ejecutar:

```bash
cd ~/llama.cpp

~/micromamba/bin/micromamba run -n llama-cpp-cuda \
  cmake -S . -B build-cuda \
  -G Ninja \
  -DGGML_CUDA=ON \
  -DCMAKE_BUILD_TYPE=Release

~/micromamba/bin/micromamba run -n llama-cpp-cuda \
  cmake --build build-cuda --parallel "$(nproc)"
```

`GGML_CUDA=ON` es la opción correcta para habilitar el backend CUDA en `llama.cpp`. citeturn660327search3

Después:

```bash
./build-cuda/bin/llama-cli --list-devices
```

Debería aparecer algo similar a:

```text
CUDA0: NVIDIA GeForce RTX 5060 Ti
```

También puedes hacer una prueba real:

```bash
./build-cuda/bin/llama-cli \
  -m /ruta/al/modelo.gguf \
  -ngl 99 \
  -p "Hola"
```

Mientras se ejecuta, en otra terminal:

```bash
watch -n 1 nvidia-smi
```

## Cuándo bajar a CUDA 13.2

Solo recrearía el entorno con CUDA 13.2 si aparece alguno de estos errores:

```text
CUDA driver version is insufficient for CUDA runtime version
```

```text
the provided PTX was compiled with an unsupported toolchain
```

```text
unsupported PTX version
```

```text
CUDA error: operation not supported
```

La compatibilidad menor puede tener restricciones cuando una aplicación depende de PTX generado con características introducidas en una revisión más nueva del Toolkit. Por eso 13.2 sigue siendo la opción más conservadora, pero **no es necesario cambiar preventivamente si 13.3 compila y ejecuta correctamente**.

## Un detalle adicional

Tu entorno instaló:

```text
gcc 15.2
g++ 15.2
CUDA 13.3
```

Si la compilación falla, el problema podría ser el compilador anfitrión y no el driver. Comprueba qué compilador está usando CMake:

```bash
grep -E 'CMAKE_CXX_COMPILER:|CMAKE_CUDA_COMPILER:' \
  build-cuda/CMakeCache.txt
```

En tu caso, el orden razonable es:

1. Compilar con CUDA 13.3.
2. Ejecutar `llama-cli --list-devices`.
3. Probar un modelo con `-ngl 99`.
4. Cambiar a CUDA 13.2 únicamente si aparece un error de runtime, PTX o incompatibilidad del driver.
---


Voy a comprobar el flujo oficial de compilación de `llama.cpp` con CUDA y en qué casos aparece `micromamba`, porque no suele ser un requisito directo del compilador.
---


El registro muestra que **Micromamba se instaló correctamente y creó el entorno**. No hay un error todavía. Sin embargo, hay una incoherencia importante:

> El script pretendía usar CUDA 13.2, pero Micromamba terminó instalando CUDA Toolkit 13.3.

## Por qué ocurrió

El script añadió el canal:

```text
nvidia/label/cuda-13.2.0
```

pero solicitó paquetes sin fijar versión:

```text
cuda-nvcc
cuda-cudart-dev
libcublas-dev
```

Además, también habilitó `conda-forge`. El solucionador encontró versiones más recientes y compatibles en `conda-forge`, por lo que eligió:

```text
cuda-version       13.3
cuda-nvcc          13.3.73
cuda-cudart-dev    13.3.29
```

Los mensajes:

```text
Shard Index ... not available, falling back to flat repodata
```

son **advertencias informativas**, no fallos. Indican que Micromamba utilizó el índice tradicional del repositorio.

## ¿CUDA 13.3 funcionará con tu controlador?

Debes mirar la versión real del controlador:

```bash
nvidia-smi
```

Interesan estas dos líneas:

```text
Driver Version: xxx.xx
CUDA Version: 13.2
```

La segunda no significa que tengas instalado CUDA Toolkit 13.2. Indica la versión máxima de CUDA reconocida por el controlador.

Para CUDA 13.x, NVIDIA establece compatibilidad menor a partir del driver 580. Sin embargo, CUDA 13.3 completo corresponde al controlador 610.43.02 o posterior. Con un controlador anterior puede funcionar mediante compatibilidad menor, pero existen limitaciones, especialmente con código PTX o características nuevas. citeturn846233view0turn846233view2

Por tanto:

- **Driver 610.43.02 o superior:** CUDA 13.3 es la opción segura.
- **Driver entre 595.45.04 y 610.43.01:** es preferible CUDA 13.2.
- **Driver entre 580 y 595:** CUDA 13.x puede funcionar parcialmente, pero conviene usar una versión alineada con el controlador.
- **Driver inferior a 580:** CUDA 13.x no es apropiado.

## Recomendación

Como `nvidia-smi` aparentemente muestra CUDA 13.2, la opción conservadora es recrear el entorno fijando explícitamente CUDA 13.2.

Primero elimina el entorno actual:

```bash
~/micromamba/bin/micromamba env remove -n llama-cpp-cuda -y
```

La ubicación del ejecutable puede ser distinta. Compruébala con:

```bash
command -v micromamba
```

Después créalo fijando la versión:

```bash
micromamba create -n llama-cpp-cuda -y \
  -c nvidia/label/cuda-13.2.0 \
  -c conda-forge \
  --strict-channel-priority \
  cmake \
  ninja \
  git \
  cuda-version=13.2 \
  cuda-nvcc=13.2 \
  cuda-cudart-dev=13.2 \
  libcublas-dev
```

Verifica el resultado:

```bash
micromamba run -n llama-cpp-cuda nvcc --version
micromamba list -n llama-cpp-cuda | grep -E 'cuda-version|cuda-nvcc|cudart|cublas'
```

Debería aparecer una versión `13.2`, no `13.3`.

## Compilación de `llama.cpp`

Puedes compilar sin activar permanentemente el entorno:

```bash
cd ~/llama.cpp

micromamba run -n llama-cpp-cuda \
  cmake -S . -B build \
  -G Ninja \
  -DGGML_CUDA=ON \
  -DCMAKE_BUILD_TYPE=Release

micromamba run -n llama-cpp-cuda \
  cmake --build build --parallel "$(nproc)"
```

El procedimiento oficial de `llama.cpp` utiliza `-DGGML_CUDA=ON`; Micromamba solo está encapsulando CMake, Ninja y el Toolkit CUDA, no forma parte de `llama.cpp` propiamente dicho. citeturn846233view1

Después comprueba que detecta la GPU:

```bash
./build/bin/llama-cli --list-devices
```

**Conclusión:** la instalación no falló, pero el script no fijó correctamente CUDA 13.2. Instalar 13.3 puede funcionar, aunque para evitar incompatibilidades con el controlador resulta más prudente corregir el script y fijar `cuda-version=13.2`.
---


**`micromamba` no es necesario para compilar `llama.cpp` con CUDA** siguiendo el procedimiento oficial. Probablemente estás usando un script, tutorial o instalador alternativo que crea un entorno aislado con Micromamba.

La compilación oficial en Ubuntu requiere principalmente:

- compilador C/C++;
- CMake;
- Git;
- CUDA Toolkit, incluido `nvcc`;
- controlador NVIDIA compatible.

El procedimiento habitual es: citeturn264314search3turn264314search38

```bash
sudo apt update
sudo apt install -y build-essential cmake git

git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp

cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release -j"$(nproc)"
```

Comprueba antes que CUDA esté disponible:

```bash
nvidia-smi
nvcc --version
```

Y después verifica la compilación:

```bash
./build/bin/llama-cli --version
```

## Por qué puede pedirte Micromamba

Lo más probable es uno de estos casos:

1. **Estás ejecutando un script de instalación de terceros.**  
   Ese script usa Micromamba para instalar CMake, Python, CUDA u otras dependencias sin modificar el sistema.

2. **Estás instalando el paquete Conda de `llama.cpp`, no compilándolo directamente.**  
   La documentación también menciona instalaciones mediante `mamba install`, pero eso es un método de distribución alternativo, no un requisito para la compilación con CMake. citeturn264314search1

3. **Estás usando un proyecto que incorpora `llama.cpp`.**  
   Herramientas como interfaces web, scripts de modelos o proyectos Python pueden exigir su propio entorno Conda/Micromamba.

4. **Puede que el mensaje diga `mamba` y no `micromamba`.**  
   `mamba` también es un gestor de paquetes del ecosistema Conda. No debe confundirse con los modelos neuronales llamados Mamba.

En resumen: **puedes evitar Micromamba y compilar directamente con CMake**, salvo que el proyecto concreto desde el que estás lanzando la compilación lo use para administrar dependencias. El dato decisivo sería el comando que ejecutaste y el mensaje de error completo.
---


**Conda** y **micromamba** son herramientas para gestionar **entornos** y **paquetes**, muy usadas en Python, ciencia de datos y machine learning.

## Conda

Conda permite:

- Instalar paquetes: Python, NumPy, PyTorch, R, CUDA, etc.
- Crear entornos aislados con distintas versiones de Python.
- Evitar que las dependencias de un proyecto interfieran con otro.

Ejemplo:

```bash
conda create -n proyecto python=3.12
conda activate proyecto
conda install numpy pandas
```

Conda normalmente se instala mediante:

- **Miniconda**: instalación pequeña.
- **Anaconda**: incluye muchos paquetes preinstalados.

**Ventajas:** muy conocido, documentación abundante y buena compatibilidad.

**Desventajas:** puede ser lento resolviendo dependencias y ocupa bastante espacio.

## Micromamba

Micromamba hace prácticamente lo mismo que Conda, pero es una implementación más ligera y rápida.

```bash
micromamba create -n proyecto python=3.12
micromamba activate proyecto
micromamba install numpy pandas
```

No necesita una instalación completa de Python ni una distribución como Anaconda.

**Ventajas:** rápido, ocupa poco espacio y funciona bien en Docker, servidores y CI/CD.

**Desventajas:** algunas instrucciones escritas específicamente para Conda pueden requerir pequeños ajustes, y tiene menos integración gráfica.

## Diferencia práctica

| Herramienta | Velocidad | Tamaño | Facilidad inicial |
|---|---:|---:|---:|
| Conda | Media o lenta | Mayor | Más familiar |
| Micromamba | Rápida | Muy pequeño | Algo más técnica |

Micromamba utiliza los mismos repositorios y formatos de paquetes del ecosistema Conda, especialmente **conda-forge**.

Para un usuario nuevo, **Miniconda** suele ser la opción más sencilla. Para Docker, automatización o una instalación ligera, **micromamba** suele ser mejor.

---
*Generado desde conversación con 9 mensajes.*
*Comparativas*
