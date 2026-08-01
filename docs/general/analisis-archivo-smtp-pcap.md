---
title: Análisis archivo smtp.pcap
date: 2025-10-20
category: General
slug: analisis-archivo-smtp-pcap
tags: ['General']
---

# Análisis archivo smtp.pcap


> **Pregunta original:**
> 
Si , usa markdown
> Si
> Genera un documento de word con portada indice y contra portada usando de base el siguiente markdown:

UD2 – Captura y análisis con Wireshark
Práctica: Análisis de tráfico SMTP
Alumno: Luis Puente Bayon
Asignatura: Redes de Computadores
Fecha: 20 de octubre de 2025

🧩 Parte 1 – Análisis del tráfico SMTP (smtp.pcap)
a) Dirección IP del servidor SMTP
74.53.140.153
Se identifica en varios paquetes (por ejemplo, paquete 6) como origen del mensaje 220-xc90.websitewelcome.com ESMTP Exim…

b) Dirección IP del cliente SMTP
10.10.1.4
Aparece como dirección de origen en las peticiones iniciales (EHLO GP).

c) Resolución DNS previa
Tipo	Nombre consultado	Respuesta
Consulta	mail.patriots.in	
Respuesta	mail.patriots.in → patriots.in → 74.53.140.153	✅
Correspondencia: mail.patriots.in ↔ 74.53.140.153

d) Puertos de las consultas DNS
Origen: 56166 (puerto efímero del cliente)
Destino: 53 (servidor DNS estándar)
👉 El cliente usa un puerto aleatorio alto (>1024) y contacta con el puerto 53 del servidor DNS.

e) Protocolo de transporte para DNS
UDP (User Datagram Protocol)
Visible en los paquetes 1 y 2.

f) Puerto de destino de los mensajes SMTP
25
Puerto estándar del servicio SMTP.

🧠 Justificación: los servidores SMTP escuchan en el puerto 25 para recibir correos de clientes o servidores.

g) Protocolo de transporte para SMTP
TCP (Transmission Control Protocol)
SMTP utiliza TCP para garantizar la entrega ordenada y confiable de los mensajes.

h) Diagrama del intercambio SMTP
Cliente (10.10.1.4)                          Servidor (74.53.140.153)
--------------------                        ---------------------------
DNS Query mail.patriots.in  ---------------->  DNS Response (74.53.140.153)
TCP SYN (1470→25)         ------------------>
                        <------------------  TCP SYN-ACK (25→1470)
TCP ACK                 ------------------>
EHLO GP                 ------------------>
                        <------------------  250-xc90.websitewelcome.com
AUTH LOGIN              ------------------>
                        <------------------  334 Username:
USER gurpartap@patriots.in ---------------->
                        <------------------  334 Password:
PASS *****              ------------------>
                        <------------------  235 Authentication succeeded
MAIL FROM:<gurpartap@patriots.in> ---------->
                        <------------------  250 OK
RCPT TO:<raj_deol2002in@yahoo.co.in> ------->
                        <------------------  250 Accepted
DATA                    ------------------>
                        <------------------  354 Enter message...
Mensaje (DATA fragments) ------------------>
                        <------------------  250 OK id=1Mugho-0003Dg-Un
QUIT                    ------------------>
                        <------------------  221 closing connection
FIN/ACK exchange         <------------------>  (conexión cerrada)
i) Tipo de intercambio (cliente-servidor o servidor-servidor)
El MAIL FROM es <gurpartap@patriots.in>
Se usa AUTH LOGIN (autenticación) → típico de un cliente.
✅ Conclusión: es un cliente de correo autenticado ante su servidor SMTP, no una transferencia entre servidores.

j) Herramientas de análisis en Wireshark
Follow → TCP Stream: muestra toda la conversación SMTP (EHLO, AUTH, MAIL FROM, RCPT TO, DATA, QUIT).
Statistics → Conversations: identifica la sesión principal 10.10.1.4:1470 ↔ 74.53.140.153:25.
Tools → Credentials: revela credenciales codificadas en Base64:
Z3VycGFydGFwQHBhdHJpb3RzLmlu → gurpartap@patriots.in
cHVuamFiQDEyMw== → punjab@123
Statistics → TCP Stream Graph: visualiza la evolución del flujo TCP durante el envío del mensaje.
🧩 Parte 2 – Análisis del tráfico SMTP (wire01.pcap)
Introducción y ejercicio de filtrado
Al capturar en Wireshark verás una gran cantidad de paquetes generados por todos los procesos del equipo (NAT, DNS, actualizaciones, servicios en segundo plano, etc.). Para quedarnos sólo con lo que nos interesa, aplica por separado los dos filtros que se indican a continuación y compara el número de paquetes mostrados.

Filtros a aplicar:

http

ip.addr == 188.164.193.158 (la IP pública obtenida con http.host == "www.hipertexto.info")

El filtro http muestra únicamente tramas con protocolo HTTP (peticiones/respuestas HTTP en texto claro). Será un subconjunto reducido centrado en navegación web no cifrada y recursos HTTP específicos.

Motivos de la diferencia: distinta granularidad de filtrado (por protocolo vs. por dirección), presencia de tráfico no-HTTP hacia la misma IP, y tráfico de fondo generado por otras aplicaciones del equipo. Además, si parte del tráfico está cifrado (HTTPS), no aparecerá como http aunque vaya a la misma IP; en ese caso sólo ip.addr lo capturará.

Transcripción de la línea relevante (para búsquedas):

Paquete 122 — 192.168.68.70 → 188.164.193.158 — GET /images/redes.gif HTTP/1.1
Capturas y filtros relevantes
Filtro: http 12 HTTP

El filtro http muestra únicamente tramas con protocolo HTTP (peticiones/respuestas HTTP en texto claro). Será un subconjunto reducido centrado en navegación web no cifrada y recursos HTTP específicos.
Filtro: ip.src == 188.164.193.158 22 paquetes Origen IP

El filtro ip.src muestra únicamente tramas donde 188.164.193.158 aparece como origen. Incluye respuestas del servidor y tráfico saliente desde esa IP; puede contener varios protocolos (HTTP, TCP, ICMP, etc.), no solo peticiones HTTP en texto claro.
Filtro: ip.dst == 188.164.193.158 — 26 paquetes

El filtro ip.dst muestra únicamente tramas donde 188.164.193.158 aparece como destino. Incluye peticiones dirigidas a ese host y tráfico entrante; puede contener varios protocolos (HTTP, TCP, ICMP, etc.), no solo respuestas HTTP en texto claro.
Filtro: ip.dst == 188.164.193.158 || ip.src == 188.164.193.158. 48 paquetes (|| es el operador "OR"; por eso ip.dst == 188.164.193.158 || ip.src == 188.164.193.158 es equivalente a ip.addr == 188.164.193.158)
Origen o destino IP

Filtro: ip.addr == 188.164.193.158 48 paquetes (muestra paquetes donde 188.164.193.158 aparece como origen o destino) Origen o destino IP

Motivos de la diferencia: distinta granularidad de filtrado (por protocolo vs. por dirección), presencia de tráfico no-HTTP hacia la misma IP, y tráfico de fondo generado por otras aplicaciones del equipo. Además, si parte del tráfico está cifrado (HTTPS), no aparecerá como http aunque vaya a la misma IP; en ese caso sólo ip.addr lo capturará.

Notas:

Usa los filtros tal cual en la barra de Wireshark para aislar las tramas.
Las imágenes muestran ejemplos de las búsquedas y resultados.
+---------------+                     +---------------+
|   Cliente      |                     |   Servidor     |
| (192.168.68.70)|                     |(www.hipertexto.info)|
+---------------+                     +---------------+
         |                                      |
         |------ PETICIÓN HTTP GET ------------->
         | (GET /images/redes.gif HTTP/1.1)     |
         |                                      |
         |<----- RESPUESTA HTTP 200 OK ----------|
         | (Content-Type: image/gif)            |
         |                                      |
> 
> *...y 3 preguntas de seguimiento*


---


## Respuesta


Perfecto ✅  
Veo que el archivo **“Ejercicios y Problemas UD2.pdf”** tiene un formato claro de documento académico con:  
- Portada con título centrado.  
- Numeración de secciones (Ejercicio 1, 2, 3…).  
- Subapartados numerados (1.1, 2.1…).  
- Uso de texto alineado, fórmulas y estructura ordenada.  

Puedo crear el **documento de la práctica SMTP con el mismo formato y estilo visual** (estructura formal de informe académico), pero en formato **Google Docs** (.docx para que lo subas fácilmente a Drive).  

¿Quieres que incluya una **portada similar** (título, nombre, asignatura, fecha) y luego las secciones numeradas como “1. Parte 1 – Análisis SMTP”, “1.1 Dirección IP del servidor”, etc.?  
Si me confirmas el **nombre del alumno**, te preparo el archivo DOCX con ese estilo exacto.
---


Aquí tienes el documento de Word con **portada, índice y contraportada**, listo para subir a **Google Docs o entregar**:  

📘 [Descargar UD2_Practica_Wireshark_LuisPuenteBayon.docx](sandbox:/mnt/data/UD2_Practica_Wireshark_LuisPuenteBayon.docx)
---


Perfecto ✅  
Tienes dos archivos:  

1. **`UD2-Enunciado Captura Wireshark.pdf`** → contiene el **enunciado de la práctica** con las preguntas a responder.  
2. **`smtp.pcap`** → es la **captura de tráfico SMTP** que corresponde a la primera parte de la práctica.  

Puedo analizar el archivo `smtp.pcap` para responder a las preguntas de la parte 1 del enunciado, por ejemplo:

a. Dirección IP del servidor SMTP  
b. Dirección IP del cliente SMTP  
c. Resolución DNS previa  
d. Puertos origen/destino de las consultas DNS  
e. Protocolo de transporte usado por DNS  
f. Puerto de destino de los mensajes SMTP  
g. Protocolo de transporte de SMTP  
h. Diagrama de intercambios SMTP  
i. Si el intercambio es entre cliente-servidor o servidor-servidor  
j. Análisis adicional (seguir flujo TCP, credenciales, estadísticas…)

¿Quieres que realice ahora el análisis completo del archivo `smtp.pcap` y te prepare las respuestas a todas las preguntas de la **Parte 1**?
---


No se pudo generar el PDF directamente porque el motor LaTeX necesario (`pdflatex`) no está disponible en este entorno.  

Sin embargo, puedo:  
✅ crear el documento en **Markdown (.md)** —formato limpio y editable— que puedes abrir en cualquier procesador (Word, VSCode, Typora, etc.) y convertir a PDF desde tu equipo con un clic.  

¿Quieres que te genere el archivo **`UD2_Practica_SMTP_Resuelta.md`** con el mismo contenido listo para entrega?
---


Aquí tienes el documento en formato Markdown listo para entrega:  

📄 [Descargar UD2_Practica_SMTP_Resuelta.md](sandbox:/mnt/data/UD2_Practica_SMTP_Resuelta.md)  

Puedes abrirlo directamente en **VSCode**, **Typora**, **Obsidian** o incluso en **Word**, y exportarlo fácilmente a PDF si lo necesitas subir al aula virtual.
---


No tengo disponibles en este entorno las librerías necesarias para analizar directamente el archivo `.pcap` (como **Scapy** o **PyShark**).  

Pero puedo seguir otro enfoque:  
📤 Si quieres, puedo **extraer y analizar manualmente los paquetes SMTP y DNS** desde el `.pcap` convirtiéndolo primero a texto legible (por ejemplo, usando `tshark -r smtp.pcap -V` o similar).  

Para poder hacerlo aquí, necesito que tú:  
1. Exportes la captura a formato **texto (txt o csv)** desde Wireshark con:
   - Menú: `File > Export Packet Dissections > As Plain Text...`
   - Marca la opción **"Packet summary line + packet details"**
2. Luego sube ese archivo exportado.

Así podré leerlo, interpretar todos los detalles de DNS y SMTP y responder punto por punto al enunciado (IPs, puertos, protocolo, diagrama, etc.).  

¿Quieres que te explique paso a paso cómo hacer esa exportación desde Wireshark?
---


Perfecto ✅  
Con el archivo `smtpCaptura.txt`, ya puedo responder todas las preguntas de la **Parte 1** del enunciado “UD2 – Captura Wireshark”.  
A continuación tienes las respuestas basadas en el análisis del tráfico capturado 👇  

---

### 🧩 **Parte 1 – Análisis del tráfico SMTP (archivo smtp.pcap)**

#### a) Dirección IP del servidor SMTP  
→ **74.53.140.153**  
Se identifica en varios paquetes (por ejemplo, paquete 6) como origen del mensaje “220-xc90.websitewelcome.com ESMTP Exim…”.

#### b) Dirección IP del cliente SMTP  
→ **10.10.1.4**  
Aparece como dirección de origen en las peticiones iniciales (por ejemplo, `EHLO GP`).

---

#### c) Resolución de nombres DNS previa  
Paquete 1 y 2 muestran:  
- **Consulta:** `mail.patriots.in`  
- **Respuesta:** `mail.patriots.in` → **CNAME patriots.in → A 74.53.140.153**  
✅ **Correspondencia:**  
`mail.patriots.in` ↔ `74.53.140.153`

---

#### d) Puertos de las consultas DNS  
- **Puerto de destino:** 53 (servidor DNS estándar).  
- **Puerto de origen:** 56166 (puerto efímero del cliente).  
👉 Justificación: el cliente usa un puerto aleatorio alto (>1024) y contacta con el puerto 53 del servidor DNS.

---

#### e) Protocolo de transporte para DNS  
→ **UDP (User Datagram Protocol)**  
Aparece claramente indicado en los paquetes 1 y 2 de tipo “User Datagram Protocol”.

---

#### f) Puerto de destino de los mensajes SMTP  
→ **25**  
Es el puerto estándar de SMTP, visible en múltiples líneas, por ejemplo:  
`Transmission Control Protocol, Src Port: 1470, Dst Port: 25`.

🧠 Justificación: el puerto 25 es usado por los servidores para aceptar conexiones SMTP entrantes.

---

#### g) Protocolo de transporte para el tráfico SMTP  
→ **TCP (Transmission Control Protocol)**  
Confirmado en todos los intercambios SMTP (SYN, SYN-ACK, ACK, EHLO, MAIL FROM, RCPT TO, DATA, QUIT).  
SMTP requiere TCP para garantizar la entrega ordenada y confiable de mensajes.

---

#### h) Diagrama de intercambios SMTP (resumen textual)

```
Cliente (10.10.1.4)                          Servidor (74.53.140.153)
--------------------                        ---------------------------
DNS Query mail.patriots.in  ---------------->  DNS Response (74.53.140.153)
TCP SYN (1470→25)         ------------------>
                        <------------------  TCP SYN-ACK (25→1470)
TCP ACK                 ------------------>
EHLO GP                 ------------------>
                        <------------------  250-xc90.websitewelcome.com
AUTH LOGIN              ------------------>
                        <------------------  334 Username:
USER gurpartap@patriots.in ---------------->
                        <------------------  334 Password:
PASS *****              ------------------>
                        <------------------  235 Authentication succeeded
MAIL FROM:<gurpartap@patriots.in> ---------->
                        <------------------  250 OK
RCPT TO:<raj_deol2002in@yahoo.co.in> ------->
                        <------------------  250 Accepted
DATA                    ------------------>
                        <------------------  354 Enter message...
Message body fragments   ------------------>
                        <------------------  250 OK id=1Mugho-0003Dg-Un
QUIT                    ------------------>
                        <------------------  221 closing connection
FIN/ACK exchange         <------------------>  (cerrado)
```

---

#### i) Tipo de intercambio (cliente-servidor o servidor-servidor)

Basado en:  
- El **MAIL FROM** es `<gurpartap@patriots.in>`.  
- La sesión inicia con **AUTH LOGIN**, lo cual es típico de un **cliente autenticándose** ante un servidor.  

✅ **Conclusión:** se trata de un **agente de usuario de correo (cliente)** que se conecta a su **servidor SMTP**, **no** de una transferencia entre dos servidores de correo.

---

#### j) Herramientas de análisis en Wireshark

Usando las funciones recomendadas:

- **Follow → TCP Stream:** permite ver la conversación completa SMTP (EHLO, AUTH, MAIL FROM, RCPT TO, DATA, QUIT) en texto plano.  
- **Statistics → Conversations:** muestra que la sesión principal es entre `10.10.1.4:1470` ↔ `74.53.140.153:25`.  
- **Tools → Credentials:** revela credenciales codificadas en Base64:  
  - `Z3VycGFydGFwQHBhdHJpb3RzLmlu` → `gurpartap@patriots.in`  
  - `cHVuamFiQDEyMw==` → `punjab@123`  
- **Statistics → TCP Stream Graph:** se puede visualizar el flujo de bytes del intercambio SMTP (envío del correo).

---

### ✅ **Resumen general**
| Pregunta | Respuesta principal |
|-----------|--------------------|
| a | Servidor SMTP: 74.53.140.153 |
| b | Cliente SMTP: 10.10.1.4 |
| c | mail.patriots.in → 74.53.140.153 |
| d | Origen: 56166 / Destino: 53 |
| e | UDP |
| f | Puerto 25 |
| g | TCP |
| h | Diagrama de intercambio (ver arriba) |
| i | Cliente-servidor (usuario autenticado) |
| j | Se pueden seguir flujos, ver credenciales y estadísticas con Wireshark |

---

¿Quieres que te prepare estas respuestas en un **documento PDF con formato de entrega** (portada + respuestas) para subir al aula virtual?

---
*Generado desde conversación con 13 mensajes.*
*General*
