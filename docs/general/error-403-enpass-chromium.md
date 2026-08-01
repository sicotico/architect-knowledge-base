---
title: Error 403 Enpass Chromium
date: 2026-06-08
category: General
slug: error-403-enpass-chromium
tags: ['General']
---

# Error 403 Enpass Chromium


> **Pregunta original:**
> 
Error 403

Enpass app has denied access to data.

Browser requesting the data is not code signed. You can share the following diagnostics with us at support@enpass.io.

Learn More

Diagnostics
browser
code : 3
origin : chrome-extension://kmcfomidfpdkfieipokbalgegidffkal
path : C:\Users\Luis\AppData\Local\Chromium\Application\chrome.exe
port : 61494
server_port : 10391
> opcion  4
> 148.0.7778.215 (Official Build, ungoogled-chromium) (64 bits) 

---


## Respuesta


Ese error indica que **Enpass está rechazando la conexión de la extensión del navegador porque no considera que el navegador esté correctamente firmado (code signed)**.

Los datos relevantes son:

- Navegador: `chrome-extension://kmcfomidfpdkfieipokbalgegidffkal`
- Ejecutable detectado: `C:\Users\Luis\AppData\Local\Chromium\Application\chrome.exe`
- Error: `code : 3`
- Mensaje: `Browser requesting the data is not code signed`

La clave está en que estás usando **Chromium**, no Google Chrome.

## Por qué ocurre

Enpass verifica que el navegador que solicita acceso a la base de contraseñas sea uno de los navegadores soportados y firmado digitalmente por su fabricante. Algunas compilaciones de Chromium:

- No están firmadas de la misma forma que Chrome.
- Son compilaciones personalizadas.
- No aparecen en la lista de navegadores autorizados por Enpass.

Por seguridad, Enpass bloquea el acceso.

## Comprobaciones rápidas

### 1. ¿Estás usando Chromium o Google Chrome?

Abre:

```
chrome://version
```

Si ves algo como:

```
Chromium
```

es probable que esa sea la causa.

### 2. Prueba con Chrome oficial

Instala o ejecuta:

urlGoogle Chromehttps://www.google.com/chrome/

Instala la extensión de Enpass allí y comprueba si el error desaparece.

### 3. Verifica que la extensión sea la oficial

El ID de extensión:

```
kmcfomidfpdkfieipokbalgegidffkal
```

debería corresponder a la extensión oficial de Enpass. Si la instalaste desde una fuente distinta a la tienda oficial, reinstálala.

### 4. Actualiza Enpass

Asegúrate de tener la última versión desde:

urlEnpass Official Websitehttps://www.enpass.io/

Las versiones antiguas suelen tener problemas de compatibilidad con navegadores basados en Chromium recientes.

### 5. Reinstala la integración del navegador

En Enpass:

1. Settings / Ajustes.
2. Browser.
3. Desactiva la integración.
4. Reinicia Enpass.
5. Actívala de nuevo.
6. Reinstala la extensión.

## Si usas un navegador derivado

Si en realidad utilizas:

- Chromium
- Ungoogled Chromium
- Brave
- Vivaldi
- Otro derivado

dime exactamente cuál y qué versión aparece en `chrome://version`. Algunas versiones funcionan con Enpass y otras son bloqueadas por la validación de firma digital. Con esa información puedo decirte si es un problema conocido o si hay una configuración específica para solucionarlo.
---


La opción 4 consiste en abrir un ticket con soporte de Enpass aportando el diagnóstico completo.

Puedes escribirles a:

**support@enpass.io**

Mensaje sugerido:

:::writing{variant="email" id="58271" subject="Enpass browser integration blocked in Ungoogled Chromium"}
Hello,

I am experiencing an issue with the Enpass browser extension and desktop application integration.

When the extension tries to access Enpass, I receive the following error:

"Error 403 - Enpass app has denied access to data. Browser requesting the data is not code signed."

My browser is:

- Ungoogled Chromium
- Version: 148.0.7778.215 (Official Build) (64-bit)
- Windows

Diagnostics reported by Enpass:

browser
code : 3
origin : chrome-extension://kmcfomidfpdkfieipokbalgegidffkal
path : C:\Users\Luis\AppData\Local\Chromium\Application\chrome.exe
port : 61494
server_port : 10391

Could you please confirm whether Ungoogled Chromium is officially supported? If not, is there any supported configuration, workaround, or whitelist mechanism that would allow Enpass browser integration to work?

Thank you.
:::

### Lo bueno de esta vía

- Obtendrás una respuesta oficial.
- Podrán confirmar si el bloqueo es intencional.
- Si existe una solución interna o experimental, soporte es quien puede indicarla.

### Lo malo

- Si la política de Enpass es permitir únicamente navegadores firmados y soportados oficialmente, es posible que la respuesta sea simplemente que Ungoogled Chromium no es compatible.
- Aunque abras un ticket, es poco probable que habiliten una excepción individual por razones de seguridad.

Dado el mensaje concreto **"Browser requesting the data is not code signed"**, mi expectativa es que te confirmen que Ungoogled Chromium no está soportado actualmente. Aun así, merece la pena consultarlo porque algunos gestores mantienen listas de navegadores compatibles que pueden ampliarse en versiones futuras.
---


Eso explica completamente el error.

**Ungoogled Chromium no está oficialmente soportado por Enpass**. El problema no es la extensión en sí, sino que Enpass intenta verificar que el navegador que solicita acceso esté firmado por un proveedor reconocido. En tu diagnóstico aparece:

```text
path : C:\Users\Luis\AppData\Local\Chromium\Application\chrome.exe
```

y la versión:

```text
148.0.7778.215 (Official Build, ungoogled-chromium)
```

Aunque el ejecutable se llame `chrome.exe`, no es Google Chrome. Ungoogled Chromium elimina muchos componentes de Google y suele compilarse y firmarse de forma distinta. Enpass detecta eso y devuelve:

```text
Browser requesting the data is not code signed
```

## Lo más probable

No es un fallo de configuración tuya.

No es un problema de puertos ni del firewall.

No es un problema de la extensión.

Es una incompatibilidad deliberada entre Enpass y Ungoogled Chromium.

## Cómo confirmarlo en 2 minutos

Instala temporalmente uno de estos navegadores:

- urlGoogle Chromehttps://www.google.com/chrome/
- urlBravehttps://brave.com/
- urlMicrosoft Edgehttps://www.microsoft.com/edge

Luego:

1. Instala la extensión oficial de Enpass.
2. Abre Enpass.
3. Prueba el autocompletado.

Si funciona inmediatamente, queda confirmado que el bloqueo es específico de Ungoogled Chromium.

## Posibles soluciones

### Opción 1: usar otro navegador para las contraseñas

La solución más fiable.

Muchos usuarios mantienen Ungoogled Chromium para navegar y Chrome/Brave únicamente para extensiones que requieren integración nativa.

**Ventaja:** funciona.

**Inconveniente:** dos navegadores.

---

### Opción 2: buscar una versión de Ungoogled Chromium firmada

Algunas compilaciones de terceros vienen firmadas de forma diferente.

**Ventaja:** seguir usando Chromium.

**Inconveniente:** no hay garantía de que Enpass la acepte.

---

### Opción 3: usar el copiado manual desde Enpass

Sin integración con el navegador.

**Ventaja:** funciona siempre.

**Inconveniente:** pierdes autocompletado.

---

### Opción 4: contactar con Enpass

Puedes enviar exactamente el diagnóstico que has pegado.

Es posible que te confirmen oficialmente si la versión 148 de Ungoogled Chromium está bloqueada o simplemente no está en su lista de navegadores permitidos.

Si quieres, puedo ayudarte a comprobar si existe algún parámetro oculto de Enpass o alguna modificación en Windows que permita registrar Ungoogled Chromium como navegador confiable, aunque normalmente los gestores de contraseñas modernos no permiten desactivar esa comprobación por motivos de seguridad.

---
*Generado desde conversación con 6 mensajes.*
*General*
