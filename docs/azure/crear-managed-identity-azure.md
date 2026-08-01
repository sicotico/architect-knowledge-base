---
title: Crear Managed Identity Azure
date: 2025-03-17
category: Azure/Cloud
slug: crear-managed-identity-azure
tags: ['Azure/Cloud', 'azure']
---

# Crear Managed Identity Azure


> **Pregunta original:**
> 
Como lo corrijo?
> como me bajo de azure cloud shell un ficheroi
> Porque me sale el erro y como lo soluciono ?
> 
> *...y 5 preguntas de seguimiento*


---


## Respuesta


Parece que tienes varios problemas al intentar iniciar sesión con una **Managed Identity** en Azure. Aquí te explico cómo corregirlos:

---

### 🔴 **Errores detectados**
1. **`zsh: command not found: az`**
   - Significa que el CLI de Azure no estaba instalado o no estaba en el `PATH`.

2. **`Failed to list subscriptions error="DefaultAzureCredential: failed to acquire a token."`**
   - Falta la variable de entorno `AZURE_TENANT_ID`.
   - Problema con la autenticación de la Managed Identity.

3. **Advertencia de que `--username` está obsoleto**:
   - Debes usar `--client-id`, `--object-id` o `--resource-id` en su lugar.

---

## ✅ **Solución paso a paso**

### 🔹 **Paso 1: Verifica que Azure CLI esté instalado correctamente**
Ejecuta:
```bash
az version
```
Si el comando no funciona, intenta reinstalarlo:

```bash
brew uninstall azure-cli
brew install azure-cli
```

Después de instalar, asegúrate de que `az` esté disponible en tu terminal:
```bash
which az
```
Si no aparece en `/usr/local/bin/az` o `/opt/homebrew/bin/az`, agrega la ruta al `PATH`:

```bash
export PATH="/opt/homebrew/bin:$PATH"
```
Para hacer esto permanente, agrégalo a tu `~/.zshrc` o `~/.bashrc`:
```bash
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

### 🔹 **Paso 2: Configura las variables de entorno necesarias**
Como el error menciona **`AZURE_TENANT_ID` faltante**, debes configurarlo.

1. **Obtén tu `TENANT_ID`**:
   ```bash
   az account show --query tenantId -o tsv
   ```
2. **Exporta la variable en tu terminal**:
   ```bash
   export AZURE_TENANT_ID="<TU_TENANT_ID>"
   ```

Si deseas que esto sea permanente, agrégalo a `~/.zshrc`:
```bash
echo 'export AZURE_TENANT_ID="<TU_TENANT_ID>"' >> ~/.zshrc
source ~/.zshrc
```

---

### 🔹 **Paso 3: Usa `--client-id` en lugar de `--username`**
El mensaje de advertencia indica que el uso de `--username` está **obsoleto**. En su lugar, usa:

```bash
az login --identity --client-id abeab4f6-d00a-40de-9315-42b937d18640
```

Si sigue fallando, prueba con el `object-id` o `resource-id`:

```bash
az login --identity --object-id <OBJECT_ID>
```

o

```bash
az login --identity --resource-id <RESOURCE_ID>
```

Puedes encontrar estos valores con:

```bash
az identity show --name MiManagedIdentity --resource-group MiGrupoRecursos --query "{clientId:clientId, objectId:principalId, resourceId:id}" -o json
```

---

### 🔹 **Paso 4: Verifica la conexión**
Después de iniciar sesión, verifica que la identidad tenga permisos en tu suscripción:

```bash
az account show
```

Si el login fue exitoso pero no ves la suscripción, asigna la identidad a un rol:

```bash
az role assignment create --assignee <clientId> --role "Reader" --scope /subscriptions/<subscription-id>
```

---

## 🎯 **Resumen**
✔ **Instala correctamente Azure CLI** (`brew install azure-cli`).  
✔ **Configura las variables de entorno** (`AZURE_TENANT_ID`).  
✔ **Usa `--client-id` en lugar de `--username`**.  
✔ **Verifica que la identidad tiene permisos** con `az role assignment create`.  

Después de estos pasos, intenta nuevamente ejecutar:

```bash
az login --identity --client-id <CLIENT_ID>
```

🚀 ¡Prueba y dime si aún tienes problemas!
---


Para descargar un archivo desde **Azure Cloud Shell** a tu máquina local, tienes varias opciones:

---

### ✅ **Opción 1: Usar el botón "Download" en Cloud Shell**
Si estás usando el **Azure Portal** ([https://shell.azure.com](https://shell.azure.com)), sigue estos pasos:

1. En **Cloud Shell**, ejecuta:
   ```bash
   ls
   ```
   Para ver los archivos disponibles.

2. Encuentra el archivo que quieres descargar y usa:
   ```bash
   clouddrive download <nombre-del-archivo>
   ```
   Por ejemplo:
   ```bash
   clouddrive download miarchivo.txt
   ```
   Esto generará un enlace de descarga en el **Cloud Shell**, que puedes hacer clic para bajar el archivo a tu máquina.

---

### ✅ **Opción 2: Usar `scp` desde tu máquina local**
Si tienes **SSH habilitado**, puedes usar `scp` para transferir archivos. 

1. **En Cloud Shell**, obtén el nombre del servidor ejecutando:
   ```bash
   echo $SSH_CONNECTION
   ```
   Esto te dará la dirección IP de Cloud Shell.

2. Desde tu **máquina local**, usa:
   ```bash
   scp azureuser@<CLOUD_SHELL_IP>:~/miarchivo.txt .
   ```
   Esto descargará `miarchivo.txt` a tu directorio actual.

---

### ✅ **Opción 3: Mover el archivo a Azure Storage y descargarlo**
Si tienes una cuenta de **Azure Storage**, puedes copiar el archivo allí y luego descargarlo.

1. **Sube el archivo a un contenedor de Storage:**
   ```bash
   az storage blob upload --account-name <tu-storage-account> --container-name <tu-container> --name miarchivo.txt --file miarchivo.txt
   ```

2. **Descárgalo desde tu navegador:**
   - Ve al portal de Azure [https://portal.azure.com](https://portal.azure.com).
   - Busca tu cuenta de **Storage**.
   - Abre el contenedor y haz clic en el archivo para descargarlo.

---

### ✅ **Opción 4: Usar `wget` o `curl` con un enlace de descarga**
Si el archivo es accesible desde una URL pública, puedes descargarlo con:

```bash
wget https://mi-url.com/miarchivo.txt
```
o
```bash
curl -O https://mi-url.com/miarchivo.txt
```

---

## 🎯 **Resumen**
- **Si estás en Cloud Shell del portal**, usa `clouddrive download <archivo>`.
- **Si tienes SSH**, usa `scp` para copiarlo.
- **Si tienes Azure Storage**, súbelo y descárgalo desde el portal.
- **Si el archivo está en internet**, usa `wget` o `curl`.

🚀 ¡Prueba y dime si necesitas más ayuda!
---


Si tienes un **Mac con Apple Silicon (M1, M2, M3)**, necesitas usar contenedores compatibles con la arquitectura **ARM64** (también conocida como `linux/arm64`). Muchas imágenes de Docker ya tienen soporte para **arm64**, pero algunas pueden requerir ajustes.

---

## 🔍 **Cómo elegir el contenedor correcto en Mac Apple Silicon**
### ✅ **1. Verifica si una imagen tiene soporte ARM64**
Antes de usar una imagen, puedes comprobar si tiene soporte para **ARM64** ejecutando:

```bash
docker manifest inspect <image-name> | grep architecture
```

Por ejemplo, para verificar la imagen de PowerShell:

```bash
docker manifest inspect mcr.microsoft.com/powershell | grep architecture
```

Si ves `"architecture": "arm64"`, significa que es compatible.

---

### ✅ **2. Usar imágenes oficiales con soporte ARM64**
Algunas imágenes populares que funcionan en **Mac Apple Silicon** incluyen:

| 📦 Imagen | ✅ Arquitectura Compatible |
|-----------|---------------------------|
| `ubuntu` | ✅ `linux/arm64`, `linux/amd64` |
| `alpine` | ✅ `linux/arm64`, `linux/amd64` |
| `debian` | ✅ `linux/arm64`, `linux/amd64` |
| `nginx` | ✅ `linux/arm64`, `linux/amd64` |
| `node` | ✅ `linux/arm64`, `linux/amd64` |
| `python` | ✅ `linux/arm64`, `linux/amd64` |
| `mcr.microsoft.com/powershell` | ✅ `linux/arm64`, `linux/amd64` |
| `mcr.microsoft.com/dotnet/runtime` | ✅ `linux/arm64`, `linux/amd64` |
| `mcr.microsoft.com/dotnet/sdk` | ✅ `linux/arm64`, `linux/amd64` |

Para ejecutar una de estas imágenes:

```bash
docker run -it --platform linux/arm64 mcr.microsoft.com/powershell
```

---

### ✅ **3. Forzar `linux/arm64` en imágenes que no detectan la arquitectura**
Si una imagen **no tiene soporte oficial** para ARM64 pero quieres intentarlo, usa:

```bash
docker run --platform linux/arm64 <image-name>
```

Por ejemplo, para PowerShell:

```bash
docker run --platform linux/arm64 -it mcr.microsoft.com/powershell
```

Si la imagen no está compilada para ARM64, puedes usar **Rosetta 2** en Mac y forzar `linux/amd64`:

```bash
docker run --platform linux/amd64 <image-name>
```

---

### ⚠ **4. Convertir imágenes a ARM64 con `buildx` (si no hay soporte nativo)**
Si necesitas ejecutar una imagen que **no soporta ARM64**, puedes **reconstruirla** para tu arquitectura:

```bash
docker buildx build --platform linux/arm64 -t mi-imagen-arm64 .
```

Esto recompilará la imagen para Mac Apple Silicon.

---

## 🎯 **Resumen**
✅ Usa imágenes oficiales con soporte para **ARM64** (`linux/arm64`).  
✅ Verifica la compatibilidad con `docker manifest inspect <imagen>`.  
✅ Si la imagen no funciona, usa `--platform linux/arm64` para forzar la arquitectura.  
✅ Para imágenes sin soporte nativo, usa `docker buildx build` para compilarlas en **ARM64**.  

🚀 **¿Necesitas una imagen específica para un servicio en particular?** ¡Dímelo y te ayudo a encontrar la mejor opción! 🎯
---


Para eliminar una imagen de **Docker**, sigue estos pasos:

---

### 🔍 **1. Ver las imágenes disponibles**
Antes de eliminar una imagen, lista las imágenes en tu sistema:

```bash
docker images
```

Esto mostrará una lista de imágenes con su **IMAGE ID** y **REPOSITORY**.

---

### 🗑 **2. Eliminar una imagen específica**
Si ya conoces el nombre o el ID de la imagen, usa:

```bash
docker rmi <image-id>
```
O si prefieres usar el nombre de la imagen:

```bash
docker rmi <image-name>
```

Por ejemplo, para eliminar la imagen de PowerShell:

```bash
docker rmi mcr.microsoft.com/powershell
```

---

### ⚠ **Si la imagen está en uso, forzar eliminación**
Si Docker te dice que la imagen está siendo utilizada por un contenedor, primero elimina el contenedor:

1. **Listar los contenedores en ejecución**:
   ```bash
   docker ps -a
   ```

2. **Eliminar el contenedor asociado**:
   ```bash
   docker rm <container-id>
   ```

3. **Ahora intenta eliminar la imagen de nuevo**:
   ```bash
   docker rmi <image-id>
   ```

Si sigue sin eliminarse, puedes forzar la eliminación con:

```bash
docker rmi -f <image-id>
```

---

### 🧹 **Eliminar todas las imágenes no utilizadas**
Si quieres limpiar imágenes que ya no están en uso:

```bash
docker image prune -a
```

Esto eliminará todas las imágenes no utilizadas, liberando espacio en disco.

---

## 🎯 **Resumen**
- **Eliminar una imagen específica:** `docker rmi <image-name>` o `docker rmi <image-id>`
- **Si está en uso, eliminar primero el contenedor:** `docker rm <container-id>`
- **Forzar eliminación:** `docker rmi -f <image-id>`
- **Eliminar todas las imágenes no usadas:** `docker image prune -a`

🚀 ¡Prueba y dime si necesitas más ayuda!
---


Para crear una **Managed Identity** en **Azure**, puedes optar por dos tipos:

1. **System-assigned (Asignada por el sistema)**: Se vincula a un recurso específico y desaparece si el recurso se elimina.
2. **User-assigned (Asignada por el usuario)**: Puede compartirse entre varios recursos y administrarse de forma independiente.

### 🚀 Pasos para crear una **Managed Identity** en Azure:

### 🔹 Opción 1: **Usando Azure Portal**
1. **Inicia sesión en el Portal de Azure**: [https://portal.azure.com](https://portal.azure.com)
2. **Ve a "Managed Identities"**:
   - Busca "Managed Identities" en la barra de búsqueda.
   - Selecciona "Managed Identities".
3. **Haz clic en "Crear"**:
   - Elige si quieres una **User-assigned** o **System-assigned** identity.
   - Si es **User-assigned**, selecciona la suscripción, grupo de recursos y el nombre.
4. **Revisar y crear**: Confirma la configuración y presiona **Crear**.

### 🔹 Opción 2: **Usando Azure CLI**
Asegúrate de estar autenticado con:
```bash
az login
```

#### **Crear una identidad asignada por el usuario**:
```bash
az identity create --name MiManagedIdentity --resource-group MiGrupoRecursos --location eastus
```
Esto devolverá información como el `clientId` y `principalId`, que necesitarás más adelante.

#### **Asignar permisos a la Managed Identity**:
Por ejemplo, darle acceso de "Lector" en un recurso:
```bash
az role assignment create --assignee <principalId> --role Reader --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group>
```

### 🔹 Opción 3: **Usando PowerShell**
```powershell
New-AzUserAssignedIdentity -ResourceGroupName "MiGrupoRecursos" -Name "MiManagedIdentity" -Location "EastUS"
```

### **Verificación**
Puedes verificar que la identidad se ha creado con:
```bash
az identity show --name MiManagedIdentity --resource-group MiGrupoRecursos
```

⚡ ¡Listo! Ahora puedes usar esta **Managed Identity** para autenticar servicios sin manejar credenciales explícitas. ¿Quieres asignarla a algún servicio específico, como Azure VM, Functions, o Kubernetes? 🚀
---


El error que te aparece:

```
Failed to connect to MSI. Please make sure MSI is configured correctly and check the network connection.
Error detail: HTTPConnectionPool(host='169.254.169.254', port=80): Max retries exceeded with url: /metadata/identity/oauth2/token...
```

Se debe a que **Managed Identity (MSI)** solo funciona dentro de recursos de Azure, como máquinas virtuales, Azure Functions o AKS, y no en tu máquina local.

---

## 🔍 **Causas del error**
1. **Intentando usar Managed Identity en una máquina local**
   - **Managed Identity solo está disponible dentro de Azure**, por lo que `az login --identity` intenta conectarse a `169.254.169.254`, que es la dirección del endpoint MSI dentro de Azure.
   - Como estás en un equipo local, este endpoint no existe y la conexión falla.

2. **Falta de credenciales alternativas**
   - Al usar `az login --identity`, no estás proporcionando credenciales locales válidas.
   - Si necesitas autenticación local, debes usar otra opción como `az login` sin `--identity`.

---

## ✅ **Soluciones**

### 🚀 **Opción 1: Usar Azure CLI con tu usuario personal**
Si estás trabajando desde tu máquina y solo necesitas acceso a Azure, inicia sesión con tu cuenta en lugar de Managed Identity:

```bash
az login
```

Esto abrirá un navegador donde puedes autenticarte con tu cuenta de Azure.

---

### 🚀 **Opción 2: Autenticarse con Managed Identity en una VM de Azure**
Si realmente quieres usar **Managed Identity**, asegúrate de que tu script se está ejecutando en un **recurso de Azure compatible**. Si estás en una VM de Azure, intenta:

```bash
az login --identity
```

Y verifica que la VM tiene una identidad administrada asignada.

---

### 🚀 **Opción 3: Usar `DefaultAzureCredential()` en código (Python)**
Si estás programando y quieres que tu código funcione tanto en local como en Azure, usa el SDK de Azure con `DefaultAzureCredential`, que intentará diferentes métodos de autenticación:

```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

credential = DefaultAzureCredential()
client = ResourceManagementClient(credential, "<subscription-id>")
```

---

### 🚀 **Opción 4: Usar `az ad sp create-for-rbac` (Service Principal)**
Si necesitas autenticación sin iniciar sesión manualmente, crea un Service Principal:

```bash
az ad sp create-for-rbac --name "MiApp" --sdk-auth
```

Esto generará un JSON con credenciales que puedes usar en `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET` y `AZURE_TENANT_ID`.

---

## 🎯 **Resumen**
- **Si estás en local, usa `az login` en lugar de `az login --identity`**.
- **Managed Identity solo funciona en Azure** (VMs, Functions, AKS, etc.).
- **Si necesitas autenticación en código**, usa `DefaultAzureCredential()`.
- **Para autenticación sin login manual, usa un Service Principal (`az ad sp create-for-rbac`)**.

Prueba con la opción que mejor se adapte a tu caso y dime si necesitas más ayuda 🚀
---


Si quieres usar la **Managed Identity** en tu equipo local, necesitarás **Azure Managed Identity for Development**. Sin embargo, las Managed Identities están diseñadas para ejecutarse en recursos de Azure. Para usarlas localmente, puedes simular el entorno con **Azure CLI** o una herramienta como el **Azure Developer CLI**.

---

### 🚀 **Opción 1: Usar Azure CLI para autenticarse como Managed Identity**
Puedes ejecutar el siguiente comando en tu terminal para autenticarte con la identidad gestionada:

```bash
az login --identity --username <clientId>
```

Si tienes una **System-assigned Managed Identity**, usa el `principalId` en lugar del `clientId`.

Para verificar que la autenticación funciona:
```bash
az account show
```

---

### 🚀 **Opción 2: Usar la Identidad en Código (Python, PowerShell, etc.)**
Si estás desarrollando una aplicación en tu equipo local y quieres que use la Managed Identity para autenticarse en Azure, puedes hacerlo con el SDK de Azure.

#### **Python (Azure Identity SDK)**
1. Instala las dependencias:
   ```bash
   pip install azure-identity azure-keyvault-secrets
   ```

2. Usa la Managed Identity en tu código:
   ```python
   from azure.identity import DefaultAzureCredential
   from azure.keyvault.secrets import SecretClient

   credential = DefaultAzureCredential()

   # Ejemplo: Autenticarse en Key Vault
   key_vault_url = "https://mi-keyvault.vault.azure.net"
   client = SecretClient(vault_url=key_vault_url, credential=credential)

   secret = client.get_secret("mi-secreto")
   print(f"Valor del secreto: {secret.value}")
   ```

🔹 **Importante**: Para que esto funcione en local, la Managed Identity debe tener permisos asignados en el recurso.

---

### 🚀 **Opción 3: Usar Managed Identity en PowerShell**
Si quieres usar PowerShell para autenticarte con la Managed Identity:
```powershell
Connect-AzAccount -Identity
```

Para verificar la identidad:
```powershell
Get-AzContext
```

---

### 📌 **Limitaciones de usar Managed Identity en local**
- **No se ejecuta de forma nativa en local**, porque está diseñada para recursos en Azure.
- **Debes usar Azure CLI** para autenticarse con ella desde tu máquina.
- **Si necesitas desarrollo en local**, lo mejor es usar `DefaultAzureCredential()`, que intentará varios métodos de autenticación (incluyendo Managed Identity si está en Azure).

¿Necesitas configurarla para un caso específico como **Azure SQL**, **Storage**, o **AKS**? 🚀
---


Para ejecutar un **contenedor de PowerShell** y mantenerlo activo, usa **Docker** con una de estas opciones:

---

### ✅ **Opción 1: Ejecutar con `-it` y mantener el contenedor interactivo**
Ejecuta el siguiente comando en tu terminal:

```bash
docker run -it mcr.microsoft.com/powershell
```

Esto abrirá una sesión interactiva de PowerShell dentro del contenedor. El contenedor se mantendrá activo mientras la sesión esté abierta.

---

### ✅ **Opción 2: Ejecutar en segundo plano (`-d`) y adjuntarse después**
Si quieres que el contenedor se mantenga activo en segundo plano, usa:

```bash
docker run -d --name mi_powershell mcr.microsoft.com/powershell sleep infinity
```

Explicación:
- `-d`: Ejecuta el contenedor en **modo background**.
- `--name mi_powershell`: Le da un nombre al contenedor.
- `sleep infinity`: Mantiene el contenedor activo indefinidamente.

Para entrar en el contenedor después:

```bash
docker exec -it mi_powershell pwsh
```

---

### ✅ **Opción 3: Usar `entrypoint` para que no se cierre**
Si quieres un comportamiento más flexible, puedes usar:

```bash
docker run -it --entrypoint pwsh mcr.microsoft.com/powershell
```

Esto asegura que el contenedor no se cierre hasta que salgas de PowerShell manualmente.

---

### 📌 **Resumen**
- 🚀 **Modo interactivo:** `docker run -it mcr.microsoft.com/powershell`
- 🏃 **Ejecutar en segundo plano:** `docker run -d --name mi_powershell mcr.microsoft.com/powershell sleep infinity`
- 🔄 **Conectarse a un contenedor en ejecución:** `docker exec -it mi_powershell pwsh`

Si tienes problemas o necesitas configuraciones específicas, dime más detalles. 🚀💻

---
*Generado desde conversación con 16 mensajes.*
*Azure/Cloud*
