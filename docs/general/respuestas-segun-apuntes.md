---
title: Respuestas según apuntes
date: 2026-06-15
category: General
slug: respuestas-segun-apuntes
tags: ['General']
---

# Respuestas según apuntes


> **Pregunta original:**
> 
La siguiente configuración corresponde a....

R1(config)# access-list 12 permit 192.168.1.0 0.0.0.255
R1(config)# ip nat inside source list 12 interface f0/2 overload
R1(config)# interface f0/1
R1(config-if)#ip address 192.168.1.1 255.255.255.0
R1(config-if)# ip nat inside
R1(config)# interface f0/2
R1(config-if)#ip address 10.1.1.1 255.255.255.252
R1(config-if)# ip nat outside
R1(config-if)# exit



Pregunta 16Selecciona una:

a.
Una configuración NAT.


b.
Una configuración PAT.


c.
Una configuración NAT y una ACL que deniega el trafico.


d.
Ninguna respuesta es correcta.
> Para actualizar o cambiar el SO (habitualmente llamada IOS en estos dispositivos) descargándola a través de TFTP debemos seguir los siguientes pasos:

Pregunta 3Selecciona una:

a.
dir bootflash:/

delete bootflash: XXXXXXXX

copy tftp bootflash

show boot

configure terminal

boot system flash XXXXXXXX

write memory

reload


b.
dir bootflash:/

delete bootflash: XXXXXXXX

copy tftp bootflash

show boot

configure terminal

boot system flash XXXXXXXX

reload

write memory


c.
dir bootflash:/

copy tftp bootflash

delete bootflash: XXXXXXXX

show boot

configure terminal

boot system flash XXXXXXXX

write memory

reload


d.
dir bootflash:/

copy tftp bootflash

delete bootflash: XXXXXXXX

show boot

configure terminal

boot system flash XXXXXXXX

reload

write memory
> Sobre AWS podemos decir...

Pregunta 2Selecciona una o más de una:

a.
Una región tiene como mínimo 2 AZ's.


b.
Existe una Edge Location por cada Región.


c.
Podemos establecer políticas de DR (Disaster Recovery) y FT (Fault Tolerance).


d.
Una AZ es como un CPD.
> 
> *...y 16 preguntas de seguimiento*


---


## Respuesta


La respuesta correcta es la **c**.

```text
R1(config-if)# encapsulation ppp
R1(config-if)# ppp authentication chap
```

Según los apuntes, **CHAP se configura sobre PPP**, no sobre HDLC. En la UD3 se indica que **PPP** permite autenticación de enlace y que puede aumentar la seguridad usando **PAP/CHAP**. En el ejemplo Cisco aparece primero la configuración de PPP con `encapsulation ppp` y después la autenticación con `ppp authentication chap`. fileciteturn4file1 fileciteturn4file0

Por qué no las otras:

- **a**: usa `encapsulation hdlc`; HDLC no incorpora autenticación de enlace según los apuntes.
- **b**: además de usar HDLC, el comando `chap authentication ppp` no es el orden mostrado.
- **d**: usa HDLC y un comando que no corresponde al ejemplo de los apuntes.

**Respuesta: c.**
---


La respuesta correcta es la **c**.

Dirección original:

```text
1522:0000:0001:0000:0000:0500:3c01:2502
```

Aplicando la notación abreviada IPv6:

```text
1522:0:1::500:3c01:2502
```

Motivo:

- Se eliminan los ceros iniciales de cada bloque:
  - `0000` → `0`
  - `0001` → `1`
  - `0500` → `500`
- La secuencia consecutiva `0000:0000` puede comprimirse como `::`.
- Solo puede usarse **una vez** `::` en una dirección IPv6.

Por eso:

- **a** es incorrecta: usa `::` dos veces.
- **b** es incorrecta: elimina también el bloque `0001`, que no puede desaparecer.
- **c** es correcta.
- **d** es incorrecta.

**Respuesta: c.**
---


La respuesta correcta es la **b. Una configuración PAT**.

Según los apuntes de la **UD3**, el comando clave es:

```text
ip nat inside source list 12 interface f0/2 overload
```

El término **`overload`** indica **PAT** o **NAT con sobrecarga**, permitiendo que varios equipos internos salgan usando una misma IP externa mediante traducción de puertos. Los apuntes muestran esta misma estructura como ejemplo de configuración PAT en Cisco. fileciteturn15file0

Revisión:

- **a. NAT**: demasiado genérica; al llevar `overload`, es específicamente **PAT**.
- **b. PAT**: correcta.
- **c. NAT y ACL que deniega tráfico**: incorrecta, la ACL usa `permit`, no `deny`.
- **d. Ninguna**: incorrecta.

**Respuesta: b.**
---


La respuesta **incorrecta** es la **c**.

Según los apuntes de la **UD6**:

- **a. Correcta.** Las **NACL** son *stateless*. fileciteturn14file1
- **b. Correcta.** Un **Security Group** puede habilitar tráfico desde/hacia otros **SG**. fileciteturn14file1
- **c. Incorrecta.** Los **SG** solo permiten reglas **ALLOW**; el **DENY** es implícito, no configurable. fileciteturn14file1
- **d. Correcta.** Las **NACL** tienen ámbito de **subnet**, mientras que los **SG** se aplican a instancia/servicio. fileciteturn14file1

**Respuesta: c.**
---


La respuesta correcta es la **a**.

Según los apuntes de la **UD2**, el orden indicado para actualizar o cambiar la IOS descargándola por **TFTP** es:

```text
dir bootflash:/
delete bootflash: XXXXXXXX
copy tftp bootflash
show boot
configure terminal
boot system flash XXXXXXXX
write memory
reload
```

Los apuntes muestran primero la comprobación del contenido de `bootflash`, luego el borrado de la IOS anterior, después la copia desde TFTP, el cambio del orden de arranque con `boot system flash`, el guardado con `write memory` y finalmente el reinicio con `reload`. fileciteturn3file4 fileciteturn3file0

Por qué no las otras:

- **b**: guarda con `write memory` después de `reload`, por tanto no asegura que el cambio quede persistido antes del reinicio.
- **c**: copia la nueva IOS antes de borrar la anterior; no es el orden que aparece en los apuntes.
- **d**: además de copiar antes de borrar, reinicia antes de guardar.

**Respuesta: a.**
---


Las respuestas correctas son: **a, c y d**.

Según los apuntes de la **UD6**, en AWS:

- **a. Correcta.** Una región suele comprender tres AZ, aunque los apuntes indican que existen regiones con cuatro y algunas con solo **dos AZ**. Por tanto, según los apuntes, el mínimo indicado es **2 AZ**. fileciteturn2file0
- **b. Incorrecta.** Los apuntes no dicen que exista una *Edge Location* por cada región. Indican que las *edge locations* son puntos de presencia usados para baja latencia, por ejemplo con CloudFront, distribuidos globalmente. fileciteturn2file0
- **c. Correcta.** Los apuntes dicen que desplegar servicios en distintas AZ e incluso regiones permite establecer estrategias de **DR** (*Disaster Recovery*) o incluso **FT** (*Fault Tolerance*). fileciteturn2file2
- **d. Correcta.** Los apuntes definen una **AZ** como una ubicación más reducida dentro de una región y dicen que podemos verla como un **CPD**. fileciteturn2file2

**Respuesta: a, c y d.**
---


La respuesta correcta es la **a**.

Según los apuntes, para configurar acceso remoto seguro por **SSH** en un switch/router Cisco se usan las líneas **VTY**, no la consola, y se restringe el transporte a **SSH**:

```text
switch(config)# ip domain-name ui1.es
switch(config)#crypto key generate rsa
switch(config)# username alumno privilege 15 secret ui1password
switch(config)#ip ssh version 2
switch(config)#line vty 0 4
switch(config-line)#transport input ssh
switch(config-line)# login local
```

Esto coincide con la opción **a**. Los apuntes indican además que SSH v2 se emplea por defecto porque SSH v1 fue vulnerable, y que en Cisco se usan las interfaces **vty** para el acceso remoto. fileciteturn1file0

Por qué no las otras:

- **b**: incorrecta porque usa `transport input ttl`; debería ser `ssh`.
- **c**: incorrecta porque usa `line console 0`; eso es acceso por consola, no remoto.
- **d**: incorrecta por ambos motivos: `line console 0` y `transport input ttl`.

**Respuesta: a.**
---


Las respuestas correctas son: **a, b, c y d**.

Según los apuntes:

- **a. Correcta.** DHCP en IPv6 puede configurarse en modo **Stateful** y **Stateless**. fileciteturn8file3
- **b. Correcta.** La dirección **link-local IPv6** sirve para comunicar dos dispositivos a través de un enlace, **sin ningún salto**, dentro del rango `FE80::/10`. fileciteturn8file3
- **c. Correcta.** En IPv4 se puede asignar más de una IP a una interfaz usando `secondary`, aunque el DHCP solo puede ofrecerse sobre la primaria. fileciteturn8file1
- **d. Correcta.** En los ejemplos de los apuntes, DHCP IPv6 se aplica a la interfaz con `ipv6 dhcp server STATEFUL` o `ipv6 dhcp server STATELESS`, mientras que en IPv4 se configura mediante `ip dhcp pool`, `network`, `default-router`, etc., no aplicado directamente en la interfaz. fileciteturn8file0
- **e. Incorrecta.** Los apuntes dicen que en IPv6 se puede asignar una dirección IPv6 estática o dinámica y, además, una **link-local** en la misma interfaz. fileciteturn8file3

**Respuesta: a, b, c y d.**
---


Las respuestas **NO válidas** son: **a, b y c**.

Según los apuntes de la **UD3**:

- Para **VRRP**, el formato correcto es:

```text
R1(config-if)# vrrp 123 ip 10.0.0.100
```

La opción **a** está mal porque invierte el orden: `123 vrrp ip...`. fileciteturn12file3

- Para **GLBP**, el formato correcto es:

```text
R1(config-if)# glbp 10 ip 192.168.1.10
```

Por eso la opción **d** sí es válida, aunque use el grupo `12` en vez de `10`. fileciteturn12file2

Revisión:

- **a. No válida**: comando VRRP mal ordenado.
- **b. No válida**: dice GLBP, pero usa `vrrp`.
- **c. No válida**: dice HSRP, pero usa `glbp`.
- **d. Válida**: sintaxis correcta para GLBP.

**Respuesta: a, b y c.**
---


La respuesta correcta es la **c**.

Según los apuntes, **Direct Connect** es una conexión dedicada y privada hacia AWS, no a través de Internet, y para configurarla se necesitan, entre otros elementos:

- un **VGW**,
- opcionalmente un **Direct Connect Gateway**,
- una **VIF pública y/o privada**,
- un **Direct Connect Endpoint**,
- un **customer o partner router**,
- y un **customer router on-premise**. fileciteturn9file1

Revisión de opciones:

- **a. Incorrecta.** El tráfico en Direct Connect **no va cifrado por defecto**; para cifrarlo habría que crear túneles VPN. fileciteturn9file0
- **b. Incorrecta.** Los apuntes indican que se puede crear **VIF pública y/o privada**, no solo pública. fileciteturn9file1
- **c. Correcta.** Se requiere un **customer o partner router**.
- **d. Incorrecta.** TLS VPN aparece en los apuntes como otro servicio distinto, asociado a **Client VPN endpoints**, no como Direct Connect. fileciteturn9file0

**Respuesta: c.**
---


La respuesta correcta es la **e. Ninguna respuesta es correcta**.

Revisión según los apuntes:

- **a. Incorrecta.** TRACEROUTE/TRACERT sí aparece como herramienta de descubrimiento basada en capa de red. fileciteturn7file4
- **b. Incorrecta.** Los apuntes dicen que **HPING3 requiere instalación en plataformas Linux**, no que sea para Linux, macOS y Windows. fileciteturn7file1
- **c. Incorrecta.** `nmap -sP 192.168.1.0/24` es escaneo mediante **pings**. El escaneo enviando TCP SYN es `nmap -PS 192.168.1.0/24`. fileciteturn7file1
- **d. Incorrecta.** `lsof -i` no es escaneo remoto; los apuntes lo clasifican como escaneo **local** de puertos abiertos, válido solo en Linux. fileciteturn7file0

**Respuesta: e.**
---


La respuesta correcta es la **b**.

Según los apuntes de la **UD5**, las redes inalámbricas 802.11 pueden trabajar con tres arquitecturas:

- **IBSS o ad hoc**.
- **BSS**.
- **ESS**. fileciteturn13file0

La opción **b** dice:

> Infraestructuras BSS, ESS y ad-hoc.

Es la que mejor coincide con los apuntes. La opción **c** incluye **IBSS, ESS y ad-hoc**, pero deja fuera **BSS** y además duplica la idea de **IBSS/ad hoc**, ya que los apuntes tratan **IBSS o ad hoc** como la misma arquitectura.

**Respuesta: b.**
---


La respuesta correcta es la **d**.

Según los apuntes de la **UD5**, para la compresión de vídeo existen tres técnicas:

- **Redundancia espacial**: los píxeles cercanos suelen parecerse mucho entre sí.
- **Redundancia estadística**: ciertos valores de bit se repiten en distintas secuencias.
- **Redundancia temporal**: se aprovecha que un píxel se repite a lo largo del tiempo. fileciteturn6file0

Por tanto:

- **a**: incorrecta, porque incluye redundancia cíclica.
- **b**: incorrecta, porque “redundancia frame a frame” no aparece así en los apuntes.
- **c**: incorrecta, porque incluye redundancia cíclica.
- **d**: correcta.

**Respuesta: d.**
---


**Falso.**

Según los apuntes, esa afirmación mezcla dos conceptos:

- Quien “asegura que nunca se saturará un enlace con tráfico excesivo” es **Traffic Policing**, porque descarta el tráfico que supera un umbral.
- **Traffic Shaping** guarda el tráfico excedente en una cola o *buffer* y lo va enviando, pero los apuntes indican que **no puede implementarse con ciertos tipos de tráfico como VoIP**, porque introduciría retardos problemáticos en la conversación. fileciteturn17file1

**Respuesta: Falso.**
---


La respuesta correcta es la **c**.

Según los apuntes de la **UD2**, la tabla de EtherChannel indica:

- **LACP**:
  - `active - active` → **Recommended**
  - `active - passive` → funciona si la negociación es correcta, pero no aparece como recomendada.
- **PAgP**:
  - `desirable - desirable` → **Recommended**
  - `auto - desirable` → funciona si la negociación es correcta. fileciteturn11file0

Revisión de opciones:

- **a. Incorrecta.** `auto - auto` pertenece a PAgP, no a LACP, y además no es la opción recomendada.
- **b. Incorrecta.** En LACP `active - passive` puede funcionar, pero la recomendada en los apuntes es `active - active`.
- **c. Correcta.** En PAgP la opción recomendada es `desirable - desirable`.
- **d. Incorrecta.** `active - active` pertenece a LACP, no a PAgP.

**Respuesta: c.**
---


La respuesta correcta es la **d**.

Según los apuntes:

- **a. Incorrecta.** `no ip domain-lookup` no se limita a servidores de dominio o DNS. En los apuntes aparece como comando válido en switches/routers para cortar la resolución cuando te equivocas de comando. fileciteturn5file0
- **b. Incorrecta.** `crypto key zeroize rsa` **no crea** claves; las **elimina**. El comando para crearlas es `crypto key generate rsa`. fileciteturn5file1
- **c. Incorrecta.** `line vty 0 4` no es para acceso por consola. El acceso por consola se configura con `line con 0`. fileciteturn5file1
- **d. Correcta.** `line vty 0 4` se usa para habilitar/configurar el acceso remoto por **SSH** mediante las líneas VTY, junto con `transport input ssh` y `login local`. fileciteturn5file1

**Respuesta: d.**
---


Entendido. A partir de ahora responderé **según lo que dicen los apuntes subidos** de Redes Avanzadas de Computadores:

- UD1: IPv4 e IPv6 fileciteturn0file0  
- UD2: Switches fileciteturn0file1  
- UD3: Routers fileciteturn0file2  
- UD4: Configuración y gestión de redes fileciteturn0file3  
- UD5: Redes inalámbricas y multimedia fileciteturn0file4  
- UD6: Redes de alta velocidad, nueva generación y *on-cloud* fileciteturn0file5  

Si algo **no aparece en los apuntes**, te lo indicaré expresamente y separaré lo que sea deducción, conocimiento externo o ampliación.
---


La respuesta correcta es la **c**.

Según los apuntes de la **UD4**:

- **a. Correcta.** DNA Center de Cisco engloba **SD-WAN** y **SD-ACCESS**; los apuntes lo definen como una suite integrada y gestionada desde una plataforma *on-cloud*. fileciteturn10file0
- **b. Correcta.** SD-WAN nace de las soluciones originales de **Meraki** y **Viptela**, ambas adquiridas por Cisco. fileciteturn10file0
- **d. Incorrecta.** Esa descripción corresponde a **SD-WAN**, no a SD-ACCESS: los apuntes dicen que SD-WAN se basa en crear túneles VPN de forma similar a MPLS. fileciteturn10file0

Por tanto, como **A y B son correctas**, la opción válida es:

**Respuesta: c.**
---


Hablamos de **Frame Relay**.

Según los apuntes de la **UD6**, Frame Relay se define precisamente como una tecnología/servicio público que proporciona conexiones entre usuarios mediante redes de alta velocidad, de **64 kbps a 2 Mbps**, con **bajo retardo**, de forma similar a las redes privadas de conmutación de circuitos. fileciteturn16file0

**Respuesta: Frame Relay.**

---
*Generado desde conversación con 38 mensajes.*
*General*
