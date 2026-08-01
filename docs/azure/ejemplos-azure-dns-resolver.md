---
title: Ejemplos Azure DNS Resolver
date: 2025-03-04
category: Azure/Cloud
slug: ejemplos-azure-dns-resolver
tags: ['Azure/Cloud', 'azure']
---

# Ejemplos Azure DNS Resolver


> **Pregunta original:**
> 
Buenos días, eres un arquitecto de azure y acaba de recibir una plataforma que tiene el servicio de Azure DNS Resolver. Necesito ejemplos de uso de DNS Resolver con explicaciones sencillas
> Como conecta esto con el vnet-link

---


## Respuesta


El **Azure DNS Private Resolver** se integra con las **zonas DNS privadas** de Azure para facilitar la resolución de nombres de dominio en redes virtuales (VNets). Para que las máquinas virtuales (VMs) y otros recursos dentro de una VNet puedan resolver nombres definidos en una zona DNS privada, es necesario establecer un **vínculo de red virtual** (vnet-link) entre la zona DNS privada y la VNet correspondiente.

**¿Cómo funciona el vnet-link en este contexto?**

1. **Asociación de la zona DNS privada a la VNet**: Al crear una zona DNS privada, puedes vincularla a una o más VNets mediante vnet-links. Este vínculo permite que las VMs dentro de esas VNets resuelvan nombres de dominio definidos en la zona DNS privada.

2. **Autoregistro de registros DNS**: Al habilitar la opción de autoregistro durante la creación del vnet-link, las VMs que se desplieguen en la VNet vinculada registrarán automáticamente sus nombres e IPs en la zona DNS privada. Esto simplifica la gestión de registros DNS en entornos dinámicos.

3. **Resolución de nombres**: Una vez establecido el vnet-link, las VMs dentro de la VNet pueden resolver nombres de dominio definidos en la zona DNS privada sin necesidad de configuraciones DNS adicionales.

**Ejemplo práctico**:

- Supongamos que tienes una zona DNS privada llamada `privada.contoso.com` y dos VNets: `VNet-A` y `VNet-B`.

- Si creas un vnet-link entre `privada.contoso.com` y `VNet-A`, las VMs dentro de `VNet-A` podrán resolver nombres como `servidor1.privada.contoso.com`.

- Si también deseas que las VMs en `VNet-B` resuelvan estos nombres, deberás crear un vnet-link adicional entre `privada.contoso.com` y `VNet-B`.

Para una guía paso a paso sobre cómo crear y asociar una zona DNS privada a una red virtual utilizando vnet-links, puedes consultar el siguiente tutorial en video:

videoAzure Private DNS Zone Virtual Network Link Tutorialturn0search7
---


Buenos días. El servicio **Azure DNS Private Resolver** facilita la resolución de nombres de dominio (DNS) en entornos híbridos, permitiendo que las cargas de trabajo tanto locales como en Azure resuelvan nombres de dominio privados sin necesidad de configurar y mantener servidores DNS personalizados.

A continuación, se presentan algunos ejemplos de uso de Azure DNS Private Resolver:

1. **Resolución de nombres de Azure desde entornos locales**: Tradicionalmente, para resolver nombres de servicios de Azure desde una red local, era necesario implementar servidores DNS reenviadores personalizados. Con Azure DNS Private Resolver, se pueden configurar puntos de conexión entrantes que permiten a los servidores DNS locales reenviar consultas directamente al resolver de Azure, simplificando la arquitectura y reduciendo la necesidad de mantenimiento adicional. citeturn0search0

2. **Resolución de nombres locales desde Azure**: De manera similar, las cargas de trabajo en Azure pueden necesitar resolver nombres de dominio de servicios alojados en entornos locales. Mediante la configuración de puntos de conexión salientes y conjuntos de reglas de reenvío en Azure DNS Private Resolver, es posible dirigir las consultas DNS desde Azure hacia los servidores DNS locales correspondientes, facilitando una integración más fluida entre ambos entornos. citeturn0search0

3. **Simplificación de la gestión DNS en entornos híbridos**: Al eliminar la necesidad de mantener servidores DNS personalizados, Azure DNS Private Resolver ofrece una solución totalmente administrada con alta disponibilidad y redundancia integrada. Esto no solo reduce los costos operativos, sino que también mejora la eficiencia y confiabilidad de la resolución de nombres en entornos híbridos. citeturn0search0

Para una explicación más detallada y visual sobre cómo funciona Azure DNS, puedes consultar el siguiente video:

videoDNS en Azure - Aprende Azure - ¡Fácil y Rápido!turn0search2

---
*Generado desde conversación con 4 mensajes.*
*Azure/Cloud*
