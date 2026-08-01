---
title: Costo copia ADF Azure
date: 2025-05-23
category: Azure/Cloud
slug: costo-copia-adf-azure
tags: ['Azure/Cloud', 'azure']
---

# Costo copia ADF Azure


> **Pregunta original:**
> 
Necesito calcular el coste de copiar un Azure Data Lake en East US a un blob storage en East Us 2. La idea es utiliza Azure Data Factory con la operación de copia de ficheros. Hay que diferenciar la copia inicia de 3 TB y separarla del coste de copia incremental de 1 GB/día
> En el resumen final desglosa el coste entre regiones
> Dame las tarifas de Azure para la copia de datos entre las regiones East US e East US 2
> 
> *...y 1 preguntas de seguimiento*


---


## Respuesta


Sí, **Azure Data Factory (ADF)** permite detectar y copiar únicamente los archivos que han cambiado desde la última ejecución, utilizando la propiedad **LastModifiedDate** de los archivos.

### 🔍 ¿Cómo funciona?

ADF puede filtrar archivos basándose en su fecha de última modificación. Esto se logra configurando los parámetros `modifiedDatetimeStart` y `modifiedDatetimeEnd` en el conjunto de datos de origen. De esta manera, solo se copian los archivos que han sido modificados dentro del rango de tiempo especificado.

### ⚙️ Configuración en ADF

1. **Definir parámetros de tiempo:**
   - `modifiedDatetimeStart`: Fecha y hora de la última ejecución exitosa.
   - `modifiedDatetimeEnd`: Fecha y hora actuales.

2. **Utilizar estos parámetros en el conjunto de datos de origen:**
   ```json
   {
     "modifiedDatetimeStart": "@pipeline().parameters.modifiedDatetimeStart",
     "modifiedDatetimeEnd": "@pipeline().parameters.modifiedDatetimeEnd"
   }
   ```


3. **Automatizar con triggers:**
   Puedes emplear un trigger de tipo *Tumbling Window* para ejecutar el pipeline a intervalos regulares, pasando automáticamente los valores de `windowStartTime` y `windowEndTime` como parámetros. citeturn0search9

### 📌 Consideraciones importantes

- **Zona horaria:** Asegúrate de que las fechas y horas estén en formato UTC, ya que ADF utiliza esta zona horaria por defecto. citeturn0search4

- **Volumen de archivos:** Si tienes una gran cantidad de archivos, el proceso de escaneo puede ser costoso en términos de tiempo y recursos. Es recomendable estructurar los datos en carpetas particionadas por fecha para optimizar el rendimiento. citeturn0search1

- **Almacenamiento del estado:** Para mantener un registro de la última ejecución, puedes almacenar la fecha y hora en una tabla de control o utilizar las variables del trigger.

### 🧪 Ejemplo práctico

Supongamos que deseas copiar diariamente los archivos modificados en las últimas 24 horas. Puedes configurar un trigger diario que pase los siguientes parámetros:

- `modifiedDatetimeStart`: `@addDays(utcnow(), -1)`
- `modifiedDatetimeEnd`: `@utcnow()`

Esto asegurará que solo se copien los archivos modificados en el último día.

Si necesitas asistencia para configurar este proceso o adaptar la solución a tus necesidades específicas, no dudes en preguntar.
---


Las tarifas de transferencia de datos entre las regiones **East US** y **East US 2** en Azure se clasifican como **transferencias interregionales dentro del mismo continente**. Según la información más reciente disponible, el coste estimado es de **$0.02 por GB** para transferencias entre regiones dentro de Norteamérica citeturn0search4.

### 📌 Resumen de tarifas relevantes:

- **Transferencia de datos entre regiones en EE. UU. (por ejemplo, de East US a East US 2):** $0.02 por GB
- **Transferencia de datos entre zonas de disponibilidad dentro de la misma región:** Sin coste citeturn0search0
- **Transferencia de datos dentro de la misma región:** Sin coste

Es importante destacar que, aunque **East US** y **East US 2** están geográficamente cercanas, Azure las considera regiones distintas, por lo que se aplican tarifas de transferencia interregional.

### 💡 Consideraciones adicionales:

- **Transferencia de datos entrante (ingress):** Gratuita en todas las regiones de Azure.
- **Transferencia de datos saliente (egress):** Se cobra según las tarifas mencionadas anteriormente.

Si necesitas asistencia adicional para calcular los costes totales de transferencia o para optimizar tu arquitectura en Azure, no dudes en preguntar.
---


Para calcular el coste de copiar datos desde un **Azure Data Lake en East US** hacia un **Blob Storage en East US 2** usando **Azure Data Factory (ADF)**, debemos considerar dos tipos de costes principales:

---

### 🔹 1. **Coste de la operación de copia con ADF**
ADF cobra principalmente por:
- **Actividad de copia por hora de ejecución**
- **Lectura y escritura de datos (por GB copiado)**

### 🔹 2. **Coste de salida de datos (data egress)**
Aunque ambos están en la misma región geográfica general (ambos en la costa este de EE. UU.), **East US ≠ East US 2**, por lo que **sí aplica coste de salida**.

---

## 🧮 Cálculo: Copia Inicial (3 TB)

### A. **Coste de Azure Data Factory (actividad de copia)**
- **Suposiciones**: 
  - Usamos integración administrada (self-hosted no aplica).
  - Transferencia entre regiones.
  - Solo se cobra por volumen y no por transformación.

**Precios estimados (2024):**
- **Copia de datos entre regiones**: ~$0.25 por GB

**Costo total por 3 TB (3,072 GB):**
```
3,072 GB × $0.25 = $768
```

### B. **Coste de salida de datos (Data Lake → Blob en otra región)**
- **Data egress entre regiones de Azure**: ~$0.02 por GB (según tabla de salida inter-región)

**Costo total:**
```
3,072 GB × $0.02 = $61.44
```

---

### 🔸 **Total copia inicial (3 TB):**
```
ADF (operación):     $768.00
Data egress:         $61.44
-------------------------------
Total:               $829.44 (estimado)
```

---

## 📅 Cálculo: Copia incremental diaria (1 GB/día)

### A. Azure Data Factory
```
1 GB × $0.25 = $0.25 / día
```

### B. Data egress
```
1 GB × $0.02 = $0.02 / día
```

---

### 🔸 **Total diario:**
```
ADF + egress = $0.25 + $0.02 = $0.27 / día
```

### 🔸 **Total mensual (30 días):**
```
$0.27 × 30 = $8.10 / mes
```

---

## ✅ Resumen Final

| Tipo de copia       | Volumen | Costo ADF | Costo egress | Total    |
|---------------------|---------|-----------|---------------|----------|
| Copia inicial       | 3 TB    | $768      | $61.44        | **$829.44** |
| Copia incremental   | 1 GB/d  | $0.25/d   | $0.02/d       | **$0.27/d** / **$8.10/mes** |

---

¿Quieres que te prepare una hoja Excel o una tabla editable para simular diferentes volúmenes o frecuencias?
---


Perfecto, aquí tienes el **resumen final actualizado** con un desglose más claro del coste **entre regiones**, separando los componentes:

---

## ✅ Resumen Final con Desglose por Coste entre Regiones

| Tipo de Copia       | Volumen | **ADF (actividad de copia)** | **Costo de transferencia entre regiones (data egress)** | **Total** |
|---------------------|---------|------------------------------|----------------------------------------------------------|-----------|
| **Copia inicial**   | 3 TB    | $768.00                      | $61.44                                                   | **$829.44** |
| **Copia incremental diaria** | 1 GB/día | $0.25/día                     | $0.02/día                                                | **$0.27/día** |
| **Copia incremental mensual** (30 días) | 30 GB   | $7.50                       | $0.60                                                    | **$8.10/mes** |

---

### 🧾 Detalles:

- **ADF (actividad de copia)**: Cobro por ejecutar la actividad de copia en Azure Data Factory, incluyendo lectura desde Data Lake y escritura en Blob Storage, con transferencia entre regiones.
- **Transferencia entre regiones (data egress)**: Azure cobra por mover datos entre regiones (East US → East US 2), incluso si son cercanas.

---

¿Te gustaría que lo convierta en un archivo Excel con fórmulas para que puedas ajustar volúmenes y precios manualmente?

---
*Generado desde conversación con 8 mensajes.*
*Azure/Cloud*
