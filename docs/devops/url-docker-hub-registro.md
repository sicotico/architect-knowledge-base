---
title: URL Docker Hub Registro
date: 2025-03-21
category: DevOps
slug: url-docker-hub-registro
tags: ['DevOps']
---

# URL Docker Hub Registro


> **Pregunta original:**
> 
Tenho una cuenta de docker hub. pero no se cual es la url de mi registry 

---


## Respuesta


¡Perfecto que ya tengas una cuenta de Docker Hub!

Tu **Docker Hub registry URL** sigue un formato estándar. En la mayoría de los casos, simplemente es:

```
docker.io/NOMBRE_DE_USUARIO
```

### Ejemplo:
Si tu nombre de usuario en Docker Hub es `juanperez`, tu registry sería:

```
docker.io/juanperez
```

### ¿Dónde se usa esto?
Cuando haces `docker push` o `docker pull`, lo usas así:

```bash
docker pull docker.io/juanperez/mi-imagen
```

O incluso puede omitir el `docker.io` (Docker lo asume por defecto):

```bash
docker pull juanperez/mi-imagen
```

---

¿Querés que te ayude a probarlo o a crear una imagen y subirla al registry?
---


¡Perfecto que ya tengas cuenta en Docker Hub! Si estás buscando la URL de tu *registry* (registro) para usar con comandos como `docker push` o `docker pull`, la URL por defecto de Docker Hub es:

```
docker.io
```

Y la forma completa de tu *registry* con tu nombre de usuario y repositorio sería:

```
docker.io/tu_usuario/tu_repositorio
```

Por ejemplo, si tu nombre de usuario en Docker Hub es `juanperez` y el repositorio se llama `miapp`, entonces la URL sería:

```
docker.io/juanperez/miapp
```

Cuando haces `docker login`, simplemente pon tu usuario y contraseña, y Docker ya sabe que estás trabajando con Docker Hub por defecto (a menos que especifiques otro registro privado).

---

### Ejemplo completo:

```bash
docker login
docker tag miimagen juanperez/miapp
docker push juanperez/miapp
```

Esto sube la imagen a Docker Hub y estará accesible en:

```
https://hub.docker.com/r/juanperez/miapp
```

¿Quieres que te ayude a configurar un `docker push` completo?

---
*Generado desde conversación con 3 mensajes.*
*DevOps*
