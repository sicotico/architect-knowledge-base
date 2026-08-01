---
title: Arquitectura Azure VPN Terceros
date: 2025-03-17
category: Azure/Cloud
slug: arquitectura-azure-vpn-terceros
tags: ['Azure/Cloud', 'azure']
---

# Arquitectura Azure VPN Terceros


> **Pregunta original:**
> 
Es un diagram de arquitectura , en la parte izquierda está Azure y un blob storage por concesión, en el lado derecho son la NTTA , NCTA. y SAP. El diagrama muestra como se envía ficheros ente Azure y. los tres terceros.

Necesito que describas la imagen con las notas que te he pasado y que cada tercero tiene su propia VPN

---


## Respuesta


El diagrama representa la arquitectura de integración de archivos entre Azure y terceros externos (NTTA, NCTA y SAP) a través de diferentes VPN. 

### **Descripción General**
1. **Azure (Izquierda)**
   - Se muestran dos entornos: **vNet I77** y **DFW**.
   - Ambos entornos contienen:
     - **Blob Storage** con tres categorías: *Plate, TAG y REcon*.
     - **Extensiones** con CBO y OBO.
     - **Data Factory Integración**, que gestiona la transmisión de archivos.
     - **Blob Storage SFTP OBO**, utilizado para almacenar archivos enviados a terceros.
     - **Ficheros** generados en la integración: *transactionFile*, *image.zip* y *XTAG.file*.

2. **Terceros Externos (Derecha)**
   - **NTTA**: Se conecta mediante una **VPN** y recibe archivos a través de *SFTP NTTA*. Su aplicación (*App NTTA*) accede a los datos.
   - **NCTA**: También usa una **VPN** y recibe archivos mediante *SFTP NCTA*, accediendo a ellos a través de *App NCTA*.
   - **SAP**: Se conecta con **VPN Prisma** y recibe archivos desde Azure.

### **Flujo de Datos**
1. Los datos en Azure son almacenados en diferentes **blob storages** dentro de *vNet I77* y *DFW*.
2. **Data Factory Integración** procesa y genera los archivos relevantes (*transactionFile*, *image.zip* y *XTAG.file*).
3. Los archivos son depositados en *blob storage SFTP OBO* antes de ser enviados a los terceros.
4. Los terceros (**NTTA, NCTA y SAP**) reciben los archivos a través de sus respectivas VPNs.
5. Se intercambian respuestas, como *ACK*, para confirmar la recepción de los datos.

Este diagrama ilustra la comunicación segura entre Azure y los terceros mediante **VPNs dedicadas**, asegurando la transferencia estructurada de archivos.

---
*Generado desde conversación con 2 mensajes.*
*Azure/Cloud*
