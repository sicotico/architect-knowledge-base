---
title: VNet sin costos
date: 2025-02-14
category: Azure/Cloud
slug: vnet-sin-costos
tags: ['Azure/Cloud', 'azure']
---

# VNet sin costos


> **Pregunta original:**
> 
{"code":"InvalidParameter","target":"osProfile.adminPassword","message":"Required parameter 'osProfile.adminPassword' is missing (null)."}
> Como utilizo el fichero de parametros con un plantilla ?
> {"code":"InvalidTemplate","message":"Deployment template validation failed: 'The resource 'Microsoft.Network/networkInterfaces/VM03' at line '841' and column '9' is defined multiple times in a template. Please see https://aka.ms/arm-syntax-resources for usage details.'."}

Como lo soluciono ??
> 
> *...y 5 preguntas de seguimiento*


---


## Respuesta


En **Safari**, no hay una opción nativa para controlar la velocidad de lectura de una web directamente, pero aquí tienes varias formas de hacerlo dependiendo de lo que necesites:

### **1️⃣ Ajustar la velocidad de lectura en "Lectura en voz alta" (Text-to-Speech)**
Si quieres que Safari **lea en voz alta** el contenido de una página web y controlar la velocidad:
1. **Selecciona el texto** de la página web.
2. Haz clic derecho y elige **"Hablar" > "Iniciar habla"**.
3. Para ajustar la velocidad:
   - Ve a **Configuración del sistema > Accesibilidad > Contenido hablado** (en macOS).
   - Ajusta la velocidad de lectura con el control deslizante.

### **2️⃣ Usar el "Modo Lector" para leer más fácilmente**
El **Modo Lector** de Safari elimina distracciones y mejora la legibilidad:
1. Abre la página web en Safari.
2. Haz clic en el **icono de Modo Lector** (líneas horizontales en la barra de direcciones) o presiona `⇧ Shift + ⌘ Command + R`.
3. Puedes ajustar el tamaño de la letra y el fondo para mejorar la lectura.

### **3️⃣ Extensiones para ajustar la velocidad de lectura**
Puedes instalar extensiones en Safari que te permitan **controlar la velocidad de lectura**:
- **Speech Central** o **Read Aloud**: Te permiten leer páginas web en voz alta y ajustar la velocidad.
- **Speed Reading Extensions**: Algunas extensiones como **SwiftRead** (en Chrome, pero funciona con Safari con extensiones compatibles) permiten leer más rápido mostrando palabras de forma rápida.

### **4️⃣ Usar Atajos de Mac (Shortcuts)**
Puedes crear un **atajo** en la app **Atajos** (`Shortcuts`) para que **lea en voz alta el contenido con velocidad ajustable**.

1. Abre la app **Atajos** en macOS.
2. Crea un nuevo atajo con la acción **"Hablar texto"**.
3. Configura la velocidad y guárdalo.
4. Ejecuta el atajo cuando estés en una web.

🔹 **¿Cuál es tu caso de uso?** ¿Quieres mejorar tu lectura rápida o solo controlar la lectura en voz alta?
---


En el **Portal de Azure**, puedes **usar una plantilla (template) para desplegar recursos** de varias formas. Las plantillas de Azure Resource Manager (**ARM templates**) permiten automatizar la creación de recursos sin necesidad de configurarlos manualmente.

---

## **🔹 Métodos para usar una plantilla en el Portal de Azure**
### **1️⃣ Usar una plantilla desde el propio portal**
Si ya tienes una plantilla JSON lista, sigue estos pasos:

1. **Accede al portal de Azure** 👉 [https://portal.azure.com](https://portal.azure.com)
2. En la barra de búsqueda, escribe **"Plantillas"** y selecciona el servicio **Plantillas**.
3. Haz clic en **"Agregar"** para crear una nueva plantilla.
4. En la sección **"Editor de plantillas"**, copia y pega tu **código JSON** de la plantilla.
5. Guarda la plantilla y haz clic en **"Implementar"**.
6. Rellena los parámetros requeridos y haz clic en **"Revisar + Crear"**.

---

### **2️⃣ Implementar una plantilla desde "Crear un recurso"**
Si estás creando un recurso y quieres usar una plantilla:

1. Ve al **Portal de Azure** y haz clic en **"Crear un recurso"**.
2. Busca el servicio que quieres desplegar, por ejemplo, una máquina virtual.
3. Configura los parámetros iniciales y antes de crear el recurso, en la última pestaña, busca **"Descargar plantilla para automatización"**.
4. Se descargará un archivo JSON con la plantilla. Puedes reutilizarlo para futuras implementaciones.

---

### **3️⃣ Implementar una plantilla desde GitHub o una URL**
Si tienes una plantilla en un repositorio o URL:

1. Ve al portal de Azure.
2. En la barra de búsqueda, escribe **"Plantillas de implementación"** y selecciona **"Implementar una plantilla personalizada"**.
3. Haz clic en **"Construir su propia plantilla en el editor"**.
4. En la parte superior, haz clic en **"Cargar archivo"** o usa la opción **"Cargar una plantilla desde URL"**.
5. Ingresa la URL de la plantilla JSON.
6. **Implementa la plantilla** y configura los valores.

---

### **4️⃣ Implementar usando Azure CLI o PowerShell**
Si prefieres hacer la implementación desde la terminal:

#### **🔹 Con Azure CLI**
```bash
az deployment group create --resource-group MiGrupoRecursos --template-file plantilla.json
```

#### **🔹 Con PowerShell**
```powershell
New-AzResourceGroupDeployment -ResourceGroupName "MiGrupoRecursos" -TemplateFile "plantilla.json"
```

---

## **📌 Consejos Finales**
✔ **Validar la plantilla** antes de implementarla.  
✔ **Personalizar parámetros** para hacerla reutilizable.  
✔ **Guardar plantillas en Azure** para futuras implementaciones.  
✔ **Usar GitHub o DevOps** para control de versiones y CI/CD.  

🔹 **¿Qué tipo de recurso necesitas desplegar con una plantilla?** 😊
---


El error:

```json
{"code":"InvalidParameter","target":"osProfile.requireGuestProvisionSignal","message":"The property 'osProfile.requireGuestProvisionSignal' is not valid because the 'Microsoft.Compute/Agentless' feature is not enabled for this subscription."}
```

significa que la propiedad **`osProfile.requireGuestProvisionSignal`** no es válida porque la función **"Agentless"** no está habilitada en tu suscripción de Azure.

---

## **🔹 Cómo solucionar este error**
Tienes dos opciones:

### **✅ Opción 1: Eliminar `requireGuestProvisionSignal` de la plantilla**
Si **no necesitas la funcionalidad "Agentless"**, la solución más rápida es **eliminar la propiedad** de la plantilla `template.json`.

🔎 **Busca la sección `osProfile` de las máquinas virtuales** en el archivo y elimínala.

### **Ejemplo de la configuración actual (con error)**:
```json
"osProfile": {
    "computerName": "[parameters('virtualMachines_VM01_name')]",
    "adminUsername": "admin01",
    "linuxConfiguration": {
        "disablePasswordAuthentication": false,
        "provisionVMAgent": true,
        "patchSettings": {
            "patchMode": "ImageDefault",
            "assessmentMode": "ImageDefault"
        }
    },
    "secrets": [],
    "allowExtensionOperations": true,
    "requireGuestProvisionSignal": true
}
```

### **Corrección (eliminar `requireGuestProvisionSignal`)**:
```json
"osProfile": {
    "computerName": "[parameters('virtualMachines_VM01_name')]",
    "adminUsername": "admin01",
    "linuxConfiguration": {
        "disablePasswordAuthentication": false,
        "provisionVMAgent": true,
        "patchSettings": {
            "patchMode": "ImageDefault",
            "assessmentMode": "ImageDefault"
        }
    },
    "secrets": [],
    "allowExtensionOperations": true
}
```

🔹 **Haz lo mismo para todas las máquinas virtuales en la plantilla (`VM01`, `VM02`, `VM03`, etc.)**.

---

### **✅ Opción 2: Habilitar la función "Agentless" en tu suscripción**
Si realmente necesitas esta funcionalidad, debes **habilitarla en tu suscripción** antes de desplegar la plantilla.

1️⃣ **Ejecuta este comando en Azure CLI**:
```bash
az feature register --namespace "Microsoft.Compute" --name "Agentless"
```

2️⃣ **Verifica si la función se ha habilitado correctamente**:
```bash
az feature show --namespace "Microsoft.Compute" --name "Agentless"
```

Si el estado es **"Registered"**, la función ya está activa. Si el estado es **"Registering"**, espera unos minutos y vuelve a intentarlo.

3️⃣ **Refresca los cambios en tu suscripción**:
```bash
az provider register --namespace "Microsoft.Compute"
```

4️⃣ **Intenta desplegar la plantilla nuevamente**.

---

## **📌 Conclusión**
- **Si "Agentless" no es obligatorio para tu despliegue**, la mejor solución es **eliminar `requireGuestProvisionSignal`** del JSON.
- **Si necesitas "Agentless"**, debes **habilitar la funcionalidad en tu suscripción** antes de volver a desplegar.

Prueba estas soluciones y dime si sigues teniendo problemas. 🚀
---


En Microsoft Azure, la creación de una **Virtual Network (VNet)** en sí misma es gratuita. Sin embargo, aunque la VNet no genera costos directos, hay algunos servicios y configuraciones dentro de la VNet que sí pueden incurrir en costos. Aquí te explico los detalles:

### **📌 Lo que es gratuito en una VNet**
1. **Creación y uso de la VNet** ➝ Definir subredes, configurar espacio de direcciones IP privadas, etc.
2. **Seguridad básica** ➝ Uso de **NSG (Network Security Groups)** sin costos adicionales.
3. **Comunicación dentro de la misma VNet** ➝ El tráfico entre máquinas virtuales en la misma VNet es gratuito.

### **💰 Lo que puede generar costos**
1. **Máquinas virtuales (VMs)** ➝ Si creas una VM dentro de la VNet, pagarás por su uso.
2. **VPN Gateway** ➝ Si usas **VPN Gateway** para conectar tu VNet con otra red (on-premises o en la nube), esto genera costos.
3. **Azure Bastion** ➝ Para acceder a las VMs sin una IP pública, Bastion tiene un costo.
4. **Peering de VNets** ➝ Si conectas dos VNets, el tráfico entre ellas tiene costos asociados.
5. **Firewalls o balanceadores de carga** ➝ Servicios como **Azure Firewall** o **Load Balancer** no son gratuitos.

### **¿Cómo tener una VNet sin pagar?**
Si solo necesitas experimentar con la configuración de redes en Azure sin costos, puedes:
- Crear una **VNet sin VMs**.
- Usar la **Cuenta gratuita de Azure** (incluye $200 por 30 días y servicios gratuitos por 12 meses).
- Configurar **NSGs, rutas y subredes** sin implementar recursos de pago.

Si necesitas algo más avanzado, como VPNs o VMs, entonces sí habrá costos.

📌 **Conclusión:** Puedes crear y configurar una **VNet sin pagar nada**, pero cualquier recurso que consuma procesamiento o tráfico externo podría generar costos.
---


El error **"The resource 'Microsoft.Network/networkInterfaces/VM03' is defined multiple times"** significa que hay más de una definición para la misma **interfaz de red (Network Interface - NIC)** con el mismo nombre en tu plantilla **ARM (Azure Resource Manager)**.

---

## **🔹 Cómo solucionar el error**
### **📌 Paso 1: Identificar las interfaces duplicadas**
1. Busca todas las definiciones de recursos **`Microsoft.Network/networkInterfaces`** en tu archivo `template.json`.
2. Verifica si hay más de una definición con el mismo nombre.

En tu caso, parece que la NIC con el nombre **"VM03"** está definida más de una vez.

---

### **📌 Paso 2: Soluciones posibles**
#### **Opción 1: Renombrar las interfaces de red duplicadas**
Si necesitas ambas interfaces de red, cámbiales el nombre agregando un sufijo para diferenciarlas.

**Ejemplo:**
Antes (Definición duplicada con el mismo nombre `VM03`):
```json
{
  "type": "Microsoft.Network/networkInterfaces",
  "apiVersion": "2024-03-01",
  "name": "[parameters('networkInterfaces_vm03391_name')]",
  "location": "spaincentral",
  ...
},
{
  "type": "Microsoft.Network/networkInterfaces",
  "apiVersion": "2024-03-01",
  "name": "[parameters('networkInterfaces_vm03391_name')]",
  "location": "spaincentral",
  ...
}
```

Después (Renombrar la segunda interfaz):
```json
{
  "type": "Microsoft.Network/networkInterfaces",
  "apiVersion": "2024-03-01",
  "name": "[parameters('networkInterfaces_vm03391_name')]",
  "location": "spaincentral",
  ...
},
{
  "type": "Microsoft.Network/networkInterfaces",
  "apiVersion": "2024-03-01",
  "name": "[parameters('networkInterfaces_vm03391_aux_name')]",
  "location": "spaincentral",
  ...
}
```

---

#### **Opción 2: Eliminar la interfaz de red duplicada**
Si la segunda interfaz de red no es necesaria, simplemente **elimina la segunda definición** del JSON.

Para hacerlo:
1. **Busca todas las definiciones de `Microsoft.Network/networkInterfaces`**.
2. **Verifica si ambas son necesarias** o si una puede eliminarse.
3. **Elimina la duplicada**.

---

### **📌 Paso 3: Validar y volver a desplegar**
Después de aplicar la corrección:
1. **Valida la plantilla** con Azure CLI:
   ```bash
   az deployment group validate --resource-group MiGrupoRecursos --template-file template.json
   ```
   Esto te ayudará a confirmar que no hay más errores antes de implementarla.

2. **Vuelve a desplegar la plantilla**:
   ```bash
   az deployment group create --resource-group MiGrupoRecursos --template-file template.json
   ```

---

✅ **Conclusión:**  
Si hay duplicados, **renómbralos o elimina los que no sean necesarios**. Luego, **valida la plantilla** y vuelve a intentarlo. 🚀
---


En **Azure**, cuando despliegas una plantilla de **Azure Resource Manager (ARM)**, puedes utilizar un **archivo de parámetros** (`parameters.json`) para personalizar la configuración sin modificar la plantilla principal (`template.json`). Esto es muy útil para reutilizar la misma plantilla en diferentes entornos (desarrollo, pruebas, producción).

---

## **📌 Cómo usar un archivo de parámetros con una plantilla**
Existen varios métodos para aplicar un archivo de parámetros al implementar una plantilla en Azure.

---

### **🔹 1. Usando el Portal de Azure**
1️⃣ **Subir la plantilla en el portal**  
- Ve al **Portal de Azure** ([portal.azure.com](https://portal.azure.com)).
- Busca **"Implementar una plantilla personalizada"**.
- Haz clic en **"Cargar archivo"** y selecciona tu `template.json`.

2️⃣ **Cargar el archivo de parámetros**  
- En la sección de parámetros, selecciona **"Cargar un archivo"** y elige tu `parameters.json`.
- Azure aplicará automáticamente los valores definidos en el archivo.

3️⃣ **Revisar y desplegar**  
- Verifica que los valores sean correctos.
- Haz clic en **"Revisar + Crear"**.

---

### **🔹 2. Usando Azure CLI**
Si trabajas en la terminal, puedes desplegar una plantilla junto con su archivo de parámetros usando **Azure CLI**:

```bash
az deployment group create \
  --resource-group MiGrupoRecursos \
  --template-file template.json \
  --parameters parameters.json
```

O si quieres definir algunos parámetros manualmente junto con el archivo:

```bash
az deployment group create \
  --resource-group MiGrupoRecursos \
  --template-file template.json \
  --parameters parameters.json nombreVM="MiNuevaVM"
```

---

### **🔹 3. Usando PowerShell**
Si prefieres **Azure PowerShell**, puedes hacerlo con el siguiente comando:

```powershell
New-AzResourceGroupDeployment `
  -ResourceGroupName "MiGrupoRecursos" `
  -TemplateFile "template.json" `
  -TemplateParameterFile "parameters.json"
```

También puedes sobrescribir un parámetro en la línea de comandos:

```powershell
New-AzResourceGroupDeployment `
  -ResourceGroupName "MiGrupoRecursos" `
  -TemplateFile "template.json" `
  -TemplateParameterFile "parameters.json" `
  -nombreVM "MiNuevaVM"
```

---

## **📌 Ejemplo de un Archivo de Parámetros (`parameters.json`)**
Un archivo de parámetros sigue el siguiente formato JSON:

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "nombreVM": {
      "value": "MiServidorAzure"
    },
    "tamañoVM": {
      "value": "Standard_DS1_v2"
    },
    "ubicacion": {
      "value": "eastus"
    }
  }
}
```
**📌 Notas:**
- Los nombres de los parámetros en `parameters.json` **deben coincidir** con los de `template.json`.
- Usa `"value"` para definir los valores.
- Puedes cambiar fácilmente valores sin tocar la plantilla.

---

## **✅ Beneficios de Usar Archivos de Parámetros**
✔ **Reutilización** de plantillas sin modificar el código JSON.  
✔ **Fácil cambio de valores** según el entorno (Dev, QA, Prod).  
✔ **Automatización** en despliegues con scripts o pipelines CI/CD.  

---

🔹 **¿Necesitas ayuda con una plantilla en particular?** 🚀
---


El error:

```json
{"code":"InvalidParameter","target":"osProfile.adminPassword","message":"Required parameter 'osProfile.adminPassword' is missing (null)."}
```

significa que la plantilla de **Azure ARM** está intentando desplegar máquinas virtuales **sin una contraseña de administrador**, lo cual es un requisito si **`disablePasswordAuthentication` está en `false`** en la configuración de Linux.

---

## **🔹 Soluciones**
Tienes **dos opciones** según el método de autenticación que deseas usar:

### **✅ Opción 1: Agregar la contraseña del administrador (`adminPassword`)**
Si quieres permitir autenticación con contraseña en las VMs, debes asegurarte de que **`adminPassword` esté definido** en `osProfile`.

📌 **Busca la configuración `osProfile` de cada VM** y agrégale el campo `adminPassword`.

#### **Antes (con error)**
```json
"osProfile": {
    "computerName": "[parameters('virtualMachines_VM01_name')]",
    "adminUsername": "admin01",
    "linuxConfiguration": {
        "disablePasswordAuthentication": false,
        "provisionVMAgent": true,
        "patchSettings": {
            "patchMode": "ImageDefault",
            "assessmentMode": "ImageDefault"
        }
    }
}
```

#### **Corrección (Agregar `adminPassword`)**
```json
"osProfile": {
    "computerName": "[parameters('virtualMachines_VM01_name')]",
    "adminUsername": "admin01",
    "adminPassword": "[parameters('adminPassword')]",
    "linuxConfiguration": {
        "disablePasswordAuthentication": false,
        "provisionVMAgent": true,
        "patchSettings": {
            "patchMode": "ImageDefault",
            "assessmentMode": "ImageDefault"
        }
    }
}
```

🔹 **Además, debes definir el parámetro `adminPassword` en la sección `parameters`** de la plantilla ARM:

```json
"parameters": {
    "adminPassword": {
        "type": "securestring"
    }
}
```

Cuando despliegues la plantilla, deberás proporcionar la contraseña segura.

---

### **✅ Opción 2: Usar autenticación con SSH en lugar de contraseña**
Si prefieres **usar claves SSH en vez de una contraseña**, puedes **eliminar el campo `adminPassword`** y asegurarte de que `disablePasswordAuthentication` esté en `true`.

#### **Corrección: Deshabilitar contraseña y habilitar SSH**
```json
"osProfile": {
    "computerName": "[parameters('virtualMachines_VM01_name')]",
    "adminUsername": "admin01",
    "linuxConfiguration": {
        "disablePasswordAuthentication": true,
        "ssh": {
            "publicKeys": [
                {
                    "path": "/home/admin01/.ssh/authorized_keys",
                    "keyData": "[parameters('sshPublicKey')]"
                }
            ]
        },
        "provisionVMAgent": true,
        "patchSettings": {
            "patchMode": "ImageDefault",
            "assessmentMode": "ImageDefault"
        }
    }
}
```

🔹 **También necesitas agregar el parámetro `sshPublicKey` en la plantilla:**
```json
"parameters": {
    "sshPublicKey": {
        "type": "string",
        "metadata": {
            "description": "Clave pública SSH para acceso a la VM."
        }
    }
}
```
Al desplegar la plantilla, debes proporcionar una clave SSH válida.

---

## **✅ Conclusión**
✔ **Si quieres usar contraseña:** Asegúrate de definir `adminPassword` en la plantilla.  
✔ **Si prefieres SSH:** Usa `disablePasswordAuthentication: true` y proporciona una clave SSH.  

🔹 **Elige la opción que mejor se adapte a tu entorno** y prueba de nuevo el despliegue. 🚀
---


El error `"Parameter 'osDisk.managedDisk.id' is not allowed."` ocurre porque en la definición del disco del sistema operativo (`osDisk`) de las máquinas virtuales se está utilizando una propiedad `managedDisk.id`, la cual no es válida cuando el disco se crea junto con la VM a partir de una imagen.

### **📌 Cómo solucionar el problema**
Debes eliminar la propiedad `managedDisk.id` dentro del `osDisk` en la sección `"storageProfile"` de cada máquina virtual.

---

#### **🚀 Solución**
En tu archivo **`template.json`**, busca esta sección dentro de cada recurso `Microsoft.Compute/virtualMachines`:

```json
"osDisk": {
    "osType": "Linux",
    "name": "[concat(parameters('virtualMachines_VM01_name'), '_OsDisk_1_80a4aa79817a4c62873eac3e808c4bb3')]",
    "createOption": "FromImage",
    "caching": "ReadWrite",
    "managedDisk": {
        "id": "[resourceId('Microsoft.Compute/disks', concat(parameters('virtualMachines_VM01_name'), '_OsDisk_1_80a4aa79817a4c62873eac3e808c4bb3'))]"
    },
    "deleteOption": "Delete"
}
```

🔴 **Error:** `managedDisk.id` está definido, pero solo se usa cuando un disco ya existe y se quiere adjuntar a la VM.

---

✅ **Corrección**
Reemplaza la configuración errónea por esta:

```json
"osDisk": {
    "osType": "Linux",
    "name": "[concat(parameters('virtualMachines_VM01_name'), '_OsDisk_1')]",
    "createOption": "FromImage",
    "caching": "ReadWrite",
    "managedDisk": {
        "storageAccountType": "Standard_LRS"
    },
    "deleteOption": "Delete"
}
```

---

### **📌 Explicación de la solución**
1. **Se elimina `"id": "[resourceId('Microsoft.Compute/disks', ...)]"`**, ya que no se debe especificar un ID para un disco creado en la misma plantilla.
2. **Se añade `"storageAccountType": "Standard_LRS"`** en `managedDisk`, que es obligatorio para los discos gestionados.
3. **Se mantiene `"createOption": "FromImage"`**, que indica que el disco se generará a partir de la imagen del SO.

---

### **📌 Aplicar la solución en todas las VMs**
Debes hacer esto en todas las máquinas virtuales (`VM01`, `VM02`, `VM03`), asegurándote de modificar la sección `osDisk` en cada una.

Si tienes más VMs con este problema, repite la corrección en cada una.

Después de hacer estos cambios, intenta desplegar la plantilla nuevamente y el error debería solucionarse. 🚀

---
*Generado desde conversación con 16 mensajes.*
*Azure/Cloud*
