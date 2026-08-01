---
title: Rendimiento RTL8153 vs RTL8156
date: 2026-06-18
category: Comparativas
slug: rendimiento-rtl8153-vs-rtl8156
tags: ['Comparativas']
---

# Rendimiento RTL8153 vs RTL8156


> **Pregunta original:**
> 
tengo unhub usb-C con conector USBA-a con el chip RTL8153  y he visto otro hub con RTL8156. Con el nuevo voy a tener problemas  , hay reviews de rendimiento  ?
> cual es el mejor adaptador usb a etherne 2,5GbE 
> Solo hay el chio de realteck , no hay otros chip mejores ?
> 
> *...y 1 preguntas de seguimiento*


---


## Respuesta


Voy a mirarlo como compra práctica: chip, estabilidad en Linux/Windows, formato USB-C/USB-A y marcas con pruebas reales. La parte buena es que en 2.5GbE hay bastante consenso; la mala es que muchas marcas cambian revisiones internas sin avisar.
---


Para tu caso, **yo elegiría un adaptador con Realtek RTL8156B o RTL8156BG**, no uno “2.5GbE” genérico.

**Mi recomendación principal:** **Plugable USBC-E2500** si quieres la opción más tranquila para Ubuntu + Windows. Usa Realtek RTL8156B según fichas de producto/distribuidores, tiene USB-C con adaptador USB-A integrado y suele tener mejor soporte/documentación que marcas más baratas. genui{"citation":{"refs":["turn495052search4","turn495052search17"]}}

**Mejor calidad/precio:** **UGREEN USB-C 2.5G, modelo CM648 / 25052**, ideal si lo encuentras a buen precio. UGREEN declara RTL8156BG, y ServeTheHome probó adaptadores UGREEN con RTL8156BG indicando que el rendimiento es el esperado y que casi todos los NIC con ese chip rinden parecido. genui{"citation":{"refs":["turn495052search2","turn575918search4"]}}

| Opción | Lo bueno | Lo malo |
|---|---|---|
| **Plugable USBC-E2500** | Más “compra segura”, USB-C + USB-A, buen soporte | Más caro |
| **UGREEN RTL8156BG** | Muy buen precio/rendimiento, chip moderno | Revisiones/modelos pueden variar |
| **Cable Matters 2.5GbE** | Suele ir bien, marca seria | Hay reviews que mencionan detalles físicos/driver según modelo |
| **TP-Link UE302C** | Marca conocida, precio razonable | Menos claro el chip/revisión; miraría reviews concretas antes |

**Evitaría como primera opción** adaptadores muy baratos sin indicar chip, o hubs 8-en-1 con HDMI/PD si lo que quieres es estabilidad. También tendría cuidado con algunos Anker 2.5GbE: hay reviews donde funcionan, pero con problemas al conectar alimentación en ciertos escenarios. genui{"citation":{"ref":"turn575918search1"}}

Para **Ubuntu 26.04 LTS y Windows 11**, el punto clave no es tanto la marca: es que Ubuntu cargue `r8152` y negocie a `2500Mb/s`. Si quieres ir a lo práctico: **Plugable si prefieres estabilidad/soporte; UGREEN RTL8156BG si quieres pagar menos sin renunciar a rendimiento**.
---


Sí, **hay otros chips**, pero en adaptadores **USB a 2.5GbE** el mercado está dominado por Realtek.

Los principales son:

| Chip | Tipo | Comentario |
|---|---|---|
| **Realtek RTL8156 / RTL8156B / RTL8156BG** | USB 2.5GbE | El más común. Buen rendimiento, barato, soporte amplio. Mejor buscar **8156B/BG**. |
| **ASIX AX88279 / AX88279A** | USB 2.5GbE | Alternativa real a Realtek. ASIX declara soporte para Windows, Linux, Android, Chrome OS y CDC-NCM en macOS/Linux. genui{"citation":{"refs":["turn772310search2","turn772310search3"]}} |
| **Aquantia/Marvell AQC111U / AQC112U** | USB 5GbE/2.5GbE | Más orientado a 5GbE. Potencialmente mejor, pero más caro, menos común y con más consumo/calor. |
| **Intel i225/i226, Marvell AQC113** | PCIe, no USB típico | Mejor opción si puedes usar PCIe/M.2, pero no suele existir como simple dongle USB. |

Mi lectura práctica: **ASIX AX88279A podría ser “mejor” sobre el papel**, porque es más nuevo y tiene cosas como TSN/PTP/Modern Standby, pero todavía no lo pondría automáticamente por encima del Realtek en compra real. Hay menos reviews, menos experiencia acumulada y menos modelos fáciles de encontrar.

Para **USB 2.5GbE en Ubuntu + Windows**, yo seguiría así:

1. **Primera opción realista:** Realtek **RTL8156B/BG** de buena marca.
2. **Alternativa interesante:** ASIX **AX88279A**, si encuentras un adaptador concreto con buenas reviews.
3. **Si quieres máxima estabilidad 24/7:** mejor **PCIe/M.2** que USB, idealmente Intel i226 o Marvell/Aquantia según equipo.
4. **Si quieres más de 2.5GbE por USB:** mirar 5GbE, pero ahí suben calor, precio y posibles rarezas de driver.

Lo bueno de Realtek: es barato, probado y fácil de encontrar.  
Lo malo: no es “premium”; algunos adaptadores fallan por suspensión, EEE, calor o drivers. Pero en 2.5GbE USB, **no hay una alternativa claramente superior y universal** ahora mismo.
---


Sí: **con RTL8156 puedes tener más rendimiento**, pero también **más riesgo de pelearte con drivers/energía** que con un RTL8153.

## Diferencia clave

| Chip | Ethernet | Bus USB | Lo esperable |
|---|---:|---:|---|
| **RTL8153** | 1 GbE | USB 3.x | ~940 Mbps reales en buenas condiciones |
| **RTL8156 / RTL8156B / RTL8156BG** | 2.5 GbE | USB 3.x | ~2.0–2.35 Gbps reales con switch/puerto/cable correctos |

Realtek lista el **RTL8156B(S)G-CG** como controlador Ethernet **10/100/1000M/2.5G** con bus **USB 3.0**. Para la familia USB Ethernet, Realtek agrupa RTL8153 como GbE y RTL8156 como 2.5GbE. citeturn858209search0turn858209search1

## Reviews / pruebas de rendimiento

Hay reviews con resultados buenos:

- **ServeTheHome, febrero 2026**, probó un adaptador UGREEN USB-A a 2.5GbE con **RTL8156BG**. Su conclusión fue que el rendimiento era el esperado para ese chip y que la mayoría de NICs con RTL8156BG rinden de forma parecida. También remarca que 2.5GbE consume bastante menos que 10GbE, típicamente en el rango de **1–2 W**, lo que ayuda en dispositivos USB baratos. citeturn569174search12
- **CNX Software, 2022**, probó un adaptador USB 3.0 a 2.5GbE con **RTL8156B** usando iperf, Samba y scp. Encontró que podía acercarse al rendimiento 2.5GbE, pero también detectó problemas iniciales de rendimiento/fiabilidad en Ubuntu 20.04 que mejoraban al usar el driver adecuado. citeturn569174search11turn858209search9
- En macOS, una prueba de varios dongles 2.5GbE indicó que adaptadores basados en **RTL8156** podían alcanzar su ancho de banda nominal cuando se conectaban a los puertos correctos; el autor prefería variantes RTL8156B frente a algunas RTL8156 más antiguas. citeturn569174search13

## Dónde puedes tener problemas

### 1. Si el “USB-C hub” internamente no da USB 3.x al Ethernet

Aunque el conector sea USB-C, algunos hubs reparten ancho de banda entre HDMI, lector SD, USB-A, PD, etc. Si el puerto Ethernet acaba colgado de una ruta limitada o compartida, no verás 2.5GbE real.

**Prueba rápida:** en Windows/Linux/macOS mira si negocia a **2500 Mbps**. Si queda en **1000 Mbps**, el RTL8156 se comportará casi igual que tu RTL8153.

### 2. Drivers en Linux / NAS / Proxmox / TrueNAS / routers

Aquí es donde más cautela tendría. Hay bastantes reportes de RTL8156 funcionando mal si carga un driver genérico o una ruta de driver incorrecta. CNX Software, por ejemplo, vio rendimiento pobre con el driver `cdc_ncm` y mejoría al usar el driver Realtek/r8152 correcto. citeturn858209search9

En Linux moderno suele ir mejor que hace años, pero en NAS, routers, mini-servidores o distros conservadoras puede seguir siendo delicado.

### 3. macOS

Puede funcionar, pero no asumiría “plug and play perfecto” en todos los casos. Hay pruebas positivas con macOS Monterey, pero también documentación comunitaria sobre limitaciones de drivers Apple/Realtek y velocidades capadas en ciertos escenarios. citeturn569174search13turn858209search10

### 4. Alimentación y calor

RTL8156 consume más que RTL8153. No es dramático, pero en hubs compactos con HDMI + PD + varios USB puede haber:

- desconexiones al conectar cargador;
- bajadas a 1 GbE;
- cortes bajo carga sostenida;
- temperatura elevada.

Una review de un adaptador Anker 2.5GbE menciona un caso donde la conexión fallaba al conectar alimentación/brick y volvía al desconectarlo, lo que apunta a problemas de diseño del adaptador/hub más que al chip en sí. citeturn569174search27

## Veredicto práctico

**Compraría el RTL8156 si:**

- tienes switch/router **2.5GbE**;
- tu equipo tiene puerto **USB 3.x real**;
- usas Windows 11, macOS reciente o Linux moderno;
- puedes devolverlo si tu combinación concreta da problemas;
- el hub tiene buenas reviews específicas sobre Ethernet 2.5G, no solo “USB-C hub 8 en 1”.

**No esperaría mejora si:**

- tu red es 1 GbE;
- lo conectas a un puerto USB 2.0 o a un hub saturado;
- el equipo es un NAS/router/Proxmox con kernel viejo;
- lo quieres para máxima estabilidad 24/7.

## Recomendación concreta

Busca preferentemente **RTL8156B / RTL8156BG**, no solo “RTL8156” genérico. En reviews recientes, el comportamiento de los RTL8156BG parece bastante homogéneo entre marcas, pero el diseño del hub —temperatura, alimentación, firmware, layout USB— sigue importando mucho. citeturn569174search12

Para un portátil normal: **probablemente no tendrás problemas graves**.  
Para servidor/NAS/router/uso 24/7: **lo consideraría útil pero no tan fiable como una NIC PCIe Intel/Realtek interna**.
---


Con ese hub concreto —**solo 2.5GbE + dos USB**— el cuello de botella **no debería ser el ancho de banda**, siempre que lo conectes a un puerto **USB 3.x real**.

## Para Ubuntu 26.04 LTS

Aquí sería razonablemente optimista.

Realtek publica driver Linux para la familia **RTL8156 / RTL8156B(G)**, y en su página actual aparece soporte para kernels **hasta 6.17**, versión **2.21.4**, fechada el **24 de noviembre de 2025**. Eso es buena señal para Ubuntu 26.04, que debería ir con kernel suficientemente moderno. citeturn587155search1

Lo importante es comprobar qué driver carga Ubuntu:

```bash
lsusb
```

Busca algo como:

```text
Realtek Semiconductor Corp. RTL8156
```

Luego:

```bash
lsmod | grep r8152
```

Deberías ver `r8152`. Ese es el driver bueno para estos adaptadores.

También puedes comprobar la velocidad negociada:

```bash
sudo ethtool <interfaz>
```

Por ejemplo:

```bash
sudo ethtool enxXXXXXXXXXXXX
```

Debería decir:

```text
Speed: 2500Mb/s
Duplex: Full
```

Si en Ubuntu carga `cdc_ncm` en lugar de `r8152`, ahí sí puede haber rendimiento irregular. Se han visto casos donde el RTL8156 funciona, pero con peor rendimiento o problemas de enlace usando el driver equivocado; con `r8152` suele mejorar. citeturn587155search6

## Para Windows 11

En Windows 11 también debería funcionar. Realtek mantiene paquete de drivers para **USB FE / GbE / 2.5GbE / 5G / 10G Family Controller**, incluyendo RTL8156 / RTL8156B(G). citeturn587155search9

Mi recomendación: no dependas solo del driver que instale Windows Update. Si ves cortes, velocidad limitada o desconexiones tras suspensión, instala el driver USB Ethernet más reciente desde Realtek o desde el fabricante del hub.

## Lo bueno

- **2.5GbE realista:** con un switch/router 2.5GbE deberías ver aproximadamente **2.2–2.35 Gbps** en `iperf3`.
- **USB suficiente:** USB 3.0 da 5 Gbps brutos; para 2.5GbE es suficiente.
- **Mejor que RTL8153:** el RTL8153 se queda en 1GbE; el RTL8156 sí justifica el cambio si tu red lo acompaña.
- **Ubuntu 26.04 debería ir mejor que Ubuntu 20.04/22.04:** muchas quejas antiguas vienen de kernels y drivers más viejos.

## Lo malo / riesgos reales

- **Suspensión/reanudación:** en portátiles, algunos RTL8156 pueden quedarse sin enlace tras suspender. Normalmente se arregla reconectando o reiniciando NetworkManager.
- **Calor:** un hub compacto con RTL8156 puede calentarse más que uno con RTL8153. No necesariamente falla, pero para uso 24/7 conviene vigilarlo.
- **EEE / ahorro de energía:** Energy Efficient Ethernet a veces provoca microcortes o latencia rara con ciertos switches. Si ocurre, se puede desactivar.
- **Identificación engañosa:** algunos fabricantes anuncian RTL8156B/RTL8156BG, pero `lsusb` puede mostrar solo `0bda:8156`. Eso no siempre distingue bien la revisión.

## Ajustes útiles si hay problemas en Ubuntu

Primero identifica la interfaz:

```bash
ip link
```

Luego prueba:

```bash
sudo ethtool -s <interfaz> speed 2500 duplex full autoneg on
```

Para desactivar EEE:

```bash
sudo ethtool --set-eee <interfaz> eee off
```

Para ver errores bajo carga:

```bash
ip -s link show <interfaz>
```

Y para probar rendimiento:

```bash
iperf3 -s
```

en una máquina de la red, y desde Ubuntu:

```bash
iperf3 -c IP_DEL_SERVIDOR
```

Con 2.5GbE sano deberías ver algo cercano a:

```text
2.2 Gbits/sec - 2.35 Gbits/sec
```

## Veredicto

Para **Ubuntu 26.04 LTS + Windows 11**, con un hub simple de **2.5GbE + 2 USB**, yo lo consideraría una compra bastante razonable.

La condición crítica es esta:

> que Ubuntu cargue `r8152` y que la conexión negocie a `2500Mb/s`.

Si eso se cumple, el RTL8156 debería darte un salto claro frente al RTL8153. El riesgo principal no es ancho de banda, sino **driver/energía/suspensión/calor**. Para escritorio o portátil normal: aceptable. Para servidor 24/7: mejor vigilar estabilidad antes de darlo por definitivo.
---


Voy a separar dos cosas: compatibilidad real del RTL8156 frente al RTL8153 y rendimiento observado en pruebas/reviews, porque el salto suele depender más de drivers, cableado y puerto que del hub en abstracto.
---


Voy a revisar el mercado actual por chipsets, porque aquí la respuesta corta suele ser “casi todo es Realtek”, pero hay matices importantes entre USB 2.5G, 5G, Thunderbolt y PCIe.
---


Hasta aquí: evitaría decidir por marca solamente. Las pruebas apuntan a que los RTL8156B/BG rinden parecido, así que conviene elegir por disipación, conector, soporte de drivers y política de devolución.
---


También veo que en Europa aparecen UGREEN y TP-Link a precios razonables; Plugable suele ser más caro pero con mejor soporte/documentación. No tomaría las valoraciones de tienda como prueba técnica, solo como señal de disponibilidad y devoluciones.

---
*Generado desde conversación con 13 mensajes.*
*Comparativas*
