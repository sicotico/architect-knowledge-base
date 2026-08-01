---
title: Testear velocidad NVMe USB-C
date: 2026-05-29
category: General
slug: testear-velocidad-nvme-usb-c
tags: ['General']
---

# Testear velocidad NVMe USB-C


> **Pregunta original:**
> 
Windows 11 y lo hice ayer para un stick usb de Amazon basics y sin problemas 
> Quiero hacer un WindowsToGo con rufus y esta carcasa con NVME y rufus no detecta el dispositivo 
> et-Disk | Format-List *

DiskNumber            : 1
PartitionStyle        : GPT
ProvisioningType      : Fixed
OperationalStatus     : Online
HealthStatus          : Healthy
BusType               : USB
UniqueIdFormat        : FCPH Name
OfflineReason         :
ObjectId              : {1}\\MSI\root/Microsoft/Windows/Storage/Providers_v2\WSP_Disk.ObjectId="{c7d59e7c-7470-11f0-840
                        d-806e6f6e6963}:DI:\\?\scsi#disk&ven_hiksemi&prod_md202#7&28ba6e78&0&000000#{53f56307-b6bf-11d0
                        -94f2-00a0c91efb8b}"
PassThroughClass      :
PassThroughIds        :
PassThroughNamespace  :
PassThroughServer     :
UniqueId              : 3001237923792379
AdapterSerialNumber   :
AllocatedSize         : 1024209543168
BootFromDisk          : False
FirmwareVersion       : 1.00
FriendlyName          : HIKSEMI MD202
Guid                  : {d0cb7857-5dec-4ce9-a341-b49cc3b6232c}

habia que marcar el check  de "Listar los disco duros USB"
> 
> *...y 8 preguntas de seguimiento*


---


## Respuesta


Perfecto. Entonces ya está identificado el problema.

El dato clave era:

```text
BusType : USB
ProvisioningType : Fixed
```

Tu SSD se presenta como un **disco duro USB fijo**, no como un pendrive extraíble. Por seguridad, Rufus lo ocultaba.

La opción:

```text
☑ Listar los discos duros USB
```

es precisamente para estos casos.

Tiene sentido que:
- El Amazon Basics apareciera directamente.
- El NVMe en la Essager no apareciera.

Rufus intenta evitar que alguien borre accidentalmente un disco externo de 1 TB lleno de datos.

## Respecto a Windows To Go

Con los resultados que has obtenido (~1 GB/s sostenidos), ese NVMe va a ofrecer una experiencia muy superior a la de un pendrive USB convencional:

| Medio | Rendimiento típico |
|---------|---------:|
| Pendrive USB normal | 30–150 MB/s |
| Pendrive rápido | 150–400 MB/s |
| Tu NVMe + Essager | ~900–1000 MB/s |

La diferencia al arrancar Windows, instalar actualizaciones o abrir aplicaciones es muy notable.

## Un detalle sobre Windows 11 To Go

Cuando Rufus detecte la ISO de Windows 11, debería ofrecerte varias opciones. Selecciona:

```text
Windows To Go
```

y no:

```text
Instalación estándar de Windows
```

porque generan estructuras de arranque distintas.

## Lo único que vigilaría

La Essager es un hub + carcasa, así que durante sesiones largas de Windows To Go:

- Comprueba que no se caliente excesivamente.
- Si notas reinicios o desconexiones, usa alimentación PD conectada al hub.
- Evita conectarla a través de otro hub USB adicional.

Pero viendo los benchmarks de 32 GiB, no hay indicios de problemas térmicos o de estabilidad.

En resumen: los tests confirman que la carcasa está rindiendo correctamente y el problema con Rufus era simplemente que estaba ocultando los discos duros USB. Ahora deberías poder crear el Windows To Go sin inconvenientes.
---


Ese resultado es incluso más informativo que el de 1 GiB.

## Comparación

| Test | 1 GiB | 32 GiB |
|--------|--------:|--------:|
| Lectura secuencial | 971 MB/s | 991 MB/s |
| Escritura secuencial | 1013 MB/s | 970 MB/s |
| Lectura Q1T1 | 853 MB/s | 841 MB/s |
| Escritura Q1T1 | 878 MB/s | 788 MB/s |

## Qué significa

La clave está en la escritura secuencial:

- A 1 GiB: **1013 MB/s**
- A 32 GiB: **970 MB/s**

La caída es de apenas un **4%**.

Eso indica que:
- El SSD no está agotando rápidamente la caché SLC.
- La carcasa no está sufriendo throttling térmico apreciable.
- La controladora USB-NVMe está trabajando correctamente.
- El rendimiento es estable en transferencias largas.

Si hubiese un problema de temperatura o de caché, verías cosas como:

- 1000 MB/s → 400 MB/s
- 1000 MB/s → 200 MB/s

al aumentar el tamaño del test.

## Conclusión sobre la carcasa

Para un portátil con USB 3.2 Gen 2 (10 Gbps):

**La carcasa está rindiendo prácticamente al máximo que permite la interfaz.**

No veo ningún indicio de:
- limitación por cable,
- limitación por hub,
- problema de firmware,
- problema térmico.

De hecho, muchos adaptadores USB-NVMe baratos se quedan en 700–850 MB/s incluso en condiciones ideales. Estar cerca de 1 GB/s en un test de 32 GiB es un resultado muy bueno.

## Lo único que me llama la atención

La unidad aparece como:

> E: 9% (90/954 GiB)

Eso sugiere un SSD de **1 TB**.

Si me dices el modelo exacto del NVMe (por ejemplo, Samsung 990 EVO, WD SN770, Crucial P3 Plus, Kingston NV2, etc.), podría decirte cuánto rendimiento estás dejando sobre la mesa por el límite USB.

Por ejemplo:
- Un Kingston NV2 de 1 TB suele dar ~3.000 MB/s internos.
- Un SN770 ~5.000 MB/s.
- Un 990 Pro ~7.000 MB/s.

Pero externamente todos ellos acabarían muy cerca de los ~1000 MB/s que estás viendo ahora. Por eso, desde el punto de vista del puerto USB de tu portátil, el conjunto parece estar aprovechado casi al 100 %.
---


Ya tenemos un dato muy relevante:

```text
Get-Disk
```

muestra:

```text
Disk 1  HIKSEMI MD202  953.87 GB  GPT
```

pero **no aparece como USB** ni como dispositivo extraíble en la salida que has pegado.

Además, en la captura de "Quitar hardware con seguridad" se ve:

```text
Expulsar MD202
 └─ HUB 1TB (E:)
```

Eso sugiere que la controladora de la Essager está presentando el SSD de una forma poco habitual para Rufus 4.11.

## Lo primero que probaría

En Rufus pulsa:

```text
Alt + L
```

No aparece en ningún menú. Es un atajo oculto que activa/desactiva la detección de discos locales USB.

Después cierra y vuelve a abrir Rufus.

---

## Segunda comprobación

Abre PowerShell:

```powershell
Get-Disk | Format-List *
```

y busca la línea:

```text
BusType :
```

para el disco HIKSEMI MD202.

Me interesa saber si pone:

- USB
- NVMe
- SATA
- RAID
- Unknown

---

## Tercera comprobación

La versión que estás usando es:

```text
Rufus 4.11.2285
```

que es bastante reciente.

Sin embargo, Rufus tiene mecanismos de protección para evitar que se sobrescriban discos externos grandes.

Ve a:

```text
Mostrar propiedades avanzadas de la unidad
```

y mira si aparece alguna opción relacionada con:

```text
Listar discos duros USB
```

o

```text
Show USB hard drives
```

---

## Si nada de eso funciona

Yo probaría una prueba definitiva:

1. Descargaría la utilidad oficial de Microsoft:

   urlMedia Creation Tool Windows 11https://www.microsoft.com/software-download/windows11

   o

2. Probaría con:

   urlVentoyhttps://www.ventoy.net/en/index.html

Si Ventoy tampoco ve el SSD, entonces el problema está en cómo la controladora del hub/carcasa presenta el dispositivo al sistema.

---

## Mi hipótesis principal

No creo que el SSD ni la carcasa estén defectuosos. Las pruebas de CrystalDiskMark son excelentes.

Sospecho que la **Essager 7 en 1 está exponiendo el NVMe mediante una controladora de hub USB que Rufus clasifica como no apta para escritura de arranque**, por lo que la oculta.

Prueba primero **Alt+L**. Es el caso más fácil de resolver y ha solucionado exactamente este síntoma muchas veces. Luego dime qué aparece en:

```powershell
Get-Disk | Format-List Number,FriendlyName,BusType
```

y podremos afinar mucho más.
---


Por los resultados que has obtenido, la conclusión práctica es que la carcasa está funcionando bien.

Sobre la **Essager 7 en 1**, las especificaciones comerciales indican:
- NVMe M.2 compatible.
- USB 3.2 Gen 2 a **10 Gbps**.
- PD 100W.
- HDMI 4K.
- Hub USB integrado. citeturn0search0turn0search2

Tus números:

| Test | Resultado |
|--------|---------:|
| Lectura secuencial | ~971 MB/s |
| Escritura secuencial | ~1013 MB/s |

son prácticamente el máximo real que suele verse en una conexión USB 3.2 Gen 2 de 10 Gbps. Eso significa que:
- La controladora NVMe↔USB está haciendo bien su trabajo.
- El cable no parece limitar a 5 Gbps.
- El portátil negocia correctamente a 10 Gbps.
- No hay una pérdida importante por el hecho de que sea además un hub. 

Lo que sí no puedo afirmar es qué controladora concreta lleva (Realtek RTL9210B, JMicron JMS583, etc.), porque Essager suele cambiar componentes entre revisiones sin cambiar el nombre comercial. Los fabricantes chinos hacen esto con bastante frecuencia.

Una prueba más exigente sería:

```text
CrystalDiskMark
32 GiB
3 pasadas
```

o copiar un archivo de 50–100 GB.

Si durante varios minutos sigue cerca de 800–1000 MB/s, entonces también disipa bien el calor y no está entrando en throttling térmico.

Mi valoración viendo únicamente:
- tu puerto USB,
- la velocidad obtenida,
- y el tipo de producto,

es que la carcasa está rindiendo como debería y no parece una de esas unidades problemáticas que se quedan en 400–500 MB/s o tienen cortes de rendimiento. citeturn0search2turn0search5

Si quieres identificar exactamente qué chip USB-NVMe monta, hay un método rápido desde Windows usando el Administrador de dispositivos o USBTreeView. Ahí sí podríamos saber si lleva una controladora considerada buena, mediocre o problemática.
---


Eso ocurre porque probablemente estás ejecutando `winsat` desde el cuadro **Ejecutar (Win+R)** o haciendo doble clic sobre algo. La ventana de consola se abre, ejecuta el comando y se cierra inmediatamente.

Hazlo así:

1. Abre **Terminal de Windows**, **PowerShell** o **Símbolo del sistema**.
   - Pulsa `Win + X` → **Terminal**.
2. Ejecuta:

```cmd
winsat disk -drive E
```

Al ejecutarlo dentro de una consola ya abierta, los resultados permanecerán visibles.

También puedes guardar la salida en un archivo:

```cmd
winsat disk -drive E > "%USERPROFILE%\Desktop\winsat.txt"
```

Luego abre `winsat.txt` desde el escritorio.

Dicho esto, para un SSD NVMe externo, **CrystalDiskMark es bastante más útil** que WinSAT. WinSAT fue diseñado principalmente para las evaluaciones de rendimiento de Windows y suele dar métricas menos detalladas.

Tus resultados de CrystalDiskMark (~970 MB/s lectura y ~1010 MB/s escritura) ya indican que:
- El puerto está funcionando a 10 Gbps.
- La carcasa está aprovechando prácticamente todo el ancho de banda disponible.
- No hay ningún problema evidente de rendimiento.

Si tienes curiosidad técnica, lo siguiente que comprobaría no es WinSAT sino el chip de la carcasa (por ejemplo ASM2362, RTL9210B, JMS583, etc.), porque eso permite evaluar la calidad de la carcasa más allá de la velocidad máxima. Si me dices la marca y modelo exactos, puedo comentarte qué tal está considerada esa controladora.
---


Con esa especificación:

**Type-C (USB 3.2 Gen 2 / DisplayPort / Power Delivery 3.0)**

el límite teórico del puerto es **10 Gbps**.

En la práctica, incluso con un NVMe muy rápido (3.000–7.000 MB/s internos), lo normal es obtener:

- **Lectura:** 850–1.050 MB/s
- **Escritura:** 800–1.000 MB/s

La cifra exacta depende de:
- La controladora USB-NVMe de la carcasa.
- La calidad del cable USB-C.
- El modelo de SSD.
- La temperatura (si entra en thermal throttling).

### Cómo interpretar CrystalDiskMark

Si ejecutas CrystalDiskMark y obtienes algo parecido a:

| Test | Resultado |
|--------|--------|
| Read SEQ | 950 MB/s |
| Write SEQ | 900 MB/s |

entonces el sistema está funcionando prácticamente al máximo para USB 3.2 Gen 2.

Si ves:

| Resultado | Posible causa |
|------------|--------------|
| ~450 MB/s | Conexión negociada a 5 Gbps |
| ~900–1.000 MB/s | Conexión correcta a 10 Gbps |
| <300 MB/s | Problema de cable, carcasa o puerto |
| Escritura empieza a 900 y cae a 200–300 MB/s | Caché SLC agotada o SSD calentándose |

### Comprueba también el cable

Un detalle frecuente es que:
- El puerto sea USB 10 Gbps.
- La carcasa soporte 10 Gbps.
- Pero el cable incluido sea solo USB 5 Gbps.

En ese caso CrystalDiskMark suele dar alrededor de **430–500 MB/s**.

### Qué velocidad no podrás alcanzar

Con ese portátil no podrás superar aproximadamente **1 GB/s**, aunque el SSD sea mucho más rápido, porque el puerto no es:
- USB 3.2 Gen 2x2 (20 Gbps)
- USB4
- Thunderbolt 3/4

Si haces el test con CrystalDiskMark y me pegas una captura o los números de lectura/escritura, puedo decirte si está rindiendo como debería o si hay algún cuello de botella.
---


"Sabrent de 1 TB" reduce un poco la incertidumbre, pero Sabrent tiene bastantes modelos distintos.

Algunos ejemplos:

- entity["brand","Sabrent","Storage brand"] Rocket Q → ~3.000 MB/s
- entity["brand","Sabrent","Storage brand"] Rocket PCIe 3.0 → ~3.400 MB/s
- entity["brand","Sabrent","Storage brand"] Rocket 4.0 → ~5.000 MB/s
- entity["brand","Sabrent","Storage brand"] Rocket 4 Plus → ~7.000 MB/s

Pero, independientemente de cuál sea, tu resultado de ~990 MB/s indica que:

```text
SSD interno  →  USB-NVMe bridge  →  USB 3.2 Gen2 (10 Gbps)  →  portátil
```

El cuello de botella es claramente el enlace USB, no el SSD.

## Una forma de verlo

Si tu SSD fuera capaz de 5.000 MB/s internamente:

- Interno: 5.000 MB/s
- Externo por USB 10 Gbps: ~1.000 MB/s

Estarías usando aproximadamente un 20% de la velocidad máxima del SSD, pero **el 100% de la velocidad disponible del puerto USB**.

## Lo importante

Tu prueba de 32 GiB ha descartado prácticamente todos los problemas habituales:

✅ Cable limitado a 5 Gbps  
✅ Carcasa defectuosa  
✅ Controladora USB lenta  
✅ Sobrecalentamiento inmediato  
✅ SSD muy lento

Por eso, si tu objetivo era comprobar si la compra de la Essager había salido bien, los números dicen que sí.

La única prueba adicional que haría por curiosidad sería copiar un archivo de 50–100 GB y observar la velocidad sostenida en el Administrador de tareas. Si durante varios minutos se mantiene por encima de 700–800 MB/s, ya no tendría ninguna preocupación sobre el conjunto SSD + carcasa.
---


Eso aporta una pista importante.

Si **ayer Rufus detectó un pendrive Amazon Basics** y hoy **no detecta el NVMe en la carcasa**, entonces el problema no es la ISO ni Rufus en general.

Las causas más probables son:

### 1. Rufus está ocultando los discos USB fijos

Los SSD externos suelen identificarse como **USB Fixed Disk**, mientras que muchos pendrives se presentan como dispositivos extraíbles.

En Rufus:

- Haz clic en **Mostrar propiedades avanzadas de unidad**.
- Activa **Listar discos duros USB** (o una opción de nombre similar, según la versión).

Es la causa más frecuente.

---

### 2. El hub integrado de la carcasa

Tu Essager 7 en 1 no es una carcasa USB simple; es un **hub USB con NVMe integrado**.

Algunas utilidades de creación de medios tienen problemas con determinados bridges USB-NVMe o hubs multifunción porque los filtran para evitar escribir sobre discos externos grandes.

Para comprobarlo:

- Abre **Administración de discos** (`diskmgmt.msc`).
- Localiza el NVMe.
- Anota el número de disco (Disco 1, Disco 2, etc.).

Después ejecuta en PowerShell:

```powershell id="u6ks2t"
Get-Disk
```

y mira si la columna `BusType` muestra:

```text id="fvw90s"
USB
```

---

### 3. El disco tiene particiones GPT existentes

A veces Rufus no se comporta igual con discos que ya tienen particiones.

Si no tienes nada que conservar:

```cmd id="a2m53n"
diskpart
list disk
select disk X
clean
exit
```

**Ojo:** esto borra completamente el SSD.

Después abre Rufus de nuevo.

---

### 4. Verificar si Rufus lo ve internamente

Pulsa **Alt+L** dentro de Rufus.

Ese atajo activa/desactiva la visualización de discos USB locales. Es una función poco conocida pero muy útil para casos como este.

---

### Mi sospecha principal

Dado que:

- CrystalDiskMark accede al disco perfectamente.
- Windows lo reconoce sin problemas.
- Es una carcasa/hub NVMe USB 10 Gbps.
- Rufus funciona con otros dispositivos.

Apostaría primero por **Alt+L** o por la opción **Listar discos duros USB**. Históricamente Rufus ha ocultado algunos discos USB externos para evitar que un usuario borre por accidente un disco de varios terabytes.

¿Qué versión de Rufus tienes (por ejemplo 4.7, 4.8, 4.9...)? Y cuando abres el desplegable **Dispositivo**, ¿aparece vacío o simplemente no aparece el SSD?
---


Sí. Esos resultados son exactamente los que esperaría de una **buena carcasa USB 3.2 Gen 2 (10 Gbps)**.

| Prueba | Resultado |
|----------|----------:|
| Lectura secuencial (Q8T1) | 971 MB/s |
| Escritura secuencial (Q8T1) | 1013 MB/s |
| Lectura secuencial (Q1T1) | 853 MB/s |
| Escritura secuencial (Q1T1) | 878 MB/s |

## Lo bueno

- Estás prácticamente **saturando el enlace USB de 10 Gbps**.
- La lectura de ~970 MB/s es muy cercana al máximo real alcanzable.
- La escritura de ~1 GB/s también es excelente.
- No hay indicios de que el cable esté limitando a 5 Gbps.
- No parece haber problemas de drivers ni de negociación del enlace.

## Lo malo o limitaciones

- No puedes saber solo con esta prueba si la carcasa sería buena a 20 Gbps o Thunderbolt; únicamente sabemos que a 10 Gbps rinde correctamente.
- El test es de **1 GiB**. Algunos SSD baratos mantienen 1 GB/s durante unos segundos y luego caen cuando se agota la caché.

## Una comprobación adicional interesante

Prueba CrystalDiskMark con:

- Tamaño: **32 GiB**
- 3 pasadas

o copia un archivo real de 50–100 GB.

Si la velocidad se mantiene cerca de 800–1000 MB/s durante toda la transferencia, entonces:
- El SSD es bueno.
- La carcasa disipa bien el calor.
- No hay throttling térmico importante.

## Conclusión

Para un portátil cuyo puerto es **USB 3.2 Gen 2 (10 Gbps)**, no parece que tengas nada que ganar cambiando de carcasa. Los ~970/1000 MB/s indican que ya estás muy cerca del límite práctico de la interfaz.

La única razón para buscar otra carcasa sería si en el futuro la conectaras a un equipo con **USB4, Thunderbolt 3/4 o USB 3.2 Gen 2x2 (20 Gbps)** y quisieras superar 1 GB/s. Con tu portátil actual, la carcasa no parece ser el cuello de botella.
---


Puedes medir la velocidad de un SSD NVMe en una carcasa USB-C de varias formas. Lo importante es distinguir entre:

- **Velocidad del SSD** (lo que puede dar el NVMe internamente).
- **Velocidad de la conexión USB** (a menudo es el cuello de botella).
- **Velocidad real de transferencia de archivos**.

## Opción 1: CrystalDiskMark (recomendada)

La herramienta más utilizada en Windows.

1. Descarga e instala urlCrystalDiskMarkhttps://crystalmark.info/en/software/crystaldiskmark/
2. Selecciona la unidad NVMe externa.
3. Deja la configuración por defecto.
4. Pulsa **All**.

Fíjate especialmente en:

- **SEQ1M Q8T1 Read/Write** → velocidad secuencial máxima.
- **SEQ1M Q1T1 Read/Write** → más representativa para uso cotidiano.

### Valores orientativos

| Conexión | Velocidad real típica |
|-----------|----------------------|
| USB 3.2 Gen 1 (5 Gbps) | 400–500 MB/s |
| USB 3.2 Gen 2 (10 Gbps) | 800–1.050 MB/s |
| USB 3.2 Gen 2x2 (20 Gbps) | 1.600–2.000 MB/s |
| Thunderbolt 3/4 | 2.500–3.500 MB/s |

Si tu NVMe es muy rápido pero ves ~950 MB/s, probablemente estás limitado por USB 10 Gbps.

---

## Opción 2: Comprobar qué velocidad negocia el USB

Windows no siempre lo muestra claramente, pero puedes usar:

- urlUSB Device Tree Viewer (USBTreeView)https://www.uwe-sieber.de/usbtreeview_e.html

Busca tu carcasa y revisa:

- **SuperSpeed (5 Gbps)**
- **SuperSpeedPlus (10 Gbps)**
- **20 Gbps**
- Thunderbolt/USB4

Esto ayuda a detectar si:
- El cable es el problema.
- El puerto es más lento de lo esperado.
- La carcasa está negociando a una velocidad inferior.

---

## Opción 3: Test real copiando archivos

1. Copia un archivo grande (20–50 GB).
2. Observa la velocidad sostenida en el Explorador o en el Administrador de tareas.

Si durante toda la copia se mantiene cerca de:
- 450 MB/s → USB 5 Gbps.
- 900–1.000 MB/s → USB 10 Gbps.
- 1.800 MB/s → USB 20 Gbps.

es una buena señal de que el conjunto funciona correctamente.

---

## Opción 4: Desde PowerShell

Si prefieres herramientas integradas:

```powershell
winsat disk -drive E
```

(cambiando `E` por la letra de tu unidad).

No es tan preciso como CrystalDiskMark, pero sirve para una comprobación rápida.

## Si me dices:

- Modelo exacto del NVMe.
- Modelo de la carcasa USB-C.
- Si el puerto es USB-C, USB4 o Thunderbolt.

Puedo decirte cuál debería ser aproximadamente la velocidad máxima esperable y ayudarte a interpretar los resultados.
---


Eso no es normal. Rufus suele detectar sin problemas los SSD externos USB, incluidos los NVMe en carcasa.

Vamos a aislar el problema.

## 1. ¿Windows ve el disco como unidad USB?

Abre PowerShell y ejecuta:

```powershell id="4h5m0f"
Get-Disk
```

o

```powershell id="08khij"
diskpart
list disk
```

Deberías ver algo parecido a:

```text id="3y5x4z"
Disk 0  512 GB  SSD interno
Disk 1  954 GB  USB
```

¿El NVMe aparece ahí?

---

## 2. ¿Qué versión de Rufus estás usando?

Las versiones recientes de Rufus detectan mejor discos USB externos.

Comprueba que sea la última:

urlRufus oficialhttps://rufus.ie/

---

## 3. Comprueba el filtro de dispositivos USB

En Rufus hay una opción que mucha gente pasa por alto.

Pulsa:

**Mostrar propiedades avanzadas de unidad**

y busca algo similar a:

```text id="nvy6mo"
Listar discos duros USB
```

o

```text id="9wmphq"
Show advanced drive properties
```

Las versiones modernas suelen ocultar los discos USB externos para evitar borrados accidentales.

---

## 4. ¿La carcasa se presenta como "Fixed Disk"?

Algunas controladoras USB-NVMe anuncian el disco como disco fijo en lugar de disco extraíble.

Rufus normalmente lo soporta, pero algunas combinaciones de firmware pueden dar problemas.

Puedes comprobarlo con:

```powershell id="a3mwko"
Get-PhysicalDisk
```

y decirme qué aparece para el NVMe.

---

## 5. ¿Qué tipo de imagen intentas grabar?

Windows To Go no aparece para cualquier ISO.

Por ejemplo:

- Windows 10 → suele funcionar.
- Windows 11 → depende de la versión de Rufus y de la ISO.
- ISOs modificadas → a veces Rufus no ofrece la opción.

---

## 6. Prueba esto

Abre Rufus como administrador.

En la esquina inferior izquierda debería haber un pequeño icono o menú relacionado con los discos USB. Activa la opción para mostrar discos USB y vuelve a abrir el desplegable de dispositivos.

---

Necesito saber dos cosas:

1. ¿El SSD aparece en **Administración de discos** (`diskmgmt.msc`)?
2. ¿En Rufus el desplegable de **Dispositivo** está vacío o solo muestra el disco interno?

Con eso normalmente se identifica el problema en un par de pasos.

---
*Generado desde conversación con 22 mensajes.*
*General*
