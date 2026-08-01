---
title: Configurar ajuste de línea
date: 2024-12-02
category: General
slug: configurar-ajuste-de-linea
tags: ['General']
---

# Configurar ajuste de línea


> **Pregunta original:**
> 
Dudas con el editor Zed. como se configura para que el texto se auto ajuste al ancho de la pantalla

---


## Respuesta


Para configurar Zed de manera que el texto se ajuste automáticamente al ancho de la pantalla, es necesario habilitar la opción de "soft wrap" (ajuste suave de línea). Esto se logra añadiendo la siguiente línea en el archivo de configuración `settings.json`:

```json
{
  "soft_wrap": true
}
```

Este ajuste permite que las líneas de texto se ajusten automáticamente al ancho de la ventana del editor, evitando la necesidad de desplazarse horizontalmente para leer líneas largas.

Para editar el archivo `settings.json` en Zed, sigue estos pasos:

1. Abre la paleta de comandos presionando `Ctrl+Shift+P` (o `Cmd+Shift+P` en macOS).
2. Escribe `zed: open settings` y selecciona la opción que aparece.
3. En el archivo de configuración que se abre, agrega o modifica la línea mencionada anteriormente para habilitar el ajuste automático de línea.
4. Guarda los cambios y el ajuste se aplicará de inmediato.

Si prefieres activar o desactivar el ajuste de línea según sea necesario, puedes asignar un atajo de teclado para esta función. Por ejemplo, para asignar `Ctrl+Alt+W` para alternar el ajuste de línea, agrega lo siguiente al archivo `keymap.json`:

```json
[
  {
    "bindings": {
      "ctrl-alt-w": "editor::ToggleSoftWrap"
    }
  }
]
```

Para editar el archivo `keymap.json`:

1. Abre la paleta de comandos con `Ctrl+Shift+P` (o `Cmd+Shift+P` en macOS).
2. Escribe `zed: open keymap` y selecciona la opción que aparece.
3. En el archivo que se abre, agrega la configuración anterior para asignar el atajo de teclado deseado.
4. Guarda los cambios y el nuevo atajo estará disponible de inmediato.

Estos ajustes te permitirán personalizar Zed para que el texto se ajuste automáticamente al ancho de la pantalla, mejorando la legibilidad y adaptándose a tus preferencias de edición.

---
*Generado desde conversación con 2 mensajes.*
*General*
