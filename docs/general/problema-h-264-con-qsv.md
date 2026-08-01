---
title: Problema H.264 con QSV
date: 2026-07-04
category: General
slug: problema-h-264-con-qsv
tags: ['General']
---

# Problema H.264 con QSV


> **Pregunta original:**
> 
dame el parametro para VideoScaler por hardware
> Ya he encontrado el H264 con QSV. Tengo una pelicula de animacion y no se que QP usar 
> Tengo instalado este pero solo me d ala la opcion de QSV H.265 
> 
> *...y 9 preguntas de seguimiento*


---


## Respuesta


Sí, puedes usar H.264 por hardware con Intel, pero hay una trampa: en HandBrake el encoder se llama **H.264 (Intel QSV)**, no “VAAPI H.264”. Si no aparece, normalmente es por plugin/driver/soporte de GPU.

HandBrake confirma que H.264 puede usar Intel Quick Sync en hardware, y que en Flatpak hace falta el plugin Intel QSV/MediaSDK aparte. También indica que el soporte oficial actual apunta a Intel **9ª gen Coffee Lake o más nuevo** con Intel HD/Iris Xe/Arc, aunque a veces funciona en generaciones anteriores. [HandBrake QSV](https://handbrake.fr/docs/en/latest/technical/video-qsv.html), [HandBrake codecs](https://handbrake.fr/docs/en/latest/technical/video-codecs.html)

Prueba esto:

```bash
flatpak update
flatpak list | grep -i handbrake
```

Luego instala el plugin oficial de HandBrake para QSV. En la web oficial aparece como:

```text
HandBrake.Plugin.IntelMediaSDK-1.10.2-x86_64.flatpak
```

Se instala así, desde la carpeta donde lo descargues:

```bash
flatpak install ./HandBrake.Plugin.IntelMediaSDK-1.10.2-x86_64.flatpak
```

Después reinicia HandBrake y revisa:

`Preferencias -> Video -> Allow use of Intel QuickSync Encoders`

Luego en la pestaña **Video**, busca:

```text
H.264 (Intel QSV)
```

Si solo aparece **H.265 QSV**, revisa el driver Intel:

```bash
sudo apt install vainfo intel-media-va-driver-non-free
vainfo
```

En `vainfo` deberías ver algo como `VAProfileH264...EncSlice`. Si no aparece ninguna línea de **H264 encode**, HandBrake no puede ofrecer H.264 QSV porque el sistema no lo está exponiendo.

Lo bueno: H.264 QSV es rápido, consume poca CPU y tiene compatibilidad excelente. Lo malo: comprime peor que H.265/AV1; para el mismo tamaño suele verse peor, o para la misma calidad ocupa más. Si tu prioridad es “archivo pequeño”, H.265 QSV o x265 software suelen ganar. Si tu prioridad es compatibilidad con TVs, móviles y reproductores, H.264 QSV tiene sentido.

Si me dices el modelo exacto de tu CPU/GPU, por ejemplo con:

```bash
lscpu | grep "Model name"
lspci | grep -i "vga\|display"
```

te digo si tu Intel debería soportar H.264 QSV o si estás chocando con una limitación real.
---


Voy a leer el registro y buscar las líneas que importan: si realmente entra QSV para encode/decode, si hay filtros que mandan trabajo a CPU, y si el audio está quedando como esperas.
---


Ya aparece la línea clave: `encode-only via system memory path`. Eso confirma que está codificando en QSV, pero el decode/scale no está encadenado en GPU; voy a mirar si al final reporta errores o estadísticas raras.
---


Para una película de animación con **H.264 QSV**, empezaría con:

```text
QP / Calidad constante: 22
```

Luego haz una prueba de 1-2 minutos con una escena oscura, una escena con movimiento y una escena con fondos planos.

Guía rápida:

| QP | Resultado |
|---:|---|
| 18-20 | Muy buena calidad, archivo grande |
| 21-23 | Buen equilibrio para animación |
| 24-26 | Más compresión, puede aparecer banding/bloques |
| 27+ | Solo si priorizas tamaño sobre calidad |

Mi recomendación práctica:

```text
Animación 1080p: QP 22
Si quieres más calidad: QP 20
Si quieres menos tamaño: QP 24
```

Lo bueno de QSV: será rápido y usará poca CPU. Lo malo: H.264 QSV no comprime tan fino como `x264` por software. En animación, los fondos planos y degradados pueden sufrir antes, así que no subiría mucho de **QP 24** salvo que no te importe perder detalle.

Si es una película que quieres conservar, usaría **H.265 QSV QP 24-26** o **x264 RF 18-20**. Si necesitas máxima compatibilidad, **H.264 QSV QP 22** está bien.
---


En tu captura estás mirando **Preajustes > Hardware**, no la lista completa de codificadores. Ahí HandBrake solo trae preajustes oficiales H.265 QSV, y eso **no significa necesariamente** que no tengas H.264 QSV.

Haz esto:

1. Cierra ese menú de preajustes.
2. Entra en la pestaña **Video**.
3. Busca el desplegable **Codificador de vídeo**.
4. Ahí debería aparecer algo como:

```text
H.264 (Intel QSV)
H.265 (Intel QSV)
```

Si aparece **H.264 (Intel QSV)**, selecciónalo manualmente y luego guarda tu propio preset: `Preajustes -> Guardar nuevo preajuste`.

Si en la pestaña **Video** tampoco aparece H.264 QSV, revisa esto:

```bash
flatpak list | grep -i handbrake
flatpak list | grep -i intel
vainfo | grep -i h264
```

Lo importante es que `vainfo` muestre soporte de codificación H.264, algo parecido a:

```text
VAProfileH264Main ... VAEntrypointEncSlice
VAProfileH264High ... VAEntrypointEncSlice
```

Si no sale `EncSlice`, tu sistema está viendo decodificación H.264, pero no codificación H.264 por hardware.

También mira en HandBrake:

```text
Preferencias -> Video -> Permitir codificadores Intel Quick Sync
```

Y activa QSV si está desactivado.

En resumen: lo de tu imagen puede ser normal, porque son solo **preajustes H.265**. La prueba real está en **Video -> Codificador de vídeo**. Si quieres, pásame la salida de esos tres comandos y te digo exactamente dónde falla.
---


Para películas normales con **H.264 QSV**, pondría:

```text
QP 21-23
```

Mi valor base sería:

```text
QP 22
```

Ajuste rápido:

| Tipo de película | QP recomendado |
|---|---:|
| Imagen real / live action | 21-23 |
| Animación | 20-22 |
| Película oscura o con mucho grano | 20-21 |
| Quieres archivo más pequeño | 23-24 |
| Quieres conservar bastante calidad | 19-21 |

Para **1080p**, usaría:

```text
QP 22 para equilibrio
QP 20 si te importa mucho la calidad
QP 24 si quieres ahorrar espacio
```

Lo bueno de QSV es que va rápido. Lo malo es que a igual QP suele comprimir peor que `x264` por software, así que no lo apretaría demasiado. Para una biblioteca personal, yo dejaría **H.264 QSV QP 22** como preset general.
---


Voy a comprobar la parte cambiante: en HandBrake para Linux esto depende bastante de la versión, del paquete Flatpak y de qué backend Intel expone tu GPU. Luego te dejo pasos prácticos para distinguir “no está soportado” de “falta un paquete/permisos”.
---


Voy a mirar esto con cuidado porque el nombre interno del scaler no es tan estable como `qsv_h264`; si te doy un valor inventado, HandBrake simplemente lo ignorará o fallará al importar el preset.
---


Eso suele pasar porque **Dolby Pro Logic / surround downmix** reparte el canal central, donde van muchos diálogos, y en estéreo puede quedar algo hundido. Para que las voces manden más, yo haría esto en HandBrake:

En la pestaña **Audio**:

```text
Códec: AAC
Mezcla: Stereo
DRC: 1.5 a 2.0
Ganancia: +2 dB o +3 dB
```

Lo más importante es **DRC**: comprime el rango dinámico, baja un poco explosiones/música y sube lo bajo, así los diálogos se entienden mejor. Empieza con:

```text
DRC: 1.5
```

Si aún oyes flojas las voces:

```text
DRC: 2.0
```

También puedes evitar **Dolby Pro Logic II** si estás escuchando en altavoces estéreo, portátil, tele o auriculares normales. Usa mejor:

```text
Mezcla: Stereo
```

No “Dolby Pro Logic II”.

Lo bueno: voces más claras y volumen más uniforme. Lo malo: pierdes algo de impacto cinematográfico; explosiones, música y ambientes sonarán menos “grandes”.

Mi ajuste recomendado para tu caso:

```text
AAC 160-192 kbps
Stereo
DRC 1.5
Ganancia +2 dB
```

Y si quieres conservar el audio original por si acaso, añade **dos pistas**: una original en passthru y otra AAC Stereo con DRC para ver la película con diálogos claros.
---


Ya se ve una causa clara en el JSON: `"VideoScaler": "swscale"` significa escalado por software. La parte más delicada es que cambiarlo a mano no siempre basta, porque si hay filtros o recortes que rompen la cadena de hardware, HandBrake vuelve a CPU para esa etapa.
---


Voy a aterrizarlo sin asumir que necesitas “hacerlo perfecto de cine”: aquí lo importante es evitar que una película HDR se vea lavada, demasiado oscura o con colores raros al pasarla a H.264 para una tele sencilla.
---


Tiene sentido para tu caso, pero ajustaría un poco.

Si usas **altavoces malos de TV**, tu prioridad real no es conservar Atmos/5.1, sino que el diálogo se entienda. Ahí tu idea de **AAC estéreo + ganancia + DRC** es práctica.

Yo usaría este preset base:

```text
Vídeo: H.264 QSV
Calidad: QP 21-22
Framerate: Igual que fuente
Audio: AAC estéreo
Bitrate audio: 160-192 kbps
DRC: 1.5
Ganancia: +2 dB
```

Si las voces siguen bajas:

```text
DRC: 2.0
Ganancia: +3 dB
```

No subiría mucho más la ganancia porque puedes provocar distorsión o clipping en explosiones/música.

Lo bueno de tu enfoque: máxima compatibilidad con Apple TV, iPhone, Windows, Ubuntu y teles; archivos fáciles de reproducir; voces más claras; menos líos con formatos HDR/audio.

Lo malo: al pasar de H.265 10-bit HDR a **H.264 8-bit SDR** puedes perder HDR, profundidad de color y eficiencia. El archivo puede quedar más grande o con menos calidad que H.265 para el mismo tamaño.

Para una TV mala y altavoces malos, yo haría esto:

```text
Películas 1080p SDR: H.264 QSV QP 21-22
Películas 4K HDR buenas: H.265 10-bit QSV QP 24-26
Audio para TV: AAC Stereo, DRC 1.5-2.0, Gain +2 dB
```

Si lo que más te importa es “verlo cómodo y entender los diálogos”, tu preset H.264 QSV QP 21 con AAC estéreo mejorado está bastante bien. Ajustaría solo el audio: **DRC 1.5 primero**, y **2.0 si sigue flojo**.
---


Voy a comprobar compatibilidad por familia de dispositivos, porque aquí la respuesta cambia mucho según si tu Apple TV es 4K o HD y según los iPhone. La parte práctica será separar “archivo maestro para conservar” de “archivo compatible para todo”.
---


Sí, este log deja bastante claro qué está pasando.

Tu Intel/QSV está bien y **sí está codificando por hardware**:

```text
encoder: H.264 (Intel QSV)
quality: 21,00 (QP)
encavcodecInit: H.264 (Intel Quick Sync Video)
```

Pero no está usando una cadena completa GPU decode + scale + encode. La línea clave es:

```text
encavcodec: using encode-only via system memory path
```

Eso significa: **QSV solo para encode**, y los frames llegan desde memoria del sistema. Además el log muestra:

```text
decoder: hevc 10-bit (yuv420p10le)
Crop and Scale ... scale: 1920 * 1080
Format (format=nv12)
```

O sea: decode HEVC 10-bit, escalado y conversión a `nv12` pasan por la ruta normal/software antes de entregar a QSV.

Veo dos cosas que corregiría:

1. Estás pasando una fuente **HDR 10-bit HEVC/Dolby Vision/HDR10+** a **H.264 QSV 8-bit**:

```text
Video: hevc (Main 10), bt2020/smpte2084
Format (format=nv12)
encoder: H.264 (Intel QSV)
```

`nv12` es 8-bit. Pierdes 10-bit y puedes tener banding o HDR raro. Si quieres conservar HDR: mejor **H.265 10-bit QSV**.

2. La geometría de salida está rara:

```text
storage dimensions: 1920 x 1080
pixel aspect ratio: 90 : 67
display dimensions: 2579 x 1080
```

La fuente es 3840x1608, aspecto 2.39:1. Para 1080p con píxeles cuadrados debería salir más o menos:

```text
1920 x 804
PAR 1:1
```

Yo pondría en Dimensiones:

```text
Anamorphic / Anamórfico: None
Keep aspect ratio: activado
Width: 1920
Height: automático
```

No fuerces 1920x1080 para una película 2.39:1 salvo que quieras píxeles no cuadrados o padding.

El audio está bien para tu caso:

```text
AAC stereo 320 kbps
gain: 2 dB
DRC: 1.9
```

Para altavoces malos de TV, lo veo razonable. Si notas sonido aplastado, baja DRC a `1.5-1.7`; si las voces siguen flojas, deja `1.9`.

Mi ajuste recomendado para esa película concreta:

```text
Si quieres conservar HDR:
H.265 10-bit QSV, QP 24-26, resolución 1920x804 o 3840x1608

Si quieres máxima compatibilidad y voces claras:
H.264 QSV, QP 21-22, convertir a SDR/BT.709, resolución 1920x804, AAC stereo DRC 1.5-1.9
```

Lo que no haría es dejar **H.264 8-bit con metadata HDR/PQ** para una fuente así. Puede funcionar, pero es una mezcla poco limpia.
---


Voy a separar dos cosas que HandBrake mezcla bastante: “codificar con QSV” no implica automáticamente “decodificar y escalar todo en GPU”. Tu preset ya tiene el encoder QSV activo, pero hay un par de campos que fuerzan la ruta software.
---


Sí, en tu caso **merece la pena mantener H.265, HDR y 10-bit**, sobre todo si tu Apple TV es **Apple TV 4K** y tus iPhone son relativamente modernos.

Apple TV 4K soporta HEVC Main/Main 10 hasta 4K 60 fps, y también HDR10/HDR10+/HLG con HEVC Main 10, además de Dolby Vision en perfiles compatibles. [Apple TV 4K specs](https://www.apple.com/apple-tv-4k/specs/) Apple también indica que iOS 11 o posterior y macOS High Sierra o posterior manejan HEIF/HEVC. [Apple Support HEVC](https://support.apple.com/en-us/116944) En Windows 11, HEVC puede requerir la extensión HEVC de Microsoft o un reproductor como VLC/mpv. [Microsoft HEVC Extensions](https://apps.microsoft.com/detail/9nmzlz57r3t7)

Mi recomendación para tu biblioteca:

| Caso | Qué usaría |
|---|---|
| Películas 4K HDR | **H.265 10-bit QSV** |
| Películas 1080p SDR | H.264 QSV si quieres compatibilidad, H.265 QSV si quieres ahorrar espacio |
| Animación 1080p | H.265 10-bit si no te importa compatibilidad antigua |
| Máxima compatibilidad universal | H.264 8-bit SDR |
| Archivo “para conservar” | H.265 10-bit, manteniendo HDR |

Para tu fuente concreta, que es **4K HEVC Main10 HDR/Dolby Vision/HDR10+**, yo no la pasaría a H.264 salvo que necesites sí o sí compatibilidad vieja. Usaría:

```text
Vídeo: H.265 10-bit (Intel QSV)
Calidad: ICQ/QP 24-26
Framerate: Same as source / Igual que fuente
Resolución: mantener 3840x1608 si quieres 4K
Audio: copiar E-AC3 o AC3 + AAC estéreo opcional
Contenedor: MKV si quieres conservar más pistas/subtítulos; MP4 si priorizas Apple
```

Lo bueno de mantener H.265/HDR/10-bit: mejor calidad, menos banding, archivos más pequeños que H.264 y encaja muy bien con Apple TV 4K/iPhone modernos.

Lo malo: en Windows puede depender del códec/reproductor; algunos dispositivos antiguos no lo reproducen bien; y si HandBrake no conserva exactamente Dolby Vision/HDR10+ como esperas, puedes acabar con HDR limitado o convertido. Para evitar disgustos, haría una prueba de 3 minutos y comprobaría en Apple TV que la tele entra en modo HDR/Dolby Vision.
---


Tu preset **sí tiene activado el encoder QSV**:

```json
"VideoEncoder": "qsv_h264"
```

Y también parece que pide decode por hardware:

```json
"VideoHWDecode": 1
```

Pero el escalador está explícitamente en software:

```json
"VideoScaler": "swscale"
```

`swscale` es el escalador de FFmpeg por CPU. Ahí no hay duda.

Lo importante: en HandBrake, QSV acelera sobre todo **encode**, y puede acelerar **decode** si el formato de entrada lo permite. Pero muchos filtros, subtítulos quemados, deblock, deinterlace, denoise, colorspace, etc. rompen la ruta de hardware y vuelven a CPU. HandBrake documenta que incluso usando QSV, CPU sigue trabajando en filtros, audio, subtítulos, muxing y otras partes del proceso. [HandBrake QSV](https://handbrake.fr/docs/en/latest/technical/video-qsv.html)

En tu preset revisaría esto:

| Campo | Estado | Comentario |
|---|---:|---|
| `VideoEncoder: qsv_h264` | Bien | Codifica por Intel QSV |
| `VideoHWDecode: 1` | Bien, en principio | Pide decodificación hardware |
| `VideoScaler: swscale` | Software | Este es el escalado por CPU |
| `UsesPictureFilters: true` | Sospechoso | Puede forzar partes por CPU |
| `SubtitleBurnBDSub: true` / `SubtitleBurnDVDSub: true` | Ojo | Si quema subtítulos, usa CPU |
| `PictureDeblockCustom` | Ojo, aunque preset esté `off` | Si activas deblock, será CPU |

Para maximizar hardware, deja el preset lo más limpio posible:

```json
"VideoEncoder": "qsv_h264",
"VideoHWDecode": 1,
"VideoScaler": "swscale",
"PictureDeinterlaceFilter": "off",
"PictureDenoiseFilter": "off",
"PictureDeblockPreset": "off",
"PictureSharpenFilter": "off",
"PictureChromaSmoothPreset": "off",
"SubtitleBurnBehavior": "none",
"SubtitleBurnBDSub": false,
"SubtitleBurnDVDSub": false
```

Sobre el scaler: si tu HandBrake no te ofrece otro escalador que `swscale` en la interfaz, entonces **no puedes forzar escalado QSV solo editando el JSON con seguridad**. El valor válido depende de la versión/build. La forma correcta de comprobarlo es crear desde la GUI un preset con el escalador hardware, exportarlo y ver qué valor pone en `VideoScaler`.

Para comprobar si el decode QSV está entrando de verdad, mira el **Registro de actividad** al iniciar una codificación. Debes buscar líneas tipo:

```text
qsv: is available
qsv decode
hardware decode
```

También puedes probar desde terminal:

```bash
flatpak run --command=HandBrakeCLI fr.handbrake.ghb --help
```

Y ver si aparece:

```text
--enable-hw-decoding qsv
```

Mi conclusión: tu problema principal no es el encoder, está bien. El scaler está en CPU porque tienes `"VideoScaler": "swscale"`, y HandBrake puede seguir usando CPU para filtros/subtítulos aunque el encode sea QSV. Para velocidad, quita filtros y no quemes subtítulos; para calidad, no me preocuparía demasiado por el scaler si solo haces recorte o mantienes 1080p.
---


En HandBrake **no hay un valor de `VideoScaler` para QSV/hardware** que puedas poner de forma fiable en el preset.

No uses:

```json
"VideoScaler": "qsv"
```

ni:

```json
"VideoScaler": "qsvscale"
```

Porque HandBrake no los documenta como valores válidos de preset. El valor que tienes:

```json
"VideoScaler": "swscale"
```

es software. En algunas versiones puede existir:

```json
"VideoScaler": "zimg"
```

pero también es CPU, solo mejor escalador/calidad.

Para hardware decode, lo correcto ya es esto:

```json
"VideoHWDecode": 1
```

Y en CLI sería:

```bash
--enable-hw-decoding qsv
```

HandBrake documenta `--enable-hw-decoding qsv`, pero no documenta un `VideoScaler` QSV equivalente; además indica que filtros/escalado/subtítulos pueden seguir usando CPU aunque el encoder sea QSV. [CLI HandBrake](https://handbrake.fr/docs/en/latest/cli/command-line-reference.html), [QSV HandBrake](https://handbrake.fr/docs/en/latest/technical/video-qsv.html)

Conclusión: en HandBrake, para tu preset, puedes acelerar **encode** con:

```json
"VideoEncoder": "qsv_h264"
```

y pedir **decode** con:

```json
"VideoHWDecode": 1
```

pero el **scaler por hardware no tiene parámetro JSON público**. Si necesitas decode + scale + encode todo en Intel GPU, eso ya sería mejor hacerlo con `ffmpeg` usando `scale_qsv`.
---


No: por ese log, **HandBrake sí está viendo bien tu gráfica integrada Intel y QSV funciona**.

Las líneas clave son estas:

```text
qsv: is available on this system
Intel Quick Sync Video support: yes
Intel Quick Sync Video integrated adapter with index 0 and renderD128
Decode support: h264 hevc (8bit: yes, 10bit: yes) av1 (8bit: yes, 10bit: yes)
H.264 encoder: yes
H.265 encoder: yes (8bit: yes, 10bit: yes)
```

Eso significa:

| Función | Estado |
|---|---|
| Intel QSV detectado | Sí |
| Decode HEVC 10-bit | Sí |
| Encode H.264 QSV | Sí |
| Encode H.265 QSV | Sí |
| Decode AV1 | Sí |
| Encode AV1 | No |

Lo de NVIDIA:

```text
Cannot load libnvidia-encode.so.1
```

no es problema si estás usando Intel. Solo dice que no hay NVENC disponible.

El punto malo está en otra parte: tu fuente es **HEVC Main10 HDR/Dolby Vision/HDR10+ 4K**:

```text
Video: hevc (Main 10), yuv420p10le, bt2020/smpte2084, 3840x1608
DOVI
hdr10+ dynamic metadata found
```

Si la conviertes a **H.264 QSV**, probablemente estás bajando a una ruta menos ideal para HDR/10-bit. Para esa fuente, mejor sería:

```text
H.265 10-bit QSV
```

si quieres conservar mejor HDR/10-bit. Si necesitas compatibilidad máxima con teles antiguas, entonces H.264 QSV vale, pero asume pérdida de HDR/metadata y peor compresión.

Sobre el decode: durante el escaneo solo dice:

```text
supported video decoders: avcodec qsv hwaccel
```

Eso indica que QSV está disponible, pero para confirmar que lo usa en la codificación tienes que mirar el log **después de pulsar Iniciar**, no solo el scan. Busca líneas como:

```text
qsv decode
sync: expecting
encqsvInit
```

Conclusión: **no tienes problema con la integrada ni con el encoder QSV**. Tu limitación real es que HandBrake no hace todo el pipeline en hardware: el encode sí, el decode puede que sí, pero escalado/filtros/tone mapping/subtítulos pueden ir por CPU. Para esa película concreta, yo usaría **H.265 QSV 10-bit**, no H.264 QSV.
---


**Qué Es**
HDR es “alto rango dinámico”: más brillo, más detalle en luces/sombras y normalmente color **BT.2020 + 10-bit**.  
SDR/BT.709 es el formato clásico de Blu-ray/TV normal: menos rango de brillo, colores estándar y normalmente **8-bit**.

Cuando pasas una película **HDR 10-bit** a **H.264 QSV**, muchas veces acabas en 8-bit. Si no conviertes bien el color, puede verse:

- lavada, como gris
- demasiado oscura
- con colores raros
- con brillo mal interpretado

**Cómo Configurarlo**
En HandBrake:

1. Abre la película.
2. Ve a la pestaña **Filtros**.
3. Busca **Espacio de color** o **Colorspace**.
4. Cambia de `Off` a:

```text
BT.709
```

Eso le dice a HandBrake: “convierte esta fuente HDR/BT.2020 a SDR/BT.709”. HandBrake documenta que el filtro **Colorspace** sirve para cambiar/tonemap a BT.709, y que si está en `Off` conserva el espacio de color original. [HandBrake Filters](https://handbrake.fr/docs/en/1.8.0/technical/filters-summary.html)

Para tu caso, el preset quedaría así:

```text
Video: H.264 QSV
QP: 21-22
Filtros > Colorspace/Espacio de color: BT.709
Dimensiones: 1920x804 aprox, no 1920x1080 forzado
Audio: AAC Stereo 320 kbps
DRC: 1.5-1.9
Gain: +2 dB
```

Lo bueno: se verá más normal en una TV sencilla, Apple TV, iPhone, Windows y Ubuntu. Es el camino más compatible.

Lo malo: pierdes HDR real y parte del color/gradación fina. Pero si tu TV es mala y priorizas que se vea bien y se oiga claro, **SDR/BT.709 + H.264 QSV** tiene bastante sentido.

Para comprobarlo rápido: codifica solo 2-3 minutos de una escena oscura y otra con luces fuertes. Si sin BT.709 se ve apagada y con BT.709 se ve natural, ya tienes el ajuste correcto.
---


La búsqueda no está mostrando un valor oficial tipo `qsvscale` o `qsv`; eso ya es una señal de que probablemente no existe como parámetro de preset público en HandBrake. Voy a contrastarlo con lo que sí documenta HandBrake para CLI/presets.

---
*Generado desde conversación con 33 mensajes.*
*General*
