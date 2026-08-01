---
title: Iniciar con Python Básico
date: 2026-07-11
category: Programación
slug: iniciar-con-python-basico
tags: ['Programación']
---

# Iniciar con Python Básico


> **Pregunta original:**
> 
Vamos a empezar con python , desde terminal , ya tengo experiencia en java 15 años de shell script y he probado repos de python con malos resultados por código caótico y difícil de seguir las intrucciones  . Asi que quiero empezar con lo básico de python en mi ordenador. usare Zed o vim según me apetezca. Más o menos lo primero para mi en los entornos y crearme la rutina de crearlo , administrarlo y entenderlo. Luego ya el hola mundo  

---


## Respuesta


Empezaría **sin frameworks, sin gestores “mágicos” y sin repos ajenos**. Primero conviene dominar el entorno estándar de Python: intérprete, `venv`, `pip` y estructura mínima de proyecto.

La idea es que cada proyecto sea autocontenido y reproducible.

# 1. Comprobar qué Python tienes

Desde terminal:

```bash
python3 --version
```

También:

```bash
which python3
python3 -m pip --version
```

En Windows:

```powershell
py --version
py -m pip --version
```

Evita asumir que `python` apunta a Python 3. En muchos sistemas:

```bash
python
```

puede no existir o apuntar a algo distinto. Al principio usaría explícitamente:

```bash
python3
```

o en Windows:

```powershell
py
```

# 2. Crear un proyecto mínimo

```bash
mkdir python-basico
cd python-basico
```

Comprueba dónde estás:

```bash
pwd
ls -la
```

Estructura inicial:

```text
python-basico/
```

Todavía no hace falta añadir `src`, paquetes, tests ni configuración avanzada.

# 3. Crear el entorno virtual

Desde dentro del directorio:

```bash
python3 -m venv .venv
```

Esto crea un intérprete y un conjunto de paquetes aislados dentro de:

```text
.venv/
```

Uso `.venv` porque:

- queda oculto en Unix;
- Zed y otros editores suelen detectarlo;
- deja claro que pertenece al proyecto;
- evita nombres ambiguos como `env`, `python` o `venv1`.

La estructura queda así:

```text
python-basico/
└── .venv/
```

## Qué contiene realmente `.venv`

No es una máquina virtual ni un contenedor. Es un directorio con:

- un ejecutable de Python;
- scripts de activación;
- una instalación local de `pip`;
- un directorio local para dependencias.

Puedes inspeccionarlo:

```bash
find .venv -maxdepth 2 -type d | sort
```

No conviene modificar su contenido manualmente.

# 4. Activar el entorno

En Bash o Zsh:

```bash
source .venv/bin/activate
```

En Fish:

```fish
source .venv/bin/activate.fish
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Al activarlo, normalmente verás algo parecido:

```text
(.venv) usuario@equipo:~/python-basico$
```

Comprueba qué ejecutable está activo:

```bash
which python
python --version
python -m pip --version
```

La ruta debería apuntar al proyecto:

```text
.../python-basico/.venv/bin/python
```

## Qué hace “activar”

La activación no cambia Python internamente. Principalmente modifica temporalmente `PATH` para que:

```bash
python
pip
```

apunten primero a los ejecutables de `.venv`.

Puedes comprobarlo:

```bash
echo "$PATH"
```

Esto es importante: **no es obligatorio activar el entorno**. También podrías ejecutar directamente:

```bash
.venv/bin/python --version
.venv/bin/python -m pip --version
```

La activación es una comodidad de terminal, no un requisito técnico.

# 5. Regla básica para usar `pip`

Dentro del entorno usaría siempre:

```bash
python -m pip
```

en lugar de:

```bash
pip
```

Por ejemplo:

```bash
python -m pip list
```

La razón es sencilla: así sabes qué intérprete está ejecutando `pip`.

Con:

```bash
pip install algo
```

puede haber confusión si hay varios Python instalados.

Con:

```bash
python -m pip install algo
```

la asociación es explícita.

Comprueba los paquetes iniciales:

```bash
python -m pip list
```

Probablemente aparecerán al menos `pip` y quizá algún paquete auxiliar.

# 6. Desactivar el entorno

```bash
deactivate
```

Comprueba de nuevo:

```bash
which python
which python3
```

Después puedes volver a activarlo:

```bash
source .venv/bin/activate
```

Esta rutina debe volverse automática.

# 7. Destruir y reconstruir el entorno

Un entorno virtual debe considerarse **desechable**.

Para borrarlo:

```bash
deactivate 2>/dev/null || true
rm -rf .venv
```

Para reconstruirlo:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip list
```

Esto es preferible a intentar “reparar” entornos deteriorados.

## Ventaja

Si puedes borrar `.venv` y reconstruirlo, el proyecto está bajo control.

## Riesgo

Si instalas paquetes manualmente pero no registras cuáles son, al borrar `.venv` perderás esa información. Más adelante resolveremos eso con un archivo de dependencias y después con `pyproject.toml`.

# 8. Primer archivo Python

Crea:

```bash
vim hello.py
```

o:

```bash
zed hello.py
```

Contenido:

```python
print("Hola, mundo")
```

Ejecuta:

```bash
python hello.py
```

Resultado:

```text
Hola, mundo
```

No necesitas compilarlo manualmente como en Java.

El intérprete:

1. lee el archivo;
2. lo compila internamente a bytecode;
3. ejecuta ese bytecode en la máquina virtual de Python.

Puede aparecer un directorio:

```text
__pycache__/
```

Es normal. Contiene bytecode cacheado, no código fuente.

# 9. Confirmar qué intérprete ejecuta el programa

Modifica `hello.py`:

```python
import sys

print("Hola, mundo")
print(sys.executable)
print(sys.version)
```

Ejecuta:

```bash
python hello.py
```

Deberías ver una ruta dentro de `.venv`:

```text
/ruta/al/proyecto/.venv/bin/python
```

Este pequeño diagnóstico es útil cuando un editor ejecuta un Python diferente del terminal.

# 10. Crear `.gitignore`

Aunque todavía no uses Git, conviene establecer desde el principio qué no pertenece al código fuente.

```bash
cat > .gitignore <<'EOF'
.venv/
__pycache__/
*.pyc
EOF
```

Comprueba:

```bash
cat .gitignore
```

El entorno virtual no debe versionarse. Puede ser grande, depende del sistema operativo y contiene rutas locales.

# 11. Rutina diaria recomendada

Al empezar a trabajar:

```bash
cd ~/ruta/python-basico
source .venv/bin/activate
which python
python --version
python -m pip list
```

Durante el trabajo:

```bash
python hello.py
```

Al terminar:

```bash
deactivate
```

No es grave olvidar `deactivate`: el entorno solo afecta a esa sesión de shell. Al cerrar la terminal desaparece la activación.

# 12. Script de diagnóstico

Puedes crear un pequeño script de shell para inspeccionar el contexto:

```bash
cat > env-info.sh <<'EOF'
#!/usr/bin/env bash

set -eu

echo "Directorio:"
pwd

echo
echo "Python:"
command -v python || true
python --version 2>/dev/null || true

echo
echo "Python 3:"
command -v python3 || true
python3 --version 2>/dev/null || true

echo
echo "Entorno virtual:"
printf 'VIRTUAL_ENV=%s\n' "${VIRTUAL_ENV:-<no activo>}"

echo
echo "pip:"
python -m pip --version 2>/dev/null || true
EOF

chmod +x env-info.sh
```

Ejecuta:

```bash
./env-info.sh
```

Antes y después de activar `.venv`. Así podrás ver exactamente qué cambia.

# 13. Estado final esperado

Tu proyecto debería quedar así:

```text
python-basico/
├── .gitignore
├── .venv/
├── env-info.sh
└── hello.py
```

Y el flujo básico:

```bash
cd python-basico
source .venv/bin/activate
python hello.py
deactivate
```

# 14. Lo que evitaría al principio

No instalaría todavía:

- Conda;
- Poetry;
- Pipenv;
- Hatch;
- gestores de versiones complejos;
- frameworks;
- plantillas de proyecto;
- extensiones que ejecuten código sin mostrar claramente el comando.

No porque sean necesariamente malas herramientas, sino porque añaden capas antes de entender el mecanismo base.

También evitaría:

```bash
sudo pip install ...
```

y:

```bash
pip install --user ...
```

para dependencias de un proyecto. Ambas opciones mezclan ámbitos y dificultan saber qué paquete pertenece a qué proyecto.

# Primera práctica

Ejecuta este ciclo completo varias veces:

```bash
mkdir practica-entorno
cd practica-entorno

python3 -m venv .venv
source .venv/bin/activate

python --version
which python
python -m pip --version

printf 'print("Hola, mundo")\n' > hello.py
python hello.py

deactivate
rm -rf .venv

python3 -m venv .venv
source .venv/bin/activate
python hello.py
```

El objetivo no es el `print`. Es comprobar que entiendes:

- qué Python estás usando;
- dónde está instalado;
- qué cambia al activar;
- cómo se destruye el entorno;
- cómo se reconstruye sin afectar al código.

---
*Generado desde conversación con 2 mensajes.*
*Programación*
