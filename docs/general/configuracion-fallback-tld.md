---
title: Configuración fallback TLD
date: 2026-05-07
category: General
slug: configuracion-fallback-tld
tags: ['General']
---

# Configuración fallback TLD


> **Pregunta original:**
> 
de version de TLS
> firefox no esta redirigiendo correctamente una conexion a un NAS de UGREEN q a la version sin SSL y no me carga. Como puedo solucionarlo porque el microsoft edge si funciona  
> usando l aip funciona perfecto
> 
> *...y 2 preguntas de seguimiento*


---


## Respuesta


El problema probablemente no es TLS directamente. El mensaje indica un fallo de resolución o conexión a `nas2.local`.

Edge suele resolver mejor ciertos nombres `.local` porque usa mecanismos adicionales de descubrimiento de red. Firefox/Waterfox depende más estrictamente de mDNS/Bonjour.

## Causa más común

`nas2.local` usa:

- mDNS / Bonjour / Zeroconf

y en Firefox/Waterfox puede fallar si:

- mDNS está desactivado,
- el servicio Bonjour no existe,
- IPv6/multicast está bloqueado,
- o el NAS anuncia mal el hostname.

---

# Solución más rápida

## Entrar usando la IP directa

En vez de:

```text id="8mzlhv"
https://nas2.local
```

usa:

```text id="0nrylr"
https://192.168.X.X
```

o

```text id="mlym4v"
http://192.168.X.X
```

La IP la puedes ver en:

- router,
- app UGREEN,
- Edge cuando sí conecta,
- `arp -a` en terminal.

---

# Solución correcta en Firefox/Waterfox

## 1. Activar mDNS

Abre:

```text id="7s93e5"
about:config
```

Busca:

```text id="ahv4ce"
network.mdns.enabled
```

Ponlo en:

```text id="ekpbb9"
true
```

Reinicia Waterfox.

---

## 2. Desactivar DNS over HTTPS

DoH rompe muchos `.local`.

Ve a:

```text id="5w1jxr"
Configuración → Red → DNS sobre HTTPS
```

Desactivado.

O en `about:config`:

```text id="fjlwmq"
network.trr.mode = 5
```

---

# En Linux

Si usas Linux, instala Avahi:

## Debian/Ubuntu

```bash
sudo apt install avahi-daemon
```

## Arch

```bash
sudo pacman -S avahi
sudo systemctl enable --now avahi-daemon
```

---

# En Windows

Instala Bonjour:

- normalmente viene con iTunes,
- o con Bonjour Print Services.

Edge puede funcionar sin esto; Firefox no siempre.

---

# Verificación

Prueba:

```bash
ping nas2.local
```

Si NO resuelve IP:

- el problema es mDNS/Bonjour.

Si sí resuelve pero Firefox no conecta:

- entonces volvemos al problema TLS/HSTS anterior.

---

# Otra alternativa estable

En el router, crea un DNS local:

```text id="92mkt3"
nas2.home
```

o

```text id="2cfb85"
nas2.lan
```

Evita `.local`, porque mezcla:

- mDNS,
- multicast,
- resolución local especial,
- compatibilidad inconsistente entre navegadores.
---


Entonces el problema está aislado a la resolución de `nas2.local`, no al NAS ni a TLS.

Firefox/Waterfox no está resolviendo correctamente mDNS/Bonjour para `.local`, mientras Edge sí.

## Ajustes que normalmente lo corrigen

En `about:config`:

### Activar mDNS

```text id="8m3hqo"
network.mdns.enabled = true
```

---

### Desactivar DNS-over-HTTPS

```text id="22ynj9"
network.trr.mode = 5
```

o desde configuración gráfica:

```text id="70b0qc"
Ajustes → Red → DNS sobre HTTPS → Desactivado
```

---

### Reiniciar el navegador completamente

Cierra todos los procesos de Waterfox/Firefox.

---

# Verificación

Después prueba:

```text id="7hph4m"
http://nas2.local
```

y

```text id="cb2l7z"
https://nas2.local
```

---

# Si sigue fallando

El sistema operativo probablemente no tiene mDNS funcionando correctamente.

## Windows

Instalar Bonjour suele arreglarlo:

- urlBonjour Print Services for Windowshttps://support.apple.com/kb/DL999

---

## Linux

Instalar/activar Avahi.

---

# Recomendación práctica

Para NAS domésticos, `.local` suele ser poco fiable entre navegadores y OS.

Más estable:

- reservar IP fija al NAS,
- o crear DNS local tipo:

```text id="0z56vg"
nas2.home
```

en el router.
---


Si te refieres a configurar un **fallback de versiones TLS** en Firefox (por ejemplo permitir TLS 1.2 cuando TLS 1.3 falla), se hace desde `about:config`.

## Configurar versiones TLS en Firefox

1. Abre:

```text
about:config
```

2. Acepta la advertencia.

3. Busca estas claves:

- `security.tls.version.min`
- `security.tls.version.max`

## Valores posibles

| Valor | TLS |
|---|---|
| 1 | TLS 1.0 |
| 2 | TLS 1.1 |
| 3 | TLS 1.2 |
| 4 | TLS 1.3 |

## Configuración recomendada

### Compatibilidad moderna

- `security.tls.version.min = 3`
- `security.tls.version.max = 4`

Esto permite:

- mínimo TLS 1.2
- fallback automático a TLS 1.2 si TLS 1.3 falla

Firefox negocia automáticamente la mejor versión soportada por el servidor.

---

## Si un sitio viejo falla

Puedes temporalmente bajar el mínimo:

```text
security.tls.version.min = 2
```

para permitir TLS 1.1.

No es recomendable habilitar TLS 1.0/1.1 permanentemente por seguridad.

---

## Verificar qué TLS usa una web

En Firefox:

1. Abre el sitio.
2. Clic en el candado.
3. `Conexión segura` → `Más información`.
4. Verás la versión TLS negociada.

O usa herramientas como:

- urlSSL Labs Server Testhttps://www.ssllabs.com/ssltest/

---

## Parámetros relacionados útiles

### Desactivar completamente TLS 1.3

```text
security.tls.version.max = 3
```

### Permitir 0-RTT TLS 1.3

```text
security.tls.enable_0rtt_data
```

### Configuración empresarial/políticas

Firefox también soporta políticas vía:

- `policies.json`
- GPO en Windows
- autoconfig JS

si necesitas aplicarlo masivamente.
---


¿Te refieres a alguno de estos casos?

1. **Fallback de dominios/TLD al escribir en la barra**  
   Ejemplo: escribir `empresa` y que Firefox pruebe automáticamente `empresa.com`, `empresa.es`, etc.

2. **Fallback DNS / DoH (DNS over HTTPS)**  
   Configurar Firefox para usar un DNS alternativo si falla el principal.

3. **Redirección automática entre TLDs**  
   Como intentar `.com` si `.es` no responde.

4. **Búsqueda con keyword fixup** en `about:config`.

Indica cuál quieres configurar y te doy los pasos exactos.
---


Lo más probable es que Firefox esté aplicando una política más estricta de HTTPS/TLS que Edge. En muchos NAS (incluidos algunos modelos de urlUGREEN NAShttps://nas.ugreen.com/) ocurre esto:

- el NAS redirige mal entre HTTP↔HTTPS,
- usa un certificado inválido/autofirmado,
- negocia TLS de forma incorrecta,
- o Firefox está forzando HTTPS automáticamente.

## Diagnóstico rápido

Prueba estas URLs explícitamente:

```text
http://IP_DEL_NAS:PUERTO
```

y

```text
https://IP_DEL_NAS:PUERTO
```

Ejemplo:

```text
http://192.168.1.50:9999
```

No uses el hostname primero. Usa la IP directa.

---

# Soluciones habituales

## 1. Desactivar “HTTPS-Only Mode”

Firefox puede estar forzando HTTPS.

Ve a:

```text
Configuración → Privacidad y seguridad → Modo solo HTTPS
```

Pon:

- “No activar modo solo HTTPS”

o añade excepción para la IP del NAS.

---

## 2. Borrar el upgrade automático HSTS

Firefox puede haber memorizado que ese host “debe” usar HTTPS.

### Limpiar HSTS

Abre:

```text
Historial → Limpiar historial reciente
```

Marca:

- “Configuración del sitio”

O más preciso:

1. Abre:

```text
about:networking#dns
```

y limpia DNS cache.

2. Luego:

```text
about:config
```

Busca:

```text
network.stricttransportsecurity.preloadlist
```

(no suele ser el problema, pero ayuda diagnosticar).

Más efectivo:

1. Abre:

```text
about:preferences#privacy
```

2. Cookies y datos → “Administrar datos”
3. Elimina el NAS.

---

## 3. Desactivar DNS over HTTPS temporalmente

Algunos NAS locales se resuelven mal con DoH.

Ve a:

```text
Configuración → Privacidad y seguridad → DNS sobre HTTPS
```

Desactívalo temporalmente.

---

## 4. Forzar compatibilidad TLS

Muchos NAS viejos o firmware recientes mal configurados fallan con TLS 1.3.

En:

```text
about:config
```

pon:

```text
security.tls.version.max = 3
```

Eso fuerza TLS 1.2.

Si funciona, el problema es implementación TLS del NAS.

---

## 5. Permitir certificados autofirmados

Si Firefox muestra:

- `SEC_ERROR_UNKNOWN_ISSUER`
- `SSL_ERROR_BAD_CERT_DOMAIN`
- `PR_END_OF_FILE_ERROR`

entra directamente por HTTPS y añade excepción:

```text
Avanzado → Aceptar el riesgo
```

Edge suele ser más permisivo con algunos certificados locales.

---

## 6. Desactivar HTTP/3

Algunos dispositivos embebidos negocian mal QUIC/HTTP3.

En:

```text
about:config
```

cambia:

```text
network.http.http3.enable = false
```

---

# El ajuste que más suele arreglarlo

En NAS domésticos:

1. desactivar HTTPS-only,
2. borrar HSTS,
3. forzar TLS 1.2 (`security.tls.version.max=3`).

Eso resuelve la mayoría de incompatibilidades con Firefox.

---

# Si sigue fallando

Necesitaría el error exacto de Firefox:

- `PR_END_OF_FILE_ERROR`
- `SSL_ERROR_RX_RECORD_TOO_LONG`
- `SEC_ERROR_*`
- pantalla en blanco,
- timeout,
- redirección infinita,
- etc.

Cada uno apunta a una causa distinta.

---
*Generado desde conversación con 10 mensajes.*
*General*
