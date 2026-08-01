---
title: Problemas con nginx y curl
date: 2026-05-06
category: Networking
slug: problemas-con-nginx-y-curl
tags: ['Networking']
---

# Problemas con nginx y curl


> **Pregunta original:**
> 
en la ubuntu 26.014 me pasa esto 
sico@sico-Modern:~$ curl nas2.local:9999
<html>
<head><title>307 Temporary Redirect</title></head>
<body>
<center><h1>307 Temporary Redirect</h1></center>
<hr><center>nginx</center>
</body>
</html>
sico@sico-Modern:~$ curl nas.local:5001
<html>
<head><title>400 The plain HTTP request was sent to HTTPS port</title></head>
<body>
<center><h1>400 Bad Request</h1></center>
<center>The plain HTTP request was sent to HTTPS port</center>
<hr><center>nginx</center>
</body>
</html>
sico@sico-Modern:~$ 

---


## Respuesta


Lo que estás viendo no es un error de Ubuntu ni de `curl`, sino del servidor (tu NAS con **nginx**) que está forzando HTTPS o redirigiendo.

Analicemos cada caso con precisión:

---

## 1) `curl nas2.local:9999` → **307 Temporary Redirect**

Esto significa:

- El servidor está respondiendo: *“esto está en otra URL”* (normalmente HTTPS).
- Código **307** = redirección temporal manteniendo método (correcto para APIs).

### Qué hacer

Ejecuta:

```bash
curl -L nas2.local:9999
```

`-L` hace que `curl` siga la redirección automáticamente.

Si quieres ver a dónde redirige:

```bash
curl -v nas2.local:9999
```

Busca cabecera `Location:`.

---

## 2) `curl nas.local:5001` → **400: HTTP request sent to HTTPS port**

Este es más claro:

- Estás usando **HTTP** (`curl` por defecto)
- Pero el puerto **5001** está configurado para **HTTPS**

👉 Esto es típico de NAS (por ejemplo entity["company","Synology","NAS manufacturer"] usa 5001 para HTTPS)

---

## Solución correcta

Usa HTTPS explícitamente:

```bash
curl https://nas.local:5001
```

---

## Probable siguiente error

Seguramente verás algo como:

```
curl: (60) SSL certificate problem
```

Porque el NAS usa certificado autofirmado.

### Solución rápida (solo testing)

```bash
curl -k https://nas.local:5001
```

`-k` = ignora validación SSL.

---

## Resumen técnico

| Caso | Problema | Solución |
|------|----------|----------|
| puerto 9999 | redirección (307) | `curl -L` |
| puerto 5001 | HTTPS obligatorio | `curl https://...` |
| certificado | autofirmado | `curl -k` |

---

## Diagnóstico adicional (opcional)

Si quieres ver exactamente qué hace nginx:

```bash
curl -vk https://nas.local:5001
```

o:

```bash
curl -I http://nas2.local:9999
```

---

Si quieres, dime qué servicio corre en ese NAS (Synology, TrueNAS, Docker, etc.) y te explico exactamente por qué nginx está configurado así y cómo cambiarlo.

---
*Generado desde conversación con 2 mensajes.*
*Networking*
