---
title: Problema HTTPS en Waterfox
date: 2026-05-07
category: Networking
slug: problema-https-en-waterfox
tags: ['Networking']
---

# Problema HTTPS en Waterfox


> **Pregunta original:**
> 
ahora necesito qu eme expliques que es y como funciona el sistema de resolucion de nombres de systemd. En l aubuntu 26.04 no lo tiene configurado y sinembarlos los logs si. Me resulta inconsistente el systemd
> al final era que el flatpack no tenia configurado nsswitch y yo en ubuntu no tenia systemctl 
> En Firefox si entro a nas2.local:9999 pero en waterfox me da error , asi que creo que hay algo en waterfox que no permite redirigir de HTTPs a HTTP. El caso es que he deshabilitado solo HTTPs y sigue igual. 
> 
> *...y 1 preguntas de seguimiento*


---


## Respuesta


Eso encaja bastante bien con el síntoma.

Si estabas usando **Waterfox como Flatpak**, el problema probablemente no era HTTPS sino **resolución de nombres `.local` dentro del sandbox**.

`.local` normalmente depende de:

- **mDNS / Avahi**
- configuración en `/etc/nsswitch.conf`
- el módulo `mdns` (`libnss-mdns`)

En Ubuntu suele haber una línea parecida a:

```text
hosts: files mdns4_minimal [NOTFOUND=return] dns
```

o:

```text
hosts: files mdns_minimal [NOTFOUND=return] resolve dns
```

Cuando el navegador corre en Flatpak:

- no siempre ve el `nsswitch.conf` del host,
- o no tiene acceso al resolvedor adecuado,
- y `nas2.local` deja de resolverse.

Además, si no tenías `systemctl`, imagino que estabas en un entorno donde **systemd no gestionaba `systemd-resolved`** (WSL, contenedor, sesión mínima, instalación rara o derivada). En esos casos muchas guías que dicen:

```bash
systemctl restart systemd-resolved
```

no aplican.

Para verificarlo normalmente basta:

```bash
getent hosts nas2.local
```

Si eso falla fuera del navegador → problema de resolución.

Y dentro del Flatpak:

```bash
flatpak run --command=sh io.gitlab.waterfox.Waterfox
getent hosts nas2.local
```

(si el runtime trae `getent`).

También suele verse con:

```bash
flatpak override --filesystem=/etc/nsswitch.conf
```

aunque depende del paquete y no siempre es la mejor solución.

En cualquier caso, buen diagnóstico: el hecho de que Firefox funcionara y Waterfox no era una pista clara de **diferencia de entorno de ejecución**, no de política HTTPS.
---


Lo que estás viendo tiene sentido, pero hay varias capas mezcladas. El punto clave es: **systemd no es “el sistema de resolución de nombres”**; tiene componentes opcionales que pueden participar en ella. En Ubuntu moderno puede haber resolución funcionando aunque `systemd-resolved` no esté activo o no esté integrado donde esperas.

## La arquitectura clásica de resolución en Linux

Cuando una aplicación hace:

```c
getaddrinfo("nas2.local")
```

no pregunta directamente a DNS.

Hace esto:

```text
Aplicación
   ↓
glibc (getaddrinfo)
   ↓
NSS (Name Service Switch)
   ↓
módulos configurados en /etc/nsswitch.conf
   ↓
DNS / mDNS / hosts / systemd-resolved / etc.
```

El archivo central es:

```text
/etc/nsswitch.conf
```

Ejemplo:

```text
hosts: files mdns4_minimal [NOTFOUND=return] dns
```

Significa:

1. mirar `/etc/hosts`
2. probar mDNS (`*.local`)
3. si no aparece → consultar DNS

---

# ¿Dónde entra systemd?

Hay dos piezas distintas.

## 1. systemd-resolved (resolver)

Servicio:

```text
systemd-resolved.service
```

Es un resolvedor local.

Recibe consultas y decide:

- qué DNS usar
- cachear respuestas
- hacer DNSSEC
- split DNS
- resolver `.local`
- integrar VPN

Normalmente escucha en:

```text
127.0.0.53:53
```

Por eso a veces ves:

```text
nameserver 127.0.0.53
```

en:

```text
/etc/resolv.conf
```

Flujo:

```text
App
 ↓
glibc
 ↓
nsswitch
 ↓
nss-resolve
 ↓
systemd-resolved
 ↓
DNS real
```

---

## 2. nss-systemd (módulo NSS)

Esto es distinto.

Archivo:

```text
libnss_resolve.so
```

o

```text
libnss_systemd.so
```

Hace que glibc consulte `systemd-resolved`.

En `nsswitch.conf` aparece algo así:

```text
hosts: files resolve dns
```

Aquí:

- `resolve` → usar systemd-resolved
- `dns` → usar DNS tradicional

---

# Entonces ¿por qué en Ubuntu 26.04 parece inconsistente?

Porque **los logs de systemd no significan que uses systemd-resolved**.

Puedes tener:

```text
systemd-journald
```

funcionando (logs)

pero NO:

```text
systemd-resolved
```

activo.

Cada servicio es independiente.

Compruébalo:

```bash
systemctl status systemd-resolved
```

o si no tienes systemctl:

```bash
ps aux | grep resolved
```

---

## Caso A — usando systemd-resolved

```text
/etc/resolv.conf
↓
nameserver 127.0.0.53
```

y

```text
hosts: files resolve
```

---

## Caso B — sin systemd-resolved

```text
/etc/resolv.conf
↓
nameserver 192.168.1.1
```

y

```text
hosts: files dns
```

glibc consulta DNS directamente.

---

## Caso C — resolución mDNS (`.local`)

Para `nas2.local` normalmente:

```text
hosts: files mdns4_minimal dns
```

Interviene:

- entity["software","Avahi","mDNS implementation"]
- `libnss-mdns`

No systemd.

---

# Por qué tu caso del Flatpak falló

Muy probablemente:

Host:

```text
glibc
↓
nsswitch.conf
↓
mdns
↓
Avahi
↓
nas2.local OK
```

Flatpak:

```text
glibc
↓
nsswitch.conf incompleto
↓
dns
↓
.local falla
```

No llegó nunca a systemd.

---

# Cómo inspeccionar el stack real

```bash
cat /etc/nsswitch.conf
```

```bash
cat /etc/resolv.conf
```

```bash
getent hosts nas2.local
```

```bash
resolvectl status
```

(si existe)

```bash
ls /lib/x86_64-linux-gnu/libnss*
```

Eso te dice quién está resolviendo realmente.

La sensación de inconsistencia suele venir de asumir que “si hay systemd entonces todo pasa por systemd”, pero Linux mantiene muchas rutas de resolución coexistiendo por compatibilidad.
---


Es probable que no sea solo “HTTPS Only Mode”. En entity["software","Waterfox","web browser"] pueden intervenir varias capas distintas:

- HTTPS-Only / HTTPS First
- DNS-over-HTTPS (DoH)
- HSTS cache
- bloqueo de mixed content
- diferencias de resolución `.local`
- políticas de seguridad heredadas de Firefox ESR

Y `.local` añade otro factor: normalmente usa mDNS/Bonjour, no DNS convencional.

## Lo más probable

Si `nas2.local:9999` funciona en entity["software","Firefox","web browser"] pero no en Waterfox, normalmente ocurre una de estas:

1. Waterfox intenta resolver `.local` vía DoH y falla.
2. Waterfox fuerza HTTPS antes de abrir HTTP.
3. Hay una entrada HSTS cacheada.
4. El certificado HTTPS del NAS está roto y Waterfox no hace fallback limpio.
5. El puerto `9999` solo escucha HTTP y Waterfox insiste en HTTPS.

---

# Pruebas rápidas

## 1. Probar URL explícita

Escribe exactamente:

```text
http://nas2.local:9999
```

No `nas2.local:9999` sin esquema.

Si así funciona, el problema es “HTTPS First”.

---

## 2. Desactivar HTTPS-Only y HTTPS-First reales

En Waterfox:

```text
about:preferences#privacy
```

Busca:

- HTTPS-Only Mode → OFF

Luego entra en:

```text
about:config
```

Busca y pon:

```text
dom.security.https_only_mode = false
dom.security.https_only_mode_ever_enabled = false
dom.security.https_first = false
dom.security.https_first_pbm = false
```

Reinicia Waterfox.

---

## 3. Desactivar DNS over HTTPS

Muy importante para `.local`.

En:

```text
about:preferences#general
```

→ Network Settings → Settings

Desmarca:

- Enable DNS over HTTPS

O en `about:config`:

```text
network.trr.mode = 5
```

Valor `5` = desactivado completamente.

Luego prueba otra vez.

---

## 4. Limpiar HSTS del host

A veces el navegador recuerda que ese host “debe” ir por HTTPS.

En historial:

```text
History → Clear Recent History
```

o directamente:

```text
about:networking#dns
```

- Clear DNS Cache

y también:

```text
about:networking#http
```

- Clear HSTS / Alt-Svc si aparece.

---

## 5. Probar con IP directa

Prueba:

```text
http://192.168.x.x:9999
```

Si la IP funciona y `nas2.local` no:

- el problema es resolución mDNS/DoH
- no HTTPS

---

# Configuración específica de `.local`

En `about:config` revisa:

```text
network.dns.disableIPv6 = false
network.trr.exclude-etc-hosts = true
```

Y especialmente:

```text
network.trr.mode
```

Valores útiles:

- `0` → normal
- `5` → DoH desactivado

Para redes locales, `5` suele evitar muchos problemas con `.local`.

---

# Diagnóstico útil

Abre:

```text
about:networking
```

Mira en:

- DNS
- Logging
- HTTP

y verifica si `nas2.local` resuelve.

---

# Conclusión

El síntoma encaja más con:

- DoH + `.local`
o
- HTTPS First/HSTS

que con el simple “HTTPS Only”.

La prueba decisiva es:

```text
http://IP_DEL_NAS:9999
```

Si eso funciona en Waterfox, ya sabes que el fallo está en la resolución o en la política HTTPS aplicada al hostname `.local`.

---
*Generado desde conversación con 7 mensajes.*
*Networking*
