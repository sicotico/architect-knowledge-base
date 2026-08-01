---
title: Explicación plano de red
date: 2026-06-12
category: General
slug: explicacion-plano-de-red
tags: ['General']
---

# Explicación plano de red


> **Pregunta original:**
> 
Es un plano de red profesional  , puedes darme una breve explicación  con la justificación técnica , muy escueta ya que soy un estudiante universitario
> Mejor justificalo usando estos apuntes 

---


## Respuesta


Sí. Una explicación breve con justificación técnica podría ser:

> Este diseño distribuye **7 puntos de acceso (APs)** de forma estratégica para cubrir una oficina de **32 × 18 m**, separando las zonas según su densidad de usuarios (recepción, oficinas, salas de reuniones, laboratorio y área abierta). En la banda de **2,4 GHz** se reutilizan únicamente los canales **1, 6 y 11**, evitando interferencias entre APs cercanos. En **5 GHz** se asignan canales diferentes a cada AP para reducir la co-canalización y aumentar la capacidad de la red. Los APs están conectados mediante **cableado Cat6 y switch PoE**, lo que simplifica la alimentación eléctrica y mejora la fiabilidad. La potencia de transmisión se mantiene moderada para minimizar solapamientos excesivos y favorecer el roaming entre APs. El objetivo es garantizar una cobertura uniforme, buena capacidad para múltiples usuarios y un nivel de señal cercano a **−67 dBm**, adecuado para aplicaciones de datos y voz sobre Wi-Fi.

### Justificación técnica resumida
- **Cobertura:** APs ubicados en el centro de cada zona de uso.
- **Interferencias:** canales 1, 6 y 11 en 2,4 GHz; canales separados en 5 GHz.
- **Capacidad:** más APs en áreas con mayor concentración de usuarios.
- **Disponibilidad:** uso de PoE y cableado estructurado Cat6.
- **Movilidad:** solapamiento controlado para permitir roaming eficiente.

Para un trabajo universitario, con ese párrafo y los 5 puntos anteriores suele ser suficiente.
---


Puedes justificarlo utilizando conceptos de las unidades de **Redes Inalámbricas**, **Switches** y **Gestión de Redes**:

> El diseño propuesto distribuye siete puntos de acceso (AP) en función de las distintas zonas de trabajo y su densidad de usuarios, garantizando que cada host inalámbrico disponga de cobertura adecuada a través de una estación base, que es el elemento encargado de proporcionar conectividad a la red cableada y coordinar las comunicaciones inalámbricas. fileciteturn0file4
>
> Para minimizar interferencias, en la banda de 2,4 GHz se utilizan los canales no solapados 1, 6 y 11, mientras que en 5 GHz se asignan canales diferentes a cada AP. Esta planificación mejora el rendimiento global de la WLAN y reduce la contención del medio compartido propia del estándar IEEE 802.11. Además, se mantiene un solapamiento controlado entre celdas de cobertura para facilitar el proceso de roaming cuando los usuarios se desplazan entre zonas de la oficina. fileciteturn0file4
>
> Los AP se conectan mediante cableado Cat6 a un switch PoE central, permitiendo transportar simultáneamente datos y alimentación eléctrica por el mismo enlace. El uso de switches PoE simplifica la instalación, reduce costes de despliegue y facilita la gestión de la infraestructura de acceso. fileciteturn0file1
>
> Finalmente, la arquitectura sigue principios de diseño de red como la simplicidad, la escalabilidad y la interoperabilidad, buscando una cobertura homogénea, facilidad de administración y capacidad de crecimiento futuro sin afectar al funcionamiento general de la red. fileciteturn0file0

### Versión muy corta (para memoria o exposición)

> La red WiFi se ha diseñado mediante la distribución estratégica de 7 puntos de acceso para garantizar cobertura uniforme y capacidad suficiente en todas las áreas de la oficina. Se emplean canales no solapados en 2,4 GHz y canales diferenciados en 5 GHz para reducir interferencias, además de un solapamiento controlado que favorece el roaming. Los AP se conectan mediante Cat6 a un switch PoE, simplificando la alimentación y la gestión de la infraestructura. El diseño sigue criterios de escalabilidad, interoperabilidad y eficiencia propios de una red empresarial. fileciteturn0file4 fileciteturn0file1 fileciteturn0file0

---
*Generado desde conversación con 4 mensajes.*
*General*
