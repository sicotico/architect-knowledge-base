---
title: Contenedor .NET 8 AKS
date: 2025-03-21
category: Azure/Cloud
slug: contenedor-net-8-aks
tags: ['Azure/Cloud', 'azure']
---

# Contenedor .NET 8 AKS


> **Pregunta original:**
> 
Quiero crear un contenedor para AKS. Lo quiero en .Net 8 Core y que sea muy simple, un "Hola mundo"

---


## Respuesta


Perfecto, te ayudo a crear un contenedor Docker en .NET 8 Core con una app muy simple tipo "Hola Mundo", lista para desplegar en AKS (Azure Kubernetes Service).

Aquí tienes todos los pasos para crear el proyecto, el contenedor y dejarlo listo para AKS:

---

### ✅ 1. Crear el proyecto en .NET 8

Abre una terminal y ejecuta:

```bash
dotnet new webapi -n HolaMundoApi --no-https
cd HolaMundoApi
```

Esto crea una API REST básica. Vamos a simplificarla para que solo diga "Hola Mundo".

---

### ✅ 2. Modificar el controlador para devolver "Hola Mundo"

Abre el archivo `Program.cs` y reemplaza todo el contenido con:

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "¡Hola Mundo desde .NET 8!");

app.Run();
```

Así la aplicación solo responde con "¡Hola Mundo!" al hacer un GET al `/`.

---

### ✅ 3. Crear el Dockerfile

En el root del proyecto (`HolaMundoApi`), crea un archivo llamado `Dockerfile` con este contenido:

```dockerfile
# Build stage
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /app

COPY . ./
RUN dotnet publish -c Release -o out

# Runtime stage
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/out .

EXPOSE 80
ENTRYPOINT ["dotnet", "HolaMundoApi.dll"]
```

---

### ✅ 4. Construir y probar el contenedor

```bash
docker build -t holamundo-api .
docker run -p 8080:80 holamundo-api
```

Abre tu navegador en `http://localhost:8080` y deberías ver:  
**¡Hola Mundo desde .NET 8!**

---

### ✅ 5. Publicar en Azure Container Registry (ACR) [opcional si lo necesitas para AKS]

Si estás usando ACR para tu AKS:

```bash
az acr login --name <tu-acr-name>
docker tag holamundo-api <tu-acr-name>.azurecr.io/holamundo-api:v1
docker push <tu-acr-name>.azurecr.io/holamundo-api:v1
```

---

¿Quieres que te ayude también con el manifiesto YAML para desplegar esto en AKS?

---
*Generado desde conversación con 2 mensajes.*
*Azure/Cloud*
