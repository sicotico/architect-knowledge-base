---
title: Limitaciones de Ethernet WAN
date: 2026-06-14
category: General
slug: limitaciones-de-ethernet-wan
tags: ['General']
---

# Limitaciones de Ethernet WAN


> **Pregunta original:**
> 
Parte B: Redes de Nueva Generación (UD6)
4B.1 Limitaciones de Ethernet en entornos de área amplia (WAN)
Las redes de área local (LAN) operan típicamente en distancias confinadas y bajo un control administrativo único, optimizadas para un ancho de banda elevado y baja latencia. En contraste, las redes de área amplia (WAN) tienen como objetivo interconectar infraestructuras dispersas geográficamente a gran escala.[1]
La tecnología Ethernet tradicional presenta carencias estructurales para cubrir escenarios WAN de forma nativa:
Gestión de la señal y distancia: No fue diseñada originalmente para gestionar la atenuación de la señal y los retardos de propagación en miles de kilómetros.
Conmutación de etiquetas y enrutamiento: Carece de mecanismos nativos eficientes, como los de MPLS, para el enrutamiento troncal de grandes operadores.
Calidad de Servicio (QoS): Presenta limitaciones para garantizar niveles de QoS estrictos en topologías complejas de malla.
Resiliencia: Los mecanismos como Spanning Tree no ofrecen los tiempos de convergencia ultra-rápidos requeridos en WAN.
4B.2 Análisis profundo de tecnologías de transporte de datos
ATM (Asynchronous Transfer Mode) y Frame Relay: Representan el legado de las redes WAN de conmutación de circuitos virtuales. ATM utiliza celdas de tamaño fijo de 53 bytes para minimizar el jitter y asegurar transmisiones síncronas con QoS riguroso. Frame Relay surgió como una alternativa eficiente en costes al usar tramas de tamaño variable.
Evolución de Ethernet (10/40/100 GbE): Los estándares Gigabit Ethernet han transformado a Ethernet en una solución robusta para redes troncales y centros de datos, utilizando fibra óptica para la agregación de enlaces masivos.
NGN (Redes de Nueva Generación): Arquitecturas basadas en paquetes con el protocolo IP como núcleo, unificando redes de telefonía y datos. Permiten la entrega transparente de servicios multimedia con independencia del punto de acceso.[1]
Parte B: Redes de Nueva Generación (UD6)
4B.1 Limitaciones de Ethernet en entornos de área amplia (WAN)
Las redes de área local (LAN) operan típicamente en distancias confinadas y bajo un control administrativo único, optimizadas para un ancho de banda elevado y baja latencia en entornos controlados. En contraste, las redes de área amplia (WAN) tienen como objetivo interconectar infraestructuras dispersas geográficamente a gran escala, a menudo atravesando fronteras nacionales o continentales.
La tecnología Ethernet tradicional, a pesar de su dominio en la LAN, presenta carencias estructurales para cubrir los escenarios WAN de forma nativa:
Gestión de la señal y distancia: No fue diseñada originalmente para gestionar la atenuación de la señal y los retardos de propagación en miles de kilómetros.
Conmutación de etiquetas y enrutamiento: Carece de mecanismos nativos eficientes, como los encontrados en MPLS, para la conmutación de etiquetas necesaria en el enrutamiento troncal de grandes operadores.
Calidad de Servicio (QoS): Presenta limitaciones para garantizar niveles de QoS estrictos y predecibles en topologías complejas de malla, fundamentales para servicios en tiempo real en redes de proveedores.
Resiliencia: Los mecanismos de recuperación de fallos de Ethernet tradicional (como Spanning Tree) no ofrecen los tiempos de convergencia ultra-rápidos que requieren las infraestructuras críticas WAN.
4B.2 Análisis profundo de tecnologías de transporte de datos
ATM (Asynchronous Transfer Mode) y Frame Relay: Estas tecnologías representan el legado de las redes WAN orientadas a la conmutación de circuitos virtuales. ATM destaca por el uso de celdas de tamaño fijo de 53 bytes (48 de carga útil y 5 de cabecera), una característica diseñada para minimizar el jitter y asegurar transmisiones síncronas de voz y datos con parámetros de Calidad de Servicio (QoS) extremadamente rigurosos. Por su parte, Frame Relay surgió como una alternativa más eficiente en costes al utilizar tramas de tamaño variable, eliminando parte del procesamiento de errores en los nodos intermedios para ganar velocidad. Aunque hoy se consideran obsoletas frente al avance de MPLS y Ethernet, ambas sentaron los principios fundamentales de la priorización de tráfico y la gestión de ancho de banda garantizado.
Evolución de Ethernet (10/40/100 GbE): Los estándares Gigabit Ethernet y sus sucesores (10, 40 y 100 GbE) han transformado a Ethernet de una tecnología puramente de área local (LAN) a una solución robusta para redes troncales y centros de datos. Utilizando principalmente la fibra óptica como medio físico, estos estándares permiten la agregación de enlaces y la gestión de flujos de datos masivos. Su éxito radica en la simplicidad del protocolo y la drástica reducción de costes por bit transmitido, convirtiéndose en el componente esencial de los backbones modernos que soportan el tráfico de Internet a nivel global.
NGN (Redes de Nueva Generación): Las NGN representan el paradigma de la convergencia tecnológica absoluta. Se definen como arquitecturas de red multi-servicio basadas en paquetes, capaces de utilizar múltiples tecnologías de transporte de banda ancha donde las funciones relacionadas con el servicio son independientes de las tecnologías subyacentes de transporte. Su núcleo es el protocolo IP, lo que permite la unificación de las antiguas redes de telefonía conmutada (RTB) y las redes de datos en una única infraestructura. Esto facilita la movilidad del usuario y la entrega transparente de servicios multimedia (voz, vídeo y datos) con independencia del punto de acceso físico, ya sea cableado o inalámbrico.

PArece contenido duplicado . corrigelo
> Te pedí los diagramas en formato drawio
> crea un diagrama de drawiopara explicar "Interferencias" , "Problema del Nodo Oculto" y "Problema del Terminal Expuesto"

---


## Respuesta


Tienes razón: generé una imagen, no un archivo editable de diagrams.net. Voy a corregirlo creando un `.drawio` real con los tres casos separados y editables.
---


Tienes razón. He creado ahora un archivo **`.drawio` editable** con 4 páginas:

1. **Resumen**
2. **Interferencias**
3. **Problema del Nodo Oculto**
4. **Problema del Terminal Expuesto**

Puedes abrirlo directamente en **diagrams.net / draw.io**:

[Descargar archivo DRAWIO](sandbox:/mnt/data/diagramas_redes_inalambricas.drawio)
---


He eliminado la duplicación y he dejado una versión única, más coherente y sin repetir apartados.

:::writing{variant="document" id="48291"}
## Parte B: Redes de Nueva Generación (UD6)

### 4B.1 Limitaciones de Ethernet en entornos de área amplia (WAN)

Las redes de área local (LAN) operan normalmente en distancias reducidas y bajo un único control administrativo. Están optimizadas para ofrecer un alto ancho de banda y baja latencia en entornos controlados. En cambio, las redes de área amplia (WAN) tienen como objetivo interconectar infraestructuras dispersas geográficamente, incluso a escala nacional o continental.

Aunque Ethernet es la tecnología dominante en redes LAN, su diseño original presenta limitaciones cuando se aplica directamente a escenarios WAN:

**Gestión de la señal y la distancia:** Ethernet tradicional no fue concebida para operar sobre miles de kilómetros, por lo que no gestiona de forma nativa problemas como la atenuación de la señal, los retardos de propagación o la necesidad de transporte óptico de larga distancia.

**Conmutación de etiquetas y enrutamiento troncal:** Ethernet carece de mecanismos nativos equivalentes a los de MPLS para realizar conmutación de etiquetas y encaminamiento eficiente en redes troncales de grandes operadores.

**Calidad de Servicio (QoS):** Aunque Ethernet ha incorporado mecanismos de priorización, presenta limitaciones para garantizar niveles estrictos y predecibles de QoS en topologías WAN complejas, especialmente en servicios sensibles al retardo, como voz, vídeo o aplicaciones en tiempo real.

**Resiliencia y recuperación ante fallos:** Los mecanismos tradicionales de Ethernet, como Spanning Tree Protocol, no ofrecen tiempos de convergencia suficientemente rápidos para las exigencias de las infraestructuras críticas WAN, donde se requieren mecanismos de protección y recuperación casi inmediatos.

### 4B.2 Análisis de tecnologías de transporte de datos

**ATM (Asynchronous Transfer Mode) y Frame Relay:**  
ATM y Frame Relay representan tecnologías WAN clásicas basadas en la conmutación de circuitos virtuales. ATM utiliza celdas de tamaño fijo de 53 bytes, formadas por 48 bytes de carga útil y 5 bytes de cabecera. Este diseño permitía reducir el jitter y facilitar la transmisión síncrona de voz, vídeo y datos con parámetros estrictos de Calidad de Servicio.

Frame Relay surgió como una alternativa más económica y eficiente, basada en tramas de tamaño variable. A diferencia de ATM, reducía parte del procesamiento de errores en los nodos intermedios para aumentar la velocidad de transmisión. Aunque actualmente ambas tecnologías han sido desplazadas en gran medida por MPLS, Ethernet metropolitana e infraestructuras IP, sentaron las bases de conceptos como la priorización del tráfico, los circuitos virtuales y la gestión del ancho de banda garantizado.

**Evolución de Ethernet: 10/40/100 GbE:**  
La evolución de Ethernet hacia velocidades de 10, 40 y 100 GbE permitió que esta tecnología dejara de estar limitada al ámbito LAN y pasara a utilizarse también en centros de datos, redes metropolitanas y troncales de operador. El uso de fibra óptica, la agregación de enlaces y la reducción del coste por bit transmitido han convertido a Ethernet en una solución clave para transportar grandes volúmenes de tráfico.

Su éxito se debe principalmente a la simplicidad del protocolo, la amplia compatibilidad con infraestructuras existentes y su menor coste frente a tecnologías WAN tradicionales. No obstante, en redes de operador suele complementarse con tecnologías como MPLS, DWDM o mecanismos avanzados de QoS para cubrir requisitos de escalabilidad, resiliencia y gestión del tráfico.

**NGN (Redes de Nueva Generación):**  
Las Redes de Nueva Generación, o NGN, representan un modelo de red basado en la convergencia de servicios sobre infraestructuras de paquetes. Su núcleo se apoya principalmente en el protocolo IP, lo que permite integrar servicios tradicionalmente separados, como telefonía, datos, vídeo y servicios multimedia, dentro de una misma arquitectura.

Una característica fundamental de las NGN es la separación entre los servicios ofrecidos y las tecnologías de transporte utilizadas. Esto permite que un usuario acceda a los mismos servicios desde distintos tipos de acceso, ya sean cableados o inalámbricos. Además, las NGN facilitan la movilidad, la interoperabilidad y la provisión flexible de servicios multimedia, sustituyendo progresivamente a las antiguas redes de telefonía conmutada y a otras infraestructuras especializadas.
:::

**Ajuste principal realizado:** he fusionado las dos versiones repetidas, conservando la más completa y eliminando redundancias. También he suavizado expresiones demasiado absolutas, como “convergencia tecnológica absoluta”, para que el texto quede más técnico y académico.

---
*Generado desde conversación con 6 mensajes.*
*General*
