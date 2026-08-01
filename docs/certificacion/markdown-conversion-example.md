---
title: Markdown Conversion Example
date: 2024-09-14
category: Certificaciones
slug: markdown-conversion-example
tags: ['Certificaciones']
---

# Markdown Conversion Example


> **Pregunta original:**
> 
Convertir a markdown

> Prefiero que lo conviertas a word 
> Quiero que conviertas el PDF , aunque sean imágenes y lo conviertas en word
> 
> *...y 1 preguntas de seguimiento*


---


## Respuesta


It seems there is an issue with the text formatting from the PDF, which contains some characters that are not compatible with the Word format. I'll modify the extraction process to handle this and attempt the conversion again.

Let me try another approach to complete the conversion.
---


I have provided a visual representation of the content from the Microsoft AZ-305 exam preparation. If you'd prefer to have the PDF content added to a Word document as images, I can proceed with that. Let me know how you'd like to continue!
---


It seems the document is quite large, and due to its length, the system is not allowing me to process it all at once. However, I can extract and convert the content to Markdown incrementally. I will begin by converting sections of the file to Markdown.

Let me start with the next section and convert it for you. I'll proceed to extract part of the document and convert it now.
---


To convert the file to Markdown format, I'll first extract a sample of the content and provide a conversion example. Here's a small portion converted from the original text to Markdown.

**Original:**

```
Litware, Inc. is a medium-sized finance company.

Litware has a main office in Boston.

The network contains an Active Directory forest named Litware.com that is linked to an Azure Active
Directory (Azure AD) tenant named Litware.com. All users have Azure Active Directory Premium P2 licenses.

Litware has a second Azure AD tenant named dev.Litware.com that is used as a development
environment.
```

**Markdown:**

```markdown
# Litware, Inc. Case Study

Litware, Inc. is a medium-sized finance company.

## Physical Locations
- Litware has a main office in Boston.

## Existing Environment

### Identity Environment
- The network contains an Active Directory forest named **Litware.com** that is linked to an Azure Active Directory (Azure AD) tenant named **Litware.com**.
- All users have Azure Active Directory Premium P2 licenses.
- Litware has a second Azure AD tenant named **dev.Litware.com** that is used as a development environment.
```

If you'd like to convert the entire document to Markdown, I can process it in stages. Let me know if you'd prefer this approach!
---


Here is a Markdown conversion for a portion of your document based on the extracted content:

```markdown
# Litware, Inc. Case Study

## Overview

Litware, Inc. is a medium-sized finance company.

### Physical Locations
- Main office located in Boston.

## Existing Environment

### Identity Environment
- The network contains an Active Directory forest named **Litware.com** linked to an Azure Active Directory (Azure AD) tenant named **Litware.com**.
- All users have Azure Active Directory Premium P2 licenses.
- A second Azure AD tenant, **dev.Litware.com**, is used for development purposes.
- Conditional access policy **capolicy1** requires users managing Azure subscriptions in production to connect via hybrid Azure AD-joined devices.

### Azure Environment
- Litware has 10 Azure subscriptions linked to the **Litware.com** tenant.
- There are five additional Azure subscriptions linked to the **dev.Litware.com** tenant.
- All subscriptions fall under an Enterprise Agreement (EA).
- Custom Azure role-based access control (RBAC) role **Role1** grants DataActions read permissions to Azure Storage blobs and files.

### On-premises Environment
- Litware’s on-premises network includes various resources and is connected to Azure through ExpressRoute.

## Planned Changes and Requirements

### Planned Changes
- **DB1** and **DB2** will be migrated to Azure.
- **App1** will be migrated to Azure virtual machines deployed on Azure dedicated hosts.

### Authentication and Authorization Requirements
- Users managing the production environment via Azure portal must connect from a hybrid Azure AD-joined device and authenticate using Azure Multi-Factor Authentication (MFA).
- The **Network Contributor** built-in RBAC role will grant permission to virtual networks in all Azure subscriptions.
- **App1** will access resources via the managed identity of its hosting virtual machines.
- **Role1** will assign permissions to storage accounts across all Azure subscriptions.
- RBAC roles will be applied at the highest level possible.

### Resiliency Requirements
- **DB1** and **DB2** must maintain availability if two availability zones in the local Azure region fail.
- **App1** must support automatic scaling and maintain availability even if two availability zones in the local Azure region fail.

### Security and Compliance Requirements
- New data must be writeable, and modifications to new and existing data must be prevented for a period of three years.
- On-premises users and services must access the Azure Storage account hosting **App1** data, and public endpoint access to the storage account must be blocked.
- All production Azure SQL databases must have **Transparent Data Encryption (TDE)** enabled.
- **App1** must not share physical hardware with other workloads.

### Business Requirements
- Minimize administrative effort.
- Minimize costs.
```

This is a sample conversion. If you'd like to continue with the conversion or need specific sections converted, let me know!
---


The PDF has been successfully converted to a Word document. You can download it using the link below:

[Download the converted Word document](sandbox:/mnt/data/Microsoft-AZ-305_converted_clean.docx) 

Let me know if you need further assistance!

---
*Generado desde conversación con 10 mensajes.*
*Certificaciones*
