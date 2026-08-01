---
title: Volver a commit anterior
date: 2025-02-14
category: General
slug: volver-a-commit-anterior
tags: ['General']
---

# Volver a commit anterior


> **Pregunta original:**
> 
Desde la web se peude hacer ???
> Estoy en github y necesito volver a un commit anterior 

---


## Respuesta


Para volver a un commit anterior en Git, tienes varias opciones dependiendo de lo que quieras hacer exactamente:

### **1. Volver a un commit anterior sin perder cambios (Temporal)**
Si solo quieres revisar el estado de un commit anterior sin cambiar permanentemente la historia:
```bash
git checkout <commit-hash>
```
🔹 **Problema**: Esto coloca tu repositorio en un estado "detached HEAD", lo que significa que no estarás en una rama. Si haces cambios, podrías perderlos.

**Para volver a la última versión de la rama principal:**
```bash
git checkout main  # o la rama en la que estabas antes
```

---

### **2. Crear una nueva rama desde un commit anterior**
Si quieres trabajar desde un commit antiguo sin perder el progreso de la rama actual:
```bash
git checkout -b nueva-rama <commit-hash>
```
Esto crea una nueva rama basada en ese commit, sin afectar la historia principal.

---

### **3. Deshacer cambios y volver a un commit anterior (Permanentemente)**
#### **a) Reset SOFT (mantiene cambios en staging)**
Si solo quieres deshacer commits pero mantener los archivos modificados en "staging":
```bash
git reset --soft <commit-hash>
```

#### **b) Reset MIXED (mantiene archivos pero los saca de staging)**
Si quieres deshacer los commits pero mantener los archivos modificados sin añadirlos al staging:
```bash
git reset --mixed <commit-hash>
```

#### **c) Reset HARD (borra commits y cambios en los archivos)**
Si quieres borrar todo hasta ese commit y perder los cambios posteriores:
```bash
git reset --hard <commit-hash>
```
⚠ **¡Cuidado!** Esto elimina todo lo que hiciste después de ese commit.

---

### **4. Revertir un commit sin modificar la historia**
Si ya publicaste los commits y no quieres eliminarlos, sino deshacer los cambios sin afectar el historial:
```bash
git revert <commit-hash>
```
Esto crea un nuevo commit que revierte los cambios de ese commit específico.

---

### **Cómo encontrar el hash del commit**
Para ver la lista de commits y encontrar el que necesitas:
```bash
git log --oneline
```
Esto mostrará una lista de commits con sus hashes cortos.

Si necesitas más ayuda dime qué quieres hacer exactamente. 🚀
---


No, en la web de GitHub no puedes volver directamente a un commit anterior en el repositorio de manera nativa. Sin embargo, tienes algunas opciones:

### **1. Descargar un Commit Específico**
Si solo quieres obtener el código de un commit anterior sin cambiar la historia del repositorio, puedes:
1. Ir al repositorio en GitHub.
2. Hacer clic en **"Commits"** (encima de la lista de archivos).
3. Hacer clic en el hash del commit que quieres revisar.
4. En la parte superior derecha, hacer clic en **"Browse files"** para ver el código en ese punto.
5. Si necesitas descargarlo, usa el botón **"Download ZIP"**.

---

### **2. Crear una Nueva Rama desde un Commit en GitHub**
Si quieres trabajar con un commit anterior en la web:
1. Ve al historial de commits.
2. Encuentra el commit deseado y haz clic en él.
3. Copia el hash del commit.
4. Abre un terminal local y escribe:
   ```bash
   git checkout -b nueva-rama <commit-hash>
   ```
5. Luego, sube la nueva rama a GitHub:
   ```bash
   git push origin nueva-rama
   ```
   Después de esto, la nueva rama aparecerá en GitHub.

---

### **3. Revertir un Commit desde la Web (Solo en Pull Requests)**
Si hiciste cambios en un Pull Request y ya fue fusionado en **main**, GitHub te permite hacer un **revert**:
1. Ve al **Pull Request** en GitHub.
2. Haz clic en **"Revert"** (aparece solo si el PR ya se fusionó).
3. Esto creará un nuevo PR que revierte los cambios anteriores.

---

Si necesitas hacer un **reset** o **checkout** completo, sí o sí debes hacerlo desde la terminal o GitHub Desktop. ¿Quieres que te ayude con otra opción? 🚀

---
*Generado desde conversación con 4 mensajes.*
*General*
