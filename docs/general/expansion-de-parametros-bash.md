---
title: Expansión de parámetros Bash
date: 2026-07-21
category: General
slug: expansion-de-parametros-bash
tags: ['General']
---

# Expansión de parámetros Bash


> **Pregunta original:**
> 
en un bash esto quiere decir que si la variable no tiene valor aplica 4096   --ctx-size "${LLAMA_CTX:-4096}" \

---


## Respuesta


Sí. Esa es la expansión de parámetros de Bash con un valor por defecto.

```bash
--ctx-size "${LLAMA_CTX:-4096}" \
```

Significa:

- Si `LLAMA_CTX` **está definida y no está vacía**, usa su valor.
- Si `LLAMA_CTX` **no está definida** o **está vacía (`""`)**, usa `4096`.

Ejemplos:

```bash
unset LLAMA_CTX
echo "${LLAMA_CTX:-4096}"
# 4096
```

```bash
LLAMA_CTX=""
echo "${LLAMA_CTX:-4096}"
# 4096
```

```bash
LLAMA_CTX=8192
echo "${LLAMA_CTX:-4096}"
# 8192
```

### Diferencia con otras variantes

```bash
${VAR:-valor}
```
Usa `valor` si `VAR` **no existe o está vacía**.

```bash
${VAR-valor}
```
Usa `valor` **solo si `VAR` no existe**. Si existe pero está vacía, devuelve la cadena vacía.

```bash
${VAR:=valor}
```
Además de devolver `valor`, **asigna** ese valor a `VAR` si estaba sin definir o vacía.

```bash
${VAR:?mensaje}
```
Aborta el script mostrando `mensaje` si `VAR` no está definida o está vacía.

En tu caso:

```bash
--ctx-size "${LLAMA_CTX:-4096}"
```

es una forma muy habitual de permitir que el usuario sobrescriba el tamaño del contexto mediante una variable de entorno:

```bash
export LLAMA_CTX=8192
./mi_script.sh
```

Si no hace el `export` (o la variable está vacía), el script utilizará `4096`.

---
*Generado desde conversación con 2 mensajes.*
*General*
