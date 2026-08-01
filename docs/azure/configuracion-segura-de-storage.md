---
title: Configuración segura de Storage
date: 2024-12-16
category: Azure/Cloud
slug: configuracion-segura-de-storage
tags: ['Azure/Cloud', 'azure']
---

# Configuración segura de Storage


> **Pregunta original:**
> 
Redactalo para incluirlo en un documento técnico 
> Ere sun arquitecto especialista en Azure. y teniendo encuesta el WAF y CAF necesito una definición de la mejor forma de configurar un Azure Storage account. El enfóquele necesita cumplir las normas de seguridad de uso exclusivo de private endpoint, solicitar el ciclo de vida al proveedor para el mismo , obligandomela a tener uno. No soporta web estática y para el caso de sFTP se utilizar un usuario local del Azure Storage Account.

¿Que puntos abordarías y como?
> El punto 1 de seguido colocado antes de del punto 4
> 
> *...y 1 preguntas de seguimiento*


---


## Respuesta


Aquí tienes el contenido redactado para incluir en un documento técnico:

---

## **Configuración de Azure Storage Account Cumpliendo WAF y CAF**

Este documento describe la configuración recomendada para una **Azure Storage Account** siguiendo las mejores prácticas establecidas en el **Well-Architected Framework (WAF)** y el **Cloud Adoption Framework (CAF)**, ajustándose a los requisitos específicos de seguridad y operación, incluyendo el uso exclusivo de Private Endpoints, configuración de ciclo de vida obligatorio, y soporte para sFTP mediante usuarios locales.

---

### **1. Configuración de Seguridad**
Para garantizar la seguridad de los datos y el cumplimiento de las normas del WAF y CAF, se deben implementar las siguientes medidas:

1. **Uso exclusivo de Private Endpoint:**
   - Configurar un **Private Endpoint** asociado a subrecursos específicos (`blob`, `file`, `queue`, o `table`) para garantizar que todo el tráfico pase por la red privada.
   - Deshabilitar el acceso público configurando el parámetro **Public Network Access** en `Disabled`.
   - Asegurar que la resolución de nombres para el Private Endpoint se administre mediante una **Azure Private DNS Zone**.
   - Aplicar políticas de Azure Policy para forzar el uso de Private Endpoints en todas las cuentas de almacenamiento.

2. **Bloqueo de acceso público:**
   - Asegurarse de que todas las configuraciones públicas estén deshabilitadas mediante reglas de firewall (`Deny All`) y Azure Policy.

3. **Control de acceso y cifrado:**
   - Implementar **Azure RBAC** (Role-Based Access Control) para garantizar el principio de privilegio mínimo.
   - Cifrar los datos en reposo utilizando claves administradas por Microsoft o claves administradas por el cliente (CMK).
   - Obligar el uso de **HTTPS** para todas las comunicaciones y deshabilitar HTTP.

---

### **2. Configuración del Ciclo de Vida y Gestión del Almacenamiento**
Para mantener un control eficiente del almacenamiento y cumplir con las políticas de retención de datos, se recomienda:

1. **Políticas de ciclo de vida:**
   - Definir reglas que automaticen la transición de blobs entre las capas de acceso (`hot`, `cool`, `archive`) según su antigüedad.
   - Configurar la eliminación automática de blobs no utilizados después de un período predefinido.

2. **Bloqueo de recursos:**
   - Aplicar un **Resource Lock** de tipo `CanNotDelete` en la cuenta de almacenamiento y sus contenedores para evitar eliminaciones accidentales.

3. **Registro y monitoreo:**
   - Habilitar el monitoreo y auditoría mediante:
     - **Azure Monitor** para alertas proactivas.
     - **Azure Storage Logging** para rastrear operaciones y accesos.
     - **Log Analytics** para consolidar logs y generar reportes detallados.

---

### **3. Configuración de Características Requeridas**
1. **Deshabilitar características no utilizadas:**
   - Desactivar la funcionalidad de `Static Website` desde la configuración de la Storage Account.
   - Deshabilitar servicios no requeridos, como `queue`, `table` y `file`, si solo se necesita soporte para `blob` o sFTP.

2. **sFTP con usuarios locales:**
   - Habilitar la funcionalidad de sFTP en la Storage Account (solo disponible en cuentas tipo `Block Blob Storage` o `General Purpose v2`).
   - Configurar un usuario local con las siguientes medidas:
     - Generar credenciales específicas para acceso mediante sFTP.
     - Asignar permisos a nivel de contenedor según el principio de privilegio mínimo.
   - Asegurar que el acceso a sFTP esté restringido mediante Private Endpoint.

3. **Auditoría de sFTP:**
   - Habilitar el registro de operaciones sFTP en el **Azure Storage Logging** para rastrear actividades y detectar accesos no autorizados.

---

### **4. Cumplimiento de Normas del WAF y CAF**
1. **Seguridad (CAF - Pilar de Seguridad):**
   - Implementar políticas de seguridad mediante Azure Policy para forzar configuraciones como:
     - Uso exclusivo de Private Endpoints.
     - Deshabilitación de acceso público.
   - Usar **Microsoft Defender for Storage** para la detección de amenazas en tiempo real.

2. **Diseño confiable (WAF):**
   - Implementar replicación de datos con configuraciones como **RA-GRS** para garantizar alta disponibilidad.
   - Configurar copias de seguridad periódicas mediante **Azure Backup** o scripts personalizados.
   - Probar regularmente la capacidad de recuperación ante desastres.

---

### **5. Automatización e Infraestructura como Código**
Para garantizar consistencia y escalabilidad en la configuración, utiliza herramientas de Infraestructura como Código (IaC):

1. **Definir configuraciones mediante:**
   - Plantillas ARM o **Bicep**.
   - Scripts de **Terraform** para automatizar la creación de Private Endpoints, reglas de ciclo de vida, configuraciones de sFTP y políticas de seguridad.

2. **Versionamiento:**
   - Almacenar y versionar los scripts en un repositorio como **GitHub** o **Azure Repos**.
   - Implementar integraciones de CI/CD para auditar y desplegar cambios en la infraestructura.

---

Esta configuración asegura que la Azure Storage Account cumple con los pilares de seguridad, confiabilidad y eficiencia del WAF y CAF, al mismo tiempo que satisface los requerimientos específicos del entorno. 

--- 

Si necesitas adaptar algún punto o incluir ejemplos prácticos (scripts o configuraciones específicas), puedo extender el documento.
---


Aquí tienes el documento ajustado con el punto 1 colocado antes del punto 4:

---

## **Configuración de Azure Storage Account Cumpliendo WAF y CAF**

Este documento describe la configuración recomendada para una **Azure Storage Account** siguiendo las mejores prácticas establecidas en el **Well-Architected Framework (WAF)** y el **Cloud Adoption Framework (CAF)**, ajustándose a los requisitos específicos de seguridad y operación, incluyendo el uso exclusivo de Private Endpoints, configuración de ciclo de vida obligatorio, y soporte para sFTP mediante usuarios locales.

---

### **1. Configuración de Seguridad**
Para garantizar la seguridad de los datos y el cumplimiento de las normas del WAF y CAF, se deben implementar las siguientes medidas:

1. **Uso exclusivo de Private Endpoint:**
   - Configurar un **Private Endpoint** asociado a subrecursos específicos (`blob`, `file`, `queue`, o `table`) para garantizar que todo el tráfico pase por la red privada.
   - Deshabilitar el acceso público configurando el parámetro **Public Network Access** en `Disabled`.
   - Asegurar que la resolución de nombres para el Private Endpoint se administre mediante una **Azure Private DNS Zone**.
   - Aplicar políticas de Azure Policy para forzar el uso de Private Endpoints en todas las cuentas de almacenamiento.

2. **Bloqueo de acceso público:**
   - Asegurarse de que todas las configuraciones públicas estén deshabilitadas mediante reglas de firewall (`Deny All`) y Azure Policy.

3. **Control de acceso y cifrado:**
   - Implementar **Azure RBAC** (Role-Based Access Control) para garantizar el principio de privilegio mínimo.
   - Cifrar los datos en reposo utilizando claves administradas por Microsoft o claves administradas por el cliente (CMK).
   - Obligar el uso de **HTTPS** para todas las comunicaciones y deshabilitar HTTP.

---

### **2. Configuración del Ciclo de Vida y Gestión del Almacenamiento**
Para mantener un control eficiente del almacenamiento y cumplir con las políticas de retención de datos, se recomienda:

1. **Políticas de ciclo de vida obligatorias:**
   - Solicitar al proveedor la definición de una política de ciclo de vida para el almacenamiento.

2. **Bloqueo de recursos:**
   - Aplicar un **Resource Lock** de tipo `CanNotDelete` en la cuenta de almacenamiento y sus contenedores para evitar eliminaciones accidentales.

---

### **3. Configuración de Características Requeridas**
1. **Deshabilitar características no utilizadas:**
   - Desactivar la funcionalidad de `Static Website` desde la configuración de la Storage Account.
   - Deshabilitar servicios no requeridos, como `queue`, `table` y `file`, si solo se necesita soporte para `blob` o sFTP.

2. **sFTP con usuarios locales:**
   - Habilitar la funcionalidad de sFTP en la Storage Account (solo disponible en cuentas tipo `Block Blob Storage` o `General Purpose v2`).
   - Configurar un usuario local con las siguientes medidas:
     - Generar credenciales específicas para acceso mediante sFTP.
     - Asignar permisos a nivel de contenedor según el principio de privilegio mínimo.
   - Asegurar que el acceso a sFTP esté restringido mediante Private Endpoint.

3. **Auditoría de sFTP:**
   - Habilitar el registro de operaciones sFTP en el **Azure Storage Logging** para rastrear actividades y detectar accesos no autorizados.

---

### **4. Cumplimiento de Normas del WAF y CAF**
1. **Seguridad (CAF - Pilar de Seguridad):**
   - Implementar políticas de seguridad mediante Azure Policy para forzar configuraciones como:
     - Uso exclusivo de Private Endpoints.
     - Deshabilitación de acceso público.
   - Usar **Microsoft Defender for Storage** para la detección de amenazas en tiempo real.

2. **Diseño confiable (WAF):**
   - Solicitar al proveedor una política de respaldo (Backup Policy) adaptada a las necesidades del negocio.
   - Probar regularmente la capacidad de recuperación y la conformidad con las políticas de seguridad.

---

Este documento asegura que la Azure Storage Account cumple con los pilares de seguridad y confiabilidad establecidos en el WAF y el CAF, ajustándose a los requerimientos específicos del entorno.

---

Si necesitas realizar más cambios o incluir ejemplos concretos, házmelo saber.
---


Para configurar una **Azure Storage Account** cumpliendo con las normas del **WAF (Well-Architected Framework)** y el **CAF (Cloud Adoption Framework)**, considerando los requisitos específicos que mencionas, te detallo los puntos que abordaría y las configuraciones recomendadas:

---

### 1. **Configuración de seguridad**
   - **Uso exclusivo de Private Endpoint:**
     - Configura un **Private Endpoint** para la cuenta de almacenamiento, asegurándote de que todo el tráfico pase únicamente por la red privada y no sea accesible desde Internet.
     - Asegura el **Deny All** en las reglas de firewall de la Storage Account para bloquear conexiones públicas.
     - Verifica que el Private Endpoint esté asociado a un subrecurso específico como `blob`, `file`, `queue`, o `table`, según el uso requerido.
     - Habilita **Azure Private DNS Zone** para la resolución interna del Private Endpoint.
   - **Deshabilita el acceso público:**
     - Configura el **Public Network Access** en `Disabled`.
   - **Implementación de políticas con Azure Policy:**
     - Define una política que requiera el uso de Private Endpoints para todas las cuentas de almacenamiento.
     - Aplica políticas para bloquear la habilitación de acceso público.

---

### 2. **Ciclo de vida y gestión del almacenamiento**
   - **Configurar políticas de ciclo de vida:**
     - Crea políticas de ciclo de vida específicas basadas en las necesidades del negocio:
       - Archivar blobs antiguos (hot -> cool -> archive).
       - Eliminar blobs no utilizados después de un tiempo determinado.
     - Usa el portal o scripts ARM/Bicep/Terraform para definir estas reglas.
   - **Bloqueo de eliminación:**
     - Aplica un **Resource Lock** de tipo `CanNotDelete` para evitar la eliminación accidental de la Storage Account o sus recursos asociados.
   - **Registro y monitoreo de accesos:**
     - Habilita **Azure Monitor**, **Log Analytics** y **Azure Storage Logging** para rastrear accesos, operaciones y cambios en la configuración.
     - Implementa alertas con **Azure Alerts** en caso de actividades sospechosas.

---

### 3. **Deshabilitar características no requeridas**
   - **Deshabilitar la característica de web estática:**
     - Desactiva la opción de `Static Website` desde la configuración de la Storage Account.
   - **Limitación de servicios no usados:**
     - Si solo necesitas `blob` y `sFTP`, desactiva `queue`, `table`, y `file` a través de configuraciones en el portal o mediante plantillas ARM/Terraform.

---

### 4. **Configuración de sFTP con usuario local**
   - **Habilitación de sFTP:**
     - En el tipo de cuenta de almacenamiento, selecciona `Block Blob Storage` o `General Purpose v2`.
     - Activa la funcionalidad de sFTP en las configuraciones avanzadas de la Storage Account.
   - **Configuración de usuario local:**
     - Crea un usuario local para el acceso a sFTP:
       - Genera credenciales específicas para el usuario.
       - Asocia permisos específicos por contenedor para este usuario.
     - Asegúrate de que el acceso a sFTP también sea restringido mediante Private Endpoint.
   - **Auditoría y control:**
     - Habilita el registro de operaciones sFTP en el **Azure Storage Logging**.
     - Implementa alertas para intentos fallidos de autenticación o accesos no autorizados.

---

### 5. **Cumplimiento de normas del CAF y WAF**
   - **CAF - Pilar de seguridad:**
     - Implementa la **Identity and Access Management (IAM):**
       - Usa **Azure RBAC** para dar permisos mínimos necesarios (principio de privilegio mínimo).
       - Asigna roles predefinidos específicos como `Storage Blob Data Contributor` en vez de roles generales.
     - Cifra los datos en reposo:
       - Usa **Azure Storage Encryption** con claves gestionadas por Microsoft o claves administradas por el cliente (CMK).
     - Cifra los datos en tránsito:
       - Obliga el uso de **HTTPS** y deshabilita HTTP en la cuenta de almacenamiento.
   - **WAF - Diseño confiable:**
     - Implementa una estrategia de recuperación ante desastres:
       - Habilita la replicación de datos (por ejemplo, **RA-GRS** si es necesario).
       - Configura copias de seguridad regulares usando **Azure Backup** o scripts personalizados.
     - Prueba regularmente la capacidad de recuperación y la conformidad con las políticas de seguridad.

---

### 6. **Automatización e infraestructura como código**
   - Usa herramientas como **Terraform**, **Bicep**, o plantillas ARM para definir la infraestructura y garantizar la consistencia:
     - Configura los módulos para incluir Private Endpoints, sFTP, ciclo de vida, y políticas de seguridad.
   - Versiona y audita estas configuraciones en un sistema de control de versiones como **GitHub** o **Azure Repos**.

---

Con estos puntos, cumples las normas del WAF y CAF, garantizando seguridad, control de acceso, y gobernanza en la configuración de Azure Storage Account. Si necesitas un ejemplo de script o plantilla ARM/Terraform para implementar alguna de estas configuraciones, avísame y puedo proporcionarlo.
---


Aquí tienes el documento ajustado:

---

## **Configuración de Azure Storage Account Cumpliendo WAF y CAF**

Este documento describe la configuración recomendada para una **Azure Storage Account** siguiendo las mejores prácticas establecidas en el **Well-Architected Framework (WAF)** y el **Cloud Adoption Framework (CAF)**, ajustándose a los requisitos específicos de seguridad y operación, incluyendo el uso exclusivo de Private Endpoints, configuración de ciclo de vida obligatorio, y soporte para sFTP mediante usuarios locales.

---

### **1. Configuración de Seguridad**
Para garantizar la seguridad de los datos y el cumplimiento de las normas del WAF y CAF, se deben implementar las siguientes medidas:

1. **Uso exclusivo de Private Endpoint:**
   - Configurar un **Private Endpoint** asociado a subrecursos específicos (`blob`, `file`, `queue`, o `table`) para garantizar que todo el tráfico pase por la red privada.
   - Deshabilitar el acceso público configurando el parámetro **Public Network Access** en `Disabled`.
   - Asegurar que la resolución de nombres para el Private Endpoint se administre mediante una **Azure Private DNS Zone**.
   - Aplicar políticas de Azure Policy para forzar el uso de Private Endpoints en todas las cuentas de almacenamiento.

2. **Bloqueo de acceso público:**
   - Asegurarse de que todas las configuraciones públicas estén deshabilitadas mediante reglas de firewall (`Deny All`) y Azure Policy.

3. **Control de acceso y cifrado:**
   - Implementar **Azure RBAC** (Role-Based Access Control) para garantizar el principio de privilegio mínimo.
   - Cifrar los datos en reposo utilizando claves administradas por Microsoft o claves administradas por el cliente (CMK).
   - Obligar el uso de **HTTPS** para todas las comunicaciones y deshabilitar HTTP.

---

### **2. Configuración del Ciclo de Vida y Gestión del Almacenamiento**
Para mantener un control eficiente del almacenamiento y cumplir con las políticas de retención de datos, se recomienda:

1. **Políticas de ciclo de vida obligatorias:**
   - Solicitar al proveedor la definición de una política de ciclo de vida para el almacenamiento.

2. **Bloqueo de recursos:**
   - Aplicar un **Resource Lock** de tipo `CanNotDelete` en la cuenta de almacenamiento y sus contenedores para evitar eliminaciones accidentales.

---

### **3. Configuración de Características Requeridas**
1. **Deshabilitar características no utilizadas:**
   - Desactivar la funcionalidad de `Static Website` desde la configuración de la Storage Account.
   - Deshabilitar servicios no requeridos, como `queue`, `table` y `file`, si solo se necesita soporte para `blob` o sFTP.

2. **sFTP con usuarios locales:**
   - Habilitar la funcionalidad de sFTP en la Storage Account (solo disponible en cuentas tipo `Block Blob Storage` o `General Purpose v2`).
   - Configurar un usuario local con las siguientes medidas:
     - Generar credenciales específicas para acceso mediante sFTP.
     - Asignar permisos a nivel de contenedor según el principio de privilegio mínimo.
   - Asegurar que el acceso a sFTP esté restringido mediante Private Endpoint.

3. **Auditoría de sFTP:**
   - Habilitar el registro de operaciones sFTP en el **Azure Storage Logging** para rastrear actividades y detectar accesos no autorizados.

---

### **4. Cumplimiento de Normas del WAF y CAF**
1. **Seguridad (CAF - Pilar de Seguridad):**
   - Implementar políticas de seguridad mediante Azure Policy para forzar configuraciones como:
     - Uso exclusivo de Private Endpoints.
     - Deshabilitación de acceso público.
   - Usar **Microsoft Defender for Storage** para la detección de amenazas en tiempo real.

2. **Diseño confiable (WAF):**
   - Solicitar al proveedor una política de respaldo (Backup Policy) adaptada a las necesidades del negocio.
   - Probar regularmente la capacidad de recuperación y la conformidad con las políticas de seguridad.

---

Este documento asegura que la Azure Storage Account cumple con los pilares de seguridad y confiabilidad establecidos en el WAF y el CAF, ajustándose a los requerimientos específicos del entorno.

--- 

Si necesitas ajustar algo más o añadir ejemplos concretos, házmelo saber.
---


Para abordar la configuración de un **Azure Storage Account** que cumpla con los lineamientos de seguridad y requisitos establecidos (WAF y CAF), debemos estructurar el enfoque cubriendo los siguientes puntos clave. Este diseño se orienta hacia la seguridad, el uso de **Private Endpoints**, la habilitación del ciclo de vida y la funcionalidad de sFTP con usuarios locales. 

### **1. Selección del Tipo de Azure Storage Account**
- **Tipo recomendado:** General-purpose v2 (GPv2).
  - Ofrece soporte para blobs, files, queues y tables, cubriendo las necesidades generales.
  - Habilita configuraciones avanzadas como Private Endpoint y políticas de ciclo de vida.
  - Permite configuraciones sFTP mediante servicios adicionales.

---

### **2. Configuración de Seguridad**
#### **Private Endpoints**
- **Activación del Private Endpoint:**
  - Configurar Private Endpoint para cada subrecurso necesario del Storage Account (Blob, File, Queue, etc.).
  - Asegurarse de que el Storage Account sea accesible únicamente desde redes privadas y desde servicios internos a través del Private Endpoint.
  - Rechazar accesos públicos deshabilitando la **"Public Network Access"**.
- **Redes permitidas:**
  - Asegurar que solo las redes aprobadas pueden acceder al Storage Account mediante la configuración de **Firewall y redes virtuales**.
  - Permitir acceso solo desde las redes virtuales específicas en Azure y los Private Endpoints asociados.
- **DNS privado:**
  - Configurar una zona DNS privada para resolver el nombre del Private Endpoint asociado.

#### **Cifrado de Datos:**
- Habilitar el cifrado con claves gestionadas por el cliente (Customer-Managed Keys - CMKs).
  - Integrar con Azure Key Vault para la gestión de claves.
- Usar **"Secure Transfer Required"** para obligar el uso de HTTPS o SMB 3.0 con cifrado.

#### **Políticas de acceso y autenticación:**
- Deshabilitar las claves de cuenta para minimizar el riesgo de exposición.
- Usar **Azure Active Directory (AAD)** para autenticar usuarios y servicios siempre que sea posible.
- Implementar control de acceso basado en roles (**RBAC**) en el nivel del contenedor para una granularidad de permisos adecuada.

---

### **3. Configuración del Ciclo de Vida**
- **Políticas de ciclo de vida:**
  - Configurar políticas de gestión de ciclo de vida para automatizar la transición de datos a niveles de almacenamiento más económicos (Hot -> Cool -> Archive).
  - Ejemplo: Configurar una regla para mover blobs a "Cool" después de 30 días y luego a "Archive" después de 180 días.
- Involucrar al proveedor para definir el ciclo de vida requerido y garantizar el cumplimiento de los tiempos estipulados.

---

### **4. Soporte de sFTP con Usuarios Locales**
- **Configuración sFTP:**
  - Habilitar sFTP para Azure Storage Account mediante la configuración avanzada.
  - Crear usuarios locales en el Storage Account con permisos específicos para sFTP.
  - Asegurar que los usuarios sFTP sean administrados de forma segura y que sus contraseñas sean robustas.
  - Limitar las operaciones sFTP a contenedores o directorios específicos según sea necesario.

#### **Aislamiento de usuarios:**
- Implementar **"Container Soft Delete"** para evitar la pérdida de datos accidental.
- Aplicar políticas de retención para mitigar riesgos de manipulación indebida.

---

### **5. Restricciones Adicionales**
- **Web estática:**
  - Confirmar que la opción de **"Static Website Hosting"** esté deshabilitada para evitar la exposición pública.
- **Monitoreo y alertas:**
  - Configurar diagnósticos y logs en Azure Monitor para capturar accesos no autorizados o intentos de intrusión.
  - Integrar con Azure Sentinel para correlación avanzada de eventos.

---

### **6. Pruebas y Validación**
- Realizar pruebas de conectividad para confirmar el aislamiento de red mediante Private Endpoint.
- Validar que solo los usuarios locales de sFTP tienen acceso al recurso y que el acceso público está denegado.
- Probar el ciclo de vida del almacenamiento para asegurar que las políticas se aplican correctamente.
- Ejecutar revisiones de cumplimiento con las normativas del WAF y CAF.

Esta configuración asegura que el **Azure Storage Account** sea seguro, cumpla con los requisitos funcionales y esté alineado con las mejores prácticas en Azure.

---
*Generado desde conversación con 9 mensajes.*
*Azure/Cloud*
