---
title: CrowdStrike y Zscaler
date: 2026-06-13
category: General
slug: crowdstrike-y-zscaler
tags: ['General']
---

# CrowdStrike y Zscaler


> **Pregunta original:**
> 
Con el Windows Defender y  una GPO no sería más sencillo y cosumiendo menos recursos locales ?
> que es EDR y DLP  ?
> tengo cloudstrin y xescaler intalados en el pc corporativo , para que vale cada uno ?

---


## Respuesta


Sí, desde un punto de vista técnico, una combinación de **Microsoft Defender for Endpoint + GPOs + herramientas del ecosistema Microsoft** puede cubrir gran parte de lo que hacen CrowdStrike y Zscaler, especialmente en organizaciones muy centradas en Windows.

Sin embargo, las empresas suelen valorar otros factores además del consumo de recursos.

## Ventajas de Defender + GPO

- Menos agentes instalados en el equipo.
- Integración nativa con Windows.
- Menor complejidad operativa.
- Menor consumo de CPU y RAM en muchos escenarios.
- Gestión centralizada si ya utilizan entity["software","Microsoft Intune","Microsoft endpoint management platform"], entity["software","Microsoft Defender for Endpoint","Enterprise endpoint security platform"] y entity["software","Active Directory","Directory service"].

Además, hoy Defender ya no es el antivirus básico de hace años. La versión empresarial compite directamente con CrowdStrike en muchos análisis independientes.

## Por qué algunas empresas siguen usando CrowdStrike

CrowdStrike históricamente destacó por:

- Capacidades EDR muy avanzadas.
- Telemetría y análisis de amenazas muy detallados.
- Mejor experiencia para equipos de ciberseguridad especializados.
- Entornos mixtos (Windows, Linux, macOS) donde Microsoft no siempre es la opción natural.

En algunas organizaciones, el departamento de seguridad considera que CrowdStrike ofrece mayor visibilidad o mejores herramientas de investigación.

## Por qué una GPO no sustituye a Zscaler

Aquí está la diferencia más importante.

Una GPO puede:

- Configurar el equipo.
- Aplicar restricciones.
- Configurar firewall.
- Definir políticas de navegador.

Pero Zscaler aporta:

- Proxy cloud global.
- Inspección de tráfico HTTPS.
- Filtrado web avanzado.
- Acceso Zero Trust a aplicaciones.
- Protección cuando el usuario está fuera de la red corporativa.

Para replicar todo eso con tecnología Microsoft normalmente necesitarías varias piezas:

- Defender for Endpoint.
- Intune.
- Microsoft Entra ID.
- Microsoft Defender for Cloud Apps.
- Microsoft Global Secure Access.
- Firewalls/proxies corporativos.

No sería simplemente "una GPO".

## Respecto al consumo de recursos

Tu intuición es razonable.

Un equipo con:
- Defender.
- GPO.
- Intune.

suele tener menos agentes de terceros que uno con:
- CrowdStrike.
- Zscaler.
- VPN corporativa.
- DLP.
- Herramientas de inventario.
- Herramientas de monitorización.

Pero en un portátil moderno con 16-32 GB de RAM, CrowdStrike y Zscaler normalmente consumen una cantidad relativamente pequeña de recursos en condiciones normales. El problema suele aparecer cuando:
- CrowdStrike realiza análisis intensivos.
- Zscaler inspecciona tráfico cifrado.
- Coinciden varios agentes de seguridad.

En esos casos sí es habitual notar más uso de CPU, memoria y latencia de red.

En resumen: **Defender + GPO puede ser más simple y ligero**, pero no necesariamente ofrece exactamente las mismas capacidades que una combinación **CrowdStrike + Zscaler**, especialmente en organizaciones que buscan un modelo Zero Trust avanzado o tienen requisitos de seguridad muy exigentes.
---


Probablemente te refieres a:

- entity["software","CrowdStrike Falcon","Endpoint security platform"] (a veces se oye como "CloudStrike")
- entity["software","Zscaler","Zero Trust security platform"] (lo que has escrito como "Xescaler")

Si son esos dos, cumplen funciones distintas y complementarias:

| Herramienta | Para qué sirve |
|------------|----------------|
| CrowdStrike Falcon | Protege el propio ordenador frente a malware, ransomware, ataques, procesos sospechosos, etc. Es un EDR/XDR (detección y respuesta en endpoints). |
| Zscaler | Controla y protege el tráfico de red e Internet. Actúa como proxy seguro y aplica políticas de acceso, filtrado web y modelo Zero Trust. |

### CrowdStrike Falcon
Está centrado en el **equipo**:

- Detecta virus y malware.
- Analiza comportamientos sospechosos.
- Puede aislar el PC de la red si detecta una amenaza grave.
- Permite a los administradores investigar qué ha ocurrido en un equipo.

Ejemplo: si ejecutas un archivo malicioso, CrowdStrike intenta detectarlo y bloquearlo.

### Zscaler
Está centrado en la **conexión a la red e Internet**:

- Filtra páginas web.
- Inspecciona tráfico HTTPS.
- Puede impedir acceder a servicios no autorizados.
- Gestiona el acceso seguro a aplicaciones corporativas sin necesidad de una VPN tradicional.

Ejemplo: cuando visitas una web, el tráfico puede pasar primero por Zscaler para comprobar que sea seguro y que cumpla las políticas de la empresa.

### ¿Por qué suelen instalar ambos?
Porque cubren capas distintas:

1. **Zscaler** protege la comunicación entre tu PC e Internet.
2. **CrowdStrike** protege el propio PC si algo consigue llegar hasta él.

Si me indicas el nombre exacto que aparece en "Aplicaciones instaladas" o en el icono de la bandeja del sistema, puedo decirte exactamente qué versión tiene tu empresa y qué funciones suele tener habilitadas.
---


Son dos categorías de herramientas de seguridad bastante distintas:

## EDR (Endpoint Detection and Response)

Un EDR protege y monitoriza los **equipos finales** (portátiles, PCs, servidores).

Su objetivo no es solo detectar malware, sino también detectar comportamientos sospechosos que un antivirus tradicional podría pasar por alto.

### Qué hace un EDR

- Registra procesos que se ejecutan.
- Monitoriza conexiones de red.
- Detecta movimientos laterales de un atacante.
- Identifica ransomware y comportamientos anómalos.
- Permite investigar incidentes.
- Puede aislar un equipo de la red.

Ejemplo:

Un empleado abre un Excel con una macro maliciosa.

Un antivirus tradicional busca firmas conocidas. Un EDR observa además que:

1. Excel lanza PowerShell.
2. PowerShell descarga un ejecutable.
3. El ejecutable intenta cifrar archivos.

Aunque el malware sea nuevo, el EDR puede detectar la cadena de comportamiento.

Herramientas conocidas:

- entity["software","CrowdStrike Falcon","Endpoint security platform"]
- entity["software","Microsoft Defender for Endpoint","Enterprise endpoint security platform"]
- entity["software","SentinelOne","Endpoint security platform"]

---

## DLP (Data Loss Prevention)

Un DLP protege los **datos**, no el equipo.

Su objetivo es evitar que información sensible salga de la empresa.

### Qué controla un DLP

- Copias a USB.
- Envíos por correo electrónico.
- Subidas a Dropbox, Google Drive, etc.
- Impresiones.
- Copiar y pegar información sensible.
- Compartición de documentos.

Ejemplo:

Un empleado intenta enviar un Excel con 5.000 números de tarjetas de crédito a una cuenta personal.

El DLP puede:

- Bloquear el envío.
- Avisar al usuario.
- Registrar el incidente.
- Notificar al equipo de seguridad.

---

## Diferencia rápida

| Concepto | Protege |
|-----------|----------|
| EDR | El dispositivo |
| DLP | La información |

### Caso práctico

Imagina que en tu portátil corporativo tienes una base de datos de clientes:

- **CrowdStrike (EDR)** detectaría si un atacante intenta comprometer el equipo.
- **DLP** impediría que esa base de datos se copie a un USB o se envíe a una cuenta personal.
- **Zscaler** podría impedir subirla a ciertos servicios web.
- **Defender** actuaría como antivirus/EDR si la empresa usa la versión empresarial.

Por eso en muchas empresas conviven EDR, DLP, proxy web, antivirus y otras herramientas: cada una protege una capa diferente del riesgo.

---
*Generado desde conversación con 6 mensajes.*
*General*
