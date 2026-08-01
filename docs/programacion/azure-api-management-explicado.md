---
title: Azure API Management Explicado: Guía Completa para Principiantes
date: 2024-09-18
category: Programación
slug: azure-api-management-explicado
tags: ['Programación', 'Azure', 'API Management', 'API Gateway']
author: 'Piconocimiento'
reading_time: 12
---

# Azure API Management Explicado: Guía Completa para Principiantes

Aprende todo sobre **Azure API Management (APIM)**, el servicio de Microsoft para gestionar, proteger y monitorear APIs en la nube.

## 🎯 Contexto del Proyecto

Tu configuración actual incluye:
- **Desarrollo de APIs REST** con múltiples equipos
- **Necesidad de governance** y control de acceso
- **Integración con servicios backend** existentes

## 📊 ¿Qué es Azure API Management?

**Azure API Management (APIM)** es un servicio empresarial completo que te permite:
- Publicar APIs para desarrolladores internos o externos
- Proteger tus APIs con políticas de seguridad
- Monitorear y analizar el uso de APIs
- Gestionar ciclos de vida completos de APIs

### Analogía Simple

```
👨‍💻 Desarrolladores → 🚪 APIM (Recepción/Seguridad) → 🖥️ Servidores Backend
```

APIM actúa como un **portero inteligente** que:
- ✅ Verifica credenciales de acceso
- ✅ Limita velocidad de peticiones
- ✅ Transforma formatos de datos
- ✅ Genera documentación automática

## 🏗️ Arquitectura de APIM

### Componentes Principales

| Componente | Descripción |
|------------|-------------|
| **Gateway** | Punto de entrada para todas las peticiones API |
| **Management API** | Interfaz de administración y configuración |
| **Developer Portal** | Sitio web para que los desarrolladores exploren APIs |
| **Analytics** | Métricas y monitoreo de uso en tiempo real |

### Topologías de Despliegue

```
# 1. Desarrollo (Single Node)
- 1 nodo en App Service Plan
- Ideal para pruebas y desarrollo

# 2. Producción (Multi-Region)
- Múltiples nodos en diferentes regiones
- Load balancing automático
- High availability garantizada
```

## 🛠️ Configuración Paso a Paso

### 1. Crear un Recurso APIM

```bash
# Crear resource group
az group create \
    --name "my-api-rg" \
    --location "eastus"

# Crear instancia de APIM
az apim create \
    --resource-group "my-api-rg" \
    --name "mi-apim-instance" \
    --organization "Mi Empresa" \
    --admin-email "admin@miempresa.com" \
    --sku-name "Developer_1" \
    --location "eastus"
```

### 2. Publicar tu Primera API

```xml
<!-- configuration.xml - Definición de API -->
<service>
  <apis>
    <api name="Productos" 
         path="/productos" 
         method="GET">
      <description>API para consultar productos</description>
      <responses>
        <response status="200">
          <description>Lista de productos</description>
          <representation contentType="application/json">
            <schema ref="ProductListSchema"/>
          </representation>
        </response>
      </responses>
    </api>
  </apis>
</service>
```

### 3. Configurar Políticas Básicas

```xml
<!-- policy.xml - Políticas de seguridad -->
<policies>
  <inbound>
    <!-- Validar suscripción -->
    <validate-subsription />
    
    <!-- Limitar velocidad: 100 peticiones/minuto -->
    <rate-limit-by-key calls="100" 
                      renewal-period="60" 
                      key-parameter-name="api-key" />
    
    <!-- Transformar request -->
    <set-header name="X-Source" 
                value="APIM-Gateway" 
                exists-action="override" />
  </inbound>
  
  <backend>
    <forward-request track-asynchronous="false" />
  </backend>
  
  <outbound>
    <!-- Añadir header de respuesta -->
    <set-header name="X-API-Version" 
                value="1.0.0" 
                exists-action="override" />
  </outbound>
</policies>
```

## 🔒 Políticas de Seguridad Comunes

### 1. Autenticación con OAuth 2.0

```xml
<!-- policy.xml - OAuth 2.0 -->
<policies>
  <inbound>
    <oauth2-server 
        authorization-server-url="https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize"
        client-id="{client-id}"
        scope="api://my-api/.default" />
  </inbound>
</policies>
```

### 2. Validación de JWT

```xml
<!-- policy.xml - JWT Validation -->
<policies>
  <inbound>
    <validate-jwt 
        header-name="Authorization"
        failed-validation-httpcode="401"
        require-scheme="Bearer">
      <openid-config url="https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration" />
      <issuers>
        <issuer>https://login.microsoftonline.com/{tenant-id}/v2.0</issuer>
      </issuers>
    </validate-jwt>
  </inbound>
</policies>
```

### 3. Rate Limiting Avanzado

```xml
<!-- policy.xml - Rate Limiting por IP -->
<policies>
  <inbound>
    <rate-limit-by-key calls="1000" 
                      renewal-period="60" 
                      counter-name="requests"
                      key="@(context.Request.IpAddress)" 
                      violation-event-name="ip-rate-violation" />
  </inbound>
</policies>
```

## 📊 Monitorización y Analytics

### 1. Métricas Principales

| Métrica | Descripción | Alerta Recomendada |
|---------|-------------|-------------------|
| **Latencia P95** | Tiempo de respuesta 95% peticiones | > 2 segundos |
| **Error Rate** | % de respuestas 4xx/5xx | > 1% |
| **Throughput** | Peticiones por minuto | Umbral personalizado |
| **Bandwidth** | Ancho de banda utilizado | 80% del límite |

### 2. Configurar Alertas con Logic Apps

```json
// logic-app.json - Alerta de alta latencia
{
  "definition": {
    "triggers": {
      "when_a_metric_crosses_threshold": {
        "conditions": [
          {
            "metricName": "ApiLatency",
            "operator": "GreaterThan",
            "threshold": 2000,
            "windowSize": "PT5M"
          }
        ]
      }
    },
    "actions": {
      "send_email_alert": {
        "type": "SendEmail",
        "inputs": {
          "to": "admin@miempresa.com",
          "subject": "Alerta: Alta latencia en API",
          "body": "La latencia promedio supera 2 segundos"
        }
      }
    }
  }
}
```

## 💡 Casos de Uso Avanzados

### 1. Backend Aggregation

```xml
<!-- policy.xml - Combinar múltiples backends -->
<policies>
  <inbound>
    <set-backend-service base-url="https://api.miempresa.com" />
    <forward-request />
  </inbound>
  <backend>
    <include-variable name="response1" value="@(((HttpResponseMessage)context.Variables["response1"]).Content)" />
    <include-variable name="response2" value="@(((HttpResponseMessage)context.Variables["response2"]).Content)" />
  </backend>
</policies>
```

### 2. Transformación de Respuesta

```xml
<!-- policy.xml - Convertir XML a JSON -->
<policies>
  <outbound>
    <transform-content 
        old-format="Xml" 
        new-format="Json" 
        template="@("{" + 
                    "\"id\": @(context.Response.Body.As<XElement>().Attribute(\"id\").Value)," +
                    "\"name\": @(context.Response.Body.As<XElement>().Attribute(\"name\").Value)" +
                    "}" )" />
  </outbound>
</policies>
```

### 3. Cache de Respuestas

```xml
<!-- policy.xml - Cache por 5 minutos -->
<policies>
  <inbound>
    <cache-lookup-content duration="300" 
                         key="@("product-" + context.Request.Url.Query.GetValueOrDefault("id"))" />
  </inbound>
  <backend>
    <forward-request />
  </backend>
  <outbound>
    <cache-store-content duration="300" />
  </outbound>
</policies>
```

## 🚀 Mejores Prácticas

### 1. Organización de APIs

```
📁 APIM Instance
├── 📂 Public APIs
│   ├── /v1/products
│   ├── /v1/orders
│   └── /v1/customers
├── 📂 Internal APIs
│   ├── /internal/reports
│   └── /internal/admin
└── 📂 Partner APIs
    ├── /partner/shipping
    └── /partner/inventory
```

### 2. Naming Conventions

```xml
<!-- Convenciones de nomenclatura -->
<api name="productos-v1" path="/v1/productos" />
<api name="pedidos-v1" path="/v1/pedidos" />
<api name="clientes-v1" path="/v1/clientes" />
```

### 3. Versionado de APIs

```bash
# Estrategia de versionado recomendada
# Opción 1: Path-based (recomendada)
/v1/productos
/v2/productos

# Opción 2: Header-based
X-API-Version: 1.0
X-API-Version: 2.0
```

## 📈 Comparativa con Otros API Gateways

| Característica | Azure APIM | AWS API Gateway | Kong | Apigee |
|----------------|------------|-----------------|------|--------|
| **Integración Azure** | Nativa | Limitada | Manual | Manual |
| **Costo (1M req)** | $3.50 | $3.50 | $2.00 | $4.00 |
| **Políticas XML** | ✅ Sí | ❌ No | ✅ Sí | ✅ Sí |
| **Developer Portal** | ✅ Incluido | ❌ Extra | ✅ Extra | ✅ Incluido |
| **Rendimiento** | Alto | Alto | Muy Alto | Alto |

## 🎓 Recursos Adicionales

### 1. Cheat Sheet de Políticas

```xml
<!-- Políticas esenciales para memorizar -->
<validate-subsription />           <!-- Validar API key -->
<rate-limit-by-key />              <!-- Limitar velocidad -->
<set-header />                     <!-- Modificar headers -->
<forward-request />                <!-- Forward a backend -->
<cache-lookup-content />           <!-- Cache responses -->
<auth-oauth2 />                    <!-- OAuth2 authentication -->
```

### 2. Templates de Prompts

```markdown
# Generar política de rate limiting
"Crea una política de APIM que limite a 100 peticiones/minuto por IP"

# Configurar autenticación JWT
"Necesito configurar validación de JWT en APIM con Azure AD"

# Crear developer portal
"Guía para personalizar el developer portal de APIM"
```

---
*Artículo unificado a partir de múltiples conversaciones sobre Azure API Management.*
*Categoría: Programación*
