---
title: Crear sitio web SharePoint
date: 2024-10-09
category: General
slug: crear-sitio-web-sharepoint
tags: ['General']
---

# Crear sitio web SharePoint


> **Pregunta original:**
> 
Tengo para administrar Azure  y AWS. Un sharepoint. Quiero crear un web o algo parecido en sharepoint. ¿Como de factible es? 

---


## Respuesta


Sí, es totalmente factible crear un sitio web o una plataforma similar en SharePoint. SharePoint es una herramienta poderosa de Microsoft diseñada para la colaboración, gestión de documentos y creación de sitios web internos (intranets) para organizaciones.

**Opciones disponibles:**

1. **SharePoint Online (parte de Microsoft 365):**
   - **Características:**
     - No requiere gestión de infraestructura física o virtual.
     - Actualizaciones y mantenimiento manejados por Microsoft.
     - Integración sencilla con otras aplicaciones de Microsoft 365 como Teams, OneDrive y Office.
   - **Ideal para:**
     - Organizaciones que buscan una solución en la nube sin preocuparse por la administración de servidores.
     - Creación de sitios de comunicación y colaboración interna.

2. **SharePoint Server On-Premises:**
   - **Características:**
     - Se instala en servidores propios, lo que permite un mayor control sobre la infraestructura.
     - Personalización y configuración más profundas.
     - Puede ser alojado en tus entornos de Azure o AWS utilizando máquinas virtuales.
   - **Ideal para:**
     - Organizaciones con requisitos específicos de seguridad, cumplimiento o personalización.
     - Aquellos que desean integrar SharePoint con otros sistemas internos.

**Consideraciones al utilizar Azure y AWS:**

- **Azure:**
  - Al ser una plataforma de Microsoft, Azure ofrece integraciones más fluidas con SharePoint.
  - Puedes desplegar máquinas virtuales con SharePoint Server y aprovechar servicios como Azure Active Directory para autenticación.
  - Servicios adicionales como Azure SQL Database pueden utilizarse para almacenar datos de SharePoint.

- **AWS:**
  - Aunque no es nativo de Microsoft, es posible alojar SharePoint Server en máquinas virtuales en AWS.
  - Requiere una configuración más detallada para integrar servicios equivalentes (por ejemplo, utilizar Amazon RDS para bases de datos).

**Pasos para crear un sitio web en SharePoint:**

1. **Planificación:**
   - Define los objetivos del sitio: colaboración interna, portal de información, gestión de proyectos, etc.
   - Determina si necesitas funcionalidades adicionales o integraciones con otras herramientas.

2. **Selección de la plataforma:**
   - Decide entre SharePoint Online o SharePoint Server On-Premises según tus necesidades y recursos.
   - Considera factores como costos, escalabilidad, mantenimiento y seguridad.

3. **Implementación:**
   - **SharePoint Online:**
     - Configura tu suscripción a Microsoft 365.
     - Crea sitios utilizando plantillas predefinidas y personalízalos según sea necesario.
   - **SharePoint Server On-Premises:**
     - Configura las máquinas virtuales en Azure o AWS.
     - Instala y configura SharePoint Server.
     - Personaliza el sitio utilizando herramientas de desarrollo como SharePoint Framework (SPFx) si es necesario.

4. **Personalización y Desarrollo:**
   - Utiliza temas y diseños para ajustar la apariencia del sitio.
   - Añade web parts y aplicaciones para extender la funcionalidad.
   - Si necesitas funcionalidades específicas, considera el desarrollo personalizado.

5. **Seguridad y Permisos:**
   - Configura permisos y accesos para garantizar que solo las personas adecuadas puedan ver o editar el contenido.
   - Implementa políticas de seguridad y cumplimiento según los requisitos de tu organización.

**Conclusión:**

Crear un sitio web o plataforma en SharePoint es una solución viable y efectiva para necesidades de colaboración y gestión de información dentro de una organización. Dada tu experiencia con Azure y AWS, puedes aprovechar estas plataformas para alojar y gestionar SharePoint Server si optas por una solución on-premises. Sin embargo, si buscas simplicidad y menor carga de administración, SharePoint Online podría ser la opción más adecuada.

Recuerda evaluar tus necesidades específicas, recursos disponibles y objetivos a largo plazo para elegir la opción que mejor se adapte a tu situación.

---
*Generado desde conversación con 2 mensajes.*
*General*
