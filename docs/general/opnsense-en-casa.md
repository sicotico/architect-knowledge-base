---
title: OPNsense en casa
date: 2026-06-13
category: General
slug: opnsense-en-casa
tags: ['General']
---

# OPNsense en casa


> **Pregunta original:**
> 
La MV de OPNSense estará en un NAS Ugreen con chip N100 y 8 GB ddr5, pero tendrá asigando 1 o 2 cores y 2 gb de RAM. Entiendo que esto es suficiente ya que el routing y la negociacion del PPOE la hacen los DECOs x20  
> Pi-hole puede identificar el tráfico DoH???
> estoy valorando montar un OPNsesne en casa , pero con el DHCP de mi router DECO x20 mesh  , usando una ruta estatica a  la MV con OPNsense y luego de ahí otro salto al router DECO x20 e internet . ¿tiene sentido ? ¿hay equipos que ya vengan con OPNsesne? ¿solo quiero que los menores de casa tenga todo bloqueado ?
> 
> *...y 7 preguntas de seguimiento*


---


## Respuesta


Exacto. Has identificado una de las limitaciones más importantes de las soluciones basadas únicamente en DNS.

Si instalas únicamente entity["software","AdGuard Home","DNS filtering software"] o entity["software","NextDNS","Cloud DNS filtering service"]:

```text
Navegador
   |
DoH a Cloudflare
   |
Internet
```

el navegador puede ignorar completamente tu servidor DNS local.

Y hoy en día:

- Chrome soporta DoH.
- Firefox soporta DoH.
- Edge soporta DoH.
- Android lo usa mediante DNS privado.
- Algunas apps implementan DoH o DoT internamente.

Por eso los controles parentales basados únicamente en DNS son cada vez menos robustos.

---

## Lo que sí funciona mejor

Para impedir evasiones necesitas actuar en alguno de estos niveles:

### Nivel 1: Control del dispositivo

Por ejemplo:

- Google Family Link.
- Microsoft Family Safety.
- Apple Screen Time.

Ventaja:

- Es muy difícil de saltar para un niño pequeño.

Inconveniente:

- Depende del sistema operativo.
- No protege dispositivos no gestionados.

---

### Nivel 2: Firewall de red

Aquí es donde OPNsense empieza a tener sentido.

Puedes:

- bloquear DNS externos;
- bloquear DoT (853/TCP);
- bloquear resolvers conocidos;
- interceptar DNS local.

Pero hay una realidad importante:

**DoH no puede bloquearse al 100% sólo con reglas IP.**

Porque:

```text
https://cloudflare-dns.com
https://dns.google
https://quad9.net
```

es tráfico HTTPS normal.

Además aparecen constantemente nuevos proveedores.

---

### Nivel 3: Filtrado por aplicación/categoría

Aquí entran:

- entity["software","Zenarmor","Network security platform"]
- entity["software","Sophos Firewall Home Edition","Home firewall edition"]

Estos sistemas inspeccionan más allá del DNS.

Pueden identificar:

- YouTube.
- TikTok.
- Discord.
- VPNs conocidas.
- Categorías de contenido.

Aunque el DNS se salte mediante DoH.

---

## La limitación real

Si hablamos de un adolescente mínimamente técnico:

- VPN comercial.
- Tailscale.
- WireGuard.
- Proxy HTTPS.
- Navegador portable.
- Hotspot móvil.

Ningún firewall doméstico garantiza un bloqueo absoluto.

Lo que haces es aumentar mucho la dificultad.

---

## En tu arquitectura concreta

Teniendo:

```text
ONT
 |
DECO X20
 |
NAS Ugreen
   └─ OPNsense VM
```

yo montaría OPNsense sólo si puedes conseguir que **los dispositivos de los menores pasen obligatoriamente por él**.

Porque entonces podrías:

- DNS propio.
- Bloqueo de DoT.
- Bloqueo de resolvers conocidos.
- Zenarmor.
- Horarios.
- Categorías.

Y eso es bastante más resistente que AdGuard Home solo.

---

## Mi valoración

### AdGuard Home solo

**Bueno**
- Muy sencillo.
- Poco consumo.

**Malo**
- DoH lo debilita mucho.
- Poco control de aplicaciones.

### OPNsense solo

**Bueno**
- Más control de red.
- Reglas avanzadas.

**Malo**
- Más complejo.
- No elimina completamente el problema de DoH.

### OPNsense + Zenarmor

**Bueno**
- Probablemente la mejor relación entre control y coste en un entorno doméstico avanzado.
- Filtra categorías independientemente del DNS.
- Detecta muchas aplicaciones y servicios.

**Malo**
- Más trabajo de configuración.
- Algunas capacidades avanzadas son de pago.

Para un usuario técnico que ya tiene un NAS N100, una ONT independiente y unos Deco, la combinación **OPNsense + Zenarmor para una red específica de menores** es la solución que veo más coherente si tu preocupación principal es precisamente que el filtrado DNS sea demasiado fácil de eludir.
---


La respuesta corta es: **no de forma fiable ni como función específica del Deco X20**.

Los Deco modernos han añadido soporte para que **el propio router use DoH/DoT hacia sus servidores DNS**, pero eso no significa que puedan impedir que los clientes usen su propio DoH. citeturn0search0turn0search6

Para bloquear DoH de los dispositivos necesitarías algo como:

- inspección de tráfico (DPI);
- filtrado por aplicación;
- bloqueo de resolvers DoH conocidos;
- proxy HTTPS o mecanismos similares.

Eso está más cerca de lo que ofrecen soluciones como entity["software","Zenarmor","Network security platform"] sobre entity["software","OPNsense","Open-source firewall"] que de lo que ofrece un Deco X20. citeturn0search2turn0search4

## Lo que sí puedes hacer con Deco

- Configurar DNS para toda la red.
- Aplicar controles parentales básicos.
- Usar HomeShield.
- En algunos firmwares configurar DoH para el propio router. citeturn0search0turn0search6

## Lo que no he visto que haga el X20

- "Bloquear todo DoH de los clientes".
- "Forzar que todos los dispositivos usen únicamente mi DNS local".
- DPI avanzado para detectar cualquier proveedor DoH.

---

## Un detalle importante

Si tus hijos tienen:

- Android con "DNS privado",
- Firefox con DoH activado,
- Chrome configurado con DNS seguro,

un filtrado DNS tradicional puede quedar neutralizado fácilmente.

Por eso, si tu preocupación principal es que **no puedan saltarse el filtrado cambiando el DNS**, entonces tu razonamiento de montar OPNsense tiene bastante sentido.

Lo que intentaría comprobar antes de invertir tiempo es si tu versión concreta del X20 dispone de:

- HomeShield gratuito o de pago.
- Red de invitados aislada.
- Algún tipo de política por dispositivo.

Porque si puedes meter los dispositivos de los menores en una red separada, entonces la arquitectura:

```text
Menores
   |
OPNsense
   |
Deco X20
   |
Internet
```

empieza a ser muy interesante y con 2 GB de RAM en el N100 debería funcionar sin problemas para ese uso. No me preocupa el hardware; me preocupa mucho más cómo vas a conseguir que **todo el tráfico de los menores pase obligatoriamente por OPNsense**. Ahí está la parte crítica del diseño.
---


Para el objetivo que has descrito (control parental relativamente estricto para los menores, manteniendo los Deco como router principal y ejecutando algo ligero en una MV del NAS), no elegiría necesariamente OPNsense por defecto.

## Opción 1: OPNsense + Zenarmor

- Muy flexible.
- Control por categorías web.
- Horarios.
- Estadísticas.
- Bloqueo DNS avanzado.

Software:
- entity["software","OPNsense","Open-source firewall"]
- entity["software","Zenarmor","Network security platform"]

Ventajas:
- Muy potente.
- Comunidad grande.
- Gratuito en gran parte.

Inconvenientes:
- Curva de aprendizaje.
- Algunas funciones más cómodas están en la versión de pago de Zenarmor.

---

## Opción 2: pfSense

- Similar a OPNsense.
- Más maduro en algunos aspectos.

Software:
- entity["software","pfSense","Open-source firewall"]

Ventajas:
- Muy estable.
- Muchísima documentación.

Inconvenientes:
- Para control parental no ofrece una ventaja clara frente a OPNsense.
- La interfaz suele resultar menos amigable.

Para tu caso concreto no veo motivos para preferirlo sobre OPNsense.

---

## Opción 3: AdGuard Home (muy interesante)

Software:
- entity["software","AdGuard Home","DNS filtering software"]

Página oficial:
- urlAdGuard Homehttps://adguard.com/en/adguard-home/overview.html

Qué hace:

- Filtrado DNS.
- Bloqueo de publicidad.
- Bloqueo de pornografía.
- Listas personalizadas.
- Estadísticas.

Ventajas:

- Consume muy pocos recursos.
- Mucho más sencillo que OPNsense.
- Perfecto para ejecutarlo en una MV pequeña o contenedor.

Inconvenientes:

- No es un firewall completo.
- Si los menores son técnicamente hábiles, puede requerir medidas adicionales para impedir DNS alternativos.

Para muchos hogares es suficiente.

---

## Opción 4: NextDNS

Software:
- entity["software","NextDNS","Cloud DNS filtering service"]

Página oficial:
- urlNextDNShttps://nextdns.io/

Ventajas:

- Probablemente el sistema de control parental más fácil de desplegar.
- Categorías muy detalladas.
- Informes.
- Bloqueo de aplicaciones.
- Sin necesidad de mantener una VM compleja.

Inconvenientes:

- Servicio externo.
- Algunas funciones avanzadas requieren suscripción.

---

## Opción 5: Sophos Home / Sophos Firewall Home Edition

Software:
- entity["software","Sophos Firewall Home Edition","Home firewall edition"]

Página oficial:
- urlSophos Firewall Home Editionhttps://www.sophos.com/en-us/free-tools/sophos-xg-firewall-home-edition

Ventajas:

- Filtrado web muy potente.
- Más orientado a seguridad empresarial.

Inconvenientes:

- Más pesado.
- Más complejo.
- Menos agradable para un laboratorio doméstico pequeño.

---

## Lo bueno y lo malo para tu caso

### Si quieres aprender redes y seguridad

**OPNsense + Zenarmor** es la mejor opción.

### Si sólo quieres bloquear contenido inapropiado

**NextDNS** o **AdGuard Home** suelen dar una relación esfuerzo/resultado mucho mejor.

### Si quieres algo intermedio

**AdGuard Home en una VM** detrás de los Deco es probablemente la solución más simple:

- apenas consume recursos;
- se integra bien con los Deco;
- no requiere rediseñar la topología;
- cubre gran parte de las necesidades de control parental.

Con lo que has contado hasta ahora, empezaría por **AdGuard Home o NextDNS** y sólo daría el salto a OPNsense si después echas en falta control más granular o te interesa el aprendizaje técnico.
---


No.

entity["software","Pi-hole","Network-level advertisement and DNS blocking"] **no puede identificar de forma fiable el tráfico DoH** porque Pi-hole opera fundamentalmente como servidor DNS. Cuando una aplicación usa DoH:

```text
Navegador
   |
HTTPS (443)
   |
Servidor DoH
```

Pi-hole ya no ve las consultas DNS. Lo único que ve es una conexión HTTPS normal.

## Lo que sí puede detectar Pi-hole

Si un dispositivo usa DNS clásico:

```text
Cliente
   |
UDP/TCP 53
   |
Pi-hole
```

entonces Pi-hole registra:

- dominios consultados;
- cliente que los consulta;
- estadísticas;
- bloqueos.

## Lo que ocurre con DoH

Con DoH:

```text
Cliente
   |
HTTPS 443
   |
dns.google
```

o

```text
Cliente
   |
HTTPS 443
   |
cloudflare-dns.com
```

Pi-hole no ve las consultas.

Verá simplemente que el dispositivo consulta inicialmente el dominio del proveedor DoH (si esa resolución pasó por él), pero después pierde visibilidad.

---

## ¿Puede Pi-hole bloquear DoH?

Sólo parcialmente.

Por ejemplo:

- bloquear `dns.google`
- bloquear `cloudflare-dns.com`
- bloquear `mozilla.cloudflare-dns.com`

Pero esto tiene varios problemas:

1. Aparecen nuevos proveedores continuamente.
2. Algunas aplicaciones llevan IPs embebidas.
3. HTTPS cifra el contenido.
4. Mantener listas es una carrera interminable.

---

## ¿Y OPNsense?

OPNsense tampoco "ve" automáticamente el contenido DoH.

La diferencia es que puedes añadir herramientas como:

- entity["software","Zenarmor","Network security platform"]
- Suricata
- listas de bloqueo de DoH
- políticas por aplicación

para identificar y bloquear muchos proveedores DoH conocidos.

Es bastante más eficaz que Pi-hole, pero tampoco es infalible.

---

## Si tu objetivo es control parental

La pregunta relevante no es "¿Pi-hole detecta DoH?", sino:

> "¿Cómo hago para que los menores no puedan saltarse el filtrado?"

Ordenadas de menos a más robustas:

| Solución | Resistencia frente a DoH |
|-----------|-----------|
| Pi-hole | Baja |
| AdGuard Home | Baja |
| NextDNS sin agente | Baja-Media |
| OPNsense + listas DoH | Media |
| OPNsense + Zenarmor | Media-Alta |
| Control del dispositivo (Family Link, Screen Time, etc.) | Alta |

La realidad es que para móviles y tablets de menores, **el control del dispositivo suele ser más efectivo que cualquier firewall doméstico**, porque impide cambiar DNS, instalar VPNs o modificar ajustes del navegador. El firewall complementa esa protección, pero rara vez la sustituye por completo.
---


Aquí hay un matiz importante: **una ruta estática no sirve para "enviar tráfico a un firewall para que lo inspeccione"**. Las rutas estáticas sólo indican *qué gateway usar para llegar a una red determinada*.

Por ejemplo:

```text
Red principal: 192.168.1.0/24
OPNsense:      192.168.1.10

Red menores:   192.168.50.0/24
```

En el Deco podrías crear:

```text
Destino: 192.168.50.0/24
Gateway: 192.168.1.10
```

Eso le dice al Deco:

> "Para llegar a la red 192.168.50.x, usa OPNsense."

Pero **no le dice**:

> "Envía todo el tráfico de Internet a OPNsense."

Son cosas distintas.

---

## Lo que probablemente tienes en mente

Algo parecido a:

```text
Cliente
   |
DECO
   |
OPNsense
   |
Internet
```

Sin embargo, el Deco no suele permitir una ruta por defecto (`0.0.0.0/0`) hacia un equipo LAN.

Y aunque lo permitiera, aparecerían problemas de routing asimétrico y doble NAT.

---

## La forma correcta

Si quieres que OPNsense filtre a los menores:

```text
              +--> Adultos
              |
DECO ---------+
              |
              +--> OPNsense --> Menores
```

Es decir:

- Deco sigue siendo el router principal.
- OPNsense crea una segunda red.
- Los dispositivos de menores tienen como gateway OPNsense.
- OPNsense usa el Deco como gateway de salida.

Ejemplo:

```text
LAN Deco
192.168.1.0/24

OPNsense WAN:
192.168.1.10

OPNsense LAN:
192.168.50.1

Gateway de OPNsense:
192.168.1.1 (Deco)
```

No necesitas rutas raras para Internet.

Sólo una ruta estática en el Deco:

```text
192.168.50.0/24 -> 192.168.1.10
```

Y ya está.

---

## ¿Puedes hacer excepciones para el tráfico de OPNsense?

Sí.

En el esquema anterior OPNsense tendría:

```text
Default Gateway = Deco
```

Todo lo que genere el propio OPNsense:

- actualizaciones,
- NTP,
- DNS,
- Zenarmor,

saldrá por el Deco normalmente.

No necesitas ninguna excepción especial.

---

## El problema práctico con los Deco

La pregunta clave es:

**¿Cómo vas a conectar los dispositivos de los menores a la LAN de OPNsense?**

Porque si todos siguen conectados al mismo SSID del Deco:

```text
Menores -> Deco -> Internet
```

nunca pasarán por OPNsense.

Necesitas alguna de estas opciones:

### Opción A

Un AP WiFi adicional conectado a la LAN de OPNsense.

```text
AP Menores
   |
OPNsense
   |
Deco
```

### Opción B

Una VLAN específica para menores.

Pero los X20 domésticos no son especialmente fuertes en VLANs avanzadas.

### Opción C

Dispositivos cableados detrás de OPNsense.

---

Por eso, antes de pensar en las rutas estáticas del Deco, intentaría resolver esta pregunta:

**¿Cómo piensas que los móviles y tablets de los menores se conecten físicamente o lógicamente a la red de OPNsense en lugar de conectarse directamente al WiFi del Deco?**

Esa respuesta determina si la arquitectura es viable o si hay que replantearla.
---


Eso cambia bastante el escenario.

Si los Deco X20 ya están conectados directamente a la ONT y son quienes levantan la conexión a Internet, entonces actualmente los Deco son tu router principal, NAT, DHCP y firewall.

En esa situación tienes tres opciones:

## Opción 1: Dejar los Deco como están y añadir OPNsense "al lado"

```text
Internet
   |
ONT
   |
DECO X20
   |
LAN
   |
OPNsense (MV)
```

Ventajas:

- No rompes nada.
- Muy fácil de probar.

Inconvenientes:

- OPNsense no controla el tráfico de toda la casa.
- No sirve como control parental global.
- Muchas funciones avanzadas quedan inutilizadas.

Lo veo útil para aprender OPNsense, no para proteger a los menores.

---

## Opción 2: Mantener Deco como router y enviar sólo los dispositivos de menores a OPNsense

```text
Internet
   |
ONT
   |
DECO X20
   |
OPNsense
   |
Dispositivos menores
```

Por ejemplo:

- un switch detrás de OPNsense;
- o un AP WiFi específico para los niños.

Ventajas:

- No tocas la red principal.
- Los adultos siguen funcionando igual.
- Los menores pasan obligatoriamente por OPNsense.

Inconvenientes:

- Necesitas separar físicamente o lógicamente esos dispositivos.
- Más complejidad operativa.

Para tu objetivo es bastante razonable.

---

## Opción 3: OPNsense como router principal

```text
Internet
   |
ONT
   |
OPNsense
   |
DECO X20 (modo AP)
```

Ventajas:

- Control total.
- DNS, firewall, IDS, filtrado web.
- VLANs.
- Redes separadas para adultos y menores.
- VPN.
- Estadísticas completas.

Inconvenientes:

- Reconfiguración completa.
- Los Deco pasarían a ser principalmente puntos de acceso mesh.

Si te gusta trastear con redes, esta suele acabar siendo la configuración definitiva.

---

## Sobre la MV

Aquí tendría cierta cautela.

Si la conexión de Internet de toda la casa va a depender de OPNsense:

- mejor mini-PC dedicada;
- o un servidor muy estable (Proxmox, ESXi, etc.).

Porque si:

- reinicias el host,
- actualizas el hipervisor,
- falla el almacenamiento,

te quedas sin Internet en toda la casa.

Por eso mucha gente usa equipos pequeños basados en entity["product","Intel N100 mini PC","Firewall appliance class"] o similares para OPNsense.

---

## Para tu caso concreto

Como comentas que **sólo quieres restringir a los menores**, probablemente no montaría OPNsense como router principal inicialmente.

Empezaría con:

```text
ONT
 |
DECO X20
 |
OPNsense
 |
Red de menores
```

y en OPNsense instalaría:

- DNS filtrado.
- Bloqueo de DNS externos.
- Zenarmor.
- Horarios de acceso.
- Bloqueo de categorías.

Así limitas el riesgo de dejar sin Internet al resto de la casa mientras aprendes cómo funciona OPNsense.

Una duda importante: ¿los menores usan principalmente **móviles/tablets por WiFi**, o también tienen **PCs/consolas**? Porque eso influye mucho en la forma más limpia de separarlos dentro de la red Deco.
---


Sí tiene sentido técnicamente, pero para tu objetivo concreto ("que los menores de casa tengan todo bloqueado") conviene analizar si no estás añadiendo demasiada complejidad.

## Lo que planteas

Entiendo algo parecido a esto:

```text
Dispositivos
      |
DECO X20 (DHCP)
      |
Ruta estática
      |
OPNsense (MV)
      |
Router principal / Internet
```

o incluso:

```text
Clientes -> DECO X20 -> OPNsense -> Internet
```

Manteniendo el DHCP en los Deco y enviando cierto tráfico hacia OPNsense mediante rutas estáticas.

### Ventajas

- Mantienes intacta la red mesh de los Deco.
- No tienes que reconfigurar toda la casa.
- Puedes probar OPNsense sin romper nada.

### Inconvenientes

- Muchas funciones de OPNsense dependen de estar en el camino real del tráfico (gateway).
- Los controles parentales, filtrado DNS, IDS/IPS, bloqueo web, etc. funcionan mejor cuando OPNsense es el router principal.
- Las rutas estáticas pueden complicar bastante la gestión.

Para un laboratorio o aprendizaje, sí.
Para control parental, no es la arquitectura que elegiría.

---

## Alternativa más lógica

Crear una red específica para menores.

Por ejemplo:

```text
Internet
   |
OPNsense
   |
DECO X20
   ├── VLAN/SSID Adultos
   └── VLAN/SSID Menores
```

Y aplicar reglas sólo a la VLAN o SSID de menores.

El problema es que los Deco X20 domésticos tienen capacidades de VLAN bastante limitadas según la versión y modo de funcionamiento.

---

## Antes de montar OPNsense: ¿qué quieres bloquear?

Hay tres niveles muy distintos:

### Nivel 1: DNS filtrado

Muy sencillo.

- urlOpenDNS FamilyShieldhttps://www.opendns.com/home-internet-security/
- urlCloudflare Family DNShttps://blog.cloudflare.com/introducing-1-1-1-1-for-families/
- urlAdGuard Family DNShttps://adguard-dns.io/en/public-dns.html

Ventajas:

- Gratis.
- Muy fácil.
- Bloquea pornografía y bastantes categorías.

Inconvenientes:

- Un adolescente con ciertos conocimientos puede saltárselo.

---

### Nivel 2: Control parental del propio Deco

Los Deco X20 incluyen HomeShield.

urlTP-Link HomeShieldhttps://www.tp-link.com/homeshield/

Permite:

- perfiles por niño;
- horarios;
- límites de tiempo;
- categorías bloqueadas.

Para muchos hogares es suficiente.

---

### Nivel 3: OPNsense

Aquí sí obtienes control serio:

- DNS propio (Unbound).
- DNS-over-TLS.
- Bloqueo por categorías.
- Listas negras.
- Bloqueo de VPN conocidas.
- Bloqueo de redes sociales.
- Horarios.
- Registro de actividad.

Normalmente se combina con:

- urlZenarmorhttps://www.zenarmor.com/
- urlOPNsensehttps://opnsense.org/

Zenarmor es probablemente lo más parecido a un "control parental avanzado" dentro de OPNsense.

---

## Equipos que ya vienen con OPNsense

Sí.

Los más conocidos:

- urlDeciso Applianceshttps://shop.opnsense.com/ (fabricante oficial de OPNsense)
- urlProtectlihttps://protectli.com/
- urlToptonhttps://www.toptonpc.com/
- urlCWWKhttps://cwwk.net/

Para una casa normal:

- N100
- 8 GB RAM
- SSD 128 GB
- 2.5 GbE

es más que suficiente.

---

## Lo que haría yo para tu caso

Si el objetivo es únicamente controlar a los menores:

1. Probar primero HomeShield de los Deco.
2. Si se queda corto, montar OPNsense en una mini-PC N100.
3. Hacer que OPNsense sea el router principal de la casa.
4. Crear una red o grupo específico para los dispositivos de los menores.
5. Instalar Zenarmor y políticas DNS estrictas.

Mantener DHCP en los Deco y usar rutas estáticas hacia una MV de OPNsense me parece una solución más adecuada para aprender OPNsense que para implementar control parental robusto. Para filtrar de verdad, OPNsense debería estar en el camino principal de salida a Internet.

Por cierto, ¿tu operador es Movistar, Digi, Orange, Vodafone u otro? Dependiendo del operador, poner OPNsense delante del Deco puede ser trivial o requerir gestionar VLANs y PPPoE.
---


Es posible. Si te recomendé hace bastante tiempo alguna combinación tipo Ubuntu + extensiones GNOME concretas, o distribuciones como Pop!_OS antes de la llegada de COSMIC, algunas recomendaciones pueden haber envejecido mal.

Para **2026** y para el caso específico de un **equipo para menores**, separaría dos objetivos:

## Si buscas control parental

GNOME no es lo importante.

Lo importante es:

- usuario sin privilegios de administrador;
- actualizaciones automáticas;
- navegador gestionado;
- bloqueo de instalación de software;
- filtrado de red.

En ese escenario mis opciones serían:

### 1. entity["software","Fedora Workstation","Linux distribution"]

**Ventajas**

- GNOME muy limpio y cercano al proyecto original.
- SELinux activado por defecto.
- Buen soporte Wayland.
- Muy difícil que un usuario normal rompa el sistema. citeturn0search21turn0search17

**Inconvenientes**

- Ciclo de actualizaciones más rápido.
- Requiere actualizar versión aproximadamente una vez al año. citeturn0search2turn0search21

---

### 2. entity["software","Ubuntu","Linux distribution"]

**Ventajas**

- Muchísima documentación.
- Excelente soporte hardware.
- GNOME 50 en Ubuntu 26.04 LTS.
- Soporte largo. citeturn0search13turn0search21

**Inconvenientes**

- Más personalizaciones sobre GNOME.
- Snap sigue generando división de opiniones.

---

### 3. entity["software","Debian","Linux distribution"]

**Ventajas**

- Extremadamente estable.
- Muy poco mantenimiento.
- Ideal si quieres que funcione años sin sorpresas. citeturn0search6turn0search2

**Inconvenientes**

- Software menos reciente.
- Hardware muy nuevo puede requerir algo más de trabajo.

---

## Si tu preocupación es que los menores intenten saltarse restricciones

Yo haría algo así:

```text
Fedora o Ubuntu
   |
Usuario sin sudo
   |
Firefox ESR o Chromium
   |
DNS bloqueado por red
   |
OPNsense
```

Y además:

- desactivar instalación de extensiones;
- bloquear ejecución de VPNs;
- impedir cambios de configuración DNS;
- usar cuenta estándar sin permisos administrativos.

---

## Lo que NO usaría

Para este caso evitaría:

- Arch.
- EndeavourOS.
- CachyOS.
- Manjaro.

No porque sean malos, sino porque están pensados para usuarios que quieren controlar el sistema, justo lo contrario de lo que buscas para un equipo infantil.

## Mi elección hoy

Si me dices:

> "Quiero un PC Linux para menores, con GNOME moderno y el menor mantenimiento posible"

elegiría **Ubuntu 26.04 LTS**.

Si me dices:

> "Quiero además aprender administración Linux y endurecer el sistema"

entonces elegiría **Fedora Workstation**. citeturn0search13turn0search21turn0search17

Lo que sí me interesa saber es la edad aproximada (8, 12, 15, 17 años). Las medidas que sirven para un niño de 10 años suelen ser completamente insuficientes para uno de 15 que ya sabe instalar una VPN o arrancar desde un USB.
---


Con 8 años, el problema cambia bastante. Ya no estás defendiéndote de alguien que va a instalar Tailscale, WireGuard o arrancar Kali desde un USB. El objetivo suele ser:

- limitar tiempo de uso;
- bloquear contenido inapropiado;
- evitar instalaciones accidentales;
- impedir compras o cambios de configuración;
- mantener el sistema sencillo.

En ese escenario, yo no sobredimensionaría la solución.

## Lo que haría

### Sistema operativo

**Ubuntu LTS** o **Fedora Workstation**.

Para un niño de 8 años probablemente elegiría Ubuntu por:

- menos mantenimiento;
- más tutoriales;
- soporte muy amplio.

### Cuenta de usuario

Crear:

```text
Administrador (solo padres)
Niño (usuario estándar)
```

Sin permisos sudo para el menor.

---

## Navegador

Usaría Firefox o Chromium con:

- SafeSearch forzado.
- YouTube Restricted Mode.
- DNS filtrado.

Aunque el filtrado DNS no sea perfecto, para un niño de 8 años suele ser suficiente como primera capa.

---

## Donde invertiría el esfuerzo

Más en el equipo que en OPNsense.

Por ejemplo:

### Bloquear BIOS/UEFI

Contraseña de firmware.

### Desactivar arranque por USB

Muy importante.

### Cifrado de disco

Opcional.

### Sin permisos de instalación

Fundamental.

---

## Sobre OPNsense

Para un niño de 8 años, OPNsense empieza a tener sentido si quieres:

- horarios automáticos;
- apagar Internet a ciertas horas;
- bloquear categorías web;
- informes de actividad.

Pero no porque vaya a saltarse DoH.

Sinceramente, la preocupación por DoH suele aparecer cuando hablamos de adolescentes de 13-16 años con cierta curiosidad técnica.

---

## Lo bueno de tu idea del NAS

Ya tienes:

```text
NAS Ugreen N100
```

Así que una VM de OPNsense te cuesta prácticamente cero.

Por tanto:

### Ventajas

- Aprendes redes.
- Puedes experimentar.
- Obtienes control parental centralizado.

### Desventajas

- Más complejidad.
- Más mantenimiento.
- Posibles incidencias cuando actualices.

---

## Mi valoración

Para un niño de 8 años, si me obligaran a priorizar:

1. Usuario sin privilegios.
2. Contraseña UEFI.
3. Arranque USB deshabilitado.
4. SafeSearch y YouTube restringido.
5. Horarios de uso.
6. OPNsense (opcional).

Antes invertiría tiempo en asegurar el dispositivo que en construir una arquitectura compleja para bloquear DoH.

De hecho, para esa edad, lo que suele acabar funcionando mejor es una combinación de restricciones moderadas en el equipo + supervisión del uso, más que un firewall extremadamente sofisticado. Un niño de 8 años normalmente se encuentra con más problemas intentando instalar un juego o cambiar ajustes del sistema que intentando evadir un filtrado DNS.
---


Sí, para el escenario que describes, **1-2 vCPU y 2 GB de RAM son más que suficientes**.

De hecho, si los Deco siguen siendo:

- cliente PPPoE,
- router principal,
- NAT principal,
- servidor DHCP,

entonces OPNsense no estaría haciendo el trabajo pesado de routing de toda la casa.

## Consumo real de OPNsense

Para funciones típicas:

- Firewall básico.
- Unbound DNS.
- Listas de bloqueo.
- Algunas reglas de filtrado.

OPNsense suele funcionar cómodamente con:

| Recurso | Recomendable |
|----------|----------|
| CPU | 1-2 vCPU |
| RAM | 2 GB |
| Disco | 16-32 GB |

El N100 además tiene potencia de sobra para eso.

---

## Lo que puede cambiar los requisitos

### Zenarmor

Si piensas usar urlZenarmorhttps://www.zenarmor.com/:

- 2 GB siguen siendo viables.
- 4 GB empiezan a ser más cómodos.

Zenarmor guarda bastante información de sesiones y estadísticas.

---

### IDS/IPS (Suricata)

Si activas:

- IDS,
- IPS,
- inspección profunda,

entonces ya no hablamos de un simple firewall.

Ahí sí recomendaría:

- 2 vCPU mínimo.
- 4 GB RAM.

Pero para control parental doméstico suele ser innecesario.

---

## El detalle más importante: la red

La CPU y RAM no son el reto.

El reto es:

**¿Cómo va a ver OPNsense el tráfico de los menores?**

Porque si tienes:

```text
ONT
 |
DECO
 |
Internet
```

y OPNsense está simplemente conectado como otro equipo más de la LAN:

```text
DECO
 ├── móviles
 ├── tablets
 ├── PCs
 └── OPNsense
```

entonces OPNsense no puede filtrar nada de forma transparente.

Necesita que el tráfico de los menores pase por él.

Por ejemplo:

```text
Niños
  |
OPNsense
  |
DECO
  |
Internet
```

o que los dispositivos de los menores usen OPNsense como:

- gateway,
- DNS,
- proxy,

según el diseño que elijas.

---

## Sobre la ruta estática que comentabas

La idea de:

```text
Clientes
   |
DECO (DHCP)
   |
ruta estática
   |
OPNsense
   |
DECO
   |
Internet
```

es válida si quieres que **sólo ciertas redes** vayan a través de OPNsense.

Por ejemplo:

```text
Red adultos: 192.168.1.0/24
Red menores: 192.168.50.0/24
```

y el Deco sabe que para llegar a `192.168.50.0/24` debe enviar tráfico a OPNsense.

Pero para que OPNsense filtre la salida a Internet de los menores, normalmente también debe ser el gateway de esa red de menores.

---

## Mi valoración

### Lo bueno

- El N100 del NAS Ugreen va sobrado.
- 2 GB RAM son suficientes para empezar.
- Mantienes la red actual funcionando.
- Riesgo bajo.

### Lo menos bueno

- La parte complicada no es el hardware.
- La parte complicada es encajar OPNsense en el flujo de tráfico de los menores para que realmente pueda aplicar políticas.

Antes de desplegar nada, definiría exactamente la topología de red (IP de los Deco, subred actual, modo router/AP, interfaces virtuales disponibles en el NAS, etc.). Con un esquema sencillo puedo decirte si la ruta estática que tienes en mente funcionará o si hay una forma más limpia de conseguir el mismo resultado.

---
*Generado desde conversación con 20 mensajes.*
*General*
