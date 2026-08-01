---
title: Análisis de emulación y simulación
date: 2026-05-17
category: General
slug: analisis-de-emulacion-y-simulacion
tags: ['General']
---

# Análisis de emulación y simulación


> **Pregunta original:**
> 
Pues vamos con la opción 3 , no hay más apuntes. Ten en cuenta que soy un estudiante de segundo de grado y de redes se muy poco. 
> Prepra el documento
> Tengo este enunciado :
PEC - Redes Avanzadas
Se evaluará la capacidad del alumnado para diseñar, implementar y justificar soluciones de red reales,
así como su comprensión de tecnologías actuales y herramientas profesionales.
1. Modalidad de trabajo
• Entrega en formato: memoria técnica (PDF), evidencias prácticas (capturas, configuraciones,
etc.) y video defensa por cada bloque.
2. Estructura del trabajo
El trabajo se compone de cuatro bloques obligatorios, todos ellos relacionados entre sí, que el
alumnado deberá desarrollar de forma coordinada para mostrar una visión global de las redes
avanzadas de computadores.
Bloque 1 – Emulación vs Simulación (Análisis técnico) 2P
Objetivo
Comprender las diferencias entre herramientas de simulación y emulación de redes, analizando sus
ventajas, limitaciones y casos de uso.
Tareas
Tarea 1.1. Explicar qué es la simulación de red y qué es la emulación de red, destacando las diferencias
conceptuales y técnicas entre ambas.
Tarea 1.2. Comparar herramientas representativas de cada enfoque: Cisco Packet Tracer (simulación)
frente a GNS3 y EVE-NG (emulación).
Tarea 1.3. Analizar los siguientes aspectos para cada herramienta:
• Nivel de realismo.
• Uso de sistemas operativos reales.
• Limitaciones técnicas y de hardware.
• Casos de uso recomendados.
Tarea 1.4. Conclusión crítica: ¿en qué escenarios se recomienda cada una de las aproximaciones?
Justificar la respuesta con ejemplos concretos.

Adjunto los PDFS de los apuntes de la asignatura. Aún no estan todos los apuntes y puede que no se peuda resolver completamente el eneunciado. Analiza este punto y dime si necesitas algo más. Todas las respuestas tienen que estar referenciadas a los ficheros PDF
> 
> *...y 2 preguntas de seguimiento*


---


## Respuesta


Perfecto. En ese caso lo más razonable es hacer un trabajo técnicamente correcto apoyándonos en:

- los PDFs de la asignatura para el marco teórico,
- y documentación oficial externa para la parte comparativa específica de herramientas.

Además, siendo segundo de grado, conviene mantener un nivel:
- técnico,
- pero entendible,
- evitando exceso de jerga de administración enterprise.

Eso suele puntuar mejor que intentar aparentar un nivel experto artificial.

# Cómo plantearía el Bloque 1

## Estructura recomendada

### 1. Introducción
Explicar:
- qué son las redes simuladas,
- qué son las redes emuladas,
- por qué se usan en formación y entornos profesionales.

Aquí podemos apoyar conceptos generales de redes y enfoque práctico desde la UD1. fileciteturn0file3L6-L7

---

### 2. Simulación vs Emulación
Aquí definimos claramente:

| Simulación | Emulación |
|---|---|
| Imita comportamiento | Ejecuta sistemas reales |
| Más ligera | Más exigente |
| Menos realismo | Más realismo |
| Ideal aprendizaje | Ideal pruebas reales |

Y aquí introducimos:
- Packet Tracer → simulación
- GNS3 y EVE-NG → emulación

---

### 3. Comparativa de herramientas

## Cisco Packet Tracer
Enfoque:
- educativo,
- simple,
- poco consumo,
- ideal para CCNA y principiantes.

Puntos fuertes:
- fácil instalación,
- interfaz intuitiva,
- no necesita IOS reales.

Limitaciones:
- simulación parcial,
- comandos no completos,
- menos realismo.

---

## GNS3
Enfoque:
- profesional/laboratorio avanzado.

Puntos fuertes:
- usa imágenes reales Cisco/Linux,
- gran realismo,
- integración con VMware/Docker.

Limitaciones:
- más complejo,
- requiere más hardware,
- configuración difícil.

---

## EVE-NG
Enfoque:
- laboratorios enterprise centralizados.

Puntos fuertes:
- acceso web,
- múltiples fabricantes,
- muy usado en formación profesional.

Limitaciones:
- curva de aprendizaje,
- alto consumo RAM/CPU,
- despliegue más complejo.

---

### 4. Tabla comparativa
Muy importante para subir nota.

Ejemplo:

| Característica | Packet Tracer | GNS3 | EVE-NG |
|---|---|---|---|
| Tipo | Simulación | Emulación | Emulación |
| Realismo | Medio | Alto | Muy alto |
| IOS reales | No | Sí | Sí |
| Consumo hardware | Bajo | Medio/alto | Alto |
| Dificultad | Baja | Media | Alta |
| Uso recomendado | Aprendizaje | Laboratorios | Entornos enterprise |

---

### 5. Conclusión crítica
Aquí es donde normalmente se gana o se pierde nota.

La conclusión NO debe ser:
> “GNS3 es mejor”.

Debe ser contextual.

Ejemplo:
- Packet Tracer es mejor para aprender fundamentos.
- GNS3 es mejor para practicar configuraciones reales.
- EVE-NG es mejor para laboratorios complejos multiusuario.

Y justificar:
- recursos hardware,
- experiencia del usuario,
- objetivo del laboratorio.

---

# Cómo citaríamos

## Referencias internas (los PDFs)

Las usaríamos para:
- fundamentos de redes,
- enfoque práctico,
- dispositivos,
- IOS,
- administración de red,
- troubleshooting,
- arquitectura de red.

Ejemplos:
- fileciteturn0file3L6-L7
- fileciteturn0file1L4-L4
- fileciteturn0file0L3-L3

---

## Referencias externas
Usaremos:
- documentación oficial Cisco,
- documentación oficial GNS3,
- documentación oficial EVE-NG.

Eso además suele gustar porque demuestra iniciativa técnica.

---

# Mi recomendación

Para tu nivel actual:
- no intentes escribir como un ingeniero senior,
- escribe claro,
- compara conceptos,
- justifica decisiones.

En redes suele puntuar mucho:
- capacidad de razonamiento,
- no memorizar comandos.

Y este bloque concretamente es más conceptual que práctico.

El siguiente paso lógico sería que te prepare:
1. un índice académico completo,
2. las referencias bibliográficas,
3. y luego ya el texto redactado apartado por apartado.
---


Entendido. Para un trabajo de 4 bloques, el error habitual es hacer el Bloque 1 demasiado largo y descompensar el conjunto.

Para este bloque te recomiendo:

- 4–6 páginas máximo,
- redacción técnica pero compacta,
- una tabla comparativa fuerte,
- y una conclusión clara.

La parte importante aquí no es profundidad extrema, sino:
- demostrar que entiendes la diferencia entre simulación y emulación,
- y justificar cuándo usar cada herramienta.

# Estructura óptima (compacta)

## 1. Introducción (medio folio)
Muy breve:
- importancia de laboratorios en redes,
- necesidad de herramientas virtuales,
- aparición de simulación y emulación.

Apoyado en el enfoque práctico de la asignatura. fileciteturn0file3L6-L7

---

## 2. Simulación vs emulación (1 página)
Definir ambos conceptos.

Aquí debes dejar muy clara esta idea:

- Simulación:
  reproduce comportamientos de red de forma aproximada.

- Emulación:
  ejecuta sistemas operativos y configuraciones reales.

Con una mini tabla basta.

---

## 3. Comparativa de herramientas (2 páginas)

### Packet Tracer
Solo lo importante:
- simulador Cisco,
- ideal aprendizaje,
- poco consumo,
- menos realismo.

### GNS3
- emulación real,
- usa imágenes IOS,
- muy potente,
- más complejo.

### EVE-NG
- emulación avanzada,
- acceso web,
- orientado a laboratorios grandes,
- requiere más hardware.

---

## 4. Tabla comparativa (media página)
Esto tiene mucho valor visual y académico.

| Característica | Packet Tracer | GNS3 | EVE-NG |
|---|---|---|---|
| Tipo | Simulación | Emulación | Emulación |
| Realismo | Medio | Alto | Muy alto |
| IOS reales | No | Sí | Sí |
| Hardware necesario | Bajo | Medio | Alto |
| Dificultad | Baja | Media | Alta |
| Uso recomendado | Aprendizaje | Laboratorios reales | Entornos complejos |

---

## 5. Conclusión crítica (medio folio)
Muy importante que sea práctica.

Algo tipo:
- Packet Tracer es recomendable para estudiantes principiantes.
- GNS3 permite prácticas más realistas.
- EVE-NG resulta adecuado para escenarios empresariales complejos.

Y añadir:
> La elección depende del nivel técnico, recursos hardware y objetivos del laboratorio.

Eso suele cerrar muy bien.

---

# Qué evitar

## No hagas:
- historia extensa de Cisco,
- explicaciones muy profundas de virtualización,
- comandos,
- instalaciones paso a paso,
- comparativas kilométricas.

Porque aún quedan 3 bloques.

---

# Mi recomendación de reparto

| Bloque | Extensión recomendada |
|---|---|
| Bloque 1 | 4–6 páginas |
| Bloque 2 | 6–8 páginas |
| Bloque 3 | 6–8 páginas |
| Bloque 4 | 6–8 páginas |

Así el trabajo queda equilibrado.
---


No puedo conectarme directamente a tu Google Docs ni editar documentos externos desde aquí.

Sí puedo:
- redactarte el bloque completo,
- estructurarlo en formato académico,
- generar un `.docx` listo para subir a Google Docs,
- o crear un documento en canvas aquí para que luego copies/pegues.

La opción más práctica es:
1. te genero el texto ya formateado,
2. con títulos, tablas y referencias,
3. y luego lo subes a Google Docs en segundos.

También puedo prepararlo ya:
- en estilo APA básico,
- con bibliografía,
- y con citas integradas a los PDFs y fuentes oficiales.
---


He preparado el documento completo del Bloque 1 con:
- estructura académica,
- contenido compacto,
- tabla comparativa,
- referencias a los PDFs,
- y bibliografía externa mínima.

Tiene una extensión adecuada para ser solo el primero de los cuatro bloques.
---


Con los apuntes que has subido se puede cubrir parcialmente el Bloque 1, pero no de forma completa y sólida si quieres que toda la respuesta quede correctamente fundamentada y referenciada exclusivamente a los PDFs.

## Lo que sí aparece en los apuntes

He revisado especialmente la UD1 y la UD4.

### Contenido útil localizado

#### Emulación
En la UD1 aparece explícitamente un apartado llamado “Emuladores”. fileciteturn0file3L29-L30

Además, en la unidad se insiste en el enfoque práctico del networking y en la necesidad de trabajar con herramientas reales y laboratorios. fileciteturn0file3L6-L7

También hay referencias indirectas importantes:
- uso de IOS reales Cisco,
- configuraciones prácticas,
- troubleshooting,
- herramientas de análisis y monitorización,
- enfoque profesional de administración de red. fileciteturn0file1L4-L4 fileciteturn0file0L3-L3

#### Herramientas relacionadas
En UD4 aparecen:
- Wireshark,
- Nmap,
- Zenmap,
- herramientas de descubrimiento y gestión de red. fileciteturn0file0L4-L7

Esto puede servir para contextualizar laboratorios de emulación.

---

## Lo que NO veo suficientemente cubierto

El problema principal es que el enunciado pide una comparación técnica concreta entre:

- Cisco Packet Tracer
- GNS3
- EVE-NG

Y eso, por lo que aparece en los PDFs actuales, no está desarrollado de manera explícita.

Tampoco veo cubiertos de forma directa:
- definición formal de simulación vs emulación,
- diferencias conceptuales profundas,
- uso de imágenes/IOS reales,
- limitaciones de virtualización,
- requisitos hardware,
- comparativa técnica entre plataformas,
- escenarios profesionales concretos.

Es decir:
podemos inferir algunas cosas desde el contexto de la asignatura, pero no sería correcto académicamente “inventar” contenido y luego citar PDFs que realmente no lo sostienen.

---

# Qué necesitarías para hacerlo bien

## Opción recomendada

Necesitaría alguno de estos elementos:

### 1. Más apuntes de la asignatura
Especialmente si existe:
- una UD sobre virtualización,
- laboratorios,
- herramientas de networking,
- Packet Tracer,
- GNS3,
- SDN/laboratorios,
- virtualización de red.

Esta sería la mejor opción porque mantendrías coherencia total con la asignatura.

---

## Opción alternativa

### 2. Permitir usar bibliografía externa
Por ejemplo:
- documentación oficial Cisco,
- documentación oficial GNS3,
- documentación oficial EVE-NG,
- artículos técnicos.

En ese caso puedo:
- hacer el bloque completo,
- citar tanto PDFs como fuentes externas,
- separar claramente qué sale de la asignatura y qué es ampliación técnica.

---

# Riesgo si lo haces solo con estos PDFs

El trabajo podría quedar:
- demasiado genérico,
- poco técnico,
- o peor: con referencias forzadas que no justifican realmente lo afirmado.

Y en un bloque comparativo técnico eso suele penalizar bastante.

---

# Mi evaluación honesta del estado actual

| Apartado | ¿Cubierto con los PDFs? | Nivel |
|---|---|---|
| 1.1 Simulación vs emulación | Parcial | Bajo |
| 1.2 Packet Tracer vs GNS3 vs EVE-NG | No | Insuficiente |
| 1.3 Realismo / SO reales / hardware | Muy parcial | Bajo |
| 1.4 Conclusión crítica | Sí, parcialmente | Medio |

---

# Qué te recomiendo

La mejor estrategia sería:

1. Subir el resto de apuntes.
2. Verificar si existe una unidad de:
   - virtualización,
   - laboratorios,
   - herramientas,
   - prácticas Cisco.
3. Si no existe:
   - usar fuentes oficiales externas,
   - pero manteniendo referencias cruzadas con los PDFs.

Con eso sí se puede hacer un bloque muy sólido y defendible.

---
*Generado desde conversación con 10 mensajes.*
*General*
