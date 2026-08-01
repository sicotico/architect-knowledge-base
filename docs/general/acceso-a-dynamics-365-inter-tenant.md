---
title: Acceso a Dynamics 365 inter-tenant
date: 2024-09-19
category: General
slug: acceso-a-dynamics-365-inter-tenant
tags: ['General']
---

# Acceso a Dynamics 365 inter-tenant


> **Pregunta original:**
> 
Estoy usando Power Apps y han de conectarse a un Api Management de Tenant B
> Quiero implantar una solución de Dynamics 365. La tengo desplegada en el tenat A y necesito acceder a recursos de tenant B. ¿Que opciones tengo?

---


## Respuesta


Para conectar **Power Apps** en Tenant A a un **API Management** que está en el **Tenant B**, hay varias consideraciones clave relacionadas con la autenticación y configuración del API para permitir este acceso entre tenants. Aquí te explico las opciones y pasos que puedes seguir para lograr esta integración.

### Pasos para conectar Power Apps de Tenant A a API Management de Tenant B

1. **Registrar una aplicación en Azure AD (Tenant B)**:
   - Ve al portal de **Azure AD** en Tenant B y registra una nueva aplicación.
   - Esta aplicación representará a Power Apps (o cualquier otra aplicación de Tenant A) en Tenant B.
   - Configura la **URL de redirección** como `https://global.consent.azure-apim.net/redirect` para permitir que Power Apps pueda autenticar a los usuarios y obtener tokens de acceso para consumir el API.
   - En la sección de **API Permissions**, otorga los permisos adecuados para acceder a los recursos protegidos por API Management, como los permisos necesarios para invocar las API expuestas.

2. **Configurar el API Management de Tenant B**:
   - En **API Management** de Tenant B, asegúrate de que las APIs a las que deseas que Power Apps acceda estén configuradas y publicadas.
   - Define las políticas de autenticación para las APIs. En este caso, querrás utilizar **OAuth 2.0** con el proveedor de identidad de **Azure AD** para autenticar las solicitudes.
   - Configura **CORS** (Cross-Origin Resource Sharing) para permitir solicitudes desde Power Apps o desde cualquier dominio de Tenant A que pueda estar haciendo las llamadas a las APIs.

3. **Crear un Custom Connector en Power Apps (Tenant A)**:
   - Ve a Power Apps en Tenant A y navega a la sección de **Custom Connectors**.
   - Crea un nuevo conector personalizado y selecciona "Usar una OpenAPI definition" o "Definir manualmente" según la preferencia.
   - Configura el conector con el **endpoint** de la API en Tenant B (proporcionado por API Management).
   - En la sección de **Autenticación**, selecciona **OAuth 2.0** e introduce los siguientes valores:
     - **Cliente ID** y **Secreto de Cliente**: Obtenidos de la aplicación registrada en Azure AD de Tenant B.
     - **URL del token**: `https://login.microsoftonline.com/{TenantB}/oauth2/v2.0/token` (reemplaza `{TenantB}` con el ID del Tenant B).
     - **Scope**: Los permisos que tu API requiere (por ejemplo, `api://{ClientID}/.default`, donde `{ClientID}` es el ID de la aplicación registrada en Tenant B).
     - **Autorización URL**: `https://login.microsoftonline.com/{TenantB}/oauth2/v2.0/authorize`.

4. **Probar y validar la conexión**:
   - Una vez creado el conector personalizado, puedes utilizarlo dentro de Power Apps para conectarte al API en Tenant B.
   - Si la configuración de autenticación es correcta, Power Apps solicitará un token de acceso desde Azure AD (Tenant B) y lo utilizará para autenticar las solicitudes a API Management en Tenant B.
   - Asegúrate de que los usuarios de Tenant A que usan Power Apps tengan permisos adecuados para acceder al conector y los recursos en API Management.

### Consideraciones importantes:

- **Autenticación y Seguridad**: Asegúrate de que las políticas de acceso condicional y los permisos en Azure AD de Tenant B estén bien configurados para permitir que los usuarios de Tenant A puedan autenticarse correctamente. El uso de OAuth 2.0 con Azure AD es una buena práctica para proteger los recursos en API Management.
  
- **Autorización de Usuarios**: Si deseas que los usuarios de Power Apps en Tenant A accedan con diferentes niveles de permisos, debes gestionar los **roles** o **grupos** en Azure AD de Tenant B y mapearlos a la política de autorización de las APIs en API Management.

- **Configuración de Cross-Tenant Access**: Si se necesita permitir el acceso entre tenants de manera más amplia, asegúrate de que las políticas de acceso cross-tenant estén habilitadas en **Azure AD**. Esto puede incluir permitir que usuarios de un tenant accedan a las aplicaciones registradas en otro tenant.

---

Con estos pasos, Power Apps en Tenant A debería poder consumir APIs gestionadas por **API Management** en Tenant B de forma segura mediante OAuth 2.0. Si tienes algún detalle específico del API o configuración que quieras profundizar, podemos revisar esos puntos para ajustar aún más la solución.
---


Para acceder a recursos en el Tenant B desde una implementación de **Dynamics 365** en el Tenant A, hay varias opciones dependiendo del tipo de recursos a los que quieras acceder y cómo quieras gestionar la identidad y el acceso. A continuación te expongo algunas de las opciones más comunes para gestionar este tipo de escenarios inter-tenant en entornos de **Azure Active Directory (Azure AD)** y **Dynamics 365**:

### 1. **Azure AD B2B (Business-to-Business) Collaboration**
   - **Descripción**: Puedes invitar usuarios de un tenant externo (en este caso, usuarios de Tenant B) a participar en Tenant A utilizando la colaboración B2B de Azure AD. Esto permite que los usuarios de Tenant B accedan a los recursos de Dynamics 365 en Tenant A utilizando sus credenciales actuales de Tenant B.
   - **Cómo funciona**: Los usuarios de Tenant B reciben una invitación para unirse al Tenant A y pueden acceder a las aplicaciones asignadas en el Tenant A, como Dynamics 365. Los usuarios son gestionados como usuarios externos, pero mantienen sus credenciales originales.
   - **Ventajas**: Es sencillo para los usuarios porque mantienen una sola cuenta. Además, es una opción muy segura y flexible, con soporte nativo para Dynamics 365.
   - **Consideraciones**: Requiere configurar políticas de acceso y seguridad adecuadas, como **Conditional Access**.

### 2. **Autenticación Delegada con Azure AD y Aplicaciones Multi-Tenant**
   - **Descripción**: Dynamics 365 se puede configurar como una aplicación multi-tenant en Azure AD. Esto significa que usuarios de diferentes tenants (en este caso, de Tenant B) pueden acceder a la misma instancia de Dynamics 365 en Tenant A. El tenant A actúa como el "Proveedor de Servicios", y el Tenant B puede autenticarse contra su propio directorio de Azure AD.
   - **Cómo funciona**: Configuras la aplicación de Dynamics 365 como una aplicación multi-tenant en Azure AD. Los usuarios de Tenant B se autenticaban contra su Azure AD (Tenant B) pero tienen acceso a los recursos de Dynamics 365 en Tenant A.
   - **Ventajas**: Los usuarios de Tenant B no necesitan una nueva cuenta ni cambiar de tenant, y puedes controlar el acceso desde un solo lugar. Es útil cuando tienes múltiples organizaciones que necesitan compartir una sola implementación de Dynamics 365.
   - **Consideraciones**: Requiere configurar adecuadamente los permisos y roles en ambos tenants.

### 3. **API de Dynamics 365 y Azure AD Application Permissions**
   - **Descripción**: Si necesitas acceder a los datos o recursos de Tenant B mediante automatización o procesos de integración, puedes usar las APIs de Dynamics 365 junto con permisos de aplicación en Azure AD. Las aplicaciones registradas en Azure AD de Tenant A pueden solicitar permisos para acceder a APIs o recursos en Tenant B.
   - **Cómo funciona**: Registras una aplicación en Azure AD del Tenant B y le otorgas los permisos necesarios para acceder a los datos que necesitas. Esta aplicación puede ser autorizada en Tenant A para interactuar con Dynamics 365 mediante APIs.
   - **Ventajas**: Útil si lo que necesitas es acceso programático a datos entre los tenants. También ofrece gran control sobre los niveles de acceso.
   - **Consideraciones**: La configuración y la gestión de permisos pueden ser más complejas. Necesitas gestionar tokens de acceso y permisos de API en ambos tenants.

### 4. **Microsoft Power Platform y Conectores**
   - **Descripción**: Si estás utilizando la Power Platform junto con Dynamics 365, podrías utilizar **conectores** para vincular recursos entre Tenant A y Tenant B. Power Automate o Power Apps pueden consumir datos de diferentes entornos, incluso si están en tenants distintos.
   - **Cómo funciona**: Configuras conectores que acceden a recursos en ambos tenants. Dependiendo del tipo de datos que estés compartiendo, puedes configurar conectores de Dynamics 365, SharePoint, u otros servicios compatibles.
   - **Ventajas**: Fácil de configurar y puedes crear flujos de trabajo entre los tenants sin necesidad de integrar a nivel de identidad o APIs.
   - **Consideraciones**: Esta opción está más orientada a automatización y flujos de trabajo, por lo que puede no ser ideal para todos los escenarios de integración.

### 5. **Azure AD Entitlement Management**
   - **Descripción**: Esta opción es útil si deseas gestionar de manera más centralizada el acceso a los recursos de Tenant A para usuarios de Tenant B. Entitlement Management permite crear catálogos y paquetes de acceso que los usuarios externos (de Tenant B) pueden solicitar para acceder a Dynamics 365.
   - **Cómo funciona**: Creas un paquete de acceso que incluye Dynamics 365 y otros recursos relevantes en Tenant A. Los usuarios de Tenant B pueden solicitar acceso y, tras su aprobación, pueden acceder a los recursos según las condiciones establecidas.
   - **Ventajas**: Ideal si gestionas acceso temporal o rotativo entre tenants y quieres asegurarte de que los usuarios externos tengan el nivel de acceso adecuado.
   - **Consideraciones**: La configuración inicial requiere planificación para definir los paquetes de acceso y las reglas de solicitud.

---

En resumen, dependiendo de tus necesidades (como la colaboración de usuarios, acceso programático o automatización), puedes optar por soluciones como la **colaboración B2B**, la **autenticación multi-tenant**, o una integración a nivel de API. La clave está en encontrar el equilibrio entre facilidad de uso y control de seguridad para tu organización.

¿Tienes alguna preferencia en cuanto al tipo de acceso o nivel de integración que te gustaría implementar? Esto podría ayudar a afinar mejor la recomendación.

---
*Generado desde conversación con 4 mensajes.*
*General*
