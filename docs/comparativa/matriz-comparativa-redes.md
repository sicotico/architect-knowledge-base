---
title: Matriz comparativa redes
date: 2026-06-14
category: Comparativas
slug: matriz-comparativa-redes
tags: ['Comparativas']
---

# Matriz comparativa redes


> **Pregunta original:**
> 
Tengo estas otras citas. Indicame a que puntos hacen referencia 
> 4A.3 Matriz comparativa de rendimiento: Redes Inalámbricas vs. Cableadas
Redes Inalámbricas (WiFi): Su principal ventaja reside en la movilidad de los usuarios y la reducción de costes de despliegue en infraestructura física (canalizaciones y cableado). Sus desventajas competitivas son la susceptibilidad a interferencias, atenuación física por obstáculos, menor ancho de banda efectivo compartido y una mayor superficie de ataque a nivel de seguridad física.
Redes Cableadas (Ethernet): Proporcionan máxima estabilidad, inmunidad frente a interferencias electromagnéticas externas, tasas de transferencia simétricas elevadas y latencias mínimas. Su limitación principal es la rigidez física y la complejidad logística de instalación en grandes infraestructuras. Las soluciones de conmutación de la serie V de HP Networking permiten conectar clientes combinando ambas tecnologías para optimizar ingresos.
Parte B: Redes de Nueva Generación (UD6)
4B.1 Limitaciones de Ethernet en entornos de área amplia (WAN)
Las redes de área local (LAN) operan típicamente en distancias confinadas y bajo un control administrativo único, optimizadas para un ancho de banda elevado y baja latencia. En contraste, las redes de área amplia (WAN) tienen como objetivo interconectar infraestructuras dispersas geográficamente a gran escala.
La tecnología Ethernet tradicional presenta carencias estructurales para cubrir escenarios WAN de forma nativa:
Gestión de la señal y distancia: No fue diseñada originalmente para gestionar la atenuación de la señal y los retardos de propagación en miles de kilómetros.
Conmutación de etiquetas y enrutamiento: Carece de mecanismos nativos eficientes, como los de MPLS, para el enrutamiento troncal de grandes operadores.
Calidad de Servicio (QoS): Presenta limitaciones para garantizar niveles de QoS estrictos en topologías complejas de malla.
Resiliencia: Los mecanismos como Spanning Tree no ofrecen los tiempos de convergencia ultra-rápidos requeridos en WAN.
4B.2 Análisis profundo de tecnologías de transporte de datos
ATM (Asynchronous Transfer Mode) y Frame Relay: Representan el legado de las redes WAN de conmutación de circuitos virtuales. ATM utiliza celdas de tamaño fijo de 53 bytes para minimizar el jitter y asegurar transmisiones síncronas con QoS riguroso. Frame Relay surgió como una alternativa eficiente en costes al usar tramas de tamaño variable.
Evolución de Ethernet (10/40/100 GbE): Los estándares Gigabit Ethernet han transformado a Ethernet en una solución robusta para redes troncales y centros de datos, utilizando fibra óptica para la agregación de enlaces masivos.
NGN (Redes de Nueva Generación): Arquitecturas basadas en paquetes con el protocolo IP como núcleo, unificando redes de telefonía y datos. Permiten la entrega transparente de servicios multimedia con independencia del punto de acceso.
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

Bloque 1 – Emulación vs Simulación (Análisis técnico)

1.1. Simulación y emulación de redes:
La simulación y la emulación son dos formas de estudiar y probar redes informáticas sin necesidad de disponer de todos los equipos físicos. Aunque ambas permiten crear entornos de práctica, funcionan de manera diferente.
La simulación reproduce el comportamiento de los dispositivos mediante modelos simplificados. En cambio, la emulación ejecuta sistemas operativos reales de red, ofreciendo un comportamiento mucho más parecido al de una infraestructura real.
La principal diferencia es que la simulación está orientada al aprendizaje y consume pocos recursos, mientras que la emulación busca un mayor realismo a costa de requerir más potencia de hardware.
1.2. Comparacion de Cisco Packet Tracer, GNS3 y EVE-NG:

Cisco Packet Tracer es una herramienta orientada a la simulacion educativa de redes Cisco. Permite crear topologias con routers, switches, PCs y servicios basicos, y es muy util para aprender comandos, direccionamiento IPv4/IPv6, VLAN, routing estatico o dinamico y pruebas de conectividad. Segun la UD1, Packet Tracer es adecuado para el aprendizaje, aunque su emulacion es menos realista y permite ciertas acciones que no se darian igual en un entorno real.

GNS3 es una plataforma de emulacion. Su enfoque es mas profesional porque permite construir topologias de red ejecutando imagenes de sistemas operativos reales o appliances virtualizados. La UD1 indica que GNS3 permite emular topologias de la manera mas real posible y configurarlas como si se estuviera ante dispositivos fisicos. Puede ejecutarse localmente, contra un servidor GNS3 externo o apoyandose en maquinas virtuales con VMware o VirtualBox.

EVE-NG tambien es una plataforma de emulacion profesional. Al igual que GNS3, permite integrar imagenes reales de routers, switches, firewalls y sistemas operativos, y suele utilizarse para laboratorios avanzados, certificaciones, pruebas multi fabricante y entornos de formacion empresarial. Su ventaja principal es la gestion centralizada via web y la facilidad para trabajar con laboratorios compartidos.

1.2 y 1.3. Comparación de herramientas:

Aspecto
Cisco Packet Tracer
GNS3
EVE-NG
Tipo
Simulación
Emulación
Emulación
Nivel de realismo
Medio
Alto
Muy alto
Sistemas operativos reales
No
Sí
Sí
Consumo de recursos
Bajo
Alto
Alto
Facilidad de uso
Muy fácil
Media
Media
Limitaciones
Funciones avanzadas limitadas
Requiere imágenes y más hardware
Requiere hardware potente
Casos de uso
Aprendizaje básico
Laboratorios avanzados
Entornos profesionales
Ventaja principal
Fácil para principiantes
Gran realismo
Máxima flexibilidad
Desventaja principal
Menor realismo
Mayor complejidad
Mayor exigencia técnica


Como puede observarse, Packet Tracer está orientado principalmente al aprendizaje académico, mientras que GNS3 y EVE-NG buscan reproducir entornos reales mediante la utilización de sistemas operativos auténticos. Esto hace que la emulación ofrezca resultados más precisos, aunque también requiere más conocimientos y recursos. 
He escrito estoy quiero saber si puedo usar el pdf adjunto como bibliografía
> Tanenbaum, A. S., & Wetherall, D. J. (2021). Redes de computadoras (6ª ed.). Pearson Educación.
Curso de la Cisco Networking Academy UI1 que realice en el 2025. Cisco Packet Tracer Documentation. Recuperado de https://www.netacad.com/
GNS3 Technologies. (2026). GNS3 Documentation. Recuperado de https://docs.gns3.com/

---


## Respuesta


Sí, puedes usar ese PDF como bibliografía, y de hecho es una fuente muy sólida porque se trata del estándar oficial IEEE para redes WLAN (Wi-Fi). fileciteturn0file0

## Lo que sí respalda de tu trabajo

El documento IEEE 802.11-2020 es adecuado para justificar aspectos relacionados con:

- Redes inalámbricas Wi-Fi.
- Arquitectura WLAN.
- Funcionamiento de la capa MAC y PHY.
- Calidad de servicio (QoS) en Wi-Fi.
- Seguridad en redes inalámbricas.
- Movilidad de estaciones.
- Evolución de los estándares Wi-Fi (802.11a/b/g/n/ac/ad/ah, etc.).

Por ejemplo, tu apartado **4A.3 Matriz comparativa de rendimiento: Redes Inalámbricas vs. Cableadas** puede apoyarse parcialmente en este estándar cuando hablas de:
- movilidad de usuarios,
- características de WLAN,
- QoS,
- seguridad,
- funcionamiento del medio inalámbrico.

Además, el propio estándar dedica el apartado 4 a describir cómo las WLAN difieren de otras redes y cómo la movilidad y el medio radioeléctrico afectan al diseño y rendimiento. fileciteturn0file0L14-L17

## Lo que NO respalda directamente

Hay partes de tu trabajo que no están cubiertas por ese PDF:

### 4B.1 Limitaciones de Ethernet en WAN
El IEEE 802.11 trata exclusivamente de redes inalámbricas WLAN. No es una fuente adecuada para justificar:

- Limitaciones de Ethernet en WAN.
- MPLS.
- Frame Relay.
- ATM.
- NGN.
- Redes troncales de operadores.

Para esos apartados sería mejor usar:
- Cisco Networking Academy.
- ITU-T (NGN).
- RFC de IETF.
- Libros de redes como Tanenbaum o Kurose & Ross.

### Comparación Packet Tracer, GNS3 y EVE-NG

Tampoco aparece en el estándar IEEE 802.11. Para justificar esa sección deberías usar:

- Documentación oficial de Packet Tracer.
- Documentación oficial de GNS3.
- Documentación oficial de EVE-NG.
- Material de tu UD1.

## Cómo citarlo

### APA 7

> Institute of Electrical and Electronics Engineers. (2021). *IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems Local and Metropolitan Area Networks—Specific Requirements. Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications (IEEE Std 802.11-2020).* IEEE. fileciteturn0file0

### IEEE

> IEEE, *IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems—Local and Metropolitan Area Networks—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications*, IEEE Std 802.11-2020, 2021. fileciteturn0file0

## Valoración

### Ventajas de incluirlo
- Es una fuente primaria.
- Es una norma oficial internacional.
- Aporta rigor técnico.
- Refuerza especialmente toda la parte Wi-Fi.

### Inconvenientes
- Es extremadamente técnico.
- No cubre WAN, NGN, ATM, Frame Relay ni Ethernet empresarial.
- No sirve para justificar Packet Tracer, GNS3 o EVE-NG.

Mi recomendación es incluirlo en la bibliografía, pero como una referencia específica para los apartados de **redes inalámbricas (4A.3)**. Para la parte **WAN y tecnologías de transporte (4B)** conviene añadir al menos una o dos fuentes adicionales especializadas en redes WAN.
---


Estas tres referencias encajan bastante bien con tu trabajo, pero cada una sirve para apartados distintos.

| Referencia | Apartados recomendados | Adecuación |
|------------|------------------------|------------|
| **Tanenbaum & Wetherall (2021). Redes de computadoras** | 4A.3 Redes inalámbricas vs cableadas, 4B.1 Limitaciones de Ethernet en WAN, 4B.2 ATM, Frame Relay, Ethernet, NGN | Muy alta |
| **Cisco Networking Academy (curso realizado en 2025)** | Bloque 1 (Simulación vs Emulación), Packet Tracer, conceptos básicos de redes LAN/WAN | Muy alta |
| **GNS3 Documentation (2026)** | Bloque 1.2 Comparación de herramientas, descripción de GNS3, características de emulación | Muy alta |

## Distribución concreta

### Tanenbaum y Wetherall

Es la referencia más potente de todas porque cubre prácticamente toda la teoría de redes.

Úsala para:

#### 4A.3 Redes inalámbricas vs cableadas
- Ventajas e inconvenientes de Ethernet.
- Ventajas e inconvenientes de Wi-Fi.
- Ancho de banda.
- Latencia.
- Interferencias.
- Movilidad.

#### 4B.1 Limitaciones de Ethernet en WAN
- Diferencia entre LAN y WAN.
- Problemas de escalabilidad.
- Retardos de propagación.
- Necesidad de protocolos de transporte WAN.

#### 4B.2 Tecnologías de transporte
- ATM.
- Frame Relay.
- MPLS (si lo mencionas).
- Ethernet de alta velocidad.
- Redes de nueva generación (NGN).

Si tu profesor revisa las fuentes, Tanenbaum es probablemente la mejor referencia para toda la Parte B.

---

### Cisco Networking Academy

Esta referencia es ideal para:

#### Bloque 1.1 Simulación y emulación
- Definiciones básicas.
- Uso educativo de Packet Tracer.
- Aprendizaje de routing, switching y direccionamiento.

#### Bloque 1.2 Comparación de herramientas

Especialmente para este párrafo:

> Cisco Packet Tracer es una herramienta orientada a la simulación educativa de redes Cisco...

y para:

> Packet Tracer está orientado principalmente al aprendizaje académico...

No la usaría para ATM, Frame Relay o NGN porque no es una fuente académica de referencia para esos temas.

---

### GNS3 Documentation

Úsala para justificar:

#### Bloque 1.2 GNS3

- Ejecución de imágenes reales.
- Integración con VMware y VirtualBox.
- Emulación de routers y switches.
- Laboratorios avanzados.

Por ejemplo:

> GNS3 permite emular topologías de la manera más real posible...

> Puede ejecutarse localmente o utilizando servidores remotos...

Todo eso debería referenciarse con GNS3 Documentation.

---

## Te falta una referencia para EVE-NG

Ahora mismo tienes fuente para:

- Packet Tracer → Cisco NetAcad.
- GNS3 → Documentación GNS3.

Pero no para:

- EVE-NG.

Te recomendaría añadir:

> EVE-NG Ltd. (2026). *EVE-NG Documentation*. Recuperado de https://www.eve-ng.net/

o la documentación oficial correspondiente.

Así cada herramienta queda respaldada por su documentación oficial.

## Reparto final recomendado

**4A.3 Redes inalámbricas vs cableadas**
- IEEE 802.11-2020
- Tanenbaum & Wetherall (2021)

**4B.1 Limitaciones de Ethernet en WAN**
- Tanenbaum & Wetherall (2021)

**4B.2 ATM, Frame Relay, Ethernet y NGN**
- Tanenbaum & Wetherall (2021)

**Bloque 1.1 Simulación vs Emulación**
- Cisco Networking Academy
- Tanenbaum (como apoyo conceptual)

**Bloque 1.2 Packet Tracer**
- Cisco Networking Academy

**Bloque 1.2 GNS3**
- GNS3 Documentation

**Bloque 1.2 EVE-NG**
- Documentación oficial EVE-NG

Con esas cuatro fuentes (IEEE 802.11, Tanenbaum, Cisco NetAcad y GNS3/EVE-NG) tendrías la bibliografía bastante bien alineada con todo el contenido que has mostrado.
---


Pásame las citas (o la bibliografía completa) y te indicaré exactamente:

| Referencia | Apartado(s) de tu trabajo donde encaja | Nivel de adecuación |
|------------|-----------------------------------------|---------------------|
| Autor, año | 4A.3 / 4B.1 / 4B.2 / Bloque 1, etc. | Alta / Media / Baja |

Además, te señalaré si alguna cita:
- está mal asignada,
- es redundante con otra,
- es demasiado genérica,
- o sería mejor usarla solo como bibliografía complementaria.

Puedes copiar las referencias directamente aquí o subir el documento donde las tengas.

---
*Generado desde conversación con 6 mensajes.*
*Comparativas*
