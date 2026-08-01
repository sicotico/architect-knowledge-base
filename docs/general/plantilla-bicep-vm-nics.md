---
title: Plantilla Bicep VM NICs
date: 2025-02-18
category: General
slug: plantilla-bicep-vm-nics
tags: ['General']
---

# Plantilla Bicep VM NICs


> **Pregunta original:**
> 
Necesito un ejemplo de plantilla de Bicep que muestre una máquina virtual y dos tarjetas de red asociadas a la máquina virtual 
> Cual seria un valor para esto:
vnet.properties.subnets[0].id
> Tengo es id en bicep:

${virtualNetworks_vnet_eu_e_bii77_001_externalid}/subnets/subnet-eu-e-bii77priv-db-priv

Y quiero usar subscriptionResourceId()

---


## Respuesta


Aquí tienes un ejemplo de una plantilla **Bicep** que despliega una **máquina virtual** en **Azure** con **dos tarjetas de red (NICs)** asociadas. 

### Características de la plantilla:
- Crea un **grupo de recursos** si no existe.
- Despliega una **máquina virtual** con dos **interfaces de red**.
- Configura una **red virtual (VNet)** y una **subred**.
- Asigna una **IP pública** a una de las NICs.

---

### **Plantilla Bicep**
```bicep
param location string = resourceGroup().location
param vmName string = 'MyVM'
param vmSize string = 'Standard_B1s'
param adminUsername string = 'azureuser'
param adminPassword string = 'P@ssw0rd123!' // Cambiar por una credencial segura o usar Key Vault
var nicNames = [ '${vmName}-nic1' '${vmName}-nic2' ]

resource vnet 'Microsoft.Network/virtualNetworks@2022-01-01' = {
  name: '${vmName}-vnet'
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: ['10.0.0.0/16']
    }
    subnets: [
      {
        name: 'default-subnet'
        properties: {
          addressPrefix: '10.0.1.0/24'
        }
      }
    ]
  }
}

resource publicIp 'Microsoft.Network/publicIPAddresses@2022-01-01' = {
  name: '${vmName}-publicIp'
  location: location
  properties: {
    publicIPAllocationMethod: 'Dynamic'
  }
}

resource nic1 'Microsoft.Network/networkInterfaces@2022-01-01' = {
  name: nicNames[0]
  location: location
  properties: {
    ipConfigurations: [
      {
        name: 'ipconfig1'
        properties: {
          subnet: {
            id: vnet.properties.subnets[0].id
          }
          publicIPAddress: {
            id: publicIp.id
          }
          privateIPAllocationMethod: 'Dynamic'
        }
      }
    ]
  }
}

resource nic2 'Microsoft.Network/networkInterfaces@2022-01-01' = {
  name: nicNames[1]
  location: location
  properties: {
    ipConfigurations: [
      {
        name: 'ipconfig2'
        properties: {
          subnet: {
            id: vnet.properties.subnets[0].id
          }
          privateIPAllocationMethod: 'Dynamic'
        }
      }
    ]
  }
}

resource vm 'Microsoft.Compute/virtualMachines@2022-01-01' = {
  name: vmName
  location: location
  properties: {
    hardwareProfile: {
      vmSize: vmSize
    }
    osProfile: {
      computerName: vmName
      adminUsername: adminUsername
      adminPassword: adminPassword
    }
    storageProfile: {
      imageReference: {
        publisher: 'MicrosoftWindowsServer'
        offer: 'WindowsServer'
        sku: '2019-Datacenter'
        version: 'latest'
      }
      osDisk: {
        createOption: 'FromImage'
        managedDisk: {
          storageAccountType: 'Standard_LRS'
        }
      }
    }
    networkProfile: {
      networkInterfaces: [
        {
          id: nic1.id
          properties: {
            primary: true
          }
        }
        {
          id: nic2.id
        }
      ]
    }
  }
}
```

---

### **Explicación de la plantilla:**
1. **Red Virtual (VNet)** con una **subred**.
2. **IP Pública** asignada a la **primera NIC**.
3. **Dos NICs** creadas y asociadas a la subred.
4. **Máquina Virtual** con Windows Server 2019:
   - **vmSize**: `Standard_B1s` (puedes cambiarlo).
   - **Admin** con credenciales.
   - **Disco OS** estándar.
   - **Redes**: La VM tiene dos **NICs** (una primaria con IP pública y una secundaria con IP privada).

Puedes modificar esta plantilla para adaptarla a tus necesidades, por ejemplo, cambiar la imagen del sistema operativo o agregar discos adicionales.

---

💡 **¿Necesitas más personalización?** Dime si quieres agregar más características, como extensiones, seguridad o configuraciones adicionales. 🚀
---


Si deseas utilizar `subscriptionResourceId()` en **Bicep** para construir el **ID de la subred**, puedes hacerlo de la siguiente manera.

---

### **Cómo usar `subscriptionResourceId()`**
La función `subscriptionResourceId()` en Bicep permite construir la ruta del **ID de un recurso en Azure**, evitando la necesidad de concatenar manualmente cadenas de texto.

#### **Ejemplo basado en tu ID**
Tu ID en formato actual:
```bicep
${virtualNetworks_vnet_eu_e_bii77_001_externalid}/subnets/subnet-eu-e-bii77priv-db-priv
```

Se puede reescribir usando `subscriptionResourceId()`:

```bicep
var subnetId = subscriptionResourceId(
  'Microsoft.Network/virtualNetworks/subnets',
  'vnet-eu-e-bii77-001',  // Nombre de la VNet
  'subnet-eu-e-bii77priv-db-priv'  // Nombre de la Subnet
)
```

---

### **Explicación**
La función `subscriptionResourceId()` toma como parámetros:
1. **Tipo de recurso** → `'Microsoft.Network/virtualNetworks/subnets'`
2. **Nombre de la VNet** → `'vnet-eu-e-bii77-001'`
3. **Nombre de la subred** → `'subnet-eu-e-bii77priv-db-priv'`

Cuando se use este valor en el despliegue de una **NIC** o cualquier otro recurso que requiera un **ID de subred**, se usará así:

```bicep
resource nic 'Microsoft.Network/networkInterfaces@2022-01-01' = {
  name: 'my-nic'
  location: location
  properties: {
    ipConfigurations: [
      {
        name: 'ipconfig1'
        properties: {
          subnet: {
            id: subnetId
          }
        }
      }
    ]
  }
}
```

---

### **Ventajas de `subscriptionResourceId()`**
✅ **Evita la concatenación manual** de strings.  
✅ **Es más limpio y fácil de mantener**.  
✅ **Funciona sin necesidad de definir previamente la VNet en el mismo archivo Bicep**.  

Si tu **VNet ya existe en la suscripción** y **quieres referenciarla sin definirla en Bicep**, este método es ideal.

---

### **¿Necesitas más ayuda?**
Si necesitas hacerlo dinámico o tienes más detalles, dime y te ayudo. 🚀
---


El valor de `vnet.properties.subnets[0].id` se genera automáticamente en la plantilla Bicep cuando se crea la **subred** dentro de la **red virtual (VNet)**. 

### **Cómo se obtiene el valor de `id` en Bicep**
En Bicep, al referenciar la propiedad `.id` de un recurso, se obtiene su **identificador de recurso en Azure**, que sigue este formato:

```plaintext
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}
```

Dado que la plantilla Bicep define la red virtual (`vnet`) y la subred en la siguiente estructura:

```bicep
resource vnet 'Microsoft.Network/virtualNetworks@2022-01-01' = {
  name: '${vmName}-vnet'
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: ['10.0.0.0/16']
    }
    subnets: [
      {
        name: 'default-subnet'
        properties: {
          addressPrefix: '10.0.1.0/24'
        }
      }
    ]
  }
}
```

La subred tiene el índice `0` en la lista `subnets`, por lo que su ID se puede obtener con:

```bicep
vnet.properties.subnets[0].id
```

### **Ejemplo de valor generado para `vnet.properties.subnets[0].id`**
Si el nombre de la VNet es **"MyVM-vnet"**, el nombre de la subred es **"default-subnet"**, y el grupo de recursos es **"MyResourceGroup"**, el valor del ID podría ser algo como:

```plaintext
/subscriptions/12345678-90ab-cdef-1234-567890abcdef/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVM-vnet/subnets/default-subnet
```

> ⚠ **Nota:** Este ID depende del **nombre del recurso, el grupo de recursos y la suscripción en la que se despliega**.

---

### **Cómo usarlo en la plantilla Bicep**
En la configuración de las **NICs**, referenciamos este ID para asignar las interfaces de red a la subred de la VNet creada:

```bicep
subnet: {
  id: vnet.properties.subnets[0].id
}
```

Azure Bicep resolverá automáticamente este valor cuando despliegues la plantilla.

---

💡 **¿Necesitas más ayuda?** Dime si quieres modificar algo o necesitas más explicaciones. 🚀

---
*Generado desde conversación con 6 mensajes.*
*General*
