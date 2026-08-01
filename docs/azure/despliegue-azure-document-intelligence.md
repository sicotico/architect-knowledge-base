---
title: Despliegue Azure Document Intelligence
date: 2024-12-16
category: Azure/Cloud
slug: despliegue-azure-document-intelligence
tags: ['Azure/Cloud', 'azure']
---

# Despliegue Azure Document Intelligence


> **Pregunta original:**
> 
Eres un especialista en Azure y esta definiendo como se debe desplegar el servicio Azure Document Intelligence. Tienes que tener en cuenta un Tier inicial, el acceso seguro, las gestiones de Roles con RBAC y como recomienda Microsoft utilizarlo para varios proyectos
> Elimina Diagrama Resumido del Despliegue, cambia a recomendaciones el titulo 5. La parte de autenticación debe de estar asociado a un Entra ID, ¿Es Posible?

---


## Respuesta


### Guía para Desplegar el Servicio **Azure Document Intelligence**

El servicio **Azure Document Intelligence** (anteriormente Form Recognizer) permite la extracción de datos estructurados de documentos utilizando modelos preentrenados o personalizados. Aquí se detalla un plan estratégico para desplegarlo adecuadamente considerando un Tier inicial, acceso seguro, RBAC, y uso compartido para múltiples proyectos.

---

### **1. Selección del Tier Inicial**

- **Tier Recomendado: `Standard S0`**
  - Este Tier es adecuado para comenzar, ya que balancea costos y capacidades.
  - Ofrece:
    - Procesamiento de documentos con modelos preentrenados y personalizados.
    - Soporte para hasta 100 documentos por segundo.
  - **Escalabilidad**: Si se requiere mayor capacidad, se puede migrar al Tier `Standard S1` para un rendimiento mejorado.
  - Para entornos de prueba y desarrollo, se puede usar el Tier gratuito (`Free F0`), aunque tiene limitaciones significativas.

---

### **2. Configuración de Acceso Seguro**

#### **a) Configuración de Redes**
- **Restricción de acceso a redes específicas**:
  - Habilitar **Azure Virtual Network (VNet)** y permitir acceso solo desde subredes específicas.
  - Usar el **servicio de endpoints privados** para conectarse directamente al recurso sin exponerlo públicamente.
- **Reglas de Firewall**:
  - Bloquear todo acceso público, excepto direcciones IP confiables.
  - Implementar filtros de acceso basados en geolocalización si es necesario.

#### **b) Integración con Azure Key Vault**
- Almacenar y gestionar claves de API y otras credenciales sensibles en **Azure Key Vault**.
- Utilizar **identidades administradas** para servicios que consuman Document Intelligence, evitando el manejo manual de credenciales.

#### **c) Autenticación**
- Configurar el servicio para que solo acepte solicitudes autenticadas mediante:
  - **Azure Active Directory (AAD)** tokens para mayor control.
  - Claves de API generadas en el recurso (solo para casos en que AAD no sea viable).

---

### **3. Gestión de Roles con RBAC**

Azure proporciona un modelo basado en roles (**Role-Based Access Control**) para restringir las acciones permitidas según el rol del usuario o aplicación. 

#### **Roles Clave para Document Intelligence**
1. **Propietario (Owner)**:
   - Uso reservado para administradores que configuran el recurso.
2. **Colaborador del Servicio Cognitivo**:
   - Permite gestionar y consumir el recurso.
   - Asignar a desarrolladores que trabajen directamente con el servicio.
3. **Lector del Servicio Cognitivo**:
   - Acceso solo de lectura.
   - Ideal para auditores o equipos que monitorean el servicio.
4. **Administrador de Seguridad**:
   - Gestiona accesos y asegura el cumplimiento de reglas de seguridad.

#### **Implementación**
- Segmentar los roles a nivel de **grupo de recursos** o **recurso específico**, según las necesidades.
- Evitar asignaciones a nivel de suscripción para minimizar privilegios excesivos.
- Utilizar **grupos de seguridad de AAD** para simplificar la gestión y asignación de roles.

---

### **4. Uso para Múltiples Proyectos**

#### **a) Uso Recomendado: Separación por Grupos de Recursos**
- **Un recurso Document Intelligence por proyecto**:
  - Ofrece mayor control sobre costos y aislamiento de datos.
- Si varios proyectos necesitan acceder al mismo recurso, asegurarse de que las aplicaciones estén configuradas con identidades únicas y permisos RBAC adecuados.

#### **b) Gobernanza**
- Implementar etiquetas de recursos para clasificar proyectos y facilitar la supervisión (e.g., `Project: ContosoApp`, `Environment: Production`).
- Utilizar **Azure Policy** para garantizar que las configuraciones de red y seguridad sean consistentes en todos los recursos.

#### **c) Costos Compartidos**
- Para proyectos pequeños o pilotos, utilizar un único recurso con límites controlados mediante políticas de consumo:
  - Configurar alertas de costos.
  - Establecer umbrales para uso máximo mensual.

---

### **5. Recomendaciones de Microsoft**

- **Iteración y Entrenamiento de Modelos**:
  - Para proyectos múltiples, almacenar modelos personalizados en contenedores o directorios separados de **Azure Blob Storage**.
  - Utilizar un enfoque modular con diferentes modelos específicos para cada tipo de documento.

- **Monitoreo y Métricas**:
  - Configurar **Azure Monitor** y **Log Analytics** para observar el rendimiento del servicio.
  - Habilitar alertas en métricas críticas como solicitudes por segundo, errores de autenticación, y costos acumulados.

- **Pruebas A/B**:
  - Comparar modelos preentrenados con personalizados en entornos de prueba antes de moverlos a producción.

---

### **Diagrama Resumido del Despliegue**
1. **Acceso seguro**:
   - Integración con VNet y Key Vault.
2. **Gestión de roles**:
   - RBAC con roles limitados.
3. **Uso compartido**:
   - Gobernanza con etiquetas y Azure Policy.
4. **Monitorización**:
   - Azure Monitor y Log Analytics.

Esto asegura que el despliegue inicial sea seguro, escalable y fácil de administrar a medida que los proyectos crecen. ¿Necesitas ayuda para implementar alguna parte?
---


### Guía para Desplegar el Servicio **Azure Document Intelligence**

El servicio **Azure Document Intelligence** (anteriormente Form Recognizer) permite la extracción de datos estructurados de documentos utilizando modelos preentrenados o personalizados. Aquí se detalla un plan estratégico para desplegarlo adecuadamente considerando un Tier inicial, acceso seguro, RBAC, y uso compartido para múltiples proyectos.

---

### **1. Selección del Tier Inicial**

- **Tier Recomendado: `Standard S0`**
  - Este Tier es adecuado para comenzar, ya que balancea costos y capacidades.
  - Ofrece:
    - Procesamiento de documentos con modelos preentrenados y personalizados.
    - Soporte para hasta 100 documentos por segundo.
  - **Escalabilidad**: Si se requiere mayor capacidad, se puede migrar al Tier `Standard S1` para un rendimiento mejorado.
  - Para entornos de prueba y desarrollo, se puede usar el Tier gratuito (`Free F0`), aunque tiene limitaciones significativas.

---

### **2. Configuración de Acceso Seguro**

#### **a) Configuración de Redes**
- **Restricción de acceso a redes específicas**:
  - Habilitar **Azure Virtual Network (VNet)** y permitir acceso solo desde subredes específicas.
  - Usar el **servicio de endpoints privados** para conectarse directamente al recurso sin exponerlo públicamente.
- **Reglas de Firewall**:
  - Bloquear todo acceso público, excepto direcciones IP confiables.
  - Implementar filtros de acceso basados en geolocalización si es necesario.

#### **b) Integración con Azure Key Vault**
- Almacenar y gestionar claves de API y otras credenciales sensibles en **Azure Key Vault**.
- Utilizar **identidades administradas** para servicios que consuman Document Intelligence, evitando el manejo manual de credenciales.

#### **c) Autenticación**
- El servicio puede integrarse con **Azure Entra ID (anteriormente Azure AD)** para gestionar la autenticación de forma segura y simplificada:
  - Configurar **roles de aplicación** en Azure Entra ID.
  - Utilizar tokens de acceso **OAuth 2.0** emitidos por Entra ID para que las aplicaciones consuman el servicio sin necesidad de claves de API.
  - Asignar identidades administradas a las aplicaciones dentro de Azure, lo que permite consumir el servicio sin manejar directamente las credenciales.

---

### **3. Gestión de Roles con RBAC**

Azure proporciona un modelo basado en roles (**Role-Based Access Control**) para restringir las acciones permitidas según el rol del usuario o aplicación. 

#### **Roles Clave para Document Intelligence**
1. **Propietario (Owner)**:
   - Uso reservado para administradores que configuran el recurso.
2. **Colaborador del Servicio Cognitivo**:
   - Permite gestionar y consumir el recurso.
   - Asignar a desarrolladores que trabajen directamente con el servicio.
3. **Lector del Servicio Cognitivo**:
   - Acceso solo de lectura.
   - Ideal para auditores o equipos que monitorean el servicio.
4. **Administrador de Seguridad**:
   - Gestiona accesos y asegura el cumplimiento de reglas de seguridad.

#### **Implementación**
- Segmentar los roles a nivel de **grupo de recursos** o **recurso específico**, según las necesidades.
- Evitar asignaciones a nivel de suscripción para minimizar privilegios excesivos.
- Utilizar **grupos de seguridad de Entra ID** para simplificar la gestión y asignación de roles.

---

### **4. Uso para Múltiples Proyectos**

#### **a) Uso Recomendado: Separación por Grupos de Recursos**
- **Un recurso Document Intelligence por proyecto**:
  - Ofrece mayor control sobre costos y aislamiento de datos.
- Si varios proyectos necesitan acceder al mismo recurso, asegurarse de que las aplicaciones estén configuradas con identidades únicas y permisos RBAC adecuados.

#### **b) Gobernanza**
- Implementar etiquetas de recursos para clasificar proyectos y facilitar la supervisión (e.g., `Project: ContosoApp`, `Environment: Production`).
- Utilizar **Azure Policy** para garantizar que las configuraciones de red y seguridad sean consistentes en todos los recursos.

#### **c) Costos Compartidos**
- Para proyectos pequeños o pilotos, utilizar un único recurso con límites controlados mediante políticas de consumo:
  - Configurar alertas de costos.
  - Establecer umbrales para uso máximo mensual.

---

### **5. Recomendaciones**

- **Iteración y Entrenamiento de Modelos**:
  - Para proyectos múltiples, almacenar modelos personalizados en contenedores o directorios separados de **Azure Blob Storage**.
  - Utilizar un enfoque modular con diferentes modelos específicos para cada tipo de documento.

- **Monitoreo y Métricas**:
  - Configurar **Azure Monitor** y **Log Analytics** para observar el rendimiento del servicio.
  - Habilitar alertas en métricas críticas como solicitudes por segundo, errores de autenticación, y costos acumulados.

- **Pruebas A/B**:
  - Comparar modelos preentrenados con personalizados en entornos de prueba antes de moverlos a producción.

Este enfoque asegura un despliegue seguro, escalable y administrable del servicio **Azure Document Intelligence**, alineado con las mejores prácticas de Microsoft y la integración con Azure Entra ID para una autenticación robusta y simplificada.

---
*Generado desde conversación con 4 mensajes.*
*Azure/Cloud*
