---
title: Eliminar eventos Exchange Mac
date: 2025-04-03
category: General
slug: eliminar-eventos-exchange-mac
tags: ['General']
---

# Eliminar eventos Exchange Mac


> **Pregunta original:**
> 
uso la app de calendario de Mac y el calendario asociado a una cuenta de exchange no se eliminan los eventos
> El evento se importado como solo lectura

---


## Respuesta


¡Ah, eso lo explica todo! Si el evento fue **importado como solo lectura**, no vas a poder eliminarlo desde la app Calendario de macOS, porque no tienes permisos de edición sobre ese evento.

### 🔍 ¿Qué significa "solo lectura" en este contexto?

Quiere decir que el calendario o el evento proviene de una fuente externa (como un archivo `.ics`, un calendario suscrito, o uno compartido sin permisos de edición), y tú solo puedes **ver** los eventos, no modificarlos ni borrarlos.

---

### 🛠 Soluciones según el origen del evento:

#### ✅ 1. **Si el evento vino de un archivo `.ics` que importaste**
- macOS puede haberlo agregado a un calendario que está marcado como "solo lectura".
- Ve a la app **Calendario**, busca en la barra lateral a qué calendario pertenece.
- Si ese calendario no te deja editar nada, puede que esté ligado a una fuente externa.

**Solución**:  
- Crea un nuevo calendario local o en tu cuenta de iCloud/Exchange.
- Copia los eventos que quieras conservar.
- Luego elimina el calendario completo (clic derecho sobre el calendario > Eliminar).

---

#### ✅ 2. **Si es un calendario suscrito (por URL)**
Los calendarios suscritos (como festivos, horarios deportivos, turnos de trabajo, etc.) **no permiten edición**.

**Solución**:
- Ve a **Ajustes del sistema > Cuentas de Internet** o en la app Calendario > **Preferencias > Cuentas**.
- Busca el calendario suscrito.
- Elimínalo directamente desde ahí.

---

#### ✅ 3. **Si es un calendario compartido de otra persona**
Puede que estés viendo un calendario compartido donde no tienes permisos completos.

**Solución**:
- Pide al dueño del calendario que te dé **permisos de edición**.
- O bien pídele que borre el evento por ti.

---

### 💡 TIP: Verifica el tipo de calendario
En la app Calendario:
- Haz clic en **Visualización > Mostrar lista de calendarios** (si no está ya visible).
- Mira el nombre del calendario donde está el evento.
- Si está en gris o dice algo como “Suscripción” o “sólo lectura”, ya sabes por qué no puedes borrarlo.

---

¿Quieres que te guíe para mover los eventos a un calendario editable o eliminar el calendario completo que los contiene?
---


Vale, vamos a ver cómo podemos solucionarlo. Si estás usando la app de **Calendario** en macOS con una cuenta de **Exchange** y los eventos **no se eliminan correctamente**, puede deberse a varias causas: problemas de sincronización, permisos, o un fallo temporal en la conexión con el servidor de Exchange.

Aquí van algunas **soluciones paso a paso** para intentar arreglarlo:

---

### ✅ 1. **Comprueba que la cuenta de Exchange está bien conectada**
- Ve a **Preferencias del Sistema > Cuentas de Internet** (o **Ajustes del sistema**, dependiendo de tu versión de macOS).
- Selecciona tu cuenta de **Exchange**.
- Asegúrate de que **Calendario** esté activado.
- Verifica que no haya mensajes de error o alertas de contraseña.

---

### ✅ 2. **Forzar sincronización del calendario**
A veces los eventos sí se eliminan localmente, pero el cambio no se refleja en el servidor:

- Abre la app **Calendario**.
- Haz clic en **Visualización > Actualizar todos los calendarios** (o usa el atajo `Cmd + R`).
- Espera unos segundos y verifica si se elimina el evento.

---

### ✅ 3. **Eliminar evento desde webmail o Outlook**
Para verificar si es un problema de la app Calendario:

- Accede a tu correo Exchange a través de **Outlook Web (OWA)** o **Outlook para escritorio**.
- Intenta eliminar el evento desde ahí.
- Si se borra correctamente, el problema está en la app Calendario.
- Si **no se borra**, puede ser un problema con los permisos del calendario (por ejemplo, si es un calendario compartido o de solo lectura).

---

### ✅ 4. **Verifica si es un calendario compartido o delegado**
Los calendarios delegados (por ejemplo, si estás viendo el calendario de otra persona o uno de grupo) a veces no permiten modificar eventos directamente desde la app Calendario.

- Haz clic derecho en el calendario en la barra lateral izquierda.
- Si ves opciones limitadas, puede que no tengas permisos de edición.

---

### ✅ 5. **Eliminar y volver a agregar la cuenta de Exchange**
Como último recurso:

- Ve a **Ajustes del sistema > Cuentas de Internet**.
- Selecciona tu cuenta de **Exchange** y elimínala.
- Reinicia tu Mac.
- Vuelve a agregar la cuenta.

---

Si después de todo esto sigue sin funcionar, dime:
- ¿Estás intentando borrar **tus propios eventos** o de otra persona?
- ¿Te ocurre con **todos los eventos** o solo algunos?
- ¿Sabes si es un calendario **compartido** o delegado?

Con esos datos te ayudo con algo más preciso.

---
*Generado desde conversación con 4 mensajes.*
*General*
