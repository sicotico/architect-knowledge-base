---
title: Integración Azure Private Link
date: 2025-01-21
category: Azure/Cloud
slug: integracion-azure-private-link
tags: ['Azure/Cloud', 'azure']
---

# Integración Azure Private Link


> **Pregunta original:**
> 
Hola, ere sun especialista en cloud de Azure. Estas generado una documentacion técnica. Tienes que describir una integracionistas desde una plataforma externa. A un storage account de azure con private link que están en diferentes tenaz. Esto requiere el uso de DNS externo, en este caso en OnPrem en Miami, guarda registro tipo A para cada recursos y con FQDN diferente. 

---


## Respuesta


Aquí tienes una descripción técnica detallada para documentar la integración de una plataforma externa con un Azure Storage Account configurado con Private Link, utilizando un DNS externo alojado OnPrem en Miami:

---

## **Integración de Plataforma Externa con Azure Storage Account mediante Private Link y DNS Externo**

### **Contexto del Escenario**
Se requiere la integración entre una plataforma externa ubicada en un entorno fuera de Azure y un **Storage Account** de Azure que utiliza **Azure Private Link**. Ambas entidades residen en diferentes tenants de Azure. Para facilitar la conectividad, se implementa un servicio de DNS externo en las instalaciones OnPrem de Miami que almacena registros A específicos para la resolución de nombres.

---

### **Arquitectura de la Solución**

#### **1. Configuración del Azure Storage Account**
- **Storage Account** configurado en Azure, habilitado con **Private Endpoint**.
- **Private Link** utilizado para exponer el recurso de almacenamiento de forma segura dentro de la red virtual (VNet) de Azure.
- El **Private Endpoint** asigna una dirección IP privada dentro de la subred específica de la VNet asociada.

#### **2. Entorno Externo**
- Plataforma externa que necesita acceder al Storage Account para lectura/escritura de datos.
- La plataforma no tiene acceso directo al espacio de nombres público del Storage Account debido a la configuración de Private Link.

---

### **Configuración de DNS y Resolución de Nombres**

#### **1. DNS Externo en OnPrem (Miami)**
- Se configura un servidor DNS externo en las instalaciones OnPrem de Miami.
- El servidor DNS aloja **registros tipo A** para la resolución de los FQDN específicos del Storage Account.

#### **2. Uso de FQDN Únicos**
Cada recurso asociado al Storage Account utiliza un **Fully Qualified Domain Name (FQDN)** diferente. Esto asegura una separación clara entre servicios y facilita la resolución DNS. Por ejemplo:
  - **Blob Service**: `storageaccountname.blob.private.mydomain.com`
  - **File Service**: `storageaccountname.file.private.mydomain.com`
  - **Queue Service**: `storageaccountname.queue.private.mydomain.com`
  - **Table Service**: `storageaccountname.table.private.mydomain.com`

#### **3. Configuración del Registro A**
Para cada FQDN, se crea un registro A que apunta a la dirección IP privada del Private Endpoint en la VNet de Azure. Por ejemplo:
- `storageaccountname.blob.private.mydomain.com -> 10.0.0.5`
- `storageaccountname.file.private.mydomain.com -> 10.0.0.6`

#### **4. Configuración en la Plataforma Externa**
- La plataforma externa utiliza el FQDN configurado en el DNS externo para interactuar con los servicios del Storage Account.
- Se asegura que las consultas DNS de la plataforma estén configuradas para resolver mediante el servidor DNS en Miami.

---

### **Pasos de Implementación**

1. **Configuración del Private Endpoint en Azure:**
   - Crear un Private Endpoint para cada servicio del Storage Account.
   - Asignar las direcciones IP privadas a través de la VNet.
   - Confirmar conectividad dentro de la VNet mediante herramientas como `nslookup` o `ping`.

2. **Configuración del DNS Externo:**
   - Crear registros A en el servidor DNS OnPrem en Miami para cada FQDN.
   - Validar que las resoluciones DNS devuelvan las IPs privadas correctas.

3. **Configuración en la Plataforma Externa:**
   - Configurar el cliente para usar el FQDN al realizar solicitudes hacia el Storage Account.
   - Validar la conectividad a nivel de aplicación.

4. **Pruebas de Conectividad:**
   - Verificar que las solicitudes desde la plataforma externa se resuelvan correctamente mediante el DNS OnPrem.
   - Confirmar que las transacciones (lectura, escritura) funcionan como se espera.

---

### **Consideraciones de Seguridad**
- **Restricción de acceso:** Asegurarse de que solo las direcciones IP permitidas de la plataforma externa puedan acceder al Private Endpoint mediante NSGs y configuraciones de firewall.
- **Cifrado:** Todo el tráfico hacia el Storage Account debe estar cifrado (por ejemplo, usando HTTPS).
- **Auditoría:** Habilitar diagnósticos en el Storage Account para monitorear el tráfico y posibles accesos no autorizados.

---

### **Beneficios de la Solución**
1. **Aislamiento:** Private Link asegura que el Storage Account no esté expuesto públicamente.
2. **Control:** El uso de DNS externo proporciona control sobre la resolución de nombres.
3. **Seguridad:** Todo el tráfico permanece dentro de redes privadas, minimizando riesgos.

---

Si necesitas más detalles o agregar diagramas técnicos, indícalo y lo adaptamos según sea necesario.

---
*Generado desde conversación con 2 mensajes.*
*Azure/Cloud*
