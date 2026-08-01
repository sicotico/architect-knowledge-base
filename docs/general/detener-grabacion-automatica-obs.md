---
title: Detener grabación automática OBS
date: 2024-09-23
category: General
slug: detener-grabacion-automatica-obs
tags: ['General']
---

# Detener grabación automática OBS


> **Pregunta original:**
> 
Tengo este error al cargar el script:
auto_stop_recording.lua
> y 8 horas ?
> convierte 7 horas en segundos
> 
> *...y 2 preguntas de seguimiento*


---


## Respuesta


Para convertir 8 horas en segundos, seguimos la misma fórmula:

\[
\text{segundos} = 8 \times 60 \times 60 = 28,800 \text{ segundos}
\]

Por lo tanto, **8 horas equivalen a 28,800 segundos**.
---


El error que estás viendo se debe a que el objeto `obs` no está correctamente inicializado en el script. Para corregir este error, debes asegurarte de que el script importe correctamente la API de OBS. El código necesita referirse correctamente al entorno de OBS Studio.

Aquí te dejo una versión corregida del script, con la estructura adecuada para evitar el error de indexación que mencionas:

### Script corregido para detener la grabación después de un tiempo determinado:

```lua
-- Referencia a la API de OBS
obs = obslua

-- Tiempo en segundos para detener la grabación (8 horas)
local stop_time_in_seconds = 8 * 60 * 60

-- Variables de estado
local start_time = 0
local is_recording = false

-- Descripción del script
function script_description()
    return "Detiene la grabación automáticamente después de un tiempo determinado (en segundos)."
end

-- Actualización de configuraciones
function script_update(settings)
    stop_time_in_seconds = obs.obs_data_get_int(settings, "stop_time")
end

-- Propiedades del script
function script_properties()
    local props = obs.obs_properties_create()
    obs.obs_properties_add_int(props, "stop_time", "Tiempo de grabación (segundos)", 1, 24 * 60 * 60, 1)
    return props
end

-- Manejo de eventos de grabación
function on_event(event)
    if event == obs.OBS_FRONTEND_EVENT_RECORDING_STARTED then
        start_time = os.time()
        is_recording = true
    elseif event == obs.OBS_FRONTEND_EVENT_RECORDING_STOPPED then
        is_recording = false
    end
end

-- Comprobación periódica del tiempo de grabación
function script_tick(seconds)
    if is_recording then
        local elapsed_time = os.time() - start_time
        if elapsed_time >= stop_time_in_seconds then
            obs.obs_frontend_recording_stop()
            is_recording = false
        end
    end
end

-- Añadir el callback de eventos
obs.obs_frontend_add_event_callback(on_event)
```

### ¿Qué he corregido?
1. **`obs = obslua`:** Asegúrate de que `obs` esté correctamente definido como una referencia a la API de OBS. La línea `obs = obslua` soluciona el problema de que `obs` sea un valor nulo (nil).
2. **Control de eventos:** El código ahora debería escuchar correctamente los eventos de inicio y detención de grabación.
3. **Descripción y propiedades del script:** Ahora está estructurado correctamente para que OBS lo entienda sin errores.

### Instrucciones de uso:
1. Copia este script.
2. Guarda el archivo con el nombre **`auto_stop_recording.lua`**.
3. Abre **OBS Studio**.
4. Ve a **Herramientas** > **Scripts**.
5. Carga el script guardado.
6. Ajusta el tiempo si lo necesitas en la interfaz de OBS.

Este script debería funcionar correctamente ahora y detenerá la grabación tras el tiempo que hayas especificado (por defecto 8 horas). Si encuentras algún otro error, no dudes en comentarlo.
---


Para configurar OBS (Open Broadcaster Software) para que detenga la grabación automáticamente después de 8 horas, puedes hacerlo a través de un **script en Lua**. OBS no tiene una opción directa en su interfaz gráfica para detener la grabación después de un tiempo específico, pero puedes añadir un script que realice esta tarea.

Sigue estos pasos para agregar un script en Lua que detenga la grabación tras 8 horas (o el tiempo que desees):

### Paso 1: Crear el script en Lua

1. Abre un editor de texto (como el Bloc de notas) y pega el siguiente código:

    ```lua
    -- Script to stop recording after a specified time (in seconds)
    
    local stop_time_in_seconds = 8 * 60 * 60  -- 8 hours in seconds
    
    local start_time = 0
    local is_recording = false
    
    function script_description()
        return "Detiene la grabación automáticamente después de un tiempo determinado (en segundos)."
    end
    
    function script_update(settings)
        stop_time_in_seconds = obs.obs_data_get_int(settings, "stop_time")
    end
    
    function script_properties()
        local props = obs.obs_properties_create()
        obs.obs_properties_add_int(props, "stop_time", "Tiempo de grabación (segundos)", 1, 24 * 60 * 60, 1)
        return props
    end
    
    function on_event(event)
        if event == obs.OBS_FRONTEND_EVENT_RECORDING_STARTED then
            start_time = os.time()
            is_recording = true
        elseif event == obs.OBS_FRONTEND_EVENT_RECORDING_STOPPED then
            is_recording = false
        end
    end
    
    function script_tick(seconds)
        if is_recording then
            local elapsed_time = os.time() - start_time
            if elapsed_time >= stop_time_in_seconds then
                obs.obs_frontend_recording_stop()
                is_recording = false
            end
        end
    end
    
    obs.obs_frontend_add_event_callback(on_event)
    ```

2. Guarda este archivo como **"auto_stop_recording.lua"** (asegúrate de que tenga la extensión `.lua`).

### Paso 2: Cargar el script en OBS

1. Abre **OBS Studio**.
2. Haz clic en **Herramientas** > **Scripts**.
3. En la ventana de Scripts, haz clic en el botón **+** para agregar un nuevo script.
4. Busca y selecciona el archivo **"auto_stop_recording.lua"** que creaste anteriormente.
5. Una vez cargado el script, verás una opción que te permite cambiar el tiempo en segundos (por defecto, ya está configurado para 8 horas).

### Paso 3: Configuración

- El script ya está configurado para detener la grabación después de 8 horas (8 * 60 * 60 segundos = 28,800 segundos).
- Si deseas cambiar el tiempo, puedes modificar el valor en la opción de "Tiempo de grabación" dentro del menú de Scripts de OBS o cambiar el valor en el archivo de script (el número de segundos).

Con esto, tu OBS detendrá la grabación automáticamente después de 8 horas.
---


El error podría deberse a una de varias razones comunes al cargar scripts en OBS. Vamos a revisar posibles soluciones y ajustar el script si es necesario:

### 1. **Revisa la sintaxis del script:**

El script anterior puede tener alguna incompatibilidad menor con la versión de OBS o la API de scripts de Lua. Prueba con este script actualizado para asegurarte de que funcione correctamente:

```lua
obs = obslua

-- Script to stop recording after a specified time (in seconds)
local stop_time_in_seconds = 8 * 60 * 60  --
---


Para convertir 7 horas en segundos, usamos la siguiente fórmula:

\[
\text{segundos} = \text{horas} \times 60 \times 60
\]

Calculando:

\[
7 \times 60 \times 60 = 25,200 \text{ segundos}
\]

Entonces, **7 horas equivalen a 25,200 segundos**.

---
*Generado desde conversación con 10 mensajes.*
*General*
