---
title: Listar Key Vaults Azure
date: 2024-12-16
category: Azure/Cloud
slug: listar-key-vaults-azure
tags: ['Azure/Cloud', 'azure']
---

# Listar Key Vaults Azure


> **Pregunta original:**
> 
Eres un especialista de Azure. Necesito lista todos lo Key Vault y su tipo
> Lo necesito en azure graph

---


## Respuesta


Para listar todos los Azure Key Vaults en tu suscripción y obtener información sobre su tipo, puedes utilizar Azure PowerShell. El cmdlet `Get-AzKeyVault` te permite obtener detalles sobre los Key Vaults en tu suscripción.

Primero, asegúrate de tener el módulo de Azure PowerShell instalado. Si no lo tienes, puedes instalarlo ejecutando:

```powershell
Install-Module -Name Az -AllowClobber -Scope CurrentUser
```

Después, conecta tu cuenta de Azure:

```powershell
Connect-AzAccount
```

Para listar todos los Key Vaults en tu suscripción:

```powershell
Get-AzKeyVault
```

Este comando mostrará una lista de todos los Key Vaults con detalles como el nombre, la ubicación y el grupo de recursos.

En cuanto al "tipo" de Key Vault, si te refieres al tipo de SKU (por ejemplo, Standard o Premium), puedes obtener esta información inspeccionando la propiedad `Sku.Family` de cada Key Vault.

Para obtener una lista con el nombre y el tipo de SKU de cada Key Vault, puedes ejecutar:

```powershell
Get-AzKeyVault | Select-Object VaultName, ResourceGroupName, @{Name="Sku";Expression={$_.Sku.Family}}
```

Este comando mostrará una tabla con el nombre del Key Vault, el grupo de recursos y su tipo de SKU.

Si deseas obtener información más detallada sobre cada Key Vault, puedes revisar la documentación oficial de Microsoft sobre el cmdlet `Get-AzKeyVault`:

- [Documentación de Get-AzKeyVault](https://github.com/Azure/azure-powershell/blob/main/src/KeyVault/KeyVault/help/Get-AzKeyVault.md)

Recuerda que para ejecutar estos comandos necesitas tener los permisos adecuados en tu suscripción de Azure.
---


Para listar todos los Azure Key Vaults y su tipo (SKU) usando Azure Resource Graph, necesitas realizar una consulta mediante Azure CLI o Azure Portal. Aquí está el proceso:

### 1. **Con Azure CLI**
Primero, asegúrate de que tienes la CLI de Azure instalada y configurada. Luego, inicia sesión:

```bash
az login
```

Ejecuta la consulta de Azure Resource Graph:

```bash
az graph query -q "
Resources
| where type =~ 'microsoft.keyvault/vaults'
| project name, location, resourceGroup, properties.sku.family, properties.sku.name
" --query "[].{Name:name, Location:location, ResourceGroup:resourceGroup, SKUFamily:properties_sku_family, SKUName:properties_sku_name}" -o table
```

### 2. **Descripción de la consulta**
- `Resources`: Accede a los recursos en tu suscripción.
- `where type =~ 'microsoft.keyvault/vaults'`: Filtra solo los recursos del tipo Key Vault.
- `project`: Selecciona las columnas que deseas mostrar:
  - `name`: Nombre del Key Vault.
  - `location`: Ubicación del Key Vault.
  - `resourceGroup`: Grupo de recursos al que pertenece.
  - `properties.sku.family`: Familia del SKU (por ejemplo, Standard o Premium).
  - `properties.sku.name`: Nombre del SKU.

### 3. **Resultado**
El comando mostrará una tabla similar a esta:

| Name            | Location | ResourceGroup | SKUFamily | SKUName |
|-----------------|----------|---------------|-----------|---------|
| MyKeyVault      | eastus   | MyResourceGrp | A         | Premium |
| AnotherKeyVault | westus   | OtherGrp      | A         | Standard |

### 4. **Ejecutar desde el Portal de Azure**
Si prefieres el portal:
1. Ve a **Resource Graph Explorer** en Azure Portal.
2. Ejecuta la misma consulta:

```kql
Resources
| where type =~ 'microsoft.keyvault/vaults'
| project name, location, resourceGroup, properties.sku.family, properties.sku.name
```

3. Visualiza y exporta los resultados directamente desde el portal.

Con esto, obtendrás la información necesaria de los Key Vaults y su tipo usando Azure Resource Graph.

---
*Generado desde conversación con 4 mensajes.*
*Azure/Cloud*
