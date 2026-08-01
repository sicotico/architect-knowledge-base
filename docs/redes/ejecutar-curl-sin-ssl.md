---
title: Ejecutar curl sin SSL
date: 2025-03-26
category: Networking
slug: ejecutar-curl-sin-ssl
tags: ['Networking']
---

# Ejecutar curl sin SSL


> **Pregunta original:**
> 
Que mas repositorios tiene pypi
> Puede ser que el curl no tenga modo inseguro ??
> El resultado e ejecutar:

openssl s_client -connect pypi.org:443

Es:

CONNECTED
> 
> *...y 6 preguntas de seguimiento*


---


## Respuesta


¡Buena pregunta! Aunque **PyPI oficial** es el principal repositorio de paquetes de Python, hay otros **mirrors, proxies, y repositorios alternativos** que sirven como respaldo, aceleradores o por motivos de red/localización.

---

## 🌐 1. **Repositorio oficial de PyPI**

- **URL**: `https://pypi.org/simple/`  
- Este es el índice oficial usado por `pip`.

---

## 🚀 2. **Mirrors y proxies públicos (no oficiales pero conocidos)**

Estos no son mantenidos por PyPI directamente, pero son populares y confiables en muchas regiones del mundo:

| Mirror | URL para `pip install` | Notas |
|-------|-------------------------|-------|
| **TUNA (Tsinghua University)** | `https://pypi.tuna.tsinghua.edu.cn/simple` | Muy usado en Asia |
| **USTC (University of Science & Tech of China)** | `https://mirrors.ustc.edu.cn/pypi/web/simple` | Otro mirror académico |
| **Aliyun** | `https://mirrors.aliyun.com/pypi/simple/` | Mirror chino de Alibaba |
| **Douban** | `https://pypi.douban.com/simple/` | Alternativa para China (a veces más lento) |
| **Google Mirror** (deprecado) | ✘ | Ya no se recomienda |
| **Cloudflare** | 🔁 `https://pypi.org` | PyPI ya usa Cloudflare globalmente |

---

## 🧰 3. **Repositorios privados o empresariales**

Muchas organizaciones tienen su propio **repositorio privado o proxy** (por seguridad, control o velocidad):

- **Artifactory**
- **Nexus Repository Manager**
- **AWS CodeArtifact**
- **Azure Artifacts**
- **DevPI** (repositorio Python auto hospedado)

Usás estos con una URL como:

```bash
pip install <paquete> --index-url=https://<empresa>/repo/pypi/simple/
```

---

## 🧪 4. **Extra Indexes**

Podés combinar múltiples fuentes:

```bash
pip install <paquete> \
  --index-url=https://pypi.org/simple \
  --extra-index-url=https://my-company-repo.com/simple/
```

---

## 🔍 Ver tu configuración actual de repositorios pip

```bash
pip config list
```

o

```bash
cat ~/.pip/pip.conf
```

---

¿Querés que te arme un ejemplo de `.pip/pip.conf` para usar un mirror alternativo por defecto?
---


Gracias por compartir el error. Eso **confirma** que tu instancia EC2 **sí tiene soporte SSL**, porque está intentando llegar a `https://pypi.org`, pero se queda esperando y luego **falla por timeout de lectura**.

Entonces el problema **no es SSL en sí**, sino que es una de estas cosas:

---

## 🧩 Diagnóstico: ¿Qué puede estar pasando?

### ✅ 1. **Tu EC2 no tiene salida a internet**

Esto es común si:
- No tiene una **IP pública** asignada.
- Está en una **VPC privada** sin NAT Gateway.
- Hay un **security group o ACL** bloqueando salida a puertos 443 o 80.

🔍 Probalo con:

```bash
ping 8.8.8.8
curl -v https://pypi.org
```

Si `ping` falla o `curl` dice `Connection timed out`, seguro es eso.

---

### ✅ 2. **Hay un proxy/firewall que interfiere con SSL**

Si estás en una red corporativa o controlada, puede haber un proxy que inspecciona HTTPS. Esto rompe muchas conexiones SSL.

🔍 Podés probar:

```bash
curl -Iv https://pypi.org
```

o

```bash
openssl s_client -connect pypi.org:443
```

Y ver si se queda colgado en el handshake.

---

### ✅ 3. **DNS no está resolviendo correctamente**

Otro sospechoso frecuente. Probalo con:

```bash
dig pypi.org
```

o

```bash
nslookup pypi.org
```

Si eso falla o tarda mucho, el DNS está mal configurado.

---

## 🛠️ Soluciones posibles

### 🚀 Opción 1: Verificá conectividad externa
Si tu instancia no tiene salida a internet:

- Asegurate de que esté en una **subred pública**.
- Que tenga una **IP pública** asignada o esté detrás de un **NAT Gateway**.
- Que los **security groups** permitan salida en puerto `443` (HTTPS).
- Que la **tabla de ruteo** tenga una ruta a `0.0.0.0/0` vía Internet Gateway o NAT.

---

### 🚧 Opción 2: Usar un mirror HTTP para pip (sin SSL, temporal)

Solo para pruebas rápidas:

```bash
pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org pytest
```

> ⚠️ Esto no es seguro, no deberías usarlo en producción.

---

### 🧰 Opción 3: Descargar paquetes desde otra máquina y pasarlos a EC2

Si la instancia **no tiene acceso a internet**, podés:

1. En tu máquina local:
```bash
pip download pytest
```

2. Subís el archivo `.whl` o `.tar.gz` a EC2 con `scp`:
```bash
scp pytest-*.whl ec2-user@<IP_EC2>:~
```

3. En EC2:
```bash
pip install ./pytest-*.whl
```

---

¿Querés que revisemos juntos tu configuración de red en la EC2 (subred, gateway, etc)? ¿O preferís seguir con alguna de las soluciones temporales?
---


Buena idea — podés usar varias URLs HTTPS conocidas y confiables para probar si `curl` funciona correctamente con SSL.

### ✅ URLs HTTPS para probar con `curl`

```bash
curl -Iv https://www.google.com
curl -Iv https://www.github.com
curl -Iv https://www.cloudflare.com
curl -Iv https://pypi.org
curl -Iv https://httpbin.org/get
```

El flag `-I` hace solo una solicitud `HEAD` (más rápida), y `-v` (verbose) te muestra el handshake SSL y headers HTTP.

---

### 🔍 Qué deberías ver si funciona bien

Algo como esto:

```
* Connected to www.google.com (142.250.XXX.XXX) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
  CAfile: /etc/ssl/certs/ca-certificates.crt
* TLSv1.3 (OUT), TLS handshake, Client hello (1)...
...
< HTTP/2 200
```

---

Si se queda colgado después de `Connected to`, entonces el handshake está lento o hay bloqueo en nivel de firewall. Si falla antes, el problema puede estar en DNS o rutas.

¿Querés que armemos un script de prueba para chequear varias URLs y ver cuál responde más rápido o si hay un patrón?
---


Sí, ¡hay un **mirror de PyPI en Cloudflare**! Desde hace un tiempo, PyPI está distribuido a través de la **infraestructura de Cloudflare**, aunque no hay un "mirror oficial alternativo" como tal — pero podés usar su infraestructura directamente.

---

## ✅ Usar Cloudflare para instalar paquetes con pip

Podés apuntar directamente a `https://pypi.org` (que ya está detrás de Cloudflare), o si querés probar una variante, usá esto:

```bash
pip install <paquete> -i https://pypi.org/simple --trusted-host pypi.org
```

Este comando ya accede al contenido servido por Cloudflare.

---

## ⚠️ Importante
No existe un subdominio tipo `cloudflare.pypi.org` ni algo así. PyPI **usa Cloudflare automáticamente** como CDN.

Si estás teniendo problemas de conexión a `https://pypi.org`, pero `curl -Iv https://www.cloudflare.com` funciona, entonces el problema podría estar más relacionado con:

- Tu resolución DNS hacia el nodo Cloudflare más cercano
- Timeout muy ajustado en `pip`
- Reintentos bloqueados por una configuración local

---

## 🔄 Alternativa avanzada: usar un mirror personalizado (ej: TUNA)

Aunque no es Cloudflare, hay mirrors rápidos mantenidos por universidades o comunidades, como el de TUNA (Tsinghua University):

```bash
pip install <paquete> -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
```

> ⚠️ Requiere confianza, no es PyPI oficial, pero es popular en regiones con acceso complicado a PyPI.

---

¿Querés que armemos un wrapper tipo script que pruebe múltiples mirrors y use el más rápido para vos?
---


¡Buenísimo! Usar **AWS CodeArtifact** como repositorio para paquetes Python (`pip`) es una forma segura y controlada de manejar tus dependencias, especialmente en entornos corporativos o sin acceso directo a PyPI.

---

## ✅ Pasos para usar **AWS CodeArtifact** con `pip`

### 1. **Crear un repositorio en CodeArtifact**

Si no lo hiciste aún:

```bash
aws codeartifact create-domain --domain my-domain

aws codeartifact create-repository \
  --domain my-domain \
  --repository my-pypi-repo \
  --upstreams repository=public-pypi
```

Esto crea un repo llamado `my-pypi-repo` que también accede a PyPI público como fallback.

---

### 2. **Obtener el token de autorización**

```bash
export CODEARTIFACT_AUTH_TOKEN=$(aws codeartifact get-authorization-token \
  --domain my-domain \
  --query authorizationToken \
  --output text)
```

Este token es válido por 12 horas.

---

### 3. **Obtener la URL del repositorio**

```bash
export CODEARTIFACT_REPO_URL=$(aws codeartifact get-repository-endpoint \
  --domain my-domain \
  --repository my-pypi-repo \
  --format pypi \
  --query repositoryEndpoint \
  --output text)
```

---

### 4. **Instalar un paquete usando pip con CodeArtifact**

```bash
pip install <paquete> \
  --extra-index-url https://aws:$CODEARTIFACT_AUTH_TOKEN@$CODEARTIFACT_REPO_URL
```

Ejemplo real:

```bash
pip install requests \
  --extra-index-url https://aws:$CODEARTIFACT_AUTH_TOKEN@my-domain-111122223333.d.codeartifact.us-east-1.amazonaws.com/pypi/my-pypi-repo/simple/
```

---

### 5. **(Opcional) Configurar `~/.pip/pip.conf` para usar siempre CodeArtifact**

```ini
[global]
extra-index-url = https://aws:<TOKEN>@<REPO_URL>/simple/
```

> ⚠️ ¡No pongas el token directamente si lo compartís o usás en scripts! Lo ideal es usar variables de entorno.

---

## 🛠️ Tip útil: Script de uso rápido

```bash
export DOMAIN=my-domain
export REPO=my-pypi-repo
export REGION=us-east-1

export CODEARTIFACT_AUTH_TOKEN=$(aws codeartifact get-authorization-token \
  --domain $DOMAIN \
  --region $REGION \
  --query authorizationToken \
  --output text)

export CODEARTIFACT_REPO_URL=$(aws codeartifact get-repository-endpoint \
  --domain $DOMAIN \
  --region $REGION \
  --repository $REPO \
  --format pypi \
  --query repositoryEndpoint \
  --output text)

pip install <paquete> --extra-index-url https://aws:$CODEARTIFACT_AUTH_TOKEN@$CODEARTIFACT_REPO_URL
```

---

¿Querés que te arme una función bash reutilizable o algo para integrarlo con un proyecto específico?
---


Para ejecutar `curl` en Linux sin validar el certificado SSL (por ejemplo, si estás accediendo a un sitio con un certificado autofirmado), puedes usar la opción `-k` o `--insecure`.

### Ejemplo:

```bash
curl -k https://example.com
```

o

```bash
curl --insecure https://example.com
```

Esta opción le dice a `curl` que ignore los errores de validación SSL, como certificados no confiables o caducados.

> ⚠️ **Advertencia**: Usar `-k` o `--insecure` desactiva la verificación de seguridad, así que úsalo solo cuando confíes plenamente en el servidor al que estás accediendo.

¿Necesitas usar `curl` para algo específico? Como enviar datos, autenticarte, descargar algo, etc.?
---


En principio, **sí lo tiene**. Todos los `curl` modernos (versiones desde hace muchos años) **incluyen la opción `-k` o `--insecure`**, a menos que haya sido **compilado de forma muy personalizada** o estés usando una versión extremadamente antigua.

### Para comprobar si tu `curl` tiene la opción insegura:

Ejecutá:

```bash
curl --help | grep -i insecure
```

Si ves algo como:

```
 -k, --insecure      Allow insecure server connections when using SSL
```

Entonces está disponible.

---

### Si no aparece:
Puede ser por alguna de estas razones:
- Tenés una versión de `curl` muy antigua.
- Está compilado sin soporte SSL (raro, pero posible).
- Estás usando una versión embebida en algún entorno muy limitado.

### Solución rápida:
Podés chequear la versión con:

```bash
curl --version
```

Y ahí deberías ver algo como:

```
curl 7.81.0 (x86_64-pc-linux-gnu) libcurl/7.81.0 OpenSSL/1.1.1n ...
```

Fijate si aparece algo como `OpenSSL`, `GnuTLS`, o `LibreSSL`. Si no aparece nada de eso, puede que no tenga soporte SSL en absoluto.

---

¿Querés que te ayude a instalar una versión actualizada o con SSL habilitado? ¿O estás en algún entorno restringido (tipo Alpine, contenedor, etc)?
---


¡Excelente! Si `openssl s_client -connect pypi.org:443` muestra `CONNECTED`, eso significa que **sí tenés salida a internet y el handshake SSL está funcionando**. Así que no es un problema de red ni de certificados.

Entonces el error que viste:

```
ReadTimeoutError("HTTPSConnectionPool(host='pypi.org', port=443): Read timed out.")
```

probablemente se debe a una de estas causas:

---

## 🧪 Posibles causas restantes

### 🔄 1. DNS lento o inestable

Incluso si `openssl` se conecta, si `pip` depende de resolución DNS que está fallando o lenta, puede dar ese error.

🔍 Verificá con:

```bash
time nslookup pypi.org
```

Si eso tarda más de 1-2 segundos, hay un problema de DNS.

---

### 🔌 2. `pip` tiene configuraciones o proxies que interfieren

Verificá si tenés algún proxy configurado:

```bash
env | grep -i proxy
```

Si ves algo como `HTTPS_PROXY`, eso puede estar redirigiendo tráfico y causando los timeouts.

También podés ver si hay una configuración en `~/.pip/pip.conf` o `/etc/pip.conf`.

---

### 🐍 3. Versión antigua de `pip` o de `Python`

Algunas versiones viejas de `pip` o `urllib3` tienen problemas con ciertos servidores HTTPS modernos (por ejemplo, HTTP/2, SNI).

🔍 Revisá:

```bash
pip --version
python --version
```

Si `pip` es < 20 o `Python` es < 3.6, podrías tener problemas de compatibilidad.

---

## ✅ Qué podés probar ahora

### Opción A: Aumentar el timeout

A veces el error es solo por latencia de red (EC2 en una región lejana, congestión, etc). Probá esto:

```bash
pip install pytest --default-timeout=100
```

---

### Opción B: Forzar HTTP en vez de HTTPS (no recomendado para producción)

```bash
pip install pytest --index-url=http://pypi.org/simple/ --trusted-host pypi.org
```

---

### Opción C: Usar un mirror alternativo (también podés probar Cloudflare o universidades)

```bash
pip install pytest -i https://pypi.python.org/simple --trusted-host pypi.python.org
```

---

### Opción D: Instalar con verbose para más detalle

Esto te puede dar pistas exactas de dónde cuelga:

```bash
pip install pytest -vvv
```

---

¿Querés compartir el resultado de `pip --version` y `env | grep -i proxy`? Con eso afinamos la solución exacta.
---


Ah, perfecto, gracias por el contexto. Si estás en una EC2 y ni `curl -k` ni `pip` pueden conectar por SSL, y encima `curl` **ni siquiera tiene `-k`**, es muy probable que:

1. Estés usando una versión de `curl` compilada **sin soporte SSL/TLS**.
2. El sistema esté **desactualizado** o muy recortado (como ocurre con AMIs mínimas o Alpine Linux).
3. El sistema tenga problemas con **certificados raíz (CA)**.

---

## ✅ Pasos para diagnosticar y resolver:

### 🔍 1. Verificá si `curl` tiene soporte SSL
```bash
curl --version
```

Te debería mostrar algo como:

```
curl 7.XX.X (x86_64-pc-linux-gnu) libcurl/7.XX.X OpenSSL/1.1.1 ...
```

Si **no aparece `OpenSSL`, `GnuTLS` o `LibreSSL`**, entonces tu `curl` está compilado sin SSL. En ese caso, no puede validar (ni siquiera ignorar) certificados SSL.

---

### 🛠️ 2. Solución: Reinstalar `curl` con soporte SSL

#### Si estás usando **Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install --reinstall curl ca-certificates
```

#### Si estás usando **Amazon Linux / RHEL / CentOS**:
```bash
sudo yum reinstall curl ca-certificates
```

#### Si estás en **Alpine Linux**:
```bash
apk add --no-cache curl ca-certificates
```

> También asegurate de tener `ca-certificates` instalado para que pueda validar certificados correctamente.

---

### 💡 Alternativa temporal: usar `wget` sin validar SSL

Si necesitás hacer algo urgente y `wget` está disponible, podés usar:

```bash
wget --no-check-certificate https://example.com
```

---

### 📦 Para `pip` que falla por SSL

Si `pip` tampoco puede acceder por SSL, podés usar el flag `--trusted-host`:

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org paquete
```

Pero eso no sirve si el problema es más profundo (como sin soporte SSL en Python). En ese caso, deberías reinstalar Python con soporte SSL, pero eso depende de tu distro.

---

¿Querés que veamos exactamente qué versión de `curl` tenés o cómo compilarlo con SSL si no podés reinstalar con `apt`/`yum`?

---
*Generado desde conversación con 18 mensajes.*
*Networking*
