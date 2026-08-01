---
title: Resumen de documento técnico
date: 2025-09-28
category: General
slug: resumen-de-documento-tecnico
tags: ['General']
---

# Resumen de documento técnico


> **Pregunta original:**
> 
Conviertelo a markdown
> Genera un resumen amplio de este docuento, manteniendo cada punto del indice

---


## Respuesta


Perfecto 🚀 Aquí tienes el **resumen en formato Markdown**, manteniendo la estructura del índice:  

```markdown
# Resumen: UD 1. Redes de computadores e Internet  

## 1.1. Concepto de red  
Una red de computadores es un conjunto de dispositivos conectados para compartir información, recursos y servicios.  
- **Ejemplo más grande**: Internet.  
- **Componentes básicos**:  
  - *Sistemas terminales (hosts)*: ordenadores, móviles, IoT.  
  - *Enlaces de comunicación*: medios guiados (cables) y no guiados (inalámbricos).  
  - *Conmutadores de paquetes*: routers y switches.  
  - *ISP (proveedores de Internet)*: proporcionan conexión mediante diferentes tecnologías.  

---

## 1.2. Tipos de redes  
- **Por tecnología de transmisión**:  
  - Difusión (un único canal compartido).  
  - Punto a punto (conexión entre pares, como en Internet).  
- **Por escala geográfica**:  
  - LAN (local).  
  - MAN (metropolitana).  
  - WAN (amplia).  
- **Por topología**: bus, anillo, estrella, árbol, malla, completa.  

---

## 1.3. Tipos de redes de conmutación  
- **Conmutación de circuitos**: reserva de recursos extremo a extremo (ej. telefonía).  
  - Multiplexación TDM (tiempo) y FDM/WDM (frecuencia/longitud de onda).  
- **Conmutación de paquetes**: mensajes divididos en paquetes con multiplexación estadística.  
  - Implica retardos: procesamiento, cola, transmisión, propagación.  
- **Comparativa**:  
  - Paquetes → más robustos, flexibles y económicos.  
  - Circuitos → garantizan ancho de banda, pero son menos eficientes.  
  - **Tendencia**: predomina la conmutación de paquetes.  

---

## 1.4. Protocolos y servicios  
- **Protocolo**: conjunto de reglas para la comunicación.  
- **Servicios de Internet**: web, correo, juegos, TV online.  
- **API**: define cómo las aplicaciones interactúan con la red.  
- **TCP/IP**: base de Internet.  

---

## 1.5. Arquitectura de red: Modelos OSI y TCP/IP  
- **Estructura en capas** para modularidad y claridad.  
- **Modelo TCP/IP (5 capas)**: aplicación, transporte, red, enlace, física.  
- **Modelo OSI (7 capas)**: añade presentación (formato/cifrado) y sesión (sincronización).  
- **Encapsulación**: cada capa añade cabeceras a los datos, eliminadas en el destino.  

---

## 1.6. Historia de redes e Internet  
- **ARPAnet (1969)**: primera red de conmutación de paquetes.  
- **Interconexión de redes**: Vinton Cerf y Robert Kahn desarrollan TCP/IP (1983). Surge el DNS.  
- **Minitel (Francia)**: acceso masivo en los 80.  
- **World Wide Web (1989-91)**: creada por Tim Berners-Lee (HTML, HTTP, navegador, servidor).  
- **Evolución moderna**: redes inalámbricas, P2P, multimedia, SDN, NFV.  

---

## 1.7. Estándares y unidades  
- **Organismos de estandarización**:  
  - ITU, ISO, IEEE (Ethernet/WiFi), IETF/IAB/IRTF (RFCs), W3C.  
- **Unidades**:  
  - Prefijos SI: kilo, mega, giga (×1000).  
  - Prefijos binarios: KiB, MiB, GiB (×1024).  
  - Ancho de banda: bits/segundo.  
  - Memoria: bytes (potencias de 2).  

---

## 1.8. Tecnologías de acceso a Internet  
### Inalámbricas  
- Satélite: cobertura global, alto retardo.  
- WiMAX: acceso rural, hasta 1 Gbps.  
- MMDS/LMDS: distribución de TV e Internet rural.  
- FSO: óptica en espacio libre, enlaces cortos.  
- WiFi: alta velocidad en entornos domésticos/públicos.  
- 4G: hasta 1 Gbps.  
- 5G: hasta 5 Gbps, baja latencia.  

### Cableadas  
- DSL/ADSL/VDSL: sobre cobre, en desuso en grandes ciudades.  
- HFC: híbrido fibra-coaxial, precursor de fibra pura.  
- FTTH: fibra hasta el hogar, >1 Gbps.  
- BPL/PLC: Internet sobre líneas eléctricas, uso reducido.  

---

## Resumen final  
Las redes de computadores permiten la comunicación entre dispositivos mediante enlaces y protocolos, siendo Internet el mayor exponente.  
- Se clasifican por transmisión, escala y topología.  
- Funcionan gracias a arquitecturas en capas (OSI y TCP/IP).  
- TCP/IP es la base de Internet.  
- La historia va de ARPAnet y la Web hasta las tecnologías actuales (5G, fibra, SDN).  
- Estándares internacionales y organismos garantizan interoperabilidad.  
- Tecnologías cableadas e inalámbricas posibilitan el acceso global a la red.  
```

---

¿Quieres que además te genere este **Markdown en un archivo `.md` descargable** para que lo uses directamente?
---


He preparado un **resumen amplio de la Unidad Didáctica 1 del documento**, manteniendo la estructura del índice original.  

---

# Resumen: UD 1. Redes de computadores e Internet  

### 1.1. Concepto de red  
Una red de computadores es un conjunto de dispositivos conectados para compartir información, recursos y servicios. El ejemplo más grande es Internet, que interconecta miles de millones de dispositivos (hosts). Los componentes básicos incluyen:  
- **Sistemas terminales (hosts)**: ordenadores, móviles, IoT, etc.  
- **Enlaces de comunicación**: medios guiados (cables) y no guiados (inalámbricos), medidos en bps.  
- **Conmutadores de paquetes**: routers y switches que reenvían la información.  
- **ISP (proveedores de Internet)**: facilitan la conexión mediante diversas tecnologías de acceso.  

---

### 1.2. Tipos de redes  
Se clasifican según:  
- **Tecnología de transmisión**:  
  - *Difusión*: un único canal compartido (ej. bus).  
  - *Punto a punto*: conexión directa entre pares de nodos (ej. Internet).  
- **Escala geográfica**:  
  - *LAN*: redes locales (edificio, casa).  
  - *MAN*: redes metropolitanas (varios edificios).  
  - *WAN*: redes extensas (países o continentes).  
- **Topología**: bus, anillo, estrella, árbol, malla y completa.  

---

### 1.3. Tipos de redes de conmutación  
- **Conmutación de circuitos**: reserva recursos de extremo a extremo (ej. telefonía). Usa multiplexación en tiempo (TDM) o en frecuencia (FDM/WDM).  
- **Conmutación de paquetes**: divide mensajes en paquetes, transmitidos de forma independiente con multiplexación estadística y reenvío *store-and-forward*. Implica retardos (procesamiento, cola, transmisión y propagación) y posibles pérdidas.  
- **Comparativa**:  
  - Paquetes → más robustos, flexibles, económicos y eficientes.  
  - Circuitos → ancho de banda garantizado y simplicidad, pero menos eficientes y más rígidos.  
  - Tendencia: predominio de la conmutación de paquetes.  

---

### 1.4. Protocolos y servicios  
Un **protocolo** es el conjunto de reglas de comunicación entre entidades. Internet proporciona **servicios** (web, correo, juegos, TV online) mediante aplicaciones distribuidas. La interacción se gestiona a través de una **API** (como la API de correo postal en el ejemplo).  
Los protocolos TCP/IP (TCP y IP) son la base de Internet.  

---

### 1.5. Arquitectura de red: Modelos OSI y TCP/IP  
- Las redes se organizan en **capas** para modularidad y claridad.  
- **Modelo TCP/IP (5 capas)**: aplicación, transporte, red, enlace y física.  
- **Modelo OSI (7 capas)**: añade presentación (formato/cifrado de datos) y sesión (sincronización y control de diálogo).  
- **Encapsulación**: cada capa añade cabeceras a los datos (payload), que se eliminan en el destino.  

---

### 1.6. Historia de redes e Internet  
- **ARPAnet (1969)**: primera red de conmutación de paquetes; Leonard Kleinrock participó en el primer mensaje entre UCLA y SRI.  
- **Interconexión de redes**: Vinton Cerf y Robert Kahn desarrollaron TCP/IP (1983 estándar en ARPAnet). Se introdujo el DNS. Francia desarrolló Minitel.  
- **World Wide Web (1989-91)**: creada por Tim Berners-Lee con HTML, HTTP, servidor y navegador. Fue la base del crecimiento masivo de Internet en los 90 y 2000.  
- **Tendencias actuales**: redes inalámbricas, P2P, servicios multimedia, SDN y NFV.  

---

### 1.7. Estándares y unidades  
- **Organismos de estandarización**:  
  - ITU (telecomunicaciones), ISO (estándares internacionales), IEEE (Ethernet y WiFi), IETF/IAB/IRTF (protocolos Internet, RFC), W3C (web).  
- **Unidades**:  
  - Prefijos SI (kilo, mega, giga…) y binarios (KiB, MiB, GiB) para distinguir múltiplos de 1000 y 1024.  
  - Ancho de banda en bps (potencias de 10), memoria en bytes (potencias de 2).  

---

### 1.8. Tecnologías de acceso a Internet  
- **Inalámbricas**:  
  - *Satélite*: cobertura amplia, alto retardo.  
  - *WiMAX, MMDS, LMDS*: acceso rural y distribución.  
  - *FSO*: óptica en espacio libre para enlaces cortos.  
  - *WiFi (802.11)*: alta velocidad en entornos domésticos y públicos.  
  - *4G*: hasta 1 Gbps; *5G*: hasta 5 Gbps y baja latencia.  
- **Cableadas**:  
  - *DSL/ADSL/VDSL*: sobre par de cobre, hoy en retirada.  
  - *HFC*: híbrido fibra-coaxial, precursor de fibra pura.  
  - *FTTH*: fibra hasta el hogar, velocidades > 1 Gbps.  
  - *BPL/PLC*: Internet sobre líneas eléctricas, uso limitado.  

---

### Resumen final  
Las redes de computadores permiten la comunicación entre dispositivos mediante enlaces y protocolos, con Internet como mayor exponente. Se estudian sus tipos, arquitecturas (OSI y TCP/IP), protocolos (TCP/IP), evolución histórica (de ARPAnet a la Web), estándares internacionales y tecnologías de acceso actuales, que combinan medios cableados e inalámbricos.  

---

¿Quieres que te prepare este **resumen estructurado en un esquema visual o mapa conceptual** (tipo diagrama) además del texto?

---
*Generado desde conversación con 4 mensajes.*
*General*
