---
title: Mejoras ROCKNIX X55
date: 2026-05-23
category: General
slug: mejoras-rocknix-x55
tags: ['General']
---

# Mejoras ROCKNIX X55


> **Pregunta original:**
> 
aparecio el logo de rocknix , la version nightly y varios mensajes de configuracion de audio , root y algo más. Despues de eso se ha quedado negra la pantall y por unos segundo el led cabio a rojo  , ahora a vuelto a ver y la tengo enchufada a la corriente  
> lleva mas de 20 minutos en negro , con el led verde 
> nightly-20260523 
> 
> *...y 6 preguntas de seguimiento*


---


## Respuesta


Perfecto. Si ya has lanzado la actualización desde el menú, en la **X55 lo normal es dejarla terminar sola**.

Ruta estándar:
`Start → System Settings → System Update → Start Update` citeturn0search3

Unas cosas útiles mientras está actualizando:

- **No apagues aunque parezca parada** durante varios minutos.
- Si está descargando una **nightly**, puede tardar bastante más que una OTA estable.
- La primera carga tras actualizar suele ser más lenta porque recompone cachés y servicios.
- Si reinicia una vez adicional, entra dentro de lo normal.

Para tu caso (vienes de **20250517 → rama nightly**):
- Tus ROMs normalmente **no deberían tocarse**.
- Configuración de EmulationStation y RetroArch normalmente se conserva, pero algunas opciones pueden resetearse si hubo cambios internos. citeturn0search0turn0search3
- Las builds de desarrollo tienen algunas limitaciones (por ejemplo ciertas integraciones como scraping/RetroAchievements pueden comportarse distinto según build). citeturn0search3

Si se queda:
- **10–15 min en “Downloading”** → suele ser red/servidor.
- **20–30 min en “Applying update”** → aún puede ser normal.
- **Pantalla negra >10 min sin actividad** → ahí ya empezaría a sospechar.

Cuando termine dime exactamente:
1. versión que aparece en **System Information**  
2. si pone **nightly-xxxxx** o una fecha  
3. si arranca desde SD o memoria interna  
4. si notas algo raro (Wi-Fi, sleep, brillo, controles, scraping)

Con eso te digo si ha quedado limpia o si conviene hacer algún ajuste post-update. citeturn0search2turn0search3
---


He revisado el estado actual de ROCKNIX y sí: lo que has visto es correcto. **La rama estable (`distribution`) prácticamente se ha congelado en 20250517** y el desarrollo activo se ha movido a **nightly builds** en otro repositorio. citeturn0search0turn0search1

Como tienes una **Powkiddy X55 (RK3566)** con **ROCKNIX 20250517**, te resumo **qué has ganado potencialmente si saltas a nightly** y qué cosas realmente te afectan en ese hardware.

- Repositorio estable: urlROCKNIX distributionhttps://github.com/ROCKNIX/distribution
- Nightlies actuales: urlROCKNIX distribution-nightlyhttps://github.com/ROCKNIX/distribution-nightly
- Descargas nightly: urlROCKNIX Nightly Downloadshttps://nightly.rocknix.org/

## Lo que ya tenías en 20250517 (tu versión)
La versión que llevas ya fue una actualización importante respecto a principios de 2025:  
- **Rebase completo de EmulationStation** (fork renovado desde Batocera).
- Muchas correcciones de interfaz.
- **Descargador de temas** integrado.
- UI Bluetooth ampliada.
- Soporte de **vibración/rumble** en dispositivos compatibles.
- Opción para activar/desactivar multitouch.
- Varias actualizaciones de emuladores y sistema. citeturn0search0turn0search12

Para X55 eso significó sobre todo mejor experiencia general y menos glitches de frontend.

---

# Mejoras que han ido llegando después (nightly)

## 1. Kernel Linux más moderno para S922X y limpieza general del árbol
Han ido actualizando kernels y simplificando builds internas. Aunque muchos commits mencionan otras plataformas, parte del trabajo termina llegando al ecosistema completo (drivers, servicios, paquetes compartidos). citeturn0search1turn0search11

Impacto en X55:
- Mejor estabilidad suspend/resume.
- Menos servicios heredados.
- Menos conflictos entre input y overlays.

No esperes +20% FPS.

---

## 2. EmulationStation sigue evolucionando
Han seguido actualizando:
- paquete de EmulationStation
- integración de nuevas opciones de cores
- limpieza del sistema de características y menús citeturn0search1turn0search11

Impacto en X55:
- navegación algo más consistente
- menos cuelgues en cambios de sistema
- mejor detección de configuraciones

---

## 3. Mejoras de overlays y monitorización
Cambios recientes:
- **MangoHud actualizado**
- estimación de **tiempo restante de batería**
- mejoras de visualización compacta citeturn0search1

Impacto en X55:
- probablemente una de las mejoras visibles si usas overlays.

---

## 4. Limpieza del sistema de entrada (InputPlumber / mandos)
Han tocado bastante:
- reinicios automáticos tras suspensión
- cambios de perfiles
- limpieza de servicios antiguos
- ajustes de compatibilidad con mandos citeturn0search1turn0search11

Impacto en X55:
- menos casos de botones que dejan de responder tras sleep.

---

## 5. PortMaster y paquetes actualizados
Se han seguido actualizando:
- PortMaster
- Heroic Launcher
- componentes del sistema citeturn0search1

Impacto en X55:
- algunos ports nuevos o menos problemas de compatibilidad.

---

# Errores que se han ido corrigiendo (y que sí podrías notar)

No todo aplica a RK3566, pero sí hay una tendencia clara:

- correcciones de audio
- arreglos de Bluetooth
- arreglos de suspensión
- arreglos de pantalla táctil
- limpieza de firmware externo
- correcciones de montaje automático de almacenamiento
- arreglos del overlay de rendimiento citeturn0search1turn0search11

---

# ¿Merece la pena actualizar una Powkiddy X55?

## Mantenerte en 20250517
Ventajas:
- Muy estable.
- Menos riesgo de romper scraping, temas o shaders.
- Ideal si solo juegas.

Inconvenientes:
- Te pierdes correcciones continuas.
- Algunos ports y paquetes quedan atrás.

## Pasarte a nightly (mi valoración para X55)
Ventajas:
- Mejor mantenimiento real hoy.
- Más correcciones acumuladas.
- Ecosistema activo.

Inconvenientes:
- Alguna nightly puede romper algo.
- Más posibilidad de regresiones.

### Mi recomendación concreta para X55:
- Si la consola es **tu máquina principal y ya va bien → sigue en 20250517**.
- Si te gusta probar y haces backup → **instala una nightly reciente (no necesariamente la última del día)** y deja 3–7 días de margen para evitar builds problemáticas.

Antes de cambiar:
1. Backup de `/storage/roms`
2. Backup de `/storage/.config`
3. Exporta favoritos y scraping
4. Guarda shaders y configuraciones RetroArch

Y para tu X55 recuerda: usa siempre el build **RK3566**, no el Generic de otra plataforma. citeturn0search3turn0search10
---


Eso después de una actualización OTA grande **no me parece automáticamente mala señal**, sobre todo si has pasado de **20250517 → nightly-20260523**.

Primero necesito que **no fuerces nada todavía**.

Haz esto:

1. Espera **5–10 minutos reales** desde que se quedó negra.
   - La primera actualización puede expandir particiones, reconstruir cosas y tardar.

2. Mira señales:
   - ¿LED encendido?
   - ¿Retroiluminación de pantalla encendida (negro iluminado) o totalmente apagada?
   - ¿Se calienta un poco?
   - ¿Se oye clic del altavoz al pulsar volumen?

Si tras **10 minutos** sigue totalmente negra:

3. Mantén pulsado **POWER unos 12–15 segundos** (no toques reset si tiene).
   - Espera 10 segundos.
   - Pulsa POWER normal para arrancar.

Si arranca:
- déjala iniciar sola;
- el primer arranque puede tardar bastante.

Si **no arranca y vuelve a negro**, prueba:
- apagar completamente,
- sacar la SD,
- volver a insertar,
- encender.

No reformatees ni grabes imagen todavía.

Y dime exactamente una de estas opciones:

A) pantalla negra pero **retroiluminada**  
B) pantalla totalmente apagada  
C) sale logo de Powkiddy y vuelve a negro  
D) vibra / LED pero nada en pantalla

Eso acota mucho si es primer arranque lento o si el update dejó el boot a medias.
---


Vale, eso cambia bastante el diagnóstico.

Lo que describes:

- apareció **logo ROCKNIX**
- salió **nightly-20260523**
- viste mensajes de configuración (**audio, root y más servicios**)
- después pantalla negra
- el LED pasó **verde → rojo unos segundos → verde**
- está conectada al cargador

Eso **suena más a que el sistema sí ha arrancado y se ha quedado colgado al levantar la interfaz gráfica (EmulationStation)**, no a boot roto.

Haz esto:

## 1. Espera solo 2 minutos más (no 20)
Porque ya pasó la fase de configuración.

## 2. Apagado limpio forzado
- Mantén **POWER 15–20 segundos**
- Confirma que el LED se apaga del todo
- Desconecta el cargador

## 3. Arranque SIN cargador
- Pulsa POWER una sola vez
- Espera **hasta 3 minutos**

Observa:
- ¿sale logo ROCKNIX?
- ¿vuelve a mensajes?
- ¿pantalla negra directamente?

## 4. Si vuelve a negro pero el sistema parece vivo
Prueba esto:

- Pulsa **VOL+ y VOL−**
- Pulsa **POWER una vez corta** (no mantener)
- Espera 10 s

Quiero descartar brillo a cero o suspensión accidental.

## 5. Si sigue negro → intenta arrancar con red desactivada
- Apaga
- Retira cualquier:
  - dongle USB
  - mando BT
  - adaptador
- Enciende

No saques todavía la SD ni reinstales.

Y dime una sola cosa después del siguiente intento:

**¿Después del logo de ROCKNIX llegas a ver el menú o pasa directamente a negro?**
---


Bien, el LED rojo ahora es una pista útil.

En la **Powkiddy X55**, con el cargador conectado, **rojo normalmente indica estado de carga / alimentación**, no necesariamente error. El problema es que no sabemos si el sistema está colgado o simplemente apagado.

Haz esto exactamente:

1. **Desconecta el cargador.**
2. Mantén **POWER 20 segundos completos**.
3. Espera **10 segundos**.
4. Pulsa **POWER una sola vez** (1 segundo, no mantener).

Observa durante **2–3 minutos**:

- ¿el LED cambia a verde?
- ¿sale logo Powkiddy?
- ¿sale logo ROCKNIX?
- ¿hay retroiluminación pero negro?
- ¿no hace absolutamente nada?

No conectes el cargador durante esta prueba.

Por lo que has contado hasta ahora, todavía me inclino más por:
- actualización aplicada correctamente,
- primer arranque terminó scripts,
- se colgó entrando al frontend.

Eso suele recuperarse con un apagado completo.

Dime exactamente qué ves después de encender sin cargador.
---


Para **tu X55 concretamente**, viniendo además de que **ya estás en ROCKNIX nightly**, mi valoración sería: **no me cambiaría a GammaOS como sistema principal**.

Hay casos donde sí tiene sentido, pero son más concretos de lo que parece.

Comparativa práctica para **Powkiddy X55 (RK3566)**:

| Aspecto | ROCKNIX (nightly actual) | GammaOS Core |
|---|---|---|
| Encender y jugar | Gana | Correcto |
| Emulación hasta PS1 / GBA / SNES / MD | Empate | Empate |
| PSP | Bien | Ligera ventaja |
| Dreamcast | Similar | Similar |
| Android (apps, streaming) | Limitado | Gana |
| PortMaster | Gana claramente | No |
| Gestión con botones | Gana | Algo más incómodo |
| Sleep / consumo en reposo | Mejorando | A veces mejor |
| Trastear | Medio | Alto |

La tendencia que comenta bastante gente que ha probado ambos en X55 es bastante consistente:
- **GammaOS Core suele sacar algo más de PSP** y algunos hablan de menor consumo en suspensión. citeturn0search0turn0search4turn0search7
- **ROCKNIX suele ganar en experiencia de consola dedicada**, integración de emuladores y especialmente **PortMaster**. citeturn0search4turn0search5
- GammaOS existe precisamente en variante adaptada a dispositivos sin táctil, pero Android sigue siendo menos natural en una X55 que un frontend Linux dedicado. citeturn0search0turn0search1

Conociendo además tu situación:
- acabas de pasar de **ROCKNIX 20250517 → nightly-20260523**
- ya estás en la rama que está recibiendo trabajo activo

Yo haría esto:

### Quédate en ROCKNIX si…
- juegas sobre todo **8/16/32 bits**
- PS1 / N64 / Dreamcast ocasional
- usas **PortMaster**
- quieres encender y jugar

### Prueba GammaOS en una segunda SD si…
- juegas **muchísimo PSP**
- quieres **Moonlight / Android / streaming**
- te apetece probar Android
- te importa exprimir algo más el RK3566

La ventaja es que **no tienes que elegir**: bastante gente mantiene **una SD con ROCKNIX y otra con GammaOS** e intercambia según el uso. citeturn0search0turn0search3

Te haría una pregunta porque cambia mucho la recomendación:

**¿Qué porcentaje de uso haces de PSP, PortMaster y Dreamcast?** Si me dices “80% PSP” igual sí te digo que merece una SD secundaria con GammaOS.
---


Con **más de 20 minutos en negro y LED verde fijo**, ya no asumiría que sigue trabajando. En una X55 tras OTA eso normalmente ya debería haber arrancado.

Haz esto en este orden:

## 1. Apagado forzado
- Mantén **POWER 15–20 segundos**.
- No pulses varias veces.
- Espera **10 segundos**.

Comprueba que el LED se apaga.

## 2. Arranque normal
- Pulsa **POWER una sola vez**.
- Espera **hasta 3–5 minutos**.

Observa:
- ¿aparece logo?
- ¿retroiluminación?
- ¿pantalla totalmente negra?

## 3. Si sigue negra → prueba reinicio frío de la SD
- Apaga otra vez (POWER 15–20 s).
- Saca la microSD.
- Espera 10 s.
- Vuelve a insertarla.
- Enciende.

## 4. Si sigue igual
Prueba mantener:
- **VOL+ + POWER** durante unos segundos al arrancar.

No es una recuperación garantizada, pero a veces fuerza una ruta distinta de arranque.

Importante: **no regrabes la SD todavía**. Muchas veces el sistema está intacto y solo el primer reinicio tras OTA se queda colgado.

Dime qué pasa después del paso 2:
- ¿sale logo de Powkiddy?
- ¿sale logo de ROCKNIX?
- ¿pantalla iluminada en negro?
- ¿LED verde permanente desde el primer segundo?
---


Con ese perfil cambia bastante mi recomendación.

Tú dices:
- **juegas poco** → quieres encender y jugar
- **PSP**
- **PS1**
- **Dreamcast**
- **muy de arcades 90s**

Para eso, en una **Powkiddy X55**, **me quedaría en ROCKNIX** y no movería el sistema principal a GammaOS.

## Lo que te aporta realmente cada sistema para tu uso

### PSP
GammaOS puede rascar alguna mejora puntual en ciertos juegos pesados.

Pero en X55 el salto **no suele convertir injugable → perfecto**. Muchas veces hablamos de:
- menos tirones,
- frames más estables,
- algún ajuste más agresivo.

Si juegas poco, probablemente no compensa cambiar de ecosistema.

En ROCKNIX prueba antes:
- PPSSPP → resolución **2×**
- backend **Vulkan** (si disponible)
- frameskip **OFF**
- `Buffered Rendering ON`
- `Auto Frameskip OFF`

### PS1
Aquí no veo motivo para GammaOS.

En X55 con ROCKNIX:
- **DuckStation** o **PCSX ReARMed**
- resolución interna ×2 si quieres

Va muy bien.

### Dreamcast
Aquí tampoco veo una ventaja clara de cambiar.

Usaría:
- **Flycast**
- resolución **1×**
- `Threaded Rendering ON`
- `Mipmapping OFF` si algún juego rasca

Para:
- entity["video_game","Crazy Taxi","Dreamcast video game"]
- entity["video_game","Soulcalibur","1998 video game"]
- entity["video_game","Marvel vs. Capcom 2","2000 video game"]

la X55 ya va razonablemente bien.

---

## Donde sí brilla TU perfil: arcades 90s

Aquí ROCKNIX me parece claramente más adecuado.

Para:
- entity["video_game","Metal Slug","SNK arcade game"]
- entity["video_game","Cadillacs and Dinosaurs","Capcom arcade game"]
- entity["video_game","Out Run","Sega arcade game"]
- entity["video_game","Street Fighter Alpha 3","Capcom fighting game"]
- entity["video_game","Daytona USA","Sega arcade game"]
- entity["video_game","DoDonPachi","Cave arcade game"]

usa:

- **FBNeo** → primera opción
- **MAME 2003 Plus** → compatibilidad retro
- **MAME current** → solo cuando haga falta

FBNeo suele dar la experiencia más limpia para arcade 80–90.

## Lo que haría yo en tu caso

Mantener:
- **ROCKNIX nightly-20260523**

Ajustar:
- PSP → PPSSPP optimizado
- Dreamcast → Flycast
- Arcade → FBNeo

No instalar GammaOS ahora.

Solo probaría GammaOS si dentro de unas semanas dices:
> “Estoy jugando sobre todo PSP y quiero exprimir cada FPS”.

Porque por tus hábitos (“juego poco + arcade + PS1 + Dreamcast”), el coste de cambiar probablemente es mayor que la mejora que notarás.
---


Bien. Si ya estás en **nightly-20260523**, entonces ya has saltado del canal estable al canal de desarrollo y estás prácticamente en la punta del árbol actual. citeturn0search0turn0search2

Para una **Powkiddy X55 (RK3566)** haría esta comprobación rápida antes de darla por buena:

## Checklist post-actualización (2 minutos)

1. **System → Information**
   - Confirma que sigue detectando **RK3566**.
   - Que el build aparece como `nightly-20260523`.

2. **Wi-Fi**
   - Desactiva y activa una vez.
   - Comprueba que recuerda la red (han tocado gestión de red y Wi-Fi en nightlies recientes). citeturn0search3

3. **Suspensión**
   - Pulsa power → sleep → espera 30 s → despierta.
   - Comprueba que vuelven botones y audio.

4. **RetroArch**
   - Abre un juego → menú rápido → mira que sigan:
     - shaders
     - overlays
     - escalado
     - hotkeys

5. **EmulationStation**
   - Verifica:
     - temas
     - favoritos
     - scraping
     - colecciones

## Algo que debes saber de nightlies

ROCKNIX indica que las **builds de desarrollo pueden tener diferencias funcionales respecto a estables** y algunos servicios integrados no siempre están garantizados igual entre compilaciones. citeturn0search4

Para X55 el riesgo típico no suele ser perder rendimiento; suele ser:
- alguna regresión en sleep,
- algún cambio en entrada/mandos,
- o una opción que vuelve al valor por defecto.

## Si notas que algo va raro después del update

Prueba en este orden:

- `Start → Quit → Restart System`
- luego `System → Danger Zone → Reset RetroArch Config`
- si sigue → borrar caché de EmulationStation (sin tocar ROMs)

Y una cosa que me interesa porque cambia mucho la recomendación:

**¿Has actualizado por OTA manteniendo la instalación antigua o has hecho instalación limpia desde imagen?**  
Y dime si tu X55 **arranca desde SD o desde eMMC interna**.

---
*Generado desde conversación con 18 mensajes.*
*General*
