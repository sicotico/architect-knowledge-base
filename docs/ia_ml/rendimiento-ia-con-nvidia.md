---
title: Rendimiento IA con NVIDIA
date: 2026-07-04
category: IA/ML
slug: rendimiento-ia-con-nvidia
tags: ['IA/ML']
---

# Rendimiento IA con NVIDIA


> **Pregunta original:**
> 
ahor atengo 2 modelos, como lo gestion con tabby
> Por ahora solo Tabby en venv, el resto de componentes lo vemos más adelante.
> Que gano usando docker en el servidor ?
> 
> *...y 65 preguntas de seguimiento*


---


## Respuesta


Bien, no es grave. La advertencia solo dice que ese extra ya no existe con ese nombre en tu versión de `huggingface_hub`. La CLI debería estar instalada igualmente.

Prueba:

```bash
which hf
hf --version
```

Si existe, descarga con el comando nuevo:

```bash
mkdir -p ~/ai/models

hf download turboderp/Qwen3-8B-exl3 \
  --revision 4.0bpw \
  --local-dir ~/ai/models/Qwen3-8B-exl3-4.0bpw
```

Si quieres instalar el acelerador de descargas aparte:

```bash
uv pip install -U hf_transfer
```

Y luego:

```bash
HF_HUB_ENABLE_HF_TRANSFER=1 hf download turboderp/Qwen3-8B-exl3 \
  --revision 4.0bpw \
  --local-dir ~/ai/models/Qwen3-8B-exl3-4.0bpw
```

Si `hf` no existe, dime qué sale con:

```bash
python -m pip show huggingface_hub
ls venv/bin | grep -E 'hf|hugging'
```
---


No hay un benchmark fiable que pueda prometerte “en tu 5060 Ti dará X tok/s” sin probarlo. Pero sí se puede estimar el orden relativo:

| Stack | Rendimiento esperado con mismo GGUF | Comentario |
|---|---:|---|
| **llama.cpp directo CUDA** | 100% referencia | Máximo control, menos capas |
| **LM Studio headless** | ~95-100% | Usa runtimes llama.cpp; si elige CUDA bien, debería ir casi igual |
| **Ollama** | ~85-95% | Más cómodo, algo más de capa/overhead |
| **TabbyAPI EXL3** | Puede superar a GGUF | Pero catálogo/modelos/admin peor para ti |

LM Studio en Linux/Windows usa llama.cpp para GGUF, según su documentación ([LM Studio docs](https://lmstudio.ai/docs/app)). También tiene modo headless con `llmster` ([LM Studio headless](https://lmstudio.ai/docs/developer/core/headless)). Así que, si comparas el mismo `.gguf`, LM Studio no debería estar muy lejos de llama.cpp directo.

Lo que sí cambia mucho el rendimiento:

```text
Q4_K_M vs Q5_K_M vs Q6_K
contexto 4K vs 16K vs 32K
flash attention on/off
KV cache cuantizada o no
-ngl completo en GPU o parcial
batch/ubatch
CUDA runtime elegido
```

Mi expectativa para tu caso:

- **LM Studio headless**: probablemente la mejor relación comodidad/rendimiento.
- **llama.cpp compilado**: útil si quieres exprimir, controlar flags y hacer benchmark limpio.
- **Ollama**: muy cómodo para probar, pero menos fino.
- **TabbyAPI**: rápido, pero ya viste el coste operativo.

Si quieres un benchmark rápido sin casarte con nada, yo probaría primero **LM Studio headless** con un GGUF conocido y mediría. Solo compilaría llama.cpp si ves que LM Studio no usa bien CUDA o quieres comparar fino.

El benchmark que haría sería con el mismo modelo, por ejemplo:

```text
Qwen3-8B Q4_K_M
Qwen3-14B Q4_K_M
Gemma 4 12B Q4_K_M
```

Y medir:

```text
tokens/s de prompt processing
tokens/s de generación
VRAM usada
si cabe todo sin offload
latencia de primer token
```

Conclusión corta: **LM Studio headless debería estar muy cerca de llama.cpp directo** si usa el runtime CUDA correcto. Ollama probablemente será algo más lento, pero mucho más cómodo. Compilar llama.cpp merece la pena solo si quieres control y medición precisa.
---


Voy a verificar la recomendación actual de Ubuntu/NVIDIA porque en GPUs 50-series el soporte de driver cambia con rapidez. Te contesto orientado a servidor headless y a IA, no a escritorio.
---


Si estás dentro del venv, sales con:

```bash
deactivate
```

Luego bórralo:

```bash
cd ~/ai/tabbyAPI
rm -rf venv314
```

Comprueba que ya no estás dentro:

```bash
which python
```

Si todo está normal, probablemente no devolverá nada o te indicará el Python del sistema solo si tienes `python` configurado. También puedes mirar el prompt: ya no debería aparecer `(venv314)`.
---


Ese te vale muy bien para primera prueba: **`turboderp/Qwen3-8B-exl3`**, rama **`4.0bpw`**. Ocupa unos **5.2 GB**, así que debería cargar cómodo en tu 5060 Ti de 16 GB.

Descárgalo así:

```bash
cd ~/ai/tabbyAPI
source venv/bin/activate
mkdir -p ~/ai/models

huggingface-cli download turboderp/Qwen3-8B-exl3 \
  --revision 4.0bpw \
  --local-dir ~/ai/models/Qwen3-8B-exl3-4.0bpw
```

Si `huggingface-cli` no existe:

```bash
uv pip install -U huggingface_hub[hf_transfer]
```

y repites el comando.

Lo bueno de ese modelo:
- Es EXL3, recomendado para ExLlamaV3.
- Autor `turboderp`, muy buen origen para probar ExLlama.
- Tamaño razonable para validar servidor sin ir al límite.

Lo malo:
- 8B no será el modelo “definitivo” más inteligente.
- `4.0bpw` es buena prueba de rendimiento, pero para uso diario en 8B podrías subir a 5-6bpw si existe la rama.

Después de descargarlo, lo siguiente será cargarlo en TabbyAPI.
---


Te entiendo. Para lo que tú querías, **TabbyAPI no ha sido el camino más cómodo**. Es muy bueno cuando ya tienes claro “este modelo EXL2/EXL3 exacto quiero servirlo rápido”, pero para **probar muchos modelos, multimodal, tools y administración cómoda**, se queda estrecho.

Mi lectura:

| Stack | Lo bueno | Lo malo |
|---|---|---|
| TabbyAPI/EXL3 | Muy rápido en NVIDIA, eficiente | Poco catálogo, admin incómoda, Python/deps delicadas |
| Ollama | Muchísimos modelos, instalación simple, multimodal/tools, fácil probar | GGUF suele rendir menos que EXL3 puro |
| LM Studio / llmster | Muy cómodo, servidor OpenAI/Anthropic-compatible, buen gestor de modelos | Menos “server Linux clásico”, algo más cerrado |
| vLLM | Mejor stack serio para endpoints, NVFP4/FP8, tools, modelos NVIDIA | Más complejo, VRAM justa, más “producción” que pruebas |
| Open WebUI | Buena administración/chat/tools/RAG | Es frontend; necesita backend debajo |

Para tu momento actual yo pivotaría a:

```text
Ollama nativo en servidor
+ Open WebUI en tu PC cliente o en el servidor
```

Por qué: **te permite probar modelos sin pelearte con ramas EXL3, Python ni loaders**. Ollama tiene tool calling documentado ([Ollama tools](https://docs.ollama.com/capabilities/tool-calling)), Open WebUI conecta con Ollama y APIs OpenAI-compatible ([Open WebUI](https://github.com/open-webui/open-webui)), y LM Studio también tiene modo servidor/headless si prefieres esa vía ([LM Studio headless](https://lmstudio.ai/docs/developer/core/headless)).

Lo que pierdes: algo de rendimiento máximo frente a TabbyAPI.  
Lo que ganas: catálogo, facilidad, multimodal, pruebas rápidas y menos dolor operativo.

Yo no borraría TabbyAPI todavía. Lo dejaría aparcado como “backend rápido para un modelo concreto”. Pero para explorar, instalaría Ollama y probaría:

```text
gemma4:12b
qwen3:8b / qwen3:14b si está disponible
llava / qwen-vl / modelos vision compatibles
mistral-small si entra
```

Luego, si encuentras un modelo que te convence, ya decides si merece buscar su EXL3 equivalente o servirlo con vLLM/NVFP4.

La expectativa importante: con **16 GB VRAM**, multimodal + contexto largo + modelo muy inteligente sigue siendo apretado. No es culpa de Tabby solamente. Pero para experimentar, **Ollama/LM Studio te van a dar mucha menos fricción**.
---


Sí, puedes tener **Open WebUI en tu PC cliente** y que se conecte al **TabbyAPI del servidor** por red.

La arquitectura sería:

```text
PC cliente
Open WebUI
        |
        | HTTP/OpenAI API
        v
Servidor IA
TabbyAPI + modelo en RTX 5060 Ti
```

Lo bueno:
- No instalas más cosas en el servidor IA.
- La GPU queda dedicada a TabbyAPI.
- Open WebUI puede correr en tu PC principal.
- Puedes cambiar la interfaz sin tocar el backend.

Lo malo:
- Tu PC cliente debe estar encendido para usar la interfaz.
- Si quieres varios usuarios o acceso permanente, mejor poner Open WebUI en el servidor.
- La configuración de red/API keys queda repartida entre dos equipos.

En Open WebUI tendrás que añadir una conexión OpenAI-compatible apuntando a:

```text
http://IP_DEL_SERVIDOR:5000/v1
```

Y como API key, la `api_key` de TabbyAPI.

Antes, en el servidor asegúrate de que Tabby escucha en LAN:

```yaml
network:
  host: 0.0.0.0
  port: 5000
  disable_auth: false
```

Y desde el PC cliente prueba:

```bash
curl http://IP_DEL_SERVIDOR:5000/v1/models \
  -H "Authorization: Bearer TU_API_KEY"
```

Si eso responde, Open WebUI debería poder conectarse.
---


No exactamente. **Unsloth no significa “destilado”**.

**Unsloth** es principalmente una organización/herramienta que hace:

- fine-tuning eficiente,
- cuantizaciones GGUF,
- conversiones,
- optimizaciones,
- notebooks y guías para ejecutar modelos.

Un modelo publicado por `unsloth/...` puede ser:

| Caso | Qué significa |
|---|---|
| Base convertido | Mismo modelo original, pasado a GGUF |
| Quantizado | Mismo modelo, menor precisión: Q4, Q5, IQ4, etc. |
| Fine-tuned | Modelo entrenado/modificado adicionalmente |
| Distilled | Modelo entrenado para imitar a otro modelo |
| Merged | Mezcla de pesos/fine-tunes |
| Dynamic quant | Cuantización especial de Unsloth |

En este caso concreto:

```text
unsloth/Qwen3.6-27B-MTP-GGUF
```

por lo que muestra la ficha, es una **conversión/cuantiﬁcación GGUF de Qwen3.6-27B con MTP**, no necesariamente un destilado.

Lo que sí es:

```text
Qwen3.6-27B original
+ formato GGUF
+ varias cuantizaciones
+ soporte MTP
```

Lo que no asumiría:

```text
destilado
fine-tune
modelo reducido entrenado para imitar a otro
```

Si fuera destilado, normalmente lo verías en el nombre o en la ficha como:

```text
distill
distilled
Distill
student
teacher
```

Y si fuera fine-tune, verías cosas como:

```text
instruct
abliterated
coder
reasoning
DPO
SFT
LoRA
merge
```

Aquí lo importante para ti es: **sí está cuantizado**, si eliges una variante tipo `UD-Q4_K_XL`, `Q5_K_M`, etc. Pero **no por ser Unsloth es destilado**.
---


Esto confirma justo el riesgo de Python 3.14. No ha fallado CUDA todavía: ha fallado antes, en **`pydantic-core`**, porque una dependencia Rust/PyO3 todavía no soporta bien Python 3.14:

```text
Python interpreter version (3.14) is newer than PyO3's maximum supported version (3.13)
```

No recomiendo usar el workaround:

```bash
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
```

Podría compilar, pero estaríamos empezando el servidor de IA con una base frágil.

Siguiente opción limpia: **Python 3.13**, no 3.12. Está dentro del máximo que soporta ese PyO3 y es más probable que esté disponible o sea fácil de instalar.

Prueba primero si Ubuntu lo tiene:

```bash
sudo apt install python3.13 python3.13-venv
```

Si instala bien:

```bash
cd ~/ai/tabbyAPI
rm -rf venv314 venv
python3.13 -m venv venv
source venv/bin/activate
python --version
python -m pip install -U pip setuptools wheel
python -m pip install -U ".[cu13]"
```

Luego test GPU:

```bash
python -c "import torch; print('torch:', torch.__version__); print('cuda available:', torch.cuda.is_available()); print('torch cuda:', torch.version.cuda); print('gpu:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"
```

Si Ubuntu tampoco tiene Python 3.13, entonces sí usaría `uv` para instalar **3.13** aislado. Mejor 3.13 que 3.12 ahora, porque el error marca explícitamente soporte hasta 3.13.
---


Está bien: **TabbyAPI ha arrancado correctamente** en `cu13`.

Lo importante del log es esto:

```text
Starting OAI API
Completions: http://127.0.0.1:5000/v1/completions
Chat completions: http://127.0.0.1:5000/v1/chat/completions
Uvicorn running on http://127.0.0.1:5000
```

La advertencia de `xFormers` no bloquea el servidor:

```text
xFormers can't load C++/CUDA extensions
```

Lo bueno: TabbyAPI arranca y la API está viva.  
Lo malo: esa parte de `xFormers` no está acelerada porque el wheel que tienes no coincide con tu combinación exacta `PyTorch 2.11.0+cu130 + Python 3.13`. Para la primera prueba no lo tocaría; primero carga un modelo y vemos si ExLlamaV3 funciona bien. Si luego hay problemas de rendimiento o carga, lo ajustamos.

De momento:

1. No uses `./start.sh`, porque te vuelve a meter `cu12`.
2. Arranca con:

```bash
source ~/ai/tabbyAPI/venv/bin/activate
cd ~/ai/tabbyAPI
python main.py
```

3. En otra terminal puedes comprobar que responde:

```bash
curl http://127.0.0.1:5000/v1/models
```

Probablemente no habrá modelos cargados aún, pero debería responder la API.

Siguiente paso: descargar un modelo EXL2/EXL3 pequeño para probar carga real. Ahí veremos si la GPU, CUDA, TabbyAPI y el formato están trabajando juntos de verdad.
---


Voy a separar dos cosas que suelen mezclarse: el modelo local “tipo Gemini” para razonar/chatear, y la capa que le da búsqueda web. El modelo no navega por sí solo; lo hace una app/servidor alrededor.
---


Es un **fine-tune de Gemma 4 12B Instruct**, no una cuantización principal para Tabby tal cual.

Concretamente, el repo dice que es una versión **“sycophancy-ablated”** de `google/gemma-4-12B-it`: han intentado reducir la tendencia del modelo a ser demasiado complaciente/adulador usando **heretic + ARA-LoRA** ([modelo](https://huggingface.co/UnstableLlama/gemma-4-12B-it-desiccated)).

En cristiano:

| Término | Qué significa |
|---|---|
| `gemma-4-12B-it` | Gemma 4 de 12B, versión instruction-tuned/chat |
| `desiccated` | Variante modificada para ser más seca/sobria |
| `sycophancy-ablated` | Reducida la tendencia a dar la razón o alabar demasiado |
| `BF16` | Pesos en alta precisión, ocupa bastante |
| `LoRA` | Técnica de modificación/fine-tuning ligero |
| `EXL3 quantization here` | Hay una versión cuantizada aparte para ExLlamaV3 |

Para tu servidor TabbyAPI, **no descargaría ese repo principal BF16**. En 12B BF16 probablemente se te va demasiado de VRAM o te deja poquísimo margen para KV cache.

Lo que te interesa es el enlace que pone:

```text
An exl3 quantization is here
```

Ese sí sería el formato adecuado para tu setup: **EXL3**.

Lo bueno de ese modelo:
- Gemma 4 12B es tamaño interesante para tu 5060 Ti.
- Puede tener un tono más crítico y menos pelota.
- Apache 2.0.

Lo malo:
- Es un fine-tune experimental de un tercero.
- “Menos adulador” no siempre significa “más correcto”.
- El repo principal es BF16, no ideal para 16 GB.
- Para Tabby necesitas la cuantización EXL3, no ese repo base.

Si quieres probarlo, busca dentro de la colección o enlace del repo la variante EXL3, idealmente algo tipo:

```text
gemma-4-12B-it-desiccated-exl3
4.0bpw
5.0bpw
```

Para tu GPU yo probaría **4.0bpw o 5.0bpw**.
---


Bien, esa lista ya nos da una señal clara: Ubuntu tiene módulos precompilados para tu kernel y ofrece ramas server/open. Voy a contrastar solo el matiz 580 vs 595 antes de darte el comando exacto, porque en NVIDIA nuevo “más reciente” suele ser mejor, pero conviene mirar si hay alguna trampa evidente.
---


Ese error es típico de **mezcla de dependencias CUDA** en el mismo venv. El cambio de `cu12` a `cu13` ha sustituido Torch/ExLlama, pero probablemente han quedado librerías NVIDIA/NCCL de la instalación anterior. No intentaría parchearlo paquete a paquete.

Lo más limpio: **recrear el venv desde cero** e instalar solo `cu13`.

Hazlo así:

```bash
cd ~/ai/tabbyAPI
deactivate 2>/dev/null || true
rm -rf venv venv314
uv venv --python 3.13 venv
source venv/bin/activate
uv pip install -U pip setuptools wheel
uv pip install -U ".[cu13]"
```

Luego prueba Torch:

```bash
python -c "import torch; print(torch.__version__); print(torch.version.cuda); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

Si sale bien, arranca **sin `start.sh`**:

```bash
python main.py
```

Y, como antes, si no lo has hecho ya, borra las keys que se imprimieron:

```bash
rm -f api_tokens.yml
```

Se regenerarán al arrancar.

El punto clave: no mezclar `start.sh` por ahora, porque te mete `cu12`. Vamos a dejar un venv limpio con `cu13` y arrancar directo.
---


Entiendo: quieres saber si merece la pena compilar llama.cpp antes de invertir tiempo. Voy a separar benchmark “teórico de motor” de benchmark “útil en tu 5060 Ti”, porque con GGUF las flags y la cuantización cambian mucho el resultado.
---


Los modelos EXL2 se suelen obtener en **Hugging Face**, no en Ollama. Piensa en esto así:

- **Ollama**: baja modelos empaquetados para su runtime, normalmente derivados de GGUF.
- **LM Studio**: muy orientado a GGUF.
- **TabbyAPI/ExLlama**: busca repos **EXL2 / EXL3 / GPTQ**, normalmente en Hugging Face.

La ruta práctica es buscar en Hugging Face por:

```text
exl2
4.0bpw
5.0bpw
Qwen exl2
Llama exl2
Mistral exl2
bartowski exl2
LoneStriker exl2
turboderp exl2
```

Repos habituales:

- [bartowski](https://huggingface.co/bartowski): muchos modelos EXL2, a menudo con varias ramas por `bpw`.
- [LoneStriker](https://huggingface.co/LoneStriker): gran cantidad de modelos EXL2, aunque conviene revisar antigüedad y modelo base.
- [turboderp](https://huggingface.co/turboderp): creador de ExLlama/EXL2, con algunos modelos de referencia.
- [royallab](https://huggingface.co/royallab): ligado al ecosistema TabbyAPI.

Ojo con una cosa importante: en muchos repos EXL2, la rama `main` **no contiene el modelo usable**, solo mediciones o metadatos. Tienes que descargar una rama tipo:

```text
4.0bpw
4.5bpw
5.0bpw
6.0bpw
8.0bpw
```

TabbyAPI tiene downloader integrado. Según su wiki, puedes descargar un repo concreto indicando la rama/revisión así ([TabbyAPI Getting Started](https://github.com/theroyallab/tabbyAPI/wiki/01.-Getting-Started)):

```bash
./start.sh download usuario/modelo-exl2 --revision 4.0bpw
```

Ejemplo conceptual:

```bash
./start.sh download bartowski/Modelo-Que-Quieras-exl2 --revision 5.0bpw
```

También puedes usar `huggingface-cli`:

```bash
pip install huggingface_hub

huggingface-cli download bartowski/NOMBRE-DEL-MODELO-exl2 \
  --revision 5.0bpw \
  --local-dir /ruta/a/tabbyAPI/models/NOMBRE-DEL-MODELO-exl2
```

Para tu **5060 Ti 16 GB**, yo miraría primero:

| Tamaño | BPW recomendado | Comentario |
|---|---:|---|
| 7B/8B | 5.0-6.5 bpw | Rápido, buena calidad, mucho margen de contexto |
| 12B/14B | 4.0-5.0 bpw | Probablemente tu punto dulce |
| 20B/22B | 3.0-4.0 bpw | Puede merecer la pena, pero más justo |
| 30B/32B | 2.4-3.5 bpw | Posible, pero con compromisos claros |

Mi consejo inicial: empieza con **un 8B a 6bpw** y **un 14B a 4 o 5bpw**. Así comparas velocidad/calidad sin pelearte con la VRAM desde el primer día.

Lo bueno de EXL2: muy rápido en NVIDIA y muy eficiente para inferencia local.  
Lo malo: menos “plug and play” que Ollama/LM Studio, y dependes más de repos comunitarios, ramas correctas y compatibilidad con la versión de ExLlama/TabbyAPI.
---


Eso cambia bastante la lectura: **por 1000 € el equipo completo está muy bien**. No es una 7900 XTX suelta, es un servidor entero con CPU, RAM, NVMe, placa, fuente, caja y una NVIDIA de 16 GB. Ahí no veo una mala compra.

Ahora lo sensato es explotarlo por sus puntos fuertes:

- **CUDA/NVIDIA**: compatibilidad y menos pelea que AMD.
- **16 GB VRAM**: suficiente para 8B-14B muy bien y algunos 27B/35B cuantizados.
- **32 GB RAM + NVMe**: buen servidor LAN, RAG, modelos en disco, Open WebUI, SearXNG, embeddings.
- **Equipo dedicado**: puede estar siempre encendido, dar endpoints, servir varios clientes.

Yo lo convertiría en un **servidor híbrido práctico**, no en “quiero correr el modelo más grande posible”:

```text
Backend cómodo principal:
LM Studio headless u Ollama

Frontend:
Open WebUI

Modelos diarios:
8B-14B Q5/Q6

Modelos pesados de prueba:
27B/35B-A3B Q3/IQ4 con contexto controlado

Especializados:
vision pequeño, coder pequeño, embeddings, reranker
```

La clave para que te dé valor no es solo el modelo grande. Es montar un flujo:

```text
chat local + búsqueda web + documentos + endpoints + tools + modelos especializados
```

Ahí el equipo puede brillar bastante más que TabbyAPI pelado.

Y sí: hay que explotarlo. Mi siguiente paso sería dejar de perseguir EXL3 por ahora y montar una base cómoda:

1. **LM Studio headless** o **Ollama**.
2. **Open WebUI**.
3. Modelos GGUF fáciles de cambiar.
4. Un benchmark simple de 3 modelos.
5. Luego decides si compilar `llama.cpp` para rascar rendimiento.

No es “tengo solo 16 GB”; es “tengo un servidor CUDA completo por 1000 €”. Bien usado, da bastante juego.
---


Sí: **Claude Code encaja mejor con lo que estás pidiendo ahora**.

Lo que tú quieres es básicamente:

```text
desde móvil / portátil
→ controlar un agente persistente
→ que instale y configure stacks completos en un servidor
→ con menos fricción de permisos
→ y con buena ergonomía operativa
```

Claude Code está más orientado a ese flujo de “agente en terminal que opera un entorno real”. Codex también puede hacerlo, pero ahora mismo parece más fragmentado entre CLI, app, cloud, desktop, IDE y móvil.

**Diferencia práctica**

| Necesidad | Claude Code | Codex |
|---|---:|---:|
| Terminal agent autónomo | Muy fuerte | Sí, pero más controlado |
| Modo permisos agresivo | Sí | Más limitado/variable |
| Instalar stacks en VPS | Muy usado para eso | Puede, pero menos directo |
| Control desde móvil | Más fácil vía sesión/remoto/cloud | Posible, pero menos claro |
| Experiencia tipo “hazlo todo” | Mejor | Más conservador |
| Seguridad por defecto | Más arriesgable | Más restrictivo |

Lo bueno de Claude Code:
- Flujo más directo para administrar servidores.
- Menos pelea con aprobaciones si eliges modo permisivo.
- Muy bueno para “instala, configura, prueba, crea systemd, deja README”.
- Encaja con VPS/Ubuntu/infra.

Lo malo:
- Precisamente por eso es más peligroso.
- En modo permisivo puede romper cosas rápido.
- Conviene usarlo con backups/snapshots.
- Hay que darle instrucciones muy claras de no tocar SSH, firewall global, drivers, etc.

Para tu servidor IA, si vas a usar Claude Code, yo lo usaría con esta regla:

```text
Autónomo para instalar servicios de IA bajo /home/sico/ai.
Preguntar antes de tocar:
- SSH
- firewall global
- drivers NVIDIA
- borrar datos
- cambiar particiones
- exponer puertos a internet
```

Y haría primero snapshot/backup de:

```text
~/ai
/etc/systemd/system
config de red/firewall
lista de paquetes
```

Así que sí: **para instalar LM Studio headless, Ollama, Open WebUI, SearXNG, systemd y pruebas de endpoints, Claude Code probablemente te va a resultar más cómodo que Codex**. Codex te sirve, pero Claude Code parece más alineado con el uso “admin DevOps agresivo” que estás buscando.
---


Vale, Ubuntu 26.04 solo te está dando 3.14 en repos base. Ahora sí usaría **`uv`** para instalar Python 3.13 aislado. No toca el Python del sistema.

Instala `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Carga la ruta:

```bash
source ~/.local/bin/env
```

Instala Python 3.13:

```bash
uv python install 3.13
```

Crea el venv de TabbyAPI:

```bash
cd ~/ai/tabbyAPI
rm -rf venv venv314
uv venv --python 3.13 venv
source venv/bin/activate
python --version
```

Debería mostrar `Python 3.13.x`.

Instala TabbyAPI:

```bash
python -m pip install -U pip setuptools wheel
python -m pip install -U ".[cu13]"
```

Y prueba GPU:

```bash
python -c "import torch; print('torch:', torch.__version__); print('cuda available:', torch.cuda.is_available()); print('torch cuda:', torch.version.cuda); print('gpu:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"
```

Lo bueno de esto: sigues con un Python moderno compatible con PyO3/pydantic-core.  
Lo malo: dependes de `uv`, pero para servidores Python aislados suele ser bastante limpio.
---


Voy a darte un plan “para agente” que sea ejecutable de forma bastante autónoma, pero con límites claros: instalación sí, abrir servicios solo en LAN, nada de borrar datos ni exponer claves. Reviso la forma actual de `llmster`/LM Studio headless para no basarlo en comandos inventados.
---


Voy a mirar la ficha concreta porque “MTP” y “GGUF” cambian bastante la recomendación: puede ser muy interesante para llama.cpp/LM Studio, pero también puede pedir configuración extra para aprovechar la predicción especulativa.
---


Ese es otro tipo de cuantización, pero **no es para TabbyAPI/ExLlama**.

`nvidia/Qwen3.6-27B-NVFP4` es un modelo cuantizado por NVIDIA con **Model Optimizer** usando **NVFP4**, pensado para ejecutarse con **vLLM** en GPUs NVIDIA Hopper/Blackwell. La propia ficha dice que el runtime soportado es **vLLM** y da este ejemplo:

```bash
vllm serve nvidia/Qwen3.6-27B-NVFP4 \
  --quantization modelopt \
  --max-model-len 262144 \
  --reasoning-parser qwen3
```

Fuente: [nvidia/Qwen3.6-27B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-27B-NVFP4).

En resumen:

| Formato | Runtime típico | ¿Sirve para TabbyAPI? |
|---|---|---:|
| EXL2 | ExLlamaV2 / TabbyAPI | Sí |
| EXL3 | ExLlamaV3 / TabbyAPI | Sí |
| GGUF | llama.cpp / Ollama / LM Studio | No directamente |
| GPTQ | ExLlama/otros, antiguo | A veces, pero menos recomendable |
| AWQ | vLLM / Transformers | No para TabbyAPI normalmente |
| FP8 | vLLM / TensorRT-LLM | No para TabbyAPI |
| **NVFP4** | **vLLM + NVIDIA ModelOpt** | **No** |

Lo bueno de NVFP4:
- Muy interesante para **Blackwell**, que es tu generación de GPU.
- Reduce mucho memoria.
- Puede rendir muy bien con vLLM.
- NVIDIA lo publica optimizado para su stack.

Lo malo para ti ahora:
- No encaja con TabbyAPI.
- vLLM añade otro stack distinto.
- Ese modelo 27B puede seguir siendo justo para 16 GB, sobre todo con KV cache largo.
- La ficha habla de pruebas en **GB300**, no en una 5060 Ti.

Traducción práctica: **no lo bajes para TabbyAPI**. Si más adelante quieres probar vLLM como segundo backend, entonces sí, este tipo de modelo es justo el que tendría sentido investigar. Para tu instalación actual busca **EXL3** o **EXL2**.
---


Sí. **BPW es una forma de expresar la cuantización**.

En GGUF/Ollama/LM Studio estás acostumbrado a nombres tipo:

```text
Q4_K_M
Q5_K_M
Q8_0
```

En EXL2 se suele expresar como:

```text
4.0bpw
5.0bpw
6.0bpw
```

La idea es la misma: **reducir precisión para que el modelo ocupe menos VRAM/RAM**.

Equivalencia aproximada, no exacta:

| GGUF | EXL2 aproximado | Calidad/tamaño |
|---|---:|---|
| Q3 | 3.0bpw | Bajo, muy comprimido |
| Q4_K_M | 4.0-4.5bpw | Buen equilibrio |
| Q5_K_M | 5.0-5.5bpw | Mejor calidad |
| Q6_K | 6.0-6.5bpw | Alta calidad |
| Q8_0 | 8.0bpw | Casi sin pérdida |

La diferencia es que **EXL2 permite cuantización mixta más flexible**. No todo el modelo tiene exactamente 4 bits; puede repartir bits de forma más inteligente entre capas para llegar a un promedio, por ejemplo **4.65bpw**.

Lo bueno: con NVIDIA suele rendir muy bien y aprovecha mejor la VRAM.  
Lo malo: no es tan universal como GGUF; si mañana quieres usar ese modelo en Ollama o LM Studio, probablemente no te sirva directamente.
---


Sí. Haría **TabbyAPI nativo en venv** y sin Docker por ahora.

Instala base:

```bash
sudo apt update
sudo apt install git curl wget build-essential python3.12-venv python3-pip
```

Clona TabbyAPI:

```bash
mkdir -p ~/ai
cd ~/ai
git clone https://github.com/theroyallab/tabbyAPI.git
cd tabbyAPI
```

Como tu driver expone **CUDA 13.2**, usa la rama de instalación **cu13**. La wiki actual de TabbyAPI indica que `cu13` es para CUDA 13.x, ExLlamaV3 y Python 3.12+ ([TabbyAPI Getting Started](https://github.com/theroyallab/tabbyAPI/wiki/01.-Getting-Started)):

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -U pip setuptools wheel
pip install -U ".[cu13]"
```

Arranque básico:

```bash
python main.py
```

O usando el script:

```bash
./start.sh
```

Lo bueno de este camino: máxima simplicidad, menos capas, más fácil depurar CUDA/ExLlama.  
Lo malo: las dependencias Python quedan en ese venv; si una actualización rompe algo, toca recrear el entorno.

Para modelos, usa el downloader de TabbyAPI. Ejemplo de forma general:

```bash
./start.sh download usuario/modelo-exl2 --revision 5.0bpw
```

Antes de descargar modelos grandes, yo probaría uno 7B/8B EXL2/EXL3 para validar carga. Luego ya vamos a **Qwen3-14B 4.5/5bpw** como candidato serio.
---


No creo que la hayas cagado, pero sí hay que ajustar expectativas.

Tu **5060 Ti 16 GB** no es una máquina para sustituir “Gemini/Claude/ChatGPT full” en todo. Es una máquina muy buena para:

- modelos locales privados,
- endpoints LAN,
- pruebas rápidas,
- RAG doméstico/empresa pequeña,
- agentes sencillos,
- modelos 8B-14B muy cómodos,
- algún 27B/35B MoE cuantizado con compromisos.

Pero **no** va a replicar bien una suscripción cloud moderna en razonamiento fuerte, multimodal avanzado, contexto enorme y tooling pulido a la vez.

La comparación con tu Mac Mini M4 Pro 24 GB es interesante:

| Equipo | Lo bueno | Lo malo |
|---|---|---|
| Mac Mini 24 GB unified | Más memoria disponible para modelos grandes | Menos ancho de banda GPU dedicado, ecosistema MLX/Metal |
| RTX 5060 Ti 16 GB | CUDA, mejor ecosistema NVIDIA, más velocidad en modelos que caben | VRAM limitada: si no cabe, no cabe |

La 5060 Ti gana cuando el modelo cabe entero en VRAM. El Mac gana cuando necesitas **más memoria unificada** aunque vaya más lento.

Sobre TabbyAPI: tu diagnóstico me parece correcto.

Lo bueno:
- API simple.
- EXL3 rápido.
- Bien para “un modelo concreto que ya sé que quiero”.

Lo malo:
- Administración pobre.
- Catálogo EXL3 limitado.
- Poca comodidad para probar.
- Multimodal/tooling no es su punto fuerte.
- Dependencias Python han sido una pérdida de tiempo en Ubuntu 26.04.

Mi recomendación ahora sería no seguir intentando que TabbyAPI sea lo que no es. Déjalo como backend secundario.

Para tu servidor, yo apuntaría a esta arquitectura:

```text
Backend principal para explorar:
LM Studio headless o Ollama

Frontend:
Open WebUI en cliente o servidor

Backend opcional rápido:
TabbyAPI solo para EXL3 concretos

Backend futuro avanzado:
vLLM para NVFP4/FP8/Qwen3.6 si merece la pena
```

Si quieres “lo más parecido a suscripción”, necesitas no solo modelo: necesitas **tooling, búsqueda, memoria, RAG, UI, gestión de contexto y buen enrutamiento**. Ahí Open WebUI + Ollama/LM Studio puede darte una experiencia más completa que TabbyAPI, aunque el motor sea algo menos rápido.

Con 16 GB, yo buscaría el “punto dulce”:

- **Gemma 4 12B Q4/Q5** para general/multimodal si funciona bien.
- **Qwen3.6 27B IQ3/IQ4** para razonamiento, si entra con contexto razonable.
- **Qwen3/Qwen3.5/Qwen3.6 14B Q5** como modelo diario estable.
- **Modelos vision 4B-12B** para multimodal, no gigantes.

La parte dura: un local de 16 GB puede ser muy útil, pero no te va a dar la sensación de “tengo Gemini Advanced entero en casa”. Para eso hoy necesitas más VRAM/RAM unificada, o aceptar cloud híbrido. La buena noticia: tu equipo sigue siendo una base muy decente para servidor IA local, solo que el stack correcto probablemente no era TabbyAPI como herramienta principal.
---


Voy a mirar ese repo concreto antes de clasificarlo, porque nombres como “desiccated” suelen indicar una variante/quantización específica y no conviene asumir por el nombre.
---


Llama.cpp puede ser justo el punto intermedio que te faltaba: menos dolor que Tabby, más control de servidor que Ollama, y muchísimo catálogo GGUF. Voy a contrastar el estado actual de CUDA/Vulkan, multimodal y tool-calling en llama.cpp antes de recomendarte una ruta.
---


Voy a mirar el repo porque “NVFP4” sí es una pista fuerte: suena a cuantización/formato NVIDIA para Blackwell, pero hay que ver con qué runtime lo publican y si sirve para TabbyAPI.
---


Con TabbyAPI gestionas dos cosas distintas:

```text
Modelos en disco ≠ modelo cargado en VRAM
```

Puedes tener muchos modelos en `/home/sico/ai/models`, pero normalmente en tu 5060 Ti cargarás **uno a la vez** en VRAM.

**1. Listar modelos disponibles**

Desde cualquier equipo con acceso a Tabby:

```bash
curl http://IP_SERVIDOR:5000/v1/model/list \
  -H "x-admin-key: TU_ADMIN_KEY"
```

**2. Ver modelo cargado / endpoint OpenAI**

```bash
curl http://IP_SERVIDOR:5000/v1/models \
  -H "Authorization: Bearer TU_API_KEY"
```

**3. Descargar el modelo actual de VRAM**

```bash
curl -X POST http://IP_SERVIDOR:5000/v1/model/unload \
  -H "x-admin-key: TU_ADMIN_KEY"
```

**4. Cargar otro modelo**

Usa el nombre exacto de la carpeta dentro de `/home/sico/ai/models`.

Ejemplo:

```bash
curl -X POST http://IP_SERVIDOR:5000/v1/model/load \
  -H "x-admin-key: TU_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model_name":"Qwen3-8B-exl3-4.0bpw"}'
```

Si el otro se llama, por ejemplo:

```text
gemma-4-12B-it-desiccated-exl3-4.0bpw
```

entonces:

```bash
curl -X POST http://IP_SERVIDOR:5000/v1/model/load \
  -H "x-admin-key: TU_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model_name":"gemma-4-12B-it-desiccated-exl3-4.0bpw"}'
```

Lo bueno: puedes cambiar de modelo sin reiniciar Tabby.  
Lo malo: cada carga/descarga tarda y puede dejar VRAM fragmentada si cambias mucho; si algo raro pasa, reiniciar Tabby limpia todo.

Para comodidad, yo me haría tres scripts en el servidor:

```bash
~/ai/bin/tabby-list
~/ai/bin/tabby-load NOMBRE_MODELO
~/ai/bin/tabby-unload
```

O más adelante una UI tipo SillyTavern + Tabby Loader.
---


Perfecto. Esta es la validación buena:

```text
torch: 2.11.0+cu130
cuda available: True
torch cuda: 13.0
gpu: NVIDIA GeForce RTX 5060 Ti
```

Eso significa que el venv con **Python 3.13** está usando GPU correctamente. Buena decisión no forzar 3.14.

Ahora ya puedes arrancar TabbyAPI:

```bash
python main.py
```

O:

```bash
./start.sh
```

Lo siguiente será descargar un modelo pequeño EXL2/EXL3 para probar carga real. Yo probaría primero uno de 7B/8B antes de ir a Qwen3-14B, solo para confirmar que el servidor arranca, carga modelo y responde.
---


Tienes dos formas. Para empezar, la más simple es **cargarlo al arrancar** editando `config.yml`.

Primero mira cómo se llama exactamente la carpeta:

```bash
ls ~/ai/models
```

Supongamos que es:

```text
Qwen3-8B-exl3-4.0bpw
```

Edita config:

```bash
cd ~/ai/tabbyAPI
nano config.yml
```

Busca la sección `model:` y déjala así:

```yaml
model:
  model_dir: /home/sico/ai/models
  model_name: Qwen3-8B-exl3-4.0bpw
```

Guarda con `Ctrl+O`, Enter, y sal con `Ctrl+X`.

Luego arranca Tabby:

```bash
source venv/bin/activate
python main.py
```

Si carga bien, deberías ver logs de carga del modelo y VRAM usada. En otra terminal puedes mirar:

```bash
nvidia-smi
```

Alternativa por API, con Tabby ya arrancado:

```bash
curl -X POST http://127.0.0.1:5000/v1/model/load \
  -H "x-admin-key: TU_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model_name":"Qwen3-8B-exl3-4.0bpw"}'
```

Pero para primera vez prefiero `config.yml`: menos piezas en movimiento.

Ojo: si en `config.yml` ya existe `model_dir: models`, cámbialo a `/home/sico/ai/models`. Si no, Tabby buscará dentro de `~/ai/tabbyAPI/models` y no encontrará el modelo.
---


Voy a ubicarte en el “mapa” de modelos EXL2: dónde se descargan, cómo reconocer repos fiables y qué cambia frente a Ollama/LM Studio. También te marco las pegas, porque aquí hay bastante conversión comunitaria y no todo lo que aparece conviene usar.
---


Sí, **Pi.dev podría hacer parte de lo que pides**, pero con matices importantes.

Pi encaja si quieres un **agente tipo Claude Code/Codex en terminal**, instalado en tu servidor, capaz de ejecutar comandos, editar archivos e instalar stacks. Además puede conectarse a proveedores OpenAI-compatible, incluyendo **LM Studio, Ollama, vLLM o llama.cpp server**, según su documentación de providers/modelos. Esto cuadra bien con tu idea de: servidor Ubuntu + LM Studio headless/llmster o llama.cpp + agente que lo administre. 【turn515113search7】【turn515113search0】

La diferencia clave: **Pi no trae un sistema fuerte de permisos/sandbox por defecto**. Corre con los permisos del usuario que lo lanza; su propio repo indica que si necesitas límites debes meterlo en contenedor o sandbox. Eso significa que puede ser más parecido al “dangerous permission” que buscas, pero también más fácil de romper el sistema si le das manga ancha. 【turn515113search6】

Mi lectura práctica:

- **Sí para:** instalar LM Studio headless, configurar `lms server`, crear servicios `systemd`, descargar modelos, modificar configs, probar endpoints, automatizar tareas.
- **Sí para local models:** puede usar LM Studio/Ollama/vLLM/llama.cpp mediante endpoint OpenAI-compatible.
- **No exactamente para:** “controlarlo cómodamente desde móvil” por sí solo. Para eso sigues necesitando SSH/tmux, una UI web, o lanzarlo desde otro equipo contra el servidor.
- **Menos maduro/pulido que Claude Code:** más flexible y abierto, pero probablemente requiere más configuración inicial.
- **Más peligroso que Codex con permisos:** porque si lo ejecutas como tu usuario y le das autonomía, puede tocar todo lo que ese usuario pueda tocar.

Para tu caso yo lo probaría así, sin darle root al principio:

```bash
mkdir -p ~/ai/agent-work
cd ~/ai/agent-work
```

Y lo usaría con una instrucción de sistema muy clara:

```text
Eres un agente DevOps en mi servidor Ubuntu 26.04.
Puedes instalar y configurar software dentro de /home/sico/ai.
Puedes crear servicios systemd de usuario.
No uses sudo salvo que me lo pidas.
No borres modelos, venvs ni configuraciones existentes sin confirmación.
Objetivo: montar LM Studio headless/llmster o llama.cpp server con endpoints LAN y documentación de recuperación.
```

Mi recomendación concreta: **Pi.dev sí merece una prueba**, pero no como sustituto mágico de Claude Code. Úsalo primero con LM Studio/llmster como backend, limitado a `/home/sico/ai`. Si demuestra que ejecuta bien tareas largas, entonces ya decides si le das más permisos.
---


Ese modelo es **muy interesante para tu nuevo enfoque**, pero en tu 5060 Ti de 16 GB lo pondría en la categoría **“probar con cautela”**, no “modelo diario garantizado”.

Qué es:

```text
unsloth/Qwen3.6-27B-MTP-GGUF
```

| Parte | Significado |
|---|---|
| `Qwen3.6-27B` | Modelo Qwen reciente de 27B |
| `MTP` | Multi-Token Prediction: puede acelerar generación prediciendo varios tokens |
| `GGUF` | Formato llama.cpp / LM Studio / Ollama |
| `Unsloth` | Conversión/cuants orientadas a uso local |

Lo bueno:
- Es **GGUF**, así que encaja con **LM Studio, llama.cpp y Ollama**.
- Es **Qwen3.6**, más actual que Qwen3 clásico.
- Tiene **MTP**, y Unsloth afirma ~**1.5-2x** más velocidad sin pérdida de precisión si el runtime lo aprovecha ([modelo](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)).
- La ficha menciona mejoras de **tool calling** y uso con Codex/OpenCode.
- Tiene instrucciones directas para `llama.cpp`, Ollama, LM Studio, vLLM y SGLang.

Lo malo:
- **27B en 16 GB es justo**, incluso en Q4.
- MTP en llama.cpp tiene limitaciones: la ficha indica que `-np > 1` y `--mmproj` aún no están soportados con MTP.
- Si usas multimodal con imagen, el coste de memoria sube.
- Para contexto largo, el KV cache te puede comer el margen.
- En LM Studio puede que funcione como GGUF normal, pero no tengo claro que aproveche todas las flags MTP automáticamente.

El comando recomendado por Unsloth para llama.cpp es:

```bash
./llama-server \
  -hf unsloth/Qwen3.6-27B-MTP-GGUF:UD-Q4_K_XL \
  -ngl 99 -c 8192 -fa on -np 1 \
  --spec-type draft-mtp --spec-draft-n-max 2
```

Para tu GPU, yo empezaría exactamente con esa cuantización **`UD-Q4_K_XL`**, pero con expectativas moderadas: puede ir justo de VRAM. Si falla, baja contexto de `8192` a `4096`.

Mi veredicto: **sí, es de los modelos que merece probar en tu servidor**. Es mucho más alineado con lo que buscabas que TabbyAPI: GGUF, tools, posible multimodal, LM Studio/Ollama/llama.cpp, y Qwen moderno. Pero no lo tomaría como prueba definitiva de “16 GB bastan”; si este va justo, no significa que el servidor no valga, significa que 27B + MTP + contexto empieza a rozar el límite.
---


Sí, **LM Studio headless puede ser una opción razonable**, y en rendimiento debería estar mucho más cerca de **llama.cpp** que de “otra cosa”, porque LM Studio usa runtimes basados en **llama.cpp** para GGUF en Linux/Windows ([LM Studio docs](https://lmstudio.ai/docs/app)). Además tiene modo headless con **llmster**, pensado precisamente para correr sin GUI como servicio ([LM Studio headless](https://lmstudio.ai/docs/developer/core/headless)).

Comparativa realista:

| Opción | Rendimiento esperado | Comodidad | Control fino | Modelos |
|---|---:|---:|---:|---:|
| llama.cpp directo | Mejor o igual | Media-baja | Muy alto | GGUF enorme |
| LM Studio headless | Muy cerca de llama.cpp | Alta | Medio | GGUF enorme |
| Ollama | Algo por debajo o similar | Muy alta | Bajo-medio | Muy amplio, fácil |
| TabbyAPI/EXL3 | Muy alto si encaja | Baja | Medio | EXL3 limitado |

**Rendimiento puro**

Si LM Studio está usando el runtime CUDA correcto, debería estar **muy cerca de llama.cpp directo**. No esperaría grandes diferencias si comparas:

```text
mismo modelo GGUF
misma cuantización
mismo contexto
misma GPU offload
mismo batch
```

Ollama también se apoya en llama.cpp, pero añade más capa de gestión: daemon, plantillas, modelo empaquetado, defaults propios. En algunas comparativas recientes lo colocan algo por debajo de llama.cpp crudo; no siempre es dramático, pero existe.

**Lo bueno de LM Studio headless**
- Mucho más cómodo que llama.cpp directo.
- Gestiona modelos mejor que Tabby.
- API OpenAI-compatible y Anthropic-compatible ([LM Studio server](https://lmstudio.ai/docs/developer/core/server)).
- Tiene modo headless real.
- Buen camino si vienes de LM Studio en escritorio.
- Soporte RTX 50-series con runtimes CUDA de llama.cpp desde hace tiempo ([LM Studio RTX 50](https://lmstudio.ai/blog/lmstudio-v0.3.15)).

**Lo malo**
- Menos transparente que compilar llama.cpp tú mismo.
- Menos automatizable que Ollama en algunos flujos.
- Si algo rinde mal, tienes que revisar qué runtime ha elegido: CUDA, Vulkan o CPU.
- Para servidor “serio”, llama.cpp directo o vLLM son más explícitos.

Mi veredicto para ti:

```text
Para probar modelos cómodamente: LM Studio headless
Para máximo control/rendimiento GGUF: llama.cpp directo
Para simplicidad brutal y ecosistema: Ollama
Para exprimir un modelo concreto NVIDIA: Tabby/vLLM
```

Yo probaría **LM Studio headless** antes que Ollama si valoras administración cómoda y ya conoces LM Studio. Pero mediría con el mismo GGUF contra llama.cpp directo para ver si hay penalización real en tu 5060 Ti.
---


Ese **sí es de la familia correcta para TabbyAPI**, porque es **EXL3**. Pero no lo elegiría como modelo principal para tu 5060 Ti.

Qué es:

| Parte del nombre | Significado |
|---|---|
| `Qwen3.6-35B-A3B` | Modelo MoE: 35B parámetros totales, ~3B activos por token |
| `abliterated` | Le han quitado/alterado parte de los rechazos/safety guardrails |
| `exl3` | Formato para ExLlamaV3/TabbyAPI |
| `6bpw` | Cuantización de 6 bits por peso, bastante alta/calidad |

Lo bueno:
- **Compatible con TabbyAPI/ExLlamaV3**.
- MoE: aunque tenga 35B totales, solo activa parte por token.
- Puede ser inteligente para su coste de inferencia.
- 6bpw conserva más calidad que 3-4bpw.

Lo malo:
- **35B totales a 6bpw probablemente no te cabe cómodo en 16 GB**, o te deja muy poco margen para KV cache.
- “Abliterated/uncensored” significa menos barreras, pero también puede degradar comportamiento, seguridad o obediencia fina.
- Tiene muy pocas descargas/likes; yo lo trataría como experimental.
- La licencia es `tongyi-qianwen`, no Apache 2.0.
- Aunque solo active 3B por token, **los pesos de los expertos tienen que estar en VRAM** si no quieres offloading.

La propia ficha dice que el modelo base tiene **35B total / 3B active parameters** y que es MoE con 256 expertos, 8 activos por token ([repo](https://huggingface.co/groxaxo/Qwen3.6-35B-A3B-abliterated-exl3-6bpw)). Eso ayuda a la velocidad, pero no elimina el problema de memoria.

Para tu 5060 Ti, buscaría una variante más baja:

```text
Qwen3.6-35B-A3B exl3 3bpw
Qwen3.6-35B-A3B exl3 3.5bpw
Qwen3.6-35B-A3B exl3 4bpw
```

A 6bpw yo lo dejaría pasar salvo que quieras probar “a ver si carga”. Para uso diario sin offload, mejor:

```text
Qwen3/Qwen3.6 14B EXL3 5bpw
Qwen3.6 27B/30B-A3B EXL3 3-4bpw
Gemma 4 12B EXL3 4-5bpw
```

Mi veredicto: **compatible, interesante, pero demasiado ambicioso a 6bpw para 16 GB**.
---


Voy a contestarlo en términos prácticos para TabbyAPI/ExLlama y tu restricción de “sin offloading”, porque técnicamente se puede diseñar algo híbrido, pero casi siempre cambia mucho el rendimiento.
---


Sí, esa es la idea general, con un matiz:

```text
Servidor IA
lmster / LM Studio headless
modelos GGUF
API OpenAI-compatible

PC cliente
LM Studio GUI o navegador/app cliente
administración y pruebas
```

**`llmster`** es el daemon/headless de LM Studio: corre sin interfaz gráfica en el servidor y sirve modelos/API. Luego desde tu equipo cliente puedes gestionarlo con herramientas de LM Studio, CLI/API, o conectarte a su endpoint.

Lo bueno:
- No necesitas escritorio en Ubuntu Server.
- Te quitas bastante dolor de Python/CUDA/venv.
- Tienes gestión de modelos más cómoda que TabbyAPI.
- Sirve API compatible con OpenAI/Anthropic.
- Usa runtimes tipo llama.cpp para GGUF.

Lo malo:
- No es tan transparente como compilar `llama.cpp` tú mismo.
- Tienes que confirmar que el runtime elegido usa CUDA y no CPU/Vulkan raro.
- La administración remota depende de cómo LM Studio exponga `llmster` y sus herramientas en tu versión.

La API quedaría algo tipo:

```text
http://IP_SERVIDOR:PUERTO/v1
```

Y desde clientes compatibles usarías esa URL como “OpenAI-compatible base URL”.

En tu caso, sí: **LM Studio en cliente + lmster en servidor** encaja bastante bien con lo que buscabas al principio: probar modelos GGUF cómodamente, tener servidor headless y no pelearte tanto con EXL3/Tabby.
---


Voy a ser cauto aquí: “3.12+” no siempre significa que el ecosistema ya vaya fino en 3.14, sobre todo con paquetes CUDA y wheels compilados. Miro rápido si TabbyAPI/ExLlama declaran compatibilidad explícita antes de recomendarte una versión.
---


Voy a revisar ese repo concreto porque aquí importan tres cosas: si es EXL3 real, si es MoE/A3B y cuánta VRAM pide a 6bpw. Con 16 GB, el “35B” del nombre puede sonar peor de lo que es si solo activa 3B, pero los pesos siguen ocupando.
---


Docker no te da más tokens/s por sí mismo. Lo que te da es **orden, aislamiento y facilidad para levantar servicios alrededor del modelo**.

Para tu servidor de IA, Docker tiene sentido sobre todo para:

| Uso | Qué ganas | Qué pierdes |
|---|---|---|
| Open WebUI | Instalación y actualización fácil | Hay que configurar volúmenes y red |
| SearXNG | Búsqueda web local aislada | Otro servicio que mantener |
| LiteLLM / proxy API | Rutas, claves, límites, varios endpoints | Más complejidad |
| Bases de datos/vector DB | Qdrant, Postgres, Redis, etc. ordenados | Más consumo RAM |
| Servicios auxiliares | Logs, reinicios, despliegue reproducible | Aprender Docker/Compose |

Para **TabbyAPI puro**, yo no veo Docker imprescindible. De hecho, para exprimir GPU y evitar líos con CUDA/PyTorch/Blackwell, puede ser más simple instalar TabbyAPI en un **venv Python nativo** al principio.

Lo bueno de Docker:
- Puedes tener `open-webui`, `searxng`, `litellm`, `qdrant`, etc. separados.
- Actualizar es más limpio.
- Evitas ensuciar Ubuntu con mil dependencias.
- Es más fácil hacer backup de configuraciones y volúmenes.
- Si algo se rompe, borras/recreas el contenedor.

Lo malo:
- Necesitas **NVIDIA Container Toolkit** para que los contenedores vean la GPU.
- Puede complicar permisos, rutas de modelos y red interna.
- Si no fijas versiones, una actualización puede romper cosas.
- Para TabbyAPI con RTX 50-series, un entorno nativo puede ser menos frágil.

Mi recomendación equilibrada:

```text
TabbyAPI/ExLlama: nativo en venv
Open WebUI: Docker
SearXNG: Docker
LiteLLM: Docker si lo necesitas
Modelos: carpeta normal en el host, montada si hace falta
```

Así tienes rendimiento y menos fricción donde importa, pero mantienes orden para los servicios periféricos.
---


Voy a distinguir dos cosas: controlar el servidor desde el móvil, y controlar una sesión de Codex/CLI que ya esté corriendo. Para lo específico de Codex/OpenAI verifico la parte oficial antes de darte una recomendación práctica.
---


Normal: en Ubuntu 26.04 ya no tienes `python3.12` en los repos base. No pasa nada; mejor no mezclar PPAs raros todavía.

La opción limpia es usar **`uv`** para instalar un Python 3.12 aislado solo para TabbyAPI.

Instala base:

```bash
sudo apt update
sudo apt install curl ca-certificates git build-essential
```

Instala `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Activa su ruta en la shell actual:

```bash
source ~/.local/bin/env
```

Instala Python 3.12 gestionado por `uv`:

```bash
uv python install 3.12
```

Crea el venv de TabbyAPI con ese Python:

```bash
cd ~/ai/tabbyAPI
uv venv --python 3.12 venv
source venv/bin/activate
python --version
```

Debería salir algo tipo:

```text
Python 3.12.x
```

Luego instala TabbyAPI:

```bash
pip install -U pip setuptools wheel
pip install -U ".[cu13]"
```

Lo bueno de este método: no toca el Python del sistema y evita pelearse con paquetes de Ubuntu.  
Lo malo: dependes de `uv` para traer esa versión de Python.

Después de instalar, comprueba que Python ve CUDA:

```bash
python -c "import torch; print(torch.cuda.is_available()); print(torch.version.cuda); print(torch.cuda.get_device_name(0))"
```

Si devuelve `True` y muestra la 5060 Ti, vamos bien.
---


Bien, ya tienes el venv con **Python 3.14.4** activo.

Ahora instala dependencias:

```bash
python -m pip install -U pip setuptools wheel
python -m pip install -U ".[cu13]"
```

Cuando termine, prueba CUDA:

```bash
python -c "import torch; print('torch:', torch.__version__); print('cuda available:', torch.cuda.is_available()); print('torch cuda:', torch.version.cuda); print('gpu:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"
```

Lo que queremos ver:

```text
cuda available: True
gpu: NVIDIA GeForce RTX 5060 Ti
```

Si eso sale bien, Python 3.14 queda validado y seguimos con TabbyAPI en ese entorno.
---


Ese log significa: **el PC de la red sí llega a TabbyAPI**, pero la petición va **sin API key válida**.

```text
192.168.68.78 ... GET /v1/models ... 401
```

`401` = no autorizado.

Prueba desde el cliente con la key:

```bash
curl http://IP_SERVIDOR:5000/v1/models \
  -H "Authorization: Bearer TU_API_KEY"
```

O con header alternativo:

```bash
curl http://IP_SERVIDOR:5000/v1/models \
  -H "x-api-key: TU_API_KEY"
```

La key está en el servidor:

```bash
cd ~/ai/tabbyAPI
cat api_tokens.yml
```

Si estás configurando Open WebUI, pon:

```text
Base URL: http://IP_SERVIDOR:5000/v1
API Key: TU_API_KEY
```

No uses la `admin_key` para Open WebUI; esa resérvala para cargar/descargar modelos.
---


Sí, **conceptualmente se puede**, pero para tu objetivo yo lo trataría como **offloading** y lo evitaría.

El **KV cache** es memoria de contexto: guarda las claves/valores de atención de los tokens ya procesados. Durante la generación, el modelo lo consulta constantemente. Si lo pones en **RAM DDR4**, la GPU tiene que ir leyendo/escribiendo por **PCIe**, y eso suele convertirse en cuello de botella fuerte. Hay estudios recientes sobre KV offloading que precisamente señalan que el límite grande pasa a ser el tráfico PCIe y la latencia de transferencias ([arXiv](https://arxiv.org/abs/2601.19910)).

En la práctica:

| Configuración | Rendimiento | Para tu caso |
|---|---|---|
| Modelo en VRAM + KV cache en VRAM | Mejor | Sí |
| Modelo en VRAM + KV cache cuantizada en VRAM | Muy bueno, ahorra VRAM | Sí |
| Modelo en VRAM + KV cache en RAM | Mucho más lento | Solo para contexto enorme |
| Modelo parcialmente en RAM | Muy lento | No, porque dijiste sin offloading |

Con **TabbyAPI/ExLlama**, lo normal y recomendable es mantener **modelo + KV cache en VRAM**. Lo que sí puedes hacer es usar **KV cache cuantizada** si el backend/modelo lo permite: por ejemplo cache en 8-bit o 4-bit. Eso reduce VRAM sin cruzar a RAM.

Para tu 5060 Ti 16 GB, la estrategia buena sería:

```text
modelo EXL2/EXL3 en VRAM
KV cache en VRAM
contexto ajustado
cache cuantizada si hace falta
sin CPU/RAM offload
```

Ejemplo realista:

- Qwen3-14B 5bpw con contexto moderado.
- Si falta VRAM, bajar a 4.5/4.0bpw o reducir contexto.
- Si sigue faltando, usar KV cache cuantizada.
- Solo después consideraría RAM offload, pero ya no sería “máximo rendimiento”.

Resumen: **sí se puede en algunos stacks, pero no es lo que quieres para un servidor rápido**. En tu máquina, mejor sacrificar algo de contexto o BPW antes que mandar el KV cache a DDR4.
---


Sí. De hecho, creo que ahora hay una narrativa mucho más sólida que la que teníamos hace unos días. memcite

En la conversación anterior habíamos convergido hacia **3 artículos**, pero con todo lo que ha salido aquí yo lo reorganizaría en una serie de **5 artículos**. El hilo conductor no sería "cómo instalar una IA local", sino **el viaje de un arquitecto de infraestructura al montar un servidor de IA de verdad**, donde aparecen las diferencias entre la teoría y la práctica.

## Artículo 1 — La memoria importa más que los TFLOPS: lo que aprendí montando un servidor de IA local

**Idea**

La mayoría compara GPUs por potencia de cálculo. Para inferencia con LLMs, el verdadero cuello de botella suele ser la VRAM.

**Índice**

- El hardware elegido (5060 Ti 16 GB)
- Por qué 16 GB parecen mucho... hasta que cargas modelos
- VRAM vs RAM
- KV Cache
- Offloading
- La duda inevitable: ¿habría sido mejor una GPU con 24 GB?
- Conclusiones reales tras usarla

---

## Artículo 2 — Del "stack perfecto" a la realidad: TabbyAPI, EXL3 y el coste de perseguir el máximo rendimiento

Este puede ser uno de los más interesantes.

**Idea**

Explicar cómo la búsqueda del máximo rendimiento también aumenta muchísimo la complejidad.

**Índice**

- Mi idea inicial
- Ubuntu Server
- Drivers NVIDIA Server
- Python 3.14... que no era compatible
- uv para instalar Python 3.13
- EXL3
- TabbyAPI
- Administración manual
- Muy pocos modelos disponibles
- ¿Realmente merece la pena?

La conclusión no sería que TabbyAPI es malo.

Sería algo como:

> Cuanto más cerca estás del máximo rendimiento, más lejos estás de la simplicidad operativa.

---

## Artículo 3 — Cuando la mejor arquitectura no es la más rápida

Este me gusta bastante porque conecta con arquitectura empresarial.

**Idea**

Comparar varios runtimes.

- Ollama
- LM Studio
- llama.cpp
- TabbyAPI
- vLLM

No como benchmark.

Sino como decisión arquitectónica.

Hablar de:

- facilidad de operación
- mantenimiento
- compatibilidad
- tooling
- administración
- rendimiento

Y terminar con algo parecido a:

> Igual que en Cloud, el sistema más rápido no siempre es el sistema que genera más valor.

---

## Artículo 4 — La nueva habilidad del arquitecto: dirigir agentes, no ejecutar comandos

Aquí entrarían Codex, Claude Code, Pi.dev...

No hablaría de modelos.

Hablaría de una nueva forma de administrar infraestructura.

**Índice**

- Antes escribíamos scripts.
- Después Terraform.
- Luego Ansible.
- Ahora damos objetivos a un agente.

Pero aparecen nuevos problemas.

- permisos
- seguridad
- confianza
- reproducibilidad
- rollback

Creo que este puede funcionar muy bien en LinkedIn.

---

## Artículo 5 — La IA local no compite contra ChatGPT: compite contra tus expectativas

Este sería más personal.

Porque durante toda la conversación hay una evolución muy clara.

Empiezas pensando:

> "Quiero el servidor más potente posible."

Después:

> "Quiero EXL3."

Después:

> "Quiero modelos multimodales."

Después:

> "Necesito administrar modelos."

Después:

> "Necesito que un agente monte el servidor."

Y acabas dándote cuenta de que el problema ya no es la velocidad.

Es la **experiencia completa**.

La reflexión final podría ser algo así:

> Durante años, en infraestructura aprendimos que el mejor producto no era el más rápido, sino el que menos fricción generaba en operación. Con la IA local está ocurriendo exactamente lo mismo.

---

# Creo que hay una sexta idea

No es técnica.

Es casi filosófica.

## Del laboratorio al producto: por qué probar tecnología y construir un sistema son cosas completamente distintas

Todo este viaje tiene un patrón muy claro.

Al principio buscabas:

- el mejor modelo
- el mejor runtime
- el mayor rendimiento

Y poco a poco las preguntas cambiaron a:

- ¿cómo hago backup?
- ¿cómo administro los modelos?
- ¿cómo automatizo las instalaciones?
- ¿cómo lo controlo desde el móvil?
- ¿cómo lo recupero en una hora si el servidor muere?

Eso es exactamente el cambio de mentalidad que vive cualquier arquitecto cuando pasa de un PoC a una plataforma de producción.

De todas las ideas, esta última es probablemente la que más puede diferenciarte en LinkedIn porque habla menos de una herramienta concreta y más de cómo piensa alguien con experiencia en infraestructura cuando aterriza en el mundo de la IA local. memcite
---


Te falta el paquete de venv para el Python del sistema. En Ubuntu viene separado.

Haz:

```bash
sudo apt update
sudo apt install python3.14-venv
```

Luego recrea el entorno desde cero:

```bash
cd ~/ai/tabbyAPI
rm -rf venv314
python3.14 -m venv venv314
source venv314/bin/activate
python --version
```

Si ya aparece:

```text
Python 3.14.x
```

continúa:

```bash
python -m pip install -U pip setuptools wheel
python -m pip install -U ".[cu13]"
```

Y la prueba clave:

```bash
python -c "import torch; print('torch:', torch.__version__); print('cuda available:', torch.cuda.is_available()); print('torch cuda:', torch.version.cuda); print('gpu:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"
```

Si eso devuelve `cuda available: True`, seguimos con 3.14. Si no, descartamos este venv y usamos otra versión.
---


Tiene sentido la frustración. Voy a contrastar rápidamente las alternativas actuales para no proponerte otro camino igual de estrecho: especialmente Ollama/llama.cpp, LM Studio, vLLM y Open WebUI frente a tus requisitos reales: probar muchos modelos, multimodal, tools y 16 GB sin offload.
---


Perfecto, esa es una decisión bastante limpia: primero validar inferencia y VRAM sin añadir capas. Voy a apoyarme en la instalación actual de TabbyAPI para darte una secuencia corta y con puntos de control.
---


Por **CUDA 13 / ExLlamaV3**.

Tu `nvidia-smi` muestra:

```text
CUDA Version: 13.2
```

Y la instalación actual de TabbyAPI distingue entre:

```text
.[cu12]  -> CUDA 12.x
.[cu13]  -> CUDA 13.x, ExLlamaV3, Python 3.12+
```

Por eso te puse **Python 3.12**: no por capricho, sino porque para la vía `cu13` TabbyAPI pide **Python 3.12 o superior**.

Lo bueno:
- Encaja con tu driver/CUDA visible.
- Mejor preparado para RTX 50-series/Blackwell.
- Evitas forzar wheels CUDA 12 si el stack ya tiene soporte CUDA 13.

Lo malo:
- Python 3.12 puede tener alguna dependencia menos madura que 3.11 en ciertos proyectos.
- Si quisieras usar ExLlamaV2/cu12 por compatibilidad con modelos EXL2 antiguos, Python 3.11 o 3.12 con `.[cu12]` podría ser otra ruta.

Para tu caso, yo mantendría:

```bash
python3.12 -m venv venv
pip install -U ".[cu13]"
```

Si TabbyAPI falla por alguna dependencia, entonces hacemos fallback a `cu12`, pero empezaría con `cu13` porque tu equipo y driver ya están en esa línea.
---


Bien. Ahora la GPU queda como toca para servidor:

- **Driver 595.71.05** funcionando.
- **CUDA 13.2** visible.
- **Persistence Mode: On**.
- **VRAM libre** casi completa.
- Temperatura y consumo en reposo correctos.

Siguiente paso razonable: instalar base de sistema y comprobar carga CUDA real. Haría:

```bash
sudo apt update
sudo apt install git curl wget build-essential python3-venv python3-pip nvtop tmux htop
```

Luego instala TabbyAPI en un entorno Python limpio y prueba primero con un modelo EXL2 pequeño/mediano. Empezaría con **Qwen3-8B EXL2 6bpw** para validar que todo carga bien, y después pasaría a **Qwen3-14B EXL2 4.5/5bpw** como modelo diario.

No instalaría CUDA Toolkit manualmente todavía. Si TabbyAPI/PyTorch lo necesitan, mejor dejar que sus wheels/paquetes traigan lo que corresponde; mezclar toolkits manuales al principio suele complicar más de lo que ayuda.
---


Perfecto. Ahora instala Python 3.13 con `uv` y crea el venv:

```bash
uv python install 3.13
```

Después:

```bash
rm -rf venv venv314
uv venv --python 3.13 venv
source venv/bin/activate
python --version
```

Cuando veas `Python 3.13.x`, instala TabbyAPI:

```bash
python -m pip install -U pip setuptools wheel
python -m pip install -U ".[cu13]"
```

Y prueba GPU:

```bash
python -c "import torch; print('torch:', torch.__version__); print('cuda available:', torch.cuda.is_available()); print('torch cuda:', torch.version.cuda); print('gpu:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"
```
---


Voy a darte una forma que no dependa de `start.sh`, porque ese script ya vimos que te reescribe preferencias a cu12. Para descargar modelos conviene usar Hugging Face directamente o el downloader de Tabby si podemos invocarlo sin reinstalar.
---


No pasa nada malo por ejecutarlo desde la carpeta de TabbyAPI.

El instalador de `uv` no instala cosas dentro de la carpeta actual. Normalmente lo deja en tu usuario, en algo como:

```text
~/.local/bin/uv
```

y añade/usa configuración en tu home, no en `~/ai/tabbyAPI`.

Puedes ejecutarlo desde ahí:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Luego:

```bash
source ~/.local/bin/env
uv --version
```

Lo único a vigilar: **no ejecutes comandos tipo `uv init`** dentro de TabbyAPI, porque eso sí podría tocar archivos del proyecto. Pero el instalador de `uv` como tal está bien.
---


**A3B** significa aproximadamente **“3B activos”**: en un modelo **MoE** (*Mixture of Experts*), no se usan todos los parámetros en cada token.

Ejemplo:

```text
Qwen3.6-35B-A3B
```

Se lee así:

```text
35B = 35 mil millones de parámetros totales
A3B = unos 3 mil millones de parámetros activos por token
```

Un modelo MoE tiene muchos “expertos” internos. Para cada token, el router del modelo elige solo algunos expertos, no todos.

Lo bueno:
- Puede comportarse como un modelo grande en conocimiento/capacidad.
- Cada token puede ser más barato de calcular que en un modelo denso de 35B.
- Puede ir más rápido que un 35B denso.

Lo malo:
- Aunque solo active 3B por token, **los 35B totales siguen ocupando memoria**.
- Para tu regla de “sin offloading”, todos esos pesos tienen que caber en VRAM.
- El consumo de VRAM se parece más al tamaño total cuantizado que al tamaño activo.

Comparación simple:

| Tipo | Ejemplo | Cálculo por token | Memoria necesaria |
|---|---|---:|---:|
| Denso | 14B | Usa los 14B | 14B cuantizado |
| MoE | 35B-A3B | Usa ~3B por token | 35B cuantizado |

Por eso un **35B-A3B** puede ser rápido, pero no necesariamente fácil de cargar en 16 GB. El “A3B” ayuda en velocidad/cómputo, no tanto en VRAM.
---


Sí, **probablemente sí**, pero con una condición importante: no sería “controlar cualquier Codex CLI por SSH”, sino **controlar una sesión de Codex vinculada a tu cuenta de ChatGPT/OpenAI** en el equipo Windows.

La idea sería:

```text
iPhone / ChatGPT app con Codex
        ↓
Cuenta OpenAI
        ↓
Codex app en Windows
        ↓
Tu máquina Windows / proyecto / comandos
```

Según reportes recientes, Codex en la app móvil permite supervisar y controlar Codex en el ordenador: revisar cambios, aprobar acciones, cambiar modelos e iniciar tareas. También se ha publicado versión Windows de la app Codex. No he encontrado una página oficial clara de OpenAI que lo detalle de forma estable, así que lo tomaría como función en evolución, no como infraestructura garantizada para servidor Linux. Fuentes: [The Verge](https://www.theverge.com/ai-artificial-intelligence/930763/openai-codex-chatgpt-ios-android-app-preview), [TechRadar](https://www.techradar.com/pro/openai-releases-a-windows-version-of-codex-coding-app).

Lo que **sí** parece encajar:
- iOS ChatGPT/Codex controlando Codex en **Windows**.
- Revisar tareas, aprobar comandos, ver progreso.
- Usarlo como “mando remoto” cómodo.

Lo que **no** esperaría:
- Que desde iOS controles directamente un **Codex CLI suelto en Ubuntu Server**.
- Que sea equivalente a una terminal remota completa.
- Que instale stacks en tu servidor Linux si Codex está corriendo en Windows, salvo que Windows tenga acceso SSH/scripts hacia el servidor.

Para tu caso, el camino cómodo podría ser:

```text
iPhone Codex
→ Codex Windows
→ repo con scripts Ansible/SSH
→ Ubuntu Server IA
```

Así usas el móvil como interfaz, Windows como “host Codex” y el servidor como objetivo. Es menos infierno que SSH móvil, pero sigue conviniendo poner límites a lo que Codex puede ejecutar.
---


Para recuperarlo rápido, yo haría **dos niveles de backup**:

**1. Backup pequeño y frecuente: configuración**
Esto es lo importante para reconstruir el servidor sin sufrir.

Guarda:

```text
~/ai/tabbyAPI/config.yml
~/ai/tabbyAPI/api_tokens.yml
~/ai/tabbyAPI/start_options.json si existe
~/ai/models/  opcional, si no quieres redescargar modelos
~/.ssh/
lista de paquetes instalados
versión de driver NVIDIA
```

Comandos útiles:

```bash
mkdir -p ~/backup-info

dpkg --get-selections > ~/backup-info/packages.txt
nvidia-smi > ~/backup-info/nvidia-smi.txt
python3 --version > ~/backup-info/python-system.txt
ls -R ~/ai > ~/backup-info/ai-tree.txt
```

Luego crea un backup comprimido de configs, sin modelos:

```bash
tar -czvf tabby-config-backup.tar.gz \
  ~/ai/tabbyAPI/config.yml \
  ~/ai/tabbyAPI/api_tokens.yml \
  ~/backup-info
```

Lo bueno: pequeño, fácil de restaurar.  
Lo malo: los modelos tendrías que bajarlos otra vez.

**2. Backup grande: modelos**
Los modelos ocupan mucho, pero si quieres recuperación rápida, guarda también:

```bash
tar -czvf ai-models-backup.tar.gz ~/ai/models
```

Lo bueno: restauras sin esperar descargas enormes.  
Lo malo: backups de decenas o cientos de GB.

**Mi recomendación real**
Usaría **restic** o **borgbackup** hacia otro disco/NAS. Haría backup frecuente de config y opcionalmente modelos.

Estructura mínima a respaldar:

```bash
~/ai/tabbyAPI/config.yml
~/ai/tabbyAPI/api_tokens.yml
~/ai/models
~/backup-info
```

Y además guardaría un archivo `restore-notes.txt` con algo así:

```text
Ubuntu Server 26.04
Driver: nvidia-driver-595-server-open
Python: uv Python 3.13
TabbyAPI: ~/ai/tabbyAPI
Arranque: source venv/bin/activate && python main.py
Modelos: /home/sico/ai/models
Puerto: 5000
```

Para recuperación ultrarrápida, lo mejor es: **config + notas + lista de modelos**, y los modelos grandes solo si tienes espacio de sobra.
---


Para tu **RTX 5060 Ti 16 GB**, mi elección principal ahora mismo sería:

**Qwen3-14B Instruct en EXL2, 4.5-5.0bpw.**

Es el mejor equilibrio para “sustituir a Gemini” en uso general: español decente, razonamiento bueno, programación razonable, modo thinking/no-thinking y contexto largo. Qwen publica Qwen3-14B como modelo abierto con contexto de hasta 128K y soporte multilingüe amplio, incluyendo español ([Qwen3](https://qwenlm.github.io/blog/qwen3/)).

La parte de **búsqueda en internet** no la pone el modelo, la pone la interfaz. Para eso usaría:

```text
TabbyAPI + Qwen3-14B EXL2 + Open WebUI + SearXNG
```

Open WebUI tiene integración de búsqueda web con SearXNG; la documentación indica cómo configurarlo y que luego se activa por sesión en el chat ([Open WebUI SearXNG](https://docs.openwebui.com/features/chat-conversations/web-search/providers/searxng/)). TabbyAPI te da el servidor OpenAI-compatible para ExLlama/EXL2 ([TabbyAPI](https://github.com/theroyallab/tabbyAPI)).

**Ranking realista para tu GPU:**

| Opción | Qué pondría | Lo bueno | Lo malo |
|---|---|---|---|
| Mejor equilibrio | **Qwen3-14B EXL2 4.5/5.0bpw** | Generalista, buen español, razonamiento, entra bien en 16 GB | No es Gemini Pro; búsqueda depende de Open WebUI/SearXNG |
| Más rápido | Qwen3-8B EXL2 6.0bpw | Muy fluido, mucho contexto | Menos capaz en tareas complejas |
| Más “Gemini-like” por multimodal | Gemma 4 12B | Google la plantea para 16 GB y multimodal local ([Google Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)) | EXL2/Tabby puede no ser el camino más maduro para multimodal |
| Más calidad si aceptas ir justo | Mistral Small 3/3.2 24B EXL2 3.5-4.0bpw | Muy buen modelo de 24B; Mistral lo vende como rápido y fuerte para su tamaño ([Mistral Small 3](https://mistral.ai/news/mistral-small-3/)) | Menos margen de VRAM, menos contexto, más lento |

Mi apuesta práctica: **Qwen3-14B EXL2 5.0bpw** como modelo diario. Si ves que la VRAM va justa con mucho contexto, baja a **4.0/4.5bpw**. Si quieres máxima fluidez, **Qwen3-8B 6.0bpw**.

No esperes paridad total con Gemini: te faltarán el entrenamiento masivo propietario, la búsqueda integrada perfecta y algunas capacidades multimodales. Pero para chat general, consultas con web, resumen, código moderado y uso privado, esa combinación es bastante sólida.
---


Instala **`nvidia-driver-595-server-open`**.

En tu lista es la opción que mejor encaja con tu caso:

```text
595 = rama más nueva disponible en Ubuntu
server = orientada a servidor/cómputo
open = módulos kernel abiertos/precompilados, buena opción para RTX 50-series
```

Yo haría:

```bash
sudo apt update
sudo apt install nvidia-driver-595-server-open nvidia-utils-595-server
sudo reboot
```

Después del reinicio:

```bash
nvidia-smi
```

Si `nvidia-smi` muestra la 5060 Ti y la versión del driver, vas bien.

No elegiría estas salvo necesidad:

- `nvidia-driver-595`: más orientado a desktop/gaming.
- `nvidia-driver-595-open`: open, pero no server.
- `nvidia-driver-580-server-open`: buena alternativa si 595 te da problemas, más conservadora.
- `nvidia-driver-580-server`: fallback si por alguna razón `open` falla.

Ubuntu recomienda los drivers con sufijo **`-server`** para servidores y tareas de cómputo, y `ubuntu-drivers --gpgpu` para este caso ([Ubuntu docs](https://ubuntu.com/server/docs/how-to/graphics/install-nvidia-drivers/)). Además, NVIDIA lista la rama 595 como rama de producción actual para Linux x86_64 en su archivo de drivers ([NVIDIA Unix drivers](https://www.nvidia.com/en-gb/drivers/unix/)).

Resumen: **pon `595-server-open`**. Si algo falla, baja a **`580-server-open`**.
---


**BPW** significa **bits per weight**, o sea: **bits por peso del modelo**.

Un modelo LLM tiene miles de millones de “pesos”. Cuantos más bits usas para guardar cada peso, más ocupa en VRAM y normalmente mejor conserva la calidad original. Cuantos menos bits, menos VRAM y más velocidad posible, pero más pérdida de calidad.

| BPW | Qué significa | Lo bueno | Lo malo |
|---:|---|---|---|
| 2.4-3.0 | Muy comprimido | Entran modelos grandes en poca VRAM | Más errores, peor razonamiento, más rarezas |
| 3.5-4.0 | Compresión fuerte pero usable | Buen equilibrio para modelos grandes | Puede perder sutileza |
| 4.5-5.0 | Punto dulce común | Buena calidad y uso razonable de VRAM | Ocupa más |
| 6.0-6.5 | Alta calidad | Cerca del modelo original | Menos modelos caben en 16 GB |
| 8.0 | Muy alta calidad | Muy poca pérdida | Ocupa mucho, menor margen de contexto |

Ejemplo sencillo: un modelo **14B a 4.0bpw** ocupa bastante menos que el mismo **14B a 6.0bpw**, pero el de 6.0bpw suele responder con más calidad.

Para tu **16 GB de VRAM**, regla rápida:

- **8B**: usa `5.0bpw`, `6.0bpw` o incluso más.
- **14B**: usa `4.0bpw` o `5.0bpw`.
- **20B/22B**: usa `3.0bpw` o `4.0bpw`.
- **30B/32B**: solo con BPW bajo, y con compromisos.

Yo empezaría con **14B 4.0bpw o 5.0bpw**. Es donde probablemente notes más mejora respecto a modelos pequeños sin hacer sufrir demasiado a la GPU.
---


Sí. Primero expón TabbyAPI en la LAN.

Edita `config.yml`:

```bash
cd ~/ai/tabbyAPI
nano config.yml
```

Busca `network:` y déjalo así:

```yaml
network:
  host: 0.0.0.0
  port: 5000
  disable_auth: false
```

`0.0.0.0` hace que escuche en todas las interfaces de red; TabbyAPI lo documenta así en su `config_sample.yml` ([config_sample.yml](https://github.com/theroyallab/tabbyAPI/blob/main/config_sample.yml)).

Reinicia Tabby:

```bash
source venv/bin/activate
python main.py
```

En el servidor mira su IP:

```bash
hostname -I
```

Desde otro equipo de la red prueba:

```bash
curl http://IP_DEL_SERVIDOR:5000/v1/models \
  -H "Authorization: Bearer TU_API_KEY"
```

Si tienes `ufw` activo:

```bash
sudo ufw allow from 192.168.0.0/16 to any port 5000 proto tcp
```

Ajusta el rango si tu red es `10.0.0.0/8` o `172.16.0.0/12`.

Para administrarlo cómodamente, tienes tres niveles:

| Opción | Para qué | Mi opinión |
|---|---|---|
| Redoc de Tabby | Ver endpoints y probar API | Ya lo tienes en `/redoc`, útil pero técnico |
| Open WebUI | Chat bonito, usuarios, modelos vía API, más adelante web search | Mejor opción general |
| SillyTavern + Tabby Loader | Cargar/descargar modelos desde UI, presets, parámetros | Muy cómodo para Tabby, menos “servidor corporativo” |

Ahora mismo, sin Docker, lo más inmediato es usar **Redoc**:

```text
http://IP_DEL_SERVIDOR:5000/redoc
```

Pero para administración cómoda de verdad yo pondría después **Open WebUI** o **SillyTavern + TabbyAPI Loader**. TabbyAPI Loader permite cargar/descargar modelos y configurar parámetros desde SillyTavern usando la admin key ([ST-tabbyAPI-loader](https://github.com/theroyallab/ST-tabbyAPI-loader)).

Importante: no abras el puerto 5000 a internet. Solo LAN o VPN tipo Tailscale/WireGuard.
---


Te falta instalar la CLI de Hugging Face en el venv de Tabby.

Haz:

```bash
cd ~/ai/tabbyAPI
source venv/bin/activate
uv pip install -U "huggingface_hub[hf_transfer]"
```

Comprueba:

```bash
which huggingface-cli
huggingface-cli --version
```

Luego descarga:

```bash
mkdir -p ~/ai/models

huggingface-cli download turboderp/Qwen3-8B-exl3 \
  --revision 4.0bpw \
  --local-dir ~/ai/models/Qwen3-8B-exl3-4.0bpw
```

Alternativa si el comando `huggingface-cli` siguiera sin aparecer:

```bash
python -m huggingface_hub.commands.huggingface_cli download turboderp/Qwen3-8B-exl3 \
  --revision 4.0bpw \
  --local-dir ~/ai/models/Qwen3-8B-exl3-4.0bpw
```
---


Sí: el script te ha cambiado el entorno a **cu12/cu128** aunque antes tenías **cu13/cu130** funcionando.

Lo bueno: **TabbyAPI ha arrancado bien** y ya tienes endpoints:

```text
http://127.0.0.1:5000/v1/completions
http://127.0.0.1:5000/v1/chat/completions
```

Lo malo: te ha downgraded:

```text
torch 2.11.0+cu130 -> torch 2.9.0+cu128
exllamav3 cu132 -> exllamav3 cu128
flash-attn cu130 -> cu128
```

Eso no significa que no use GPU. Los drivers NVIDIA son compatibles hacia atrás, así que CUDA 12.8 puede funcionar sobre tu driver CUDA 13.2. Pero si queremos el camino moderno para tu RTX 50-series, mejor dejarlo en **cu13**.

Primero: como has pegado la API key y admin key en el chat, yo las rotaría. Para el servidor con `Ctrl+C` y luego:

```bash
rm -f api_tokens.yml
```

Se regenerarán al arrancar.

Después, corrige a cu13:

```bash
cd ~/ai/tabbyAPI
source venv/bin/activate
rm -f start_options.json
uv pip install -U ".[cu13]"
```

Comprueba que volvió a cu13:

```bash
python -c "import torch; print(torch.__version__); print(torch.version.cuda); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

Quieres ver algo parecido a:

```text
2.11.0+cu130
13.0
True
NVIDIA GeForce RTX 5060 Ti
```

Luego arranca evitando que `start.sh` vuelva a elegir cu12:

```bash
python main.py
```

Resumen: **lo que tienes funciona**, pero para tu objetivo yo lo dejaría en **cu13** y arrancaría con `python main.py` en vez de `./start.sh` hasta que veamos cómo fijar esa preferencia.
---


Con ese equipo, **LM Studio headless / `llmster` es bastante razonable** si priorizas facilidad para probar modelos.

Tu perfil real:

```text
CPU: i5-12500F
RAM: 32 GB DDR4
GPU: RTX 5060 Ti 16 GB
SO: Ubuntu Server 26.04 LTS
Objetivo: servidor IA local, probar modelos, endpoint LAN
```

Qué te encaja mejor:

| Opción | Encaje en tu equipo |
|---|---|
| LM Studio headless | Muy buen equilibrio comodidad/rendimiento |
| Ollama | Muy cómodo, menos control fino |
| llama.cpp compilado | Mejor control y benchmark, más manual |
| TabbyAPI | Rápido pero catálogo/admin limitado |
| vLLM | Interesante para NVFP4/Qwen3.6, pero más complejo |

Con **16 GB VRAM**, modelos razonables:

| Modelo | Cuantización aproximada | Comentario |
|---|---:|---|
| 8B | Q5/Q6/Q8 | Cómodo |
| 12B/14B | Q4/Q5 | Punto dulce |
| 27B | Q3/IQ4 | Justo |
| 35B-A3B | IQ3/IQ4 | Muy justo, probar con contexto moderado |
| 70B | No recomendado sin offload | Demasiado compromiso |

Tu **32 GB DDR4** ayudan para:
- cargar modelos desde disco,
- tener servicios auxiliares,
- algo de offload si aceptaras perder velocidad,
- Open WebUI/SearXNG/embeddings más adelante.

Pero si mantienes la regla **sin offload**, el límite práctico sigue siendo la **VRAM de 16 GB**.

Yo haría este orden:

1. **LM Studio headless** para comodidad.
2. Probar GGUFs Q4/Q5 de 8B-14B.
3. Probar algún Qwen3.6 27B en IQ4/Q3 si quieres apurar.
4. Solo compilar `llama.cpp` si ves que LM Studio no rinde bien o quieres flags más finas.
5. Dejar TabbyAPI apartado para EXL3 concretos que merezcan la pena.

Para tu objetivo actual, sí: **lmster en servidor + LM Studio/Open WebUI en cliente** parece mejor camino que seguir peleando TabbyAPI.
---


Sí, **llama.cpp tiene bastante sentido para ti**. Probablemente es el punto medio entre TabbyAPI y Ollama:

```text
Más flexible que TabbyAPI
Más controlable que Ollama
Menos lío Python que vLLM/Tabby
Muchísimo catálogo GGUF
```

Lo bueno:
- Usa **GGUF**, que tiene muchísimo más catálogo que EXL3.
- Tiene servidor **OpenAI-compatible** con `llama-server` (`/v1/chat/completions`) ([llama.cpp](https://github.com/ggml-org/llama.cpp)).
- Soporta **tool/function calling** con `--jinja` ([docs function calling](https://github.com/ggml-org/llama.cpp/blob/master/docs/function-calling.md)).
- Soporta **multimodal** en `llama-server` con `mmproj` para modelos compatibles ([docs multimodal](https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md)).
- No dependes de Python 3.13/3.14 ni de wheels raras.
- Puedes hacer **offload completo a GPU** si el modelo cabe, o controlar capas si algún día aceptas híbrido.

Lo malo:
- No suele ser tan rápido como EXL3 en NVIDIA para batch pequeño.
- Los modelos GGUF grandes pueden tentar a usar offload CPU, que tú querías evitar.
- Multimodal requiere bajar el **GGUF del modelo + mmproj** correcto.
- Para RTX 50/Blackwell, yo lo compilaría desde fuente con CUDA, no usaría binarios al azar.

Para tu equipo, yo probaría esta ruta:

```bash
sudo apt install git cmake build-essential libcurl4-openssl-dev
cd ~/ai
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=120
cmake --build build --config Release -j$(nproc)
```

Luego sirves un GGUF:

```bash
./build/bin/llama-server \
  -m /home/sico/ai/models/modelo.gguf \
  --host 0.0.0.0 \
  --port 8080 \
  -ngl 999 \
  -c 8192
```

`-ngl 999` intenta meter todas las capas en GPU. Si no cabe, fallará o tendrás que bajar modelo/contexto; eso respeta tu idea de no offloading.

Para empezar con 16 GB buscaría GGUFs tipo:

```text
Qwen3 8B Q5_K_M / Q6_K
Qwen3 14B Q4_K_M / Q5_K_M
Gemma 4 12B Q4_K_M / Q5_K_M
Qwen2.5-VL / Gemma vision si quieres multimodal
```

Mi veredicto: **sí, probaría llama.cpp antes de abandonar el servidor**. Es menos “máximo rendimiento NVIDIA” que Tabby, pero mucho más cómodo para experimentar con modelos reales, multimodal y tools.
---


Veo que este repo está justo orientado a lo que querías probar: GGUF, llama.cpp/LM Studio/Ollama, multimodal, tools y MTP. Ahora la pregunta dura es si la cuantización recomendada cabe con margen en 16 GB.
---


Tienes razón: mis ejemplos de “Qwen3” eran genéricos y ya van un poco por detrás si estás mirando lo último. A día de hoy, para buscar modelos deberías distinguir:

| Nombre | Qué es |
|---|---|
| `Qwen3` | Familia base de 2025: 0.6B, 1.7B, 4B, 8B, 14B, 32B, 30B-A3B, 235B-A22B |
| `Qwen3.5` | Evolución 2026, con modelos nuevos y omni/multimodales |
| `Qwen3.6` | Línea más reciente que estás viendo: `27B`, `35B-A3B`, etc. |
| `Qwen3.6-Plus/Max` | Normalmente modelos de API/plataforma, no siempre pesos locales abiertos |

Los repos oficiales actuales que has estado viendo existen como:

```text
Qwen/Qwen3.6-27B
Qwen/Qwen3.6-35B-A3B
```

La colección oficial de Qwen3.6 aparece en Hugging Face y el repo de QwenLM lista lanzamientos de `Qwen3.6-35B-A3B` y `Qwen3.6-27B` en abril de 2026 ([Qwen3.6 GitHub](https://github.com/QwenLM/Qwen3.6), [Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B), [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)).

Para tu búsqueda en GGUF/LM Studio/llama.cpp, yo buscaría ya:

```text
Qwen3.6-27B GGUF
Qwen3.6-27B Q4_K_M GGUF
Qwen3.6-35B-A3B GGUF
Qwen3.6-35B-A3B IQ4_XS GGUF
Qwen3.6-35B-A3B Q3_K_M GGUF
```

Pero para **16 GB sin offload**, cuidado:

| Modelo | Probabilidad de encajar cómodo |
|---|---:|
| `Qwen3-14B` Q4/Q5 | Alta |
| `Qwen3.6-27B` Q3/Q4 | Justo |
| `Qwen3.6-35B-A3B` Q3/IQ4 | Muy justo, depende del contexto |
| `Qwen3.6-35B-A3B` 6bpw | No lo esperaría cómodo |

Así que sí: si estamos comparando opciones actuales, debería hablar más de **Qwen3.6**. Los ejemplos `Qwen3-8B` y `Qwen3-14B` siguen siendo útiles como modelos pequeños/medianos estables, pero no son la última línea.
---


Me falta una pieza para no venderte humo: en 16 GB, “mejor” no es siempre el modelo más grande. Si el modelo entra demasiado justo, pierdes contexto, latencia y estabilidad; por eso voy a priorizar algo que puedas usar todos los días, no solo cargar una vez para hacer una captura.
---


Bájalos con **Hugging Face CLI**, no con `start.sh`, para que no vuelva a tocar dependencias.

Primero instala la CLI dentro del venv:

```bash
cd ~/ai/tabbyAPI
source venv/bin/activate
uv pip install -U huggingface_hub[hf_transfer]
```

Crea carpeta de modelos:

```bash
mkdir -p ~/ai/models
```

Formato general:

```bash
huggingface-cli download USUARIO/REPO \
  --revision RAMA \
  --local-dir ~/ai/models/NOMBRE_LOCAL
```

Ejemplo con un modelo EXL2:

```bash
huggingface-cli download royallab/L3-8B-Instruct-abliterated-v3-exl2 \
  --revision 4bpw \
  --local-dir ~/ai/models/L3-8B-Instruct-abliterated-v3-exl2-4bpw
```

En EXL2/EXL3, la **rama** suele ser el BPW:

```text
4bpw
4.0bpw
4_0
5bpw
5.0bpw
6bpw
```

Depende del repo. Hay que mirar la pestaña **Files and versions** del modelo en Hugging Face.

Para tu servidor, yo buscaría en Hugging Face:

```text
Qwen3 8B exl2
Qwen3 14B exl2
Qwen3 14B exl3
bartowski Qwen3 exl2
LoneStriker Qwen3 exl2
```

Algunos repos guardan cada cuantización en ramas; otros hacen un repo separado por cuantización. Lo importante es que dentro de la carpeta descargada veas archivos tipo:

```text
config.json
tokenizer.json
*.safetensors
```

Luego en TabbyAPI tienes dos opciones:

1. Editar `config.yml` y apuntar a la carpeta/modelo.
2. Usar el endpoint admin para cargar modelo.

Primero descarguemos uno pequeño. Si quieres ir seguro para prueba inicial, baja un **8B 4-6bpw**. Después vamos a por **Qwen3-14B 4.5/5bpw**.
---


Perfecto: el driver está bien cargado y la GPU está limpia.

Lo bueno:
- Detecta correctamente **RTX 5060 Ti**.
- Driver **595.71.05** activo.
- CUDA visible: **13.2**.
- VRAM completa disponible: **16311 MiB**.
- Consumo/temperatura en reposo muy bien: **34C, 4W**.
- No hay procesos ocupando VRAM.

Lo malo o a vigilar:
- `Persistence-M` está en **Off**. Para servidor de IA conviene activarlo, reduce latencias de inicialización y evita que la GPU “desaparezca” entre cargas.
- Todavía falta probar carga real con PyTorch/TabbyAPI; `nvidia-smi` solo confirma driver.

Activa persistence mode:

```bash
sudo nvidia-smi -pm 1
```

Y para comprobar:

```bash
nvidia-smi
```

Si quieres dejar el equipo preparado para IA, el siguiente bloque sería instalar herramientas base:

```bash
sudo apt install git curl wget build-essential python3-venv python3-pip nvtop tmux htop
```

Luego ya iría TabbyAPI/ExLlama y un modelo EXL2 pequeño primero para validar rendimiento.
---


Voy a comprobar la nomenclatura actual de Qwen porque ahí hay bastante confusión: algunos repos dicen Qwen3 aunque sean 3.5/3.6, otros usan fechas o nombres del cuantizador, y los GGUF añaden todavía otra capa.
---


Ahora ya estamos en la parte buena: Tabby está vivo y el modelo está en disco. Voy a darte la vía más controlada, editando `config.yml` o cargando por API, sin volver a usar `start.sh`.
---


Voy a comprobar a qué “Pi.dev” te refieres y qué capacidades reales tiene ahora, porque hay varias piezas con nombres parecidos y no quiero venderte otro flujo que luego sea igual de incómodo.
---


Sí, puedes plantearlo como “modo autónomo”, pero con una frontera: **Codex puede ejecutar el plan sin pedirte permiso en cada paso si lo lanzas con permisos amplios**, pero no conviene darle barra libre absoluta sin reglas. Lo bueno es que para instalar `llmster` el plan es bastante acotado.

LM Studio documenta que `llmster` es el daemon headless recomendado, se instala con:

```bash
curl -fsSL https://lmstudio.ai/install.sh | bash
```

y se arranca con:

```bash
lms daemon up
```

También expone API OpenAI-compatible, incluyendo `/v1/models`, `/v1/chat/completions`, `/v1/responses` y embeddings ([LM Studio headless](https://lmstudio.ai/docs/developer/core/headless), [OpenAI-compatible](https://lmstudio.ai/docs/developer/openai-compat)).

**Prompt Para Codex**
Usa algo así:

```text
Quiero que configures este Ubuntu Server 26.04 como servidor LM Studio headless con llmster.

Objetivo:
- Instalar LM Studio headless/llmster.
- Verificar que detecta la RTX 5060 Ti con CUDA.
- Configurar el servidor para escuchar en la LAN, no en internet.
- Exponer API OpenAI-compatible.
- Crear un servicio systemd para arrancar al boot.
- Documentar comandos de operación: status, start, stop, logs, listar modelos, descargar modelo, cargar modelo, descargar de VRAM.
- No instalar Docker.
- No tocar TabbyAPI salvo para documentar que queda apartado.
- No borrar modelos ni configuraciones existentes.
- No abrir puertos fuera de LAN.
- Si necesitas descargar paquetes oficiales de LM Studio, hazlo.
- Si una acción es destructiva o borra datos, para y pregunta.

Trabaja de forma autónoma:
1. Detecta IP LAN, GPU, driver, CUDA visible y servicios en puertos 1234/5000/8080.
2. Instala dependencias mínimas.
3. Instala llmster siguiendo la documentación oficial.
4. Arranca el daemon.
5. Configura API en LAN.
6. Activa autenticación si está disponible.
7. Crea systemd user service o system service, elige el más robusto para Ubuntu Server y explica la elección.
8. Prueba:
   - lms funciona
   - endpoint /v1/models responde desde localhost
   - endpoint responde desde IP LAN
   - nvidia-smi muestra carga cuando se ejecute un modelo
9. Deja un README en ~/ai/LMSTUDIO_SERVER.md con todo.

Al final dame:
- Qué se instaló.
- Puertos abiertos.
- Comandos para administrar.
- Cómo conectar Open WebUI/cliente.
- Qué queda pendiente.
```

**Permisos**
Si quieres que no te pregunte cada paso, en Codex tendrías que ejecutarlo en un modo equivalente a:

```text
workspace-write + network enabled + approvals on-failure/never
```

o el equivalente que tenga tu instalación. Lo bueno: instala fluido. Lo malo: si el agente se equivoca, puede dejar servicios/paquetes mal puestos. Yo no usaría un “dangerous” total salvo en una máquina recién instalada o snapshot.

**Regla sensata**
Dale permiso autónomo para:

```text
apt install
curl oficial de lmstudio.ai
crear systemd service
editar archivos bajo ~/ai y ~/.config
abrir puerto LAN concreto
```

Pero que pregunte para:

```text
rm -rf
purge de paquetes
cambiar firewall global
exponer a internet
tocar SSH
desinstalar drivers NVIDIA
```

Así consigues casi lo mismo que ves con Claude Code, pero sin jugar a la ruleta con el servidor.
---


Sí, lo enfocaría así: **TabbyAPI sigue siendo la opción base más sensata para tu objetivo**. El “NVIDIA Toolkit” puede significar varias cosas, y no todas te dan más rendimiento.

**Separación importante:**

| Nombre | Para qué sirve | ¿Lo usaría ahora? |
|---|---|---|
| NVIDIA driver | Lo que ya tienes | Sí, ya está correcto |
| CUDA Toolkit | Compiladores/librerías CUDA completas | No de entrada |
| NVIDIA Container Toolkit | Permite usar la GPU dentro de Docker | Sí, si vas con Docker/Open WebUI/SearXNG |
| TensorRT-LLM | Stack NVIDIA de inferencia optimizada | Lo miraría después, no como primera instalación |
| TabbyAPI + ExLlama | Servidor OpenAI-compatible para EXL2/EXL3 | Sí, primera opción |

Para **máxima inteligencia sin offloading** en 16 GB, tu límite real no es la potencia de la 5060 Ti, es la **VRAM**. Sin offload, todo el modelo + KV cache deben caber en esos ~16 GB. Por eso mi stack recomendado sería:

```text
TabbyAPI
+ ExLlamaV3/ExLlamaV2
+ modelos EXL2/EXL3
+ Open WebUI si quieres interfaz y búsqueda
+ SearXNG para web search local
```

TabbyAPI es el backend oficial/recomendado para ExLlamaV2/V3 y expone API compatible con OpenAI ([ExLlamaV3](https://github.com/turboderp-org/exllamav3), [TabbyAPI](https://github.com/theroyallab/tabbyAPI)).

**Modelos que probaría, en orden:**

| Prioridad | Modelo/formato | Motivo | Pega |
|---|---|---|---|
| 1 | **Qwen3-14B EXL2/EXL3 4.5-5bpw** | Mejor equilibrio inteligencia/VRAM/velocidad | No es el máximo absoluto |
| 2 | **Qwen3-30B-A3B EXL2/EXL3 3bpw** | Puede ser más capaz en algunas tareas por MoE | Muy justo; contexto limitado |
| 3 | **Gemma 4 12B cuantizado** | Muy atractivo para 16 GB y multimodal según Google | Ecosistema EXL/Tabby quizá menos directo |
| 4 | **Mistral Small 24B 3-3.5bpw** | Modelo fuerte generalista | Cuantización agresiva, puede perder calidad |

Mi apuesta diaria: **Qwen3-14B 5bpw**.  
Mi prueba “a ver hasta dónde llega”: **Qwen3-30B-A3B 3bpw**, sin offload y con contexto moderado.

Sobre **TensorRT-LLM**: NVIDIA lo presenta como su biblioteca optimizada para inferencia LLM de alto rendimiento en GPUs NVIDIA ([NVIDIA TensorRT-LLM](https://developer.nvidia.com/tensorrt-llm)). Lo bueno es que puede sacar mucho rendimiento, especialmente con cuantizaciones NVIDIA modernas. Lo malo: más fricción, conversiones, compatibilidad por modelo, y menos cómodo para ir cambiando modelos como harías con TabbyAPI. Para un servidor casero potente pero de una sola GPU de 16 GB, yo lo dejaría como segunda fase.

Instalaría ahora:

```bash
sudo apt install git curl wget build-essential python3-venv python3-pip nvtop tmux htop
```

Y si vas a usar Docker:

```bash
sudo apt install docker.io docker-compose-v2
```

Luego sí añadiría **NVIDIA Container Toolkit**, pero solo si vas a contenerizar servicios. Para TabbyAPI puro en venv no es imprescindible.

Conclusión: **empieza con TabbyAPI + EXL2/EXL3**. No instales CUDA Toolkit manualmente todavía. Si más adelante quieres exprimir benchmarks o montar un endpoint más “producción”, probamos TensorRT-LLM/vLLM, pero ahora mismo el camino con mejor relación rendimiento/complicación es TabbyAPI.
---


Sí: con una NVIDIA y TabbyAPI, el formato que normalmente te va a dar mejor rendimiento es **EXL2** usando **ExLlamaV2/ExLlamaV3**. TabbyAPI es precisamente un servidor para ExLlama, y el propio repo indica que para GGUF miran a otro proyecto hermano, no a TabbyAPI directamente ([TabbyAPI](https://github.com/theroyallab/tabbyAPI)). ExLlamaV2 también recomienda TabbyAPI como servidor OpenAI-compatible ([ExLlamaV2](https://github.com/turboderp-org/exllamav2)).

**Mi recomendación para tu equipo:**

| Capa | Opción recomendada | Lo bueno | Lo malo |
|---|---|---|---|
| SO | Ubuntu Server LTS | Estable, fácil de mantener | Driver NVIDIA en GPUs nuevas puede requerir versión reciente |
| Driver | NVIDIA propietario/open kernel module reciente | Mejor CUDA/rendimiento | Evitar Nouveau para IA |
| Backend | TabbyAPI + ExLlamaV3/ExLlamaV2 | Muy rápido en NVIDIA, ideal para una sola GPU | Menos flexible que llama.cpp |
| Formato | **EXL2** | Mejor elección para rendimiento puro en NVIDIA | Menos universal que GGUF |
| Alternativa | GGUF + llama.cpp | Muy compatible, flexible, sirve para CPU/GPU/offload | En tu caso suele rendir menos que EXL2 |
| Modelos | 7B/8B en 4-6 bpw, 12B/14B en 4-5 bpw | Buena calidad y velocidad en 16 GB | 30B/32B ya exige cuantización agresiva y contexto moderado |

Para tu **5060 Ti 16 GB**, yo empezaría con modelos **EXL2 de 4.0 a 5.0 bpw**. Un 7B/8B a 5-6 bpw debería ir cómodo. Un 14B a 4-5 bpw será probablemente el punto dulce si buscas más calidad. Un 32B puede entrar muy justo en 16 GB, pero con cuantización baja y contexto recortado; ahí ganarías “inteligencia bruta” a costa de velocidad, calidad de cuantización y margen de VRAM.

Cosas que sí instalaría además:

```bash
nvidia-driver
nvidia-container-toolkit   # si vas con Docker
nvtop
tmux
htop
ufw
tailscale                  # si quieres acceder fuera de casa sin abrir puertos
```

Y para servirlo bien:

- **TabbyAPI** como servidor principal.
- **Open WebUI** si quieres interfaz web cómoda.
- **LiteLLM** si quieres enrutar varios modelos o exponer una API estilo OpenAI más flexible.
- **Caddy** o **nginx** si lo vas a publicar con HTTPS.
- `systemd` para dejar TabbyAPI arrancando solo.

Lo más importante: **no te obsesiones con CUDA Toolkit completo al principio**. Muchas instalaciones Python ya traen wheels preparados; lo crítico es que `nvidia-smi` funcione bien y que PyTorch/ExLlama vean la GPU. En una 5060 Ti, usa un driver muy reciente; hubo reportes de soporte Linux temprano irregular en RTX 5060/5060 Ti, así que conviene validar con `nvidia-smi` antes de montar todo encima ([foro NVIDIA](https://forums.developer.nvidia.com/t/rtx-5060-driver/334371)).

Resumen corto: **Ubuntu Server + driver NVIDIA reciente + TabbyAPI + EXL2**. GGUF está bien para compatibilidad, pero si tu prioridad es rendimiento en esa NVIDIA, EXL2 es el camino.
---


Voy a mirarlo desde el objetivo concreto: endpoints locales, máxima inteligencia dentro de 16 GB, cero offloading. La pregunta clave es si conviene priorizar TabbyAPI/EXL2 o moverse a un stack NVIDIA más “oficial” como TensorRT-LLM, que puede rendir mucho pero también trae más complejidad.
---


Yo **no tiraría con Python 3.14 para TabbyAPI ahora mismo**, salvo que quieras hacer de beta tester.

Aunque Ubuntu 26.04 lo traiga como Python del sistema, para IA con CUDA lo prudente es usar una versión con más ruedas precompiladas y menos sorpresas. En este caso elegiría:

```text
Python 3.12
```

Motivo: TabbyAPI indica `cu13` como **CUDA 13.x + ExLlamaV3 + Python 3.12+**, pero muchas dependencias GPU no soportan igual de bien 3.14. Que el propio `cuda-python` soporte 3.14 no garantiza que PyTorch, ExLlama, FlashAttention u otras piezas tengan wheels correctos para 3.14. De hecho, sigue siendo habitual que librerías CUDA vayan por detrás en versiones nuevas de Python.

Lo bueno de Python 3.14:
- Es el Python del sistema en tu Ubuntu.
- Más moderno.

Lo malo:
- Mayor riesgo de que `pip` compile cosas desde fuente.
- Mayor riesgo de instalar versiones CPU por falta de wheel CUDA.
- Más errores raros con dependencias.
- Menos documentación práctica para TabbyAPI/ExLlama.

Usa Python 3.12 en un venv dedicado. No afecta al Python del sistema:

```bash
sudo apt install python3.12 python3.12-venv
cd ~/ai/tabbyAPI
python3.12 -m venv venv
source venv/bin/activate
python --version
```

Debería decir algo como:

```text
Python 3.12.x
```

Luego:

```bash
pip install -U pip setuptools wheel
pip install -U ".[cu13]"
```

Resumen: **sistema con Python 3.14, TabbyAPI con Python 3.12 en venv**. Es la opción más estable.
---


Significa esto:

Cuando instalas una librería con `pip`, por ejemplo PyTorch, normalmente no compilas nada. `pip` busca un paquete ya preparado llamado **wheel**.

Un wheel es un archivo precompilado tipo:

```text
torch-2.x.x-cp312-cp312-linux_x86_64.whl
```

Ese nombre dice cosas como:

```text
cp312 = Python 3.12
linux_x86_64 = Linux 64-bit
cuda/cu13 = versión con soporte GPU/CUDA
```

El problema: para cada combinación tiene que existir un wheel compatible:

```text
Python 3.12 + Linux + CUDA 13 + x86_64
Python 3.13 + Linux + CUDA 13 + x86_64
Python 3.14 + Linux + CUDA 13 + x86_64
```

Si usas Python 3.14 y todavía no hay wheel CUDA para esa combinación, pueden pasar varias cosas:

1. `pip` falla directamente.
2. `pip` intenta compilar desde código fuente, que suele ser lento y propenso a fallar.
3. `pip` instala una versión **CPU-only**, o sea, sin CUDA.

Una versión CPU-only funciona, pero no usa la NVIDIA. Entonces verías algo como:

```python
import torch
torch.cuda.is_available()
```

Y te respondería:

```text
False
```

Eso sería malo para ti porque TabbyAPI/ExLlama necesita usar la GPU. Tendrías driver NVIDIA perfecto, `nvidia-smi` perfecto, pero Python no podría usar CUDA.

Por eso conviene usar Python 3.12: hay más probabilidad de que todas las piezas GPU tengan wheels correctos. Es menos moderno, pero más fiable para IA local.
---


Sí, exactamente. Lo que estamos montando ahora es la **base nativa**:

```text
Ubuntu
+ driver NVIDIA
+ Python/venv
+ TabbyAPI
+ acceso directo a la GPU
```

Si lo metieras en Docker, la base cambiaría a:

```text
Ubuntu
+ driver NVIDIA en el host
+ Docker
+ NVIDIA Container Toolkit
+ runtime/configuración GPU para Docker
+ contenedor TabbyAPI
```

El driver **siempre** va en el host. El contenedor no “trae” el driver real; usa el driver del host a través del NVIDIA Container Toolkit.

Lo bueno de Docker:
- Reproducible.
- Más fácil borrar/recrear.
- Aísla dependencias.
- Útil cuando metas Open WebUI, SearXNG, LiteLLM, etc.

Lo malo ahora:
- Añade una capa más justo cuando estamos validando GPU + Tabby.
- Hay que instalar y configurar NVIDIA Container Toolkit.
- Hay que montar carpetas de modelos/config.
- Si falla CUDA, tienes que distinguir si falla el driver, Docker, el toolkit, el contenedor o TabbyAPI.

Por eso para **primer arranque de TabbyAPI** yo prefiero nativo en venv. Cuando ya sepamos:

```text
TabbyAPI instala
Torch/ExLlama ve la GPU
un modelo carga
la API responde
```

entonces Docker deja de ser una incógnita y pasa a ser una decisión de despliegue. Para ahora, venv es menos ruido.
---


Sí, tiene sentido. Es una buena prueba antes de meternos en `uv` o Python 3.12. La única condición: hazlo en un **venv separado**, así si falla no ensucia nada.

Prueba con Python 3.14:

```bash
cd ~/ai/tabbyAPI
python3.14 -m venv venv314
source venv314/bin/activate
python -m pip install -U pip setuptools wheel
python -m pip install -U ".[cu13]"
```

Luego verifica GPU:

```bash
python -c "import torch; print('torch:', torch.__version__); print('cuda available:', torch.cuda.is_available()); print('torch cuda:', torch.version.cuda); print('gpu:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"
```

Resultado bueno sería algo como:

```text
cuda available: True
gpu: NVIDIA GeForce RTX 5060 Ti
```

Si sale `True`, perfecto: seguimos con Python 3.14 y no complicamos más.

Si sale `False`, o instala Torch CPU-only, o falla compilando dependencias, entonces descartamos ese venv y pasamos a Python 3.12/3.13 gestionado por `uv`.

Lo bueno de probar 3.14: aprovechas el Python nativo de Ubuntu 26.04.  
Lo malo: si una dependencia CUDA aún no tiene wheel para 3.14, el fallo puede ser confuso o instalar algo sin GPU. Por eso la prueba de `torch.cuda.is_available()` es la frontera clara.
---


Vamos con `uv` + Python 3.13.

Desde una shell normal, sin `(venv314)`:

```bash
cd ~/ai/tabbyAPI
deactivate 2>/dev/null || true
rm -rf venv314 venv
```

Instala `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Carga `uv` en esta sesión:

```bash
source ~/.local/bin/env
```

Instala Python 3.13:

```bash
uv python install 3.13
```

Crea el venv:

```bash
uv venv --python 3.13 venv
source venv/bin/activate
python --version
```

Debería salir:

```text
Python 3.13.x
```

Luego instala TabbyAPI:

```bash
python -m pip install -U pip setuptools wheel
python -m pip install -U ".[cu13]"
```

Y prueba CUDA:

```bash
python -c "import torch; print('torch:', torch.__version__); print('cuda available:', torch.cuda.is_available()); print('torch cuda:', torch.version.cuda); print('gpu:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"
```

Resultado que queremos:

```text
cuda available: True
gpu: NVIDIA GeForce RTX 5060 Ti
```
---


Sí, puedes controlar un **Codex instalado en tu servidor desde el móvil**, pero no como “app mágica remota” del Codex local. Lo normal sería controlarlo como cualquier proceso de terminal remoto.

La forma práctica:

```text
Móvil
SSH app
   ↓
Servidor Ubuntu
tmux
   ↓
Codex CLI
```

**Opción recomendada**
1. Instala una app SSH en el móvil:
   - iOS: Blink Shell, Termius, Prompt.
   - Android: Termius, JuiceSSH, ConnectBot.

2. En el servidor usa `tmux`:

```bash
sudo apt install tmux
tmux new -s codex
```

3. Dentro de `tmux`, lanzas Codex:

```bash
codex
```

4. Desde el móvil te conectas por SSH y recuperas la sesión:

```bash
tmux attach -t codex
```

Lo bueno:
- Funciona desde cualquier móvil.
- Si se corta la conexión, Codex sigue vivo.
- Puedes dejar tareas largas corriendo.
- No necesitas exponer una web al exterior.

Lo malo:
- Es terminal puro.
- En móvil puede ser incómodo para editar mucho texto.
- Las aprobaciones siguen apareciendo en la sesión, salvo que configures Codex con más permisos.

Para acceso fuera de casa, yo usaría **Tailscale** antes que abrir SSH a internet:

```text
Móvil con Tailscale
Servidor con Tailscale
SSH por IP privada de Tailscale
```

Sobre “sin pedirme permiso a cada paso”: eso depende de cómo lances Codex. Puedes usar un modo más autónomo, pero yo lo limitaría a un servidor de pruebas. Lo razonable sería:

```text
Permitir:
- instalar paquetes
- editar /home/sico/ai
- crear servicios systemd concretos
- descargar desde fuentes oficiales

Preguntar:
- borrar datos
- tocar SSH
- cambiar firewall global
- desinstalar drivers NVIDIA
- exponer servicios a internet
```

Si quieres algo más cómodo que SSH desde móvil, puedes montar después:
- **code-server**: VS Code en navegador.
- **ttyd / wetty**: terminal web.
- **Open WebUI / dashboards** para IA, no para controlar Codex directamente.

Mi recomendación: **SSH + tmux + Tailscale**. Es simple, robusto y perfecto para controlar Codex en el servidor desde el móvil sin convertir tu servidor en una superficie de ataque enorme.
---


Te entiendo. Esa duda es muy normal, pero no lo leería como “me equivoqué claramente”.

La **RX 7900 XTX 24 GB** te habría dado más memoria, sí. Eso importa mucho para LLMs. Pero también te habría metido en el mundo **ROCm**, que en local AI suele ser más irregular que NVIDIA/CUDA.

Comparación honesta:

| GPU | Lo bueno | Lo malo |
|---|---|---|
| RTX 5060 Ti 16 GB | CUDA, compatibilidad amplia, menos dolor con IA, buena eficiencia | VRAM limitada |
| RX 7900 XTX 24 GB | 8 GB más de VRAM, mejor para modelos grandes GGUF/ROCm si va bien | ROCm más delicado, menos soporte en muchos stacks |
| RTX 5070 Ti/5080/5090 | Mejor equilibrio NVIDIA + VRAM/rendimiento | Mucho más caras |

La 7900 XTX habría sido mejor para:

- GGUF grandes en llama.cpp/LM Studio,
- modelos 27B/32B/35B con más contexto,
- más margen de KV cache,
- menos necesidad de cuantización agresiva.

Pero peor o más incierta para:

- vLLM,
- TensorRT/NVFP4,
- CUDA-first tooling,
- ExLlama,
- compatibilidad general con librerías nuevas,
- menos pelea técnica.

Tu 5060 Ti no es mala compra; es una compra con un límite claro: **16 GB**. Lo que te está doliendo es haber descubierto tarde que en IA local **la VRAM manda más que casi todo**.

Mi consejo práctico: no tomes una decisión desde el remordimiento. Primero prueba bien un stack más cómodo, tipo:

```text
LM Studio headless / Ollama
+ Open WebUI
+ GGUF Q4/Q5
```

Si después de 2-3 semanas ves que constantemente piensas “este modelo no entra por 2-6 GB”, entonces sí tienes un dato real: tu cuello de botella es VRAM. Ahí podrías valorar vender la 5060 Ti y saltar a 24 GB o más.

Pero si lo que te molesta ahora es sobre todo la experiencia TabbyAPI, cambiar de GPU no arreglaría eso. La 7900 XTX te habría dado más memoria, pero no necesariamente menos fricción.
---


Instala **Ubuntu Server normal**, no **minimized**.

Para tu caso, lo bueno de la normal es que tendrás menos fricción con drivers, red, herramientas base, headers, logs y dependencias. Lo malo es que instala algunos paquetes de más. La minimized solo la elegiría si quisieras una base muy limpia y ya sabes exactamente qué paquetes vas a añadir después. En un servidor de IA nuevo, no merece mucho la pena el ahorro.

Sobre **“buscar drivers de terceros”**: yo **no lo activaría para la GPU durante la instalación**. Haría la instalación limpia, reiniciaría, actualizaría el sistema y luego instalaría el driver NVIDIA server desde Ubuntu con `ubuntu-drivers --gpgpu`. Así evitas que el instalador te meta un driver genérico/no server o una rama no ideal para la RTX 5060 Ti.

Después del primer arranque:

```bash
sudo apt update
sudo apt full-upgrade
sudo reboot
```

Luego mira qué drivers ofrece para cómputo:

```bash
sudo ubuntu-drivers list --gpgpu
```

Y deja que Ubuntu elija el recomendado para servidor/cómputo:

```bash
sudo ubuntu-drivers install --gpgpu
```

Si quieres elegirlo manualmente, usa uno con sufijo **`-server`**, por ejemplo si aparece algo tipo:

```text
nvidia-driver-580-server
nvidia-driver-580-server-open
nvidia-driver-590-server
nvidia-driver-590-server-open
```

Para una RTX 50-series, yo priorizaría el **más nuevo recomendado por Ubuntu** y, si aparece como recomendado, la variante **`-server-open`**. Pero no fuerces un número a ciegas: en esa GPU es mejor mirar qué detecta `ubuntu-drivers list --gpgpu`.

Ubuntu documenta que los drivers **Enterprise Ready / `-server`** son los recomendados para servidores y tareas de cómputo, y que `ubuntu-drivers --gpgpu` es el camino recomendado para instalación en servidor ([Ubuntu Server NVIDIA drivers](https://ubuntu.com/server/docs/how-to/graphics/install-nvidia-drivers/)).

Una cosa importante: si puedes, deja **Secure Boot desactivado** en BIOS/UEFI para simplificar. Con Secure Boot también se puede, pero los módulos firmados/keys pueden añadir una capa de problemas que en un servidor casero de IA no aporta gran cosa.

Resumen directo:

```text
Ubuntu Server: normal
Minimized: no
Buscar drivers terceros en instalador: no
Instalar NVIDIA después: sí, con ubuntu-drivers --gpgpu
Tipo de driver: -server / -server-open recomendado por Ubuntu
```
---


Voy a comparar LM Studio headless, Ollama y llama.cpp desde rendimiento realista en tu 5060 Ti, no solo “qué motor es más elegante”. Aquí importan backend, formato, facilidad de cambiar modelos y cuánto control te deja cada uno.
---


Lo que voy viendo apunta a una respuesta bastante práctica: no hay un “Gemini local” completo en 16 GB, pero sí hay combinaciones muy decentes. Para búsqueda web, la elección importante no es solo el modelo, sino usar una interfaz que haga RAG/búsqueda y le pase resultados al modelo.
---


Los enlaces previos de la búsqueda ya no están disponibles como referencias internas, así que voy a refrescar únicamente la página de instalación/wiki de TabbyAPI y cierro con los comandos.
---


Ese venv de `uv` se ha creado sin `pip`. No es grave. Con `uv` puedes instalar dentro del venv sin usar `pip`.

Estando en `(venv)` y en `~/ai/tabbyAPI`, ejecuta:

```bash
uv pip install -U pip setuptools wheel
uv pip install -U ".[cu13]"
```

Luego prueba:

```bash
python -m pip --version
```

Y después el test de GPU:

```bash
python -c "import torch; print('torch:', torch.__version__); print('cuda available:', torch.cuda.is_available()); print('torch cuda:', torch.version.cuda); print('gpu:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"
```

Si `uv pip install -U ".[cu13]"` falla, pega el primer error importante, no hace falta todo el log.
---


En el servidor:

```bash
sudo ufw status
```

Si está activo verás algo como:

```text
Status: active
```

Si no está activo:

```text
Status: inactive
```

Para más detalle:

```bash
sudo ufw status verbose
```

Y si quieres ver si el puerto 5000 está escuchando:

```bash
ss -tulpn | grep 5000
```
---


Sí: en `UD-Q4_K_XL`, la parte `Q4` indica cuantización alrededor de **4 bits**. Lo demás describe **el esquema concreto de cuantización**.

Ejemplo:

```text
UD-Q4_K_XL
```

Se puede leer así:

| Parte | Significado aproximado |
|---|---|
| `UD` | Unsloth Dynamic quantization |
| `Q4` | Cuantización de 4 bits |
| `K` | Familia de cuantización tipo K-quants de llama.cpp/GGUF |
| `XL` | Variante/tamaño/calidad dentro de la serie dinámica de Unsloth |

En GGUF no basta con decir “4 bits”, porque hay muchas formas de cuantizar a 4 bits. Por ejemplo:

```text
Q4_0
Q4_1
Q4_K_S
Q4_K_M
Q4_K_L
IQ4_XS
IQ4_NL
UD-Q4_K_XL
```

Todas son “alrededor de 4 bits”, pero no tienen la misma calidad, tamaño ni velocidad.

Regla práctica:

| Tipo | Qué suele implicar |
|---|---|
| `Q4_0` / `Q4_1` | Cuants antiguas/sencillas |
| `Q4_K_M` | Muy común, buen equilibrio |
| `Q5_K_M` | Más calidad, más VRAM |
| `Q6_K` | Alta calidad, más pesada |
| `IQ4_XS` | Muy eficiente, buen tamaño/calidad |
| `UD-Q4_K_XL` | Cuantización dinámica de Unsloth, suele priorizar calidad dentro de 4-bit |

Para tu 16 GB, normalmente miraría:

```text
Q4_K_M
IQ4_XS
UD-Q4_K_XL
```

Y si va justo:

```text
Q3_K_M
IQ3_*
```

Si va sobrado y quieres calidad:

```text
Q5_K_M
Q6_K
```
---


Sí. Para tu caso hay que separar dos tareas:

| Tarea | Qué necesitas |
|---|---|
| Descargar modelos a disco | Hugging Face CLI, SSH, scripts |
| Cargar/descargar de VRAM | TabbyAPI admin API o una UI compatible |

Mi recomendación práctica:

**1. Descargar modelos: por SSH con `hf`**
Es lo más limpio y no toca dependencias de Tabby.

```bash
cd ~/ai/tabbyAPI
source venv/bin/activate

hf download turboderp/Qwen3-8B-exl3 \
  --revision 4.0bpw \
  --local-dir ~/ai/models/Qwen3-8B-exl3-4.0bpw
```

Todo modelo que quieras que Tabby vea, déjalo bajo:

```text
/home/sico/ai/models
```

**2. Administrar VRAM: usa la API admin de Tabby**
Desde tu PC cliente puedes llamar:

```bash
curl http://IP_SERVIDOR:5000/v1/model/list \
  -H "x-admin-key: TU_ADMIN_KEY"
```

Cargar modelo:

```bash
curl -X POST http://IP_SERVIDOR:5000/v1/model/load \
  -H "x-admin-key: TU_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model_name":"Qwen3-8B-exl3-4.0bpw"}'
```

Descargar de VRAM:

```bash
curl -X POST http://IP_SERVIDOR:5000/v1/model/unload \
  -H "x-admin-key: TU_ADMIN_KEY"
```

**3. UI cómoda**
Opciones reales:

| Opción | Descarga modelos | Carga/descarga VRAM | Comentario |
|---|---:|---:|---|
| Redoc de Tabby | No | Sí, técnico | Ya lo tienes en `http://IP:5000/redoc` |
| Open WebUI | No ideal | No ideal para Tabby admin | Muy bueno para chat de usuario |
| SillyTavern + Tabby Loader | Parcial | Sí | Mejor UI cómoda para gestionar Tabby |
| Scripts propios | Sí | Sí | Feo pero robusto |
| Docker stack futuro | Sí | Sí | Más orden, más capas |

Para lo que describes, **SillyTavern + TabbyAPI Loader** encaja mejor que Open WebUI como panel de administración de Tabby. Open WebUI lo usaría más adelante como interfaz de chat para usuarios.

Yo haría ahora:
1. Mantener descargas por `hf` en SSH.
2. Usar `/redoc` para probar endpoints.
3. Crear 3 scripts simples: `list-models`, `load-model`, `unload-model`.
4. Más adelante, si quieres UI cómoda de verdad para Tabby, instalar SillyTavern en tu PC cliente con Tabby Loader.

Importante: protege bien la **admin key**. La API key normal sirve para inferencia; la admin key puede cargar/descargar modelos, así que no la metas en clientes que no controles.
---


Sí, bien visto. **No dejes que siga por `cu12`** si queremos usar la ruta que ya validamos con CUDA 13/Python 3.13.

Si todavía está instalando, para con:

```bash
Ctrl+C
```

Luego borra la preferencia que acaba de guardar:

```bash
cd ~/ai/tabbyAPI
rm -f start_options.json
```

Reinstala explícitamente `cu13` dentro del venv:

```bash
source venv/bin/activate
uv pip install -U ".[cu13]"
```

Comprueba otra vez:

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.version.cuda); print(torch.cuda.get_device_name(0))"
```

Y para arrancar, mejor de momento **sin `start.sh`**, porque el script te está autodetectando mal:

```bash
python main.py
```

Lo importante: `start.sh` no es “TabbyAPI” en sí, es un ayudante que instala/actualiza según preferencias. Si el ayudante se empeña en `cu12`, lo evitamos y arrancamos directo con `python main.py`.
---


Bien: eso significa que la API está viva y protegida. Falta pasarle la API key.

La puedes leer aquí:

```bash
cd ~/ai/tabbyAPI
cat api_tokens.yml
```

Verás algo parecido a:

```yaml
api_key: ...
admin_key: ...
```

Luego prueba con la `api_key`:

```bash
curl http://127.0.0.1:5000/v1/models \
  -H "Authorization: Bearer TU_API_KEY"
```

Si no hay modelo cargado todavía, puede devolver lista vacía o algo similar, pero ya no debería decir que falta API key.

No pegues aquí las keys nuevas; con que me digas si responde o qué error da, vale.
---


Voy a separar acceso por red de administración. Lo primero es exponer Tabby solo en la LAN y comprobar firewall; lo segundo es elegir una capa cómoda, porque TabbyAPI como tal es más API que panel de control.
---


Voy a contrastar lo actual sobre formatos/backends NVIDIA porque aquí cambian bastante las recomendaciones según CUDA, FlashAttention, cuantización y soporte de GPU reciente. Luego te doy una propuesta práctica con pros y contras.
---


Voy a comprobarlo con fuente actual, porque Codex ha ido cambiando mucho entre CLI, app, web, IDE y móvil. La pregunta concreta es si el Codex de iOS puede “engancharse” a un agente local en Windows, no solo abrir tareas cloud.

---
*Generado desde conversación con 166 mensajes.*
*IA/ML*
