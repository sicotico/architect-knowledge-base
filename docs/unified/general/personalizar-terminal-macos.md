---
title: Personalizar Terminal macOS
date: 2025-02-28
category: General
slug: personalizar-terminal-macos
tags: ['General']
author: 'Piconocimiento'
reading_time: 5
---

# Personalizar Terminal macOS


> **Nota:** Este artículo es una versión unificada y mejorada de múltiples conversaciones sobre el mismo tema.


## 🎯 Contexto del Proyecto


1. **Puedes enseñarme ejemplos de exa?...**


2. **Estoy en MacOS 15 y quiero personalizar el terminal. ¿Cuál es la manera más sencilla de tener colore...**


3. **
Desintalar ohmyzsh Terminal MAc...**


## 📚 Contenido Unificado


Sí, aquí tienes algunos ejemplos de uso de `exa` en macOS con iconos y colores. Si ya instalaste `exa` con `brew install exa`, prueba estos comandos:

---

### **1. Listar archivos con iconos y colores**
Ejecuta:
```sh
exa --icons
```
**Ejemplo de salida:**
```
📄 archivo.txt    📂 Documentos    📂 Imágenes    📂 Descargas
```

---

### **2. Mostrar detalles de los archivos**
Ejecuta:
```sh
exa -lh --icons
```
Esto muestra permisos, tamaño legible, fecha de modificación e iconos.
**Ejemplo de salida:**
```
drwxr-xr-x  4 usuario  staff   128B  10 feb 15:30 📂 Documentos
drwxr-xr-x  5 usuario  staff   160B  10 feb 15:00 📂 Imágenes
-rw-r--r--  1 usuario  staff   2.3K  09 feb 22:45 📄 notas.txt
-rwxr-xr-x  1 usuario  staff   5.1M  08 feb 10:12 🖥️  programa
```

---

### **3. Mostrar archivos ocultos**
```sh
exa -a --icons
```
Incluye archivos ocultos (`.archivo`).

---

### **4. Mostrar estructura de carpetas en árbol**
```sh
exa -T --icons
```
**Ejemplo de salida:**
```
📂 Proyecto
 ├── 📄 README.md
 ├── 📂 src
 │   ├── 📄 main.py
 │   ├── 📄 utils.py
 ├── 📂 assets
 │   ├── 🖼️  logo.png
```

---

### **5. Ordenar archivos por fecha de modificación (más reciente primero)**
```sh
exa -l --icons --sort newest
```

---

### **6. Mostrar permisos en formato extendido**
```sh
exa -l --icons --git
```
Si la carpeta es un repositorio Git, también muestra el estado de Git.

---

### **7. Alias recomendado para `ls` en `~/.zshrc`**
Si quieres que `exa` se use automáticamente en lugar de `ls`, agrega esto a `~/.zshrc`:
```sh
alias ls='exa --icons --color=always'
alias ll='exa -lh --icons'
alias la='exa -lha --icons'
alias lt='exa -T --icons'
```
Luego, ejecuta:
```sh
source ~/.zshrc
```

Así, cada vez que uses `ls`, `ll`, `la` o `lt`, `exa` mostrará información de manera más clara.

---

¿Quieres más personalización o tienes dudas?
---


Para personalizar el terminal en **macOS 15 (Sequoia)** con colores e indicadores de carpetas, sigue estos pasos:

---

### 1. **Activar Colores en el Terminal**
Por defecto, macOS usa el shell `zsh`, y puedes habilitar colores en la línea de comandos añadiendo estas configuraciones a tu archivo de configuración.

#### **Editar el archivo de configuración de `zsh`**
Abre el terminal y ejecuta:
```sh
nano ~/.zshrc
```

Luego, agrega las siguientes líneas:

```sh
# Habilitar colores en `ls`
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

# Usar `ls` con colores por defecto
alias ls='ls -G'

# Mostrar una mejor indicación del directorio actual en el prompt
export PS1='%F{blue}%n@%m%f:%F{green}%~%f%# '
```

Guarda el archivo presionando `CTRL + X`, luego `Y` y `Enter`.

Aplica los cambios con:
```sh
source ~/.zshrc
```

---

### 2. **Mostrar Indicadores de Carpetas**
Para mostrar iconos o indicadores de carpetas en `ls`, usa `exa` en lugar de `ls`.

#### **Instalar `exa` (Alternativa mejorada de `ls`)**
Si tienes **Homebrew** instalado, ejecuta:
```sh
brew install exa
```

Luego, reemplaza `ls` por `exa` con alias:
```sh
alias ls='exa --icons --color=always'
```

Si quieres una vista más detallada con permisos y fechas, usa:
```sh
alias ll='exa -lh --icons'
```

Aplica los cambios nuevamente con:
```sh
source ~/.zshrc
```

Ahora, cuando ejecutes `ls`, verás los nombres de archivos y carpetas con colores e iconos.

---

### 3. **Usar un Tema Personalizado con Oh My Zsh**
Si quieres una personalización más avanzada, instala **Oh My Zsh** y usa un tema con un buen prompt.

#### **Instalar Oh My Zsh**
```sh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Una vez instalado, puedes cambiar el tema editando `.zshrc`:

```sh
nano ~/.zshrc
```

Busca la línea:
```sh
ZSH_THEME="robbyrussell"
```
Y cámbiala por:
```sh
ZSH_THEME="agnoster"
```
o prueba otros temas como `"powerlevel10k"` para una personalización más avanzada.

Luego, recarga la configuración:
```sh
source ~/.zshrc
```

---

### **Resultado**
- Los archivos y carpetas se mostrarán con colores.
- `ls` mostrará iconos de carpetas y archivos con `exa`.
- El prompt indicará en qué carpeta estás de manera más visible.

Si necesitas más ayuda o quieres probar diferentes estilos, dime cómo te gustaría que se vea tu terminal.
---


Para desinstalar Oh My Zsh en el Terminal de tu Mac y restaurar la configuración anterior, sigue estos pasos:

**1. Ejecutar el script de desinstalación:**

Oh My Zsh incluye un script que facilita su desinstalación. Para ejecutarlo:

- Abre la aplicación Terminal.
- Escribe el siguiente comando y presiona Enter:

  
```bash
  uninstall_oh_my_zsh
  ```


Este comando eliminará Oh My Zsh y restaurará tu configuración anterior de `zsh` o `bash`. citeturn0search5

**2. Alternativa manual si el script no está disponible:**

Si el comando anterior no funciona, puedes desinstalar Oh My Zsh manualmente:

- Abre el Terminal.
- Elimina el directorio de Oh My Zsh ejecutando:

  
```bash
  rm -rf ~/.oh-my-zsh
  ```


- Si deseas restaurar tu configuración anterior de `zsh`, reemplaza el archivo `.zshrc` actual con el respaldo creado durante la instalación de Oh My Zsh:

  
```bash
  mv ~/.zshrc.pre-oh-my-zsh ~/.zshrc
  ```


- Si prefieres volver a `bash` como shell predeterminado, ejecuta:

  
```bash
  chsh -s /bin/bash
  ```


  Luego, elimina el archivo `.zshrc`:

  
```bash
  rm ~/.zshrc
  ```


**3. Reiniciar el Terminal:**

Después de completar los pasos anteriores, cierra y vuelve a abrir el Terminal para aplicar los cambios.

Para una guía visual sobre cómo desinstalar Oh My Zsh y alternativas recomendadas, puedes consultar el siguiente video:

[Uninstall Oh My ZSH Right Now And Do This Instead](https://www.youtube.com/watch?v=21_WkzBErQk)

Siguiendo estos pasos, podrás desinstalar Oh My Zsh de tu Mac y restaurar la configuración original de tu Terminal.
---


Personalizar el Terminal en tu Mac puede mejorar tanto su apariencia como su funcionalidad. A continuación, te presento algunas recomendaciones para lograrlo:

**1. Cambiar la apariencia del Terminal predeterminado:**

Puedes modificar el aspecto del Terminal ajustando colores, fuentes y efectos. Para ello:

- Abre la aplicación Terminal.
- Ve a `Terminal` > `Configuración` en la barra de menú.
- Haz clic en `Perfiles` y selecciona un perfil existente o crea uno nuevo.
- En la pestaña `Texto`, puedes cambiar la fuente, el color del texto y del fondo, así como aplicar efectos de transparencia.

Estos ajustes te permitirán adaptar la apariencia del Terminal a tus preferencias. citeturn0search1

**2. Utilizar iTerm2 para mayor personalización:**

iTerm2 es una alternativa al Terminal de macOS que ofrece más opciones de personalización y funcionalidades avanzadas. Para instalarlo:

- Si no tienes Homebrew instalado, primero instálalo ejecutando en el Terminal:

  
```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```


- Luego, instala iTerm2 con:

  
```bash
  brew install --cask iterm2
  ```


Una vez instalado, puedes personalizar iTerm2 de manera similar al Terminal predeterminado, pero con opciones adicionales. citeturn0search3

**3. Mejorar la funcionalidad con Zsh y Oh My Zsh:**

Zsh es un shell más avanzado que Bash, y Oh My Zsh es un framework que facilita su gestión y personalización. Para instalarlos:

- Instala Zsh utilizando Homebrew:

  
```bash
  brew install zsh
  ```


- Configura Zsh como tu shell predeterminado ejecutando:

  
```bash
  chsh -s /bin/zsh
  ```


- Instala Oh My Zsh con:

  
```bash
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
  ```


Con Oh My Zsh, puedes añadir temas y plugins que mejoran la funcionalidad y apariencia de tu Terminal. citeturn0search3

**4. Personalizar el prompt con Powerlevel10k:**

Powerlevel10k es un tema para Zsh que ofrece un prompt altamente configurable y atractivo. Para instalarlo:

- Clona el repositorio de Powerlevel10k en el directorio de temas de Oh My Zsh:

  
```bash
  git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
  ```


- Edita el archivo de configuración de Zsh (`~/.zshrc`) y establece el tema:

  
```bash
  ZSH_THEME="powerlevel10k/powerlevel10k"
  ```


- Aplica los cambios recargando la configuración:

  
```bash
  source ~/.zshrc
  ```


Al reiniciar el Terminal, se iniciará un asistente de configuración para personalizar el prompt según tus preferencias. citeturn0search3

**5. Añadir funcionalidades adicionales:**

Existen herramientas que pueden mejorar aún más tu experiencia en el Terminal:

- **lsd**: Una versión mejorada del comando `ls` con colores y formatos adicionales. Instálalo con:

  
```bash
  brew install lsd
  ```


- **ccat**: Una alternativa al comando `cat` que añade resaltado de sintaxis. Instálalo con:

  
```bash
  brew install ccat
  ```


- **lolcat**: Una herramienta que aplica colores arcoíris a la salida de comandos. Instálala con:

  
```bash
  gem install lolcat
  ```


Estas herramientas añadirán funcionalidad y estilo a tu Terminal. citeturn0search4

Para una guía visual y más detallada sobre cómo personalizar tu Terminal en macOS, te recomiendo el siguiente video:

videoComo PERSONALIZAR la terminal de MAC | 2024turn0search0

Siguiendo estos pasos, podrás personalizar tu Terminal en Mac para que se adapte a tus necesidades y preferencias estéticas.
---


Oh My Zsh y Oh My Posh son herramientas diseñadas para mejorar y personalizar la experiencia en la línea de comandos, pero tienen enfoques y ámbitos de aplicación distintos. A continuación, se detallan sus diferencias principales:

**Oh My Zsh:**

- **Enfoque y Funcionalidad:** Es un framework de código abierto destinado a gestionar la configuración del shell Zsh. Proporciona una amplia gama de plugins y temas que enriquecen la funcionalidad y apariencia del terminal. citeturn0search7

- **Compatibilidad:** Funciona exclusivamente con el shell Zsh, comúnmente utilizado en sistemas Unix y Unix-like, como macOS y diversas distribuciones de Linux.

- **Características Destacadas:**
  - **Plugins:** Incluye más de 300 plugins que abarcan desde integración con sistemas de control de versiones hasta herramientas de desarrollo específicas.
  - **Temas:** Ofrece más de 150 temas predefinidos para personalizar el prompt del terminal.

**Oh My Posh:**

- **Enfoque y Funcionalidad:** Es un motor de prompts personalizables que permite diseñar y configurar el aspecto del prompt en diversos shells mediante un archivo de configuración. citeturn0search1

- **Compatibilidad:** Es multiplataforma y multishell, compatible con PowerShell, Bash, Zsh, Fish y otros. Esto lo hace especialmente útil para usuarios que trabajan en entornos heterogéneos o que prefieren una herramienta unificada para diferentes shells.

- **Características Destacadas:**
  - **Configuración Centralizada:** Permite definir la apariencia del prompt mediante un único archivo de configuración, facilitando la portabilidad y consistencia entre diferentes entornos.
  - **Temas Personalizables:** Aunque no es compatible directamente con los temas de Oh My Zsh, ofrece la posibilidad de recrear o adaptar temas según las preferencias del usuario. citeturn0search5

**Compatibilidad y Uso Conjunto:**

Es posible utilizar Oh My Posh junto con Oh My Zsh para aprovechar las capacidades de personalización de ambos. Por ejemplo, un usuario puede gestionar plugins y funciones mediante Oh My Zsh y, simultáneamente, emplear Oh My Posh para personalizar el prompt del terminal. Para lograr esto, se debe instalar Oh My Posh y configurar el archivo `.zshrc` para inicializar el prompt personalizado proporcionado por Oh My Posh. citeturn0search9

**Consideraciones de Rendimiento:**

Al seleccionar entre estas herramientas, es importante tener en cuenta el rendimiento. Algunos usuarios han reportado diferencias en la velocidad y eficiencia entre Oh My Posh y otras soluciones como Starship. Por lo tanto, se recomienda evaluar cuál se adapta mejor a las necesidades y preferencias individuales. citeturn0search2

En resumen, la elección entre Oh My Zsh y Oh My Posh depende del entorno de trabajo y las necesidades específicas del usuario. Oh My Zsh es ideal para quienes utilizan exclusivamente Zsh y buscan una solución integrada con una amplia gama de plugins. Por otro lado, Oh My Posh ofrece una mayor flexibilidad y compatibilidad con múltiples shells, siendo adecuado para entornos diversos o para quienes buscan una configuración de prompt unificada en diferentes plataformas.
---


Sí, puedes utilizar Oh My Zsh en el Terminal nativo de macOS. Oh My Zsh es un framework de código abierto que facilita la gestión y personalización de tu configuración de Zsh, el shell predeterminado en macOS. A continuación, te indico cómo instalar y configurar Oh My Zsh en el Terminal de tu Mac:

**1. Instalar Oh My Zsh:**

Para instalar Oh My Zsh, abre el Terminal y ejecuta el siguiente comando:


```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```


Este comando descargará e instalará Oh My Zsh en tu sistema. citeturn0search1

**2. Configurar el Terminal para usar Zsh:**

Si deseas asegurarte de que el Terminal utilice Zsh por defecto, sigue estos pasos:

- Abre el Terminal y ejecuta:

  
```bash
  chsh -s /bin/zsh
  ```


  Este comando cambia tu shell predeterminado a Zsh. citeturn0search5

- Reinicia el Terminal para que los cambios surtan efecto.

**3. Personalizar Oh My Zsh:**

Después de la instalación, puedes personalizar Oh My Zsh modificando el archivo de configuración `.zshrc`. Para ello:

- Abre el archivo `.zshrc` con tu editor de texto preferido, por ejemplo:

  
```bash
  nano ~/.zshrc
  ```


- Dentro de este archivo, puedes cambiar el tema ajustando la línea `ZSH_THEME="nombre_del_tema"`. Oh My Zsh incluye una variedad de temas que puedes explorar en su [repositorio oficial](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes).

- Además, puedes habilitar plugins agregándolos a la línea `plugins=(git)`, separando cada plugin con un espacio. Por ejemplo:

  
```bash
  plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
  ```


- Guarda los cambios y recarga la configuración ejecutando:

  
```bash
  source ~/.zshrc
  ```


Para una guía visual sobre cómo instalar y configurar Oh My Zsh en el Terminal de macOS, puedes consultar el siguiente video:

[Instalar Oh My Zsh en el Terminal de macOS - Guía Paso a Paso](https://www.youtube.com/watch?v=LVp2ebDWRZE)

Siguiendo estos pasos, podrás disfrutar de las funcionalidades y personalizaciones que ofrece Oh My Zsh en el Terminal nativo de tu Mac.

---
*Artículo unificado a partir de 2 conversaciones con 12 mensajes totales.*
*General*
