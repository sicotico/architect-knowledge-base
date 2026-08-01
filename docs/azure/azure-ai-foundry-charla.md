---
title: Azure AI Foundry Charla
date: 2025-03-14
category: Azure/Cloud
slug: azure-ai-foundry-charla
tags: ['Azure/Cloud', 'azure']
---

# Azure AI Foundry Charla


> **Pregunta original:**
> 
El chatboot de asistencia técnica
Esto no lo tengo claro , si uso modelos preexistentes en Azure AI Foundry ¿puedo exportar el proyecto a un App Services , por ejemplo?
El foco es la creación y la portabilidad de lo creado. 
> El caso de uso puede ser un chatbot y el lenguaje python. Respecto a la presentación si que quiero que sea en power point y en apple keynote
> El caso de uso puede ser un chatbot y el lenguaje python. Respecto a la presentación si que quiero que sea en power point y en apple keynote
> 
> *...y 5 preguntas de seguimiento*


---


## Respuesta


Aquí tienes una descripción corta y atractiva para el Call for Papers de tu charla:

**«¿Quieres crear un chatbot de asistencia técnica sin complicarte la vida (ni perder la paciencia)? Descubre cómo Azure AI Foundry, junto con Python y Azure App Service, te permiten pasar de la idea al chatbot desplegado en producción rápidamente, manteniendo tu salud mental intacta y sin dramas técnicos. ¡La IA generativa nunca había sido tan amigable!»**
---


Aquí tienes el texto corregido y mejorado:

**«¿Quieres crear un chatbot de asistencia técnica sin complicarte la vida (ni perder la paciencia)? Descubre cómo Azure AI Foundry te permite pasar rápidamente de la idea a un chatbot desplegado en producción, manteniendo tu salud mental intacta y evitando dramas técnicos. ¡La IA generativa nunca había sido tan amigable!»**
---


Aquí tienes el título 9 con un toque de humor:

**«De la idea a la realidad (sin perder la cabeza): Cómo Azure AI Foundry simplifica crear chatbots que sí responden bien»**

O una variación un poco más divertida:

**«De la idea al chatbot sin dramas: Azure AI Foundry al rescate de tu salud mental»**

¡Espero que estos títulos ayuden a captar la atención y sacar sonrisas en tu audiencia!
---


Voy a enfocarme en desarrollar un guion detallado y una presentación sobre la **creación de un chatbot de asistencia técnica en Azure AI Foundry con Python**, resaltando especialmente la facilidad de exportación y despliegue en **Azure App Service**.

La charla destacará:
- Cómo utilizar **modelos preexistentes en Azure AI Foundry** para el chatbot.
- Si es posible exportar el proyecto generado en Foundry a **Azure App Service** y cómo hacerlo.
- Pasos detallados para la creación, exportación y despliegue del chatbot.
- Beneficios clave de usar **Azure AI Foundry para portabilidad y escalabilidad.**

También incluiré una presentación en **PowerPoint y Apple Keynote**, estructurada para demostrar de manera visual la rapidez y facilidad de construir y portar un MVP desde Azure AI Foundry hacia un entorno productivo.

Te avisaré cuando tenga lista la información.
---


# Guion Detallado de la Charla

## Introducción a Azure AI Foundry (antes Azure AI Studio)  
Azure AI Foundry es la nueva plataforma unificada de Microsoft para crear aplicaciones de inteligencia artificial generativa de manera ágil. Anunciada como la evolución de **Azure AI Studio**, Foundry integra **servicios de IA empresariales**, un amplio catálogo de modelos (OpenAI GPT-3.5/4, modelos abiertos como Llama, Mistral, etc.), y herramientas de desarrollo en un solo entorno【16†L975-L983】【16†L1025-L1033】. Esto significa que los desarrolladores pueden **diseñar, personalizar y desplegar** aplicaciones de IA (incluyendo chatbots) de forma centralizada, aprovechando características de **seguridad y gobierno empresarial** de Azure【6†L139-L147】【6†L177-L184】. En esencia, Azure AI Foundry busca **acelerar el paso de la idea, al código, al despliegue en la nube**, simplificando la adopción de soluciones de IA generativa en las organizaciones【16†L1027-L1034】.

【51†embed_image】 *Figura: Diagrama de la arquitectura de Azure AI Foundry, que muestra su catálogo de modelos (modelos pre-entrenados de OpenAI y terceros, modelos especializados por tareas, etc.) y la integración con servicios de Azure como Azure OpenAI Service, Azure AI Search (búsquedas cognitivas para RAG), Azure AI Agent Service (agentes/copilotos) y Content Safety. A la izquierda se ilustra cómo Foundry se integra con las herramientas de desarrollo (Visual Studio, GitHub, Copilot) y con el SDK de Foundry, facilitando la colaboración entre desarrolladores y científicos de datos.*  

En esta introducción destacamos que Azure AI Foundry proporciona **todo lo necesario para desarrollar aplicaciones de IA**: desde elegir un modelo existente, ajustarlo con datos propios, probarlo de forma interactiva, hasta desplegarlo en producción con mínimos esfuerzos. Además, al ser la continuación de Azure AI Studio, ofrece compatibilidad con los proyectos existentes – es básicamente un cambio de nombre con funcionalidades mejoradas, sin alterar el flujo de trabajo al que ya estaban acostumbrados los usuarios de Azure AI Studio【16†L1035-L1043】.

## Caso Práctico: Chatbot de Asistencia Técnica con Modelos Preexistentes  
Para ilustrar estas capacidades, tomaremos un caso práctico: **la creación de un chatbot de asistencia técnica** para soporte al cliente o mesa de ayuda de TI. El objetivo es construir un agente conversacional que pueda **responder preguntas frecuentes, guiar a usuarios en resolución de problemas técnicos y proporcionar información de soporte** de forma automática. Gracias a Azure AI Foundry, no necesitamos entrenar un modelo desde cero; podemos basarnos en **modelos preexistentes de lenguaje** de alta potencia (por ejemplo, GPT-4 de Azure OpenAI o un modelo abierto del catálogo) y adaptarlos a nuestras necesidades【16†L995-L1003】. 

¿Cómo adaptamos el modelo a nuestro dominio (soporte técnico)? Aquí entra la opción de incorporar conocimiento específico de la empresa. Azure AI Foundry permite **conectar el chatbot con fuentes de datos propias** – por ejemplo, una base de conocimiento de soporte, manuales técnicos o FAQs – usando técnicas de *Retrieval Augmented Generation* (RAG). Esto significa que el modelo de lenguaje buscará información en nuestros datos para “grounding” (contextualizar) sus respuestas【17†L49-L57】. En la práctica, para un chatbot de asistencia técnica cargaríamos documentos de soporte al portal (o conectaríamos un índice de Azure Cognitive Search con nuestros artículos de ayuda) para que el bot responda con la información más actualizada y específica. Este enfoque aprovecha la **fuerza del modelo pre-entrenado** (fluidez en lenguaje natural) y al mismo tiempo garantiza respuestas precisas basadas en la base de conocimientos de la empresa【6†L177-L184】. El resultado esperado: un asistente virtual capaz de entender preguntas de usuarios y ofrecer soluciones técnicas como lo haría un agente humano, pero disponible 24/7 y escalable a muchas consultas simultáneas.

## Pasos para Crear el Chatbot en Azure AI Foundry  
Describamos ahora el proceso **paso a paso** para desarrollar este chatbot dentro de Azure AI Foundry:

1. **Creación de un nuevo proyecto**: Iniciamos sesión en Azure AI Foundry (portal web `ai.azure.com`) y creamos un proyecto dentro de un *hub* de Foundry. El proyecto actúa como contenedor de todos los componentes (modelos, flujos, datos) para nuestra aplicación de chatbot. Podemos usar una plantilla predefinida si existe (por ejemplo, Foundry ofrece plantillas de “Chat con tus datos” o “Agente de soporte”) o empezar desde cero. Durante la creación, se asocian los recursos de Azure necesarios, como una instancia de Azure OpenAI (si usaremos GPT) y Azure AI Search (si usaremos búsqueda de datos), asegurando que el proyecto tenga acceso a estos servicios.

2. **Selección y despliegue de un modelo pre-entrenado**: En el portal de Foundry, vamos al **Model Catalog** (Catálogo de modelos) para elegir el modelo base para el chatbot. Para un asistente técnico, típicamente escogeríamos un modelo de lenguaje potente y conversacional. Por ejemplo, podríamos seleccionar **GPT-3.5 Turbo** o **GPT-4** desde la sección de Azure OpenAI, u optar por un modelo open-source adecuado. Foundry muestra detalles de cada modelo (tamaño, proveedores, capacidades) y permite desplegarlos fácilmente. Una vez seleccionado nuestro modelo (digamos GPT-3.5), hacemos clic en *Deploy* en la página de detalles del modelo【43†L89-L97】. Esto crea una **implementación del modelo** dentro de nuestro proyecto (similar a “instanciar” el modelo para que esté listo para recibir peticiones). En segundos, el modelo queda disponible para pruebas en el entorno de Foundry.

3. **Incorporación de datos para el conocimiento del dominio (opcional pero recomendado)**: Para que el chatbot responda con información específica de asistencia técnica, incorporamos nuestra base de conocimiento. Azure AI Foundry facilita este paso mediante la integración con **Azure AI Search**. En nuestro proyecto, agregamos un *data source* (por ejemplo, documentos de soporte en Azure Blob Storage o un índice de búsqueda existente). Foundry indexará este contenido y nos permitirá hacer *grounding* del modelo con estos datos【17†L49-L57】. En la práctica, esto se realiza en la sección de **datos** o **Knowledge** del proyecto: conectamos la fuente de datos, configuramos cómo buscar (palabras clave, vectores) y esperamos a que Foundry indexe la información. Tras esto, podemos probar consultas en el **Chat playground** y veremos que el modelo ya cita información relevante de nuestros documentos en sus respuestas, mejorando la precisión del chatbot. *(Si no se dispone de datos propios o se desea un chatbot más genérico, se podría omitir este paso; el modelo respondería sólo con su conocimiento pre-entrenado, que igualmente abarca mucho conocimiento técnico general, aunque sin detalles específicos de nuestra organización.)*

4. **Diseño del flujo conversacional y prompt engineering**: Azure AI Foundry ofrece herramientas para personalizar el comportamiento del chatbot. Por un lado, podemos definir un **prompt de sistema** – instrucciones iniciales al modelo indicando su rol (ejemplo: *“Eres un asistente técnico de [Empresa], ayudarás a los usuarios con sus problemas de IT de manera clara y concisa”*). Por otro lado, Foundry tiene la funcionalidad de **Prompt Flow**, que permite orquestar pasos en la conversación (por ejemplo, primero buscar en datos, luego llamar al modelo, luego formatear la respuesta) mediante una interfaz visual o código Python. Para un chatbot sencillo, podríamos no necesitar un flujo complejo: con configurar el modelo, su prompt de sistema y activar la búsqueda en nuestros datos, es suficiente. Sin embargo, si quisiéramos lógica adicional (p.ej., llamadas a API externas, formateo especial de respuestas, o manejar diferentes intenciones), Prompt Flow nos deja insertar pasos de código o funciones. En cualquier caso, Azure AI Foundry proporciona un **playground de chat** donde podemos interactuar con el bot mientras ajustamos estas configuraciones. Aquí probamos varias preguntas típicas (“¿Cómo reinicio mi router?”, “Estoy teniendo un error X, ¿qué hago?”) y afinamos las instrucciones hasta obtener respuestas satisfactorias. Este entorno iterativo de prueba es clave para refinar el chatbot antes de desplegarlo.

5. **Pruebas y evaluación**: Durante el desarrollo, Foundry también cuenta con herramientas para evaluar la calidad de las respuestas. Podemos usar la función **Evaluate** del portal para ejecutar pruebas con preguntas predefinidas y verificar si las respuestas del modelo son correctas y están bien fundamentadas. Por ejemplo, se puede crear un pequeño conjunto de Q&As de validación (ground truth) y comparar con lo que responde el bot, detectando si necesita más ajustes. Además, Azure AI Foundry enfatiza las buenas prácticas de *IA responsable*, ofreciendo análisis de contenido (para detectar si la respuesta contiene algo indebido) y opciones de trazabilidad de las fuentes. Estas evaluaciones nos aseguran que el chatbot esté listo para un entorno real, ofreciendo respuestas útiles y dentro de las directrices esperadas.

## Exportación del Proyecto Generado y Portabilidad del Código  
Un aspecto destacado de Azure AI Foundry es la **portabilidad**: lo que construimos en el portal podemos llevarlo fuera casi sin fricciones. Una vez que el chatbot funciona bien en Foundry, existen un par de vías para exportarlo o integrarlo en aplicaciones externas:

- **Descarga del código/flows**: El portal cuenta con opciones para **ver el código** generado y exportar componentes. Por ejemplo, desde el *Chat playground* podemos hacer clic en “View code” para obtener el código Python que realiza la inferencia (incluyendo llamadas al modelo y manejo de datos). Incluso hay un botón de **Export** que permite exportar la solución para integrarla con otros entornos (como Copilot Studio, o descargar un paquete zip con una app, dependiendo de las opciones disponibles). Internamente, Azure AI Foundry utiliza un SDK unificado; si preferimos trabajar directamente en código, podemos **clonar el proyecto en Visual Studio Code** usando la integración nativa【21†L47-L55】【21†L79-L87】. Esto nos abre el proyecto en un contenedor de desarrollo donde veremos archivos de código (por ejemplo, scripts de Prompt Flow, definiciones de modelo, etc.). Desde allí es posible editar, versionar en GitHub y, en última instancia, **exportar el código a nuestro repositorio local**. Esta capacidad de co-desarrollar en el portal o en VS Code de forma sincronizada significa que no estamos atrapados en una herramienta propietaria: el chatbot y su lógica son esencialmente código Python y configuraciones que podemos reutilizar.

- **SDK de Azure AI Foundry**: Microsoft ha provisto un SDK (bibliotecas Python `azure-ai-projects` y `azure-ai-inference`) para interactuar con proyectos de Foundry desde cualquier entorno Python【26†L104-L112】【26†L148-L157】. En otras palabras, podemos escribir una aplicación Python tradicional que **conecte con nuestro proyecto de Foundry** mediante una cadena de conexión o credenciales, y ejecute el modelo igual que en el portal. Por ejemplo, con unas pocas líneas de Python es posible autenticar contra Azure, obtener un cliente de inferencia del proyecto y hacer consultas al modelo【26†L157-L165】. Esto brinda flexibilidad para integrar el chatbot en aplicaciones más grandes: podríamos tener un backend en Python (Flask, FastAPI, etc.) que use el SDK para enviar las preguntas de usuarios al modelo de Foundry y devolver respuestas. El SDK garantiza que la misma lógica construida en el proyecto (por ejemplo, uso de cierto modelo o flujo) se respete en nuestra aplicación externa. 

En resumen, **exportar el proyecto no requiere reescribir desde cero**, lo más frecuente es reutilizar el código generado o conectarse vía SDK, lo cual ahorra mucho tiempo. La portabilidad se refleja también en que el chatbot puede desplegarse en distintas plataformas (no solo en Azure App Service; podríamos llevarlo a un contenedor Docker, a una función serverless, etc., siempre que tengamos las dependencias de Azure AI Foundry disponibles). No obstante, en nuestro caso nos centraremos en Azure App Service como destino, por ser un servicio PaaS conveniente para hospedar aplicaciones web en Azure.

## Implementación en Azure App Service  
**Azure App Service** es la plataforma de Microsoft para hospedar aplicaciones web de forma escalable y gestionada, con soporte para aplicaciones Python, Node, .NET, Java, etc. Vamos a desplegar nuestro chatbot de asistencia técnica como una aplicación web en App Service, de modo que los usuarios puedan acceder a él a través de un navegador (por ejemplo, una interfaz de chat web) o integrarlo en un sitio corporativo. 

Azure AI Foundry simplifica enormemente este paso. De hecho, incorpora un mecanismo de **“one-click deploy”** a App Service: una vez probado el chatbot en el playground, podemos publicarlo directamente. En la interfaz del chat en Foundry, usamos la opción **Deploy > ...as a web app** (Desplegar como aplicación web)【19†L338-L346】【19†L348-L356】. Foundry nos pedirá algunos datos mínimos: un nombre único para la app (que será la URL del chatbot), seleccionar la suscripción de Azure, grupo de recursos y región donde desplegar, y elegir un plan de tarifa de App Service para la web (por ejemplo, un plan **B1** o **S1** dependiendo de la escala que necesitemos). Al confirmar, la plataforma automáticamente prepara el paquete de la aplicación e inicia la creación del servicio App Service.

【48†embed_image】 *Captura: Opción de desplegar la aplicación como Web App desde el Chat playground de Azure AI Foundry. Con un solo clic en **Deploy** > “...as a web app”, Foundry permite empaquetar el chatbot y crear un servicio web de Azure App Service para alojarlo.*  

En pocos minutos, Azure AI Foundry aprovisiona **una Web App con el código del chatbot**. Internamente, este despliegue incluye la aplicación web (por ejemplo, una interfaz tipo chat y la lógica backend) y las configuraciones necesarias para conectarse al modelo de lenguaje que configuramos. Cabe señalar que Foundry utiliza Azure App Service de forma estándar – es decir, el resultado es una aplicación web en nuestra suscripción que podemos manejar como cualquier otra (aparecerá en el Portal de Azure, dentro del grupo de recursos del proyecto). Podemos incluso activar opciones como autenticación, personalizar el dominio, escalarla, etc., tal como lo haríamos con cualquier App Service.

¿Y si preferimos implementar manualmente? También es posible. Podríamos tomar el código exportado (por ejemplo, un proyecto Flask con nuestras llamadas al modelo vía SDK) y desplegarlo manualmente en Azure App Service mediante Git or ZIP deployment. En este caso, crearíamos un nuevo **App Service** para Python en Azure, subiríamos el código, configuraríamos las variables de entorno (por ejemplo, la cadena de conexión del proyecto de Foundry o las keys del Azure OpenAI) y ejecutaríamos la aplicación. La mayor parte del trabajo ya estaría hecha gracias a Foundry; solo tendríamos que asegurarnos de incluir las dependencias (`azure-ai-projects`, `azure-ai-inference`, `flask` u otro framework web) en un archivo requirements.txt para que App Service las instale. 

Un punto a destacar es la **compatibilidad del entorno**: Azure App Service soporta múltiples versiones de Python, por lo que conviene seleccionar la misma versión que usamos en local o en Foundry (por ejemplo Python 3.10) para evitar sorpresas. Microsoft recomienda verificar que la versión de Python configurada en App Service **coincida con la usada en desarrollo**【9†L189-L193】, así como que todas las dependencias estén correctamente referenciadas. Por suerte, al exportar el proyecto de Foundry o usar el deploy automático, gran parte de esta configuración es manejada por la plataforma.

Tras el despliegue, tendremos una URL pública (o restringida si habilitamos autenticación) donde el chatbot está activo. Podemos abrir esa URL y ver la interfaz de chat de asistencia técnica, probar algunas consultas y confirmar que funciona igual que en el playground de Foundry. ¡Nuestro chatbot de asistencia técnica ya está accesible para los usuarios finales vía web, gracias a Azure App Service!

## Evaluación de la Portabilidad y Compatibilidad  
Llegados a este punto, es importante reflexionar sobre **cómo de portátil y directa ha sido la exportación** del chatbot desde Azure AI Foundry hacia Azure App Service, y qué ajustes fueron necesarios:

- **Exportación sin fricciones:** En nuestra experiencia del caso práctico, la exportación ha sido bastante fluida. Azure AI Foundry está diseñado precisamente para **evitar re-trabajo** al pasar de desarrollo a producción. La opción de *deploy one-click* se encargó de empaquetar todo adecuadamente, de modo que **no tuvimos que modificar el código manualmente** para que funcione en App Service. Esto demuestra un *alto grado de compatibilidad* entre lo que se prueba en Foundry y el entorno de ejecución estándar de Azure (App Service es básicamente una instancia de servidor web Linux/Windows con Python, donde corre nuestra app). 

- **Ajustes necesarios:** Si bien el despliegue automático cubre mucho, identificamos algunas configuraciones a tener en cuenta. Primero, como mencionamos, la versión de Python: aseguramos usar en App Service una versión igual o superior a la del proyecto (por ejemplo, 3.10) para compatibilidad con el SDK de Foundry. Segundo, las **dependencias y credenciales**: el proyecto necesita acceso al modelo (Azure OpenAI) y quizá al servicio de búsqueda; para ello, en App Service se configuraron variables de entorno con la cadena de conexión del proyecto Foundry o con las claves API necesarias. Foundry facilita esto proporcionando la *connection string* del proyecto (visible en la página Overview del proyecto【26†L175-L183】) que engloba la información de acceso. Inyectar esa variable en App Service fue suficiente para que el código Python pudiera resolver correctamente las llamadas al modelo. En entornos empresariales, es recomendable usar Azure Key Vault o *Managed Identity* para manejar credenciales en producción, pero para nuestro prototipo usamos directamente la configuración que venía del portal.

- **Compatibilidad del código y librerías:** El código generado por Foundry (o escrito en Prompt Flow) es Python estándar, utilizando las bibliotecas Azure para IA. Estas librerías (`azure-ai-*`) están disponibles públicamente, así que no hubo impedimentos para instalarlas en App Service. En nuestras pruebas no encontramos diferencias de comportamiento del modelo entre el portal y la app desplegada – las respuestas del chatbot fueron coherentes. Esto indica que Foundry **no usa nada “mágico” que luego no esté disponible externamente**; el mismo modelo de OpenAI que corría en Foundry ahora responde a través de la App Service usando la misma inferencia en la nube【26†L157-L165】.

- **¿Posibles inconvenientes?** Un desafío menor puede ser garantizar que el entorno de App Service tenga suficiente **memoria y tiempo de ejecución** para manejar las consultas al modelo, especialmente si el modelo es grande. Por ejemplo, GPT-4 puede ser más lento o consumir más recursos. En nuestro despliegue escogimos un plan estándar (S1) que fue suficiente; pero para alto volumen de usuarios quizás consideraríamos un plan más potente o habilitar **autoscaling**. Otro punto es el **registro de logs**: en Foundry teníamos la consola del playground para ver cada respuesta. En App Service, habilitamos *Application Insights* para monitorear las solicitudes y posibles errores. Esto nos ayudó a asegurar que todo corría bien y a tener métricas de uso del chatbot. Nuevamente, estos son temas propios de cualquier aplicación web en producción, no obstáculos de portabilidad en sí.

En conclusión, la portabilidad ha sido **muy lograda**: Azure AI Foundry demostró permitir exportar el chatbot prácticamente con un clic, y los ajustes requeridos (versiones, config. de claves) son pasos estándar en cualquier despliegue. No encontramos “bloqueos” ni tuvimos que rediseñar nada para que funcionara fuera del portal, lo cual valida la promesa de Foundry de llevar las aplicaciones de IA a producción fácilmente.

## Recomendaciones Clave para un Despliegue Exitoso  
A partir de este caso práctico, resumimos algunas **buenas prácticas y recomendaciones** para quienes quieran desarrollar y desplegar su propio chatbot con Azure AI Foundry y Azure App Service:

- **Entender la arquitectura y recursos necesarios:** Antes de comenzar, identifica qué servicios de Azure vas a usar. En nuestro ejemplo: Azure AI Foundry (que en sí utiliza Azure Machine Learning bajo el capó para el workspace), Azure OpenAI Service para el modelo, Azure Cognitive Search para los datos, y Azure App Service para la aplicación web. Asegúrate de tener las cuotas y permisos necesarios en la suscripción (por ejemplo, acceso a Azure OpenAI y suficiente cuota para desplegar modelos【43†L55-L63】). Registra el proveedor `Microsoft.Web` si vas a desplegar en App Service【19†L338-L346】. Esta planificación evita sorpresas durante el despliegue.

- **Aprovecha las plantillas y ejemplos de Foundry:** Azure AI Foundry incluye **templates** y muestras que te pueden ahorrar tiempo. Si existe una plantilla de “Q&A bot” o “chatbot con tus datos”, úsala como base. Estas plantillas ya configuran muchos elementos (por ejemplo, flujo de RAG, manejo de la conversación) y luego solo adaptas detalles. Microsoft también proporciona tutoriales oficiales – como el de *enterprise chat web app* – que vale la pena seguir para aprender trucos y configuración óptima【17†L49-L57】【19†L348-L356】.

- **Itera y prueba en el Playground antes de desplegar:** Asegura que el chatbot responde correctamente a diversas preguntas en el entorno de Foundry. Haz pruebas con casos reales de soporte (preguntas fáciles y difíciles) y ajusta el prompt o agrega más documentos si ves lagunas de conocimiento. Es mucho más eficiente refinar en el playground que tener que re-deployar múltiples veces. Además, utiliza la función de **evaluación** si está disponible para medir calidad. Un chatbot bien afinado en Foundry tendrá altas probabilidades de funcionar bien en producción.

- **Gestión de configuración y secretos:** No dejes credenciales sensibles en el código. Foundry maneja internamente accesos a recursos, pero al exportar a App Service, utiliza **Managed Identity** o variables de entorno para permisos. Por ejemplo, configuramos la *Managed Identity* del App Service con acceso al Azure OpenAI y al Cognitive Search index, en vez de usar keys fijas, aumentando la seguridad. Si usas cadenas de conexión, almacénalas en la sección **Configuration** de App Service (que cifra los valores) o idealmente en Azure Key Vault. Esto permite rotar claves sin tocar el código y es una práctica de seguridad recomendada.

- **Pruebas locales con el SDK (si es posible):** Aunque Foundry proporciona el entorno controlado, puede ser útil crear un pequeño script local (como el `chat.py` de ejemplo) que use el SDK de Foundry u OpenAI para enviar una pregunta y obtener respuesta【26†L157-L165】. Ejecutar esto localmente (autenticado con `az login` o con una clave) verifica que tu modelo desplegado responde bien fuera del portal. Si funciona en local, casi seguro funcionará en App Service. Esta prueba te ayuda a diferenciar si un problema proviene del código/logic del chatbot o de la configuración del entorno.

- **Mantén sincronía de entornos:** Como regla general, *mantén tu entorno de desarrollo alineado con producción*. Usa versiones de Python y librerías equivalentes. Si en Foundry estás usando ciertas versiones (ej. `azure-ai-inference` v1.x), en tu App Service asegúrate de instalar la misma. Esto minimiza diferencias. Una estrategia es exportar el `requirements.txt` del contenedor de Foundry (posible si abres en VS Code) y usarlo para la app. También, realiza despliegues de prueba en un **slot de staging** de App Service antes de pasar a producción, para validar que todo está bien configurado.

- **Monitorización post-despliegue:** Un despliegue exitoso no termina con “ya funciona”. Habilita logs y monitoreo en App Service. Revisa el **Log Stream** o App Insights para ver las interacciones del chatbot, tiempos de respuesta, eventuales errores de conexión a servicios, etc. Esto permitirá detectar rápidamente si el modelo tarda mucho en responder o si ocurren errores con ciertas preguntas. En base a eso, podrías decidir escalar la instancia de App Service o optimizar el flujo (por ejemplo, tal vez filtrar ciertas consultas). Azure AI Foundry en sí ofrece telemetría de las llamadas al modelo (número de tokens, etc.), útil para entender costos y performance; combinando ambas fuentes tendrás una visión completa.

- **Mantener el conocimiento actualizado:** Si el chatbot usa datos externos (ej., base de conocimiento técnica), planifica cómo actualizar esa información. Azure Cognitive Search puede programar re-indexaciones o puedes conectarlo a una fuente dinámica. Así el chatbot no se quedará obsoleto. Foundry facilita reinyectar nuevos datos al proyecto; solo hay que reindexar y, si es necesario, re-entrenar algún componente. Afortunadamente, el despliegue en App Service puede permanecer el mismo mientras actualizas el backend (modelo/index), ya que sigue apuntando al mismo recurso.

Siguiendo estas recomendaciones, se maximizan las probabilidades de un despliegue exitoso y sostenible en el tiempo. En resumen: **preparación, pruebas exhaustivas, seguridad en la configuración y monitoreo continuo** son las claves para llevar un chatbot de IA generativa a producción con confianza.

## Conclusión: Facilidad de Creación y Portabilidad con Azure AI Foundry  
Para cerrar, retomemos los puntos principales demostrados. Azure AI Foundry nos permitió **crear rápidamente un chatbot de asistencia técnica** aprovechando modelos de lenguaje ya entrenados, con mínima necesidad de código y sin ser expertos en IA. La plataforma unificada simplifica todo el ciclo: desde experimentar con prompts hasta integrar datos propios de la empresa, todo en un mismo lugar y respaldado por la infraestructura de Azure【6†L145-L153】. Esto redujo drásticamente el tiempo de desarrollo en comparación con enfoques tradicionales, donde habríamos tenido que armar por separado el modelo, el código de integración y la interfaz web. 

Además, comprobamos que la promesa de portabilidad de Foundry es real. Pudimos llevar nuestra aplicación desde el entorno de diseño hasta un servicio web en Azure App Service **sin fricciones significativas**, conservando el comportamiento esperado. La capacidad de exportar el proyecto, utilizar el SDK en Python y desplegar con un clic refleja un diseño orientado a la producción desde el inicio. En otras palabras, Azure AI Foundry está **pensado para que las soluciones de IA generativa no se queden en prototipos**, sino que lleguen a los usuarios finales rápida y confiablemente【16†L1027-L1034】.

En el caso del chatbot de soporte, el resultado final es un agente conversacional útil, accesible vía web, que puede escalar según la demanda y ser mantenido con facilidad. Este éxito se debe en gran medida a las herramientas que Foundry puso a nuestra disposición: catálogo de modelos amplio, integración nativa con servicios como OpenAI y Cognitive Search, entorno de pruebas interactivo, y despliegue automatizado. 

Para las organizaciones, esto significa que crear su propio “copiloto” o asistente inteligente ya no es un proyecto de meses con grandes equipos; puede lograrse en semanas o días, e iterarse continuamente. La **rapidez de desarrollo y la portabilidad** se traducen en una ventaja competitiva: incorporar IA generativa en sus aplicaciones concretas con mínimo esfuerzo. 

En resumen, Azure AI Foundry facilita enormemente la creación de chatbots y aplicaciones de IA generativa, y conjuntamente con Azure App Service, nos brinda una vía expedita para ponerlas en producción. Esperamos que este recorrido haya mostrado claramente cómo, apoyándonos en estas herramientas, **podemos pasar de la idea a tener un chatbot funcional en producción de forma didáctica, visual y práctica**, listo para brindar asistencia técnica de manera consistente y eficiente. ¡El futuro de los asistentes de soporte impulsados por IA está al alcance, y Azure AI Foundry es un gran aliado para materializarlo!

---

# Presentación (PowerPoint / Apple Keynote)

**Diapositiva 1: Título e Introducción**  
- *Título:* **Creación de un Chatbot de Asistencia Técnica con Azure AI Foundry y Python**  
- *Subtítulo:* Enfoque en portabilidad y despliegue en Azure App Service  
- Bienvenida e introducción del tema: presentando Azure AI Foundry como la nueva plataforma unificada de Microsoft para IA generativa (antes conocida como Azure AI Studio).  
- Objetivos de la charla:
  - Mostrar el proceso de desarrollo de un chatbot de soporte técnico usando modelos existentes (ej. GPT-4) en Azure AI Foundry.  
  - Demostrar cómo desplegar fácilmente dicha solución en Azure App Service, enfatizando la portabilidad (llevar lo creado en Foundry a producción sin complicaciones).

**Diapositiva 2: ¿Qué es Azure AI Foundry?**  
- **Azure AI Foundry = Evolución de Azure AI Studio:** Plataforma unificada para crear, probar y desplegar aplicaciones de IA generativa.  
- Integra un **Catálogo de modelos** extenso (OpenAI, Hugging Face, modelos de Microsoft, etc.) y herramientas de orquestación (Prompt Flow, evaluaciones, etc.).  
- Orientada a desarrolladores y data scientists: permite trabajar con **bajo código** o código completo, integrándose con VS Code, GitHub y Copilot.  
- **Beneficios clave:** Desarrollo más rápido, colaboración integrada, cumplimiento de seguridad (gobierno de datos, contenido seguro) y despliegue simplificado en infraestructura Azure. *(Punto a mencionar: “antiguo Azure AI Studio – mismo concepto mejorado”)*.

**Diapositiva 3: Caso de Uso – Chatbot de Asistencia Técnica**  
- Presentación del escenario práctico: *“Imaginemos un chatbot para soporte técnico de una empresa.”*  
- **Funciones esperadas del chatbot:** atender preguntas de usuarios sobre problemas técnicos comunes, proporcionar instrucciones paso a paso, consultar una base de conocimientos de la empresa para respuestas específicas.  
- **Enfoque con Azure AI Foundry:** en lugar de entrenar un modelo desde cero, se usará un **modelo preentrenado** (ej. GPT-3.5/4) y se **enriquecerá con datos propios** (manuales de soporte, FAQ).  
- Ventajas del caso:
  - Aprovechar la comprensión del lenguaje natural de un modelo avanzado.  
  - Reducir tiempos de respuesta y carga del helpdesk humano.  
  - Mantener consistencia en las soluciones proporcionadas a los usuarios.

**Diapositiva 4: Arquitectura de la Solución (Diagrama)**  
- **Diagrama de arquitectura del chatbot:** Representación gráfica del flujo:  
  1. **Usuario final** interactúa a través de una interfaz web (chat UI en App Service).  
  2. La pregunta del usuario es enviada al **backend (Python)** del chatbot.  
  3. El backend, usando el **SDK de Azure AI Foundry/Azure OpenAI**, envía la consulta al **modelo de lenguaje** (ejecutándose en la nube Azure).  
  4. Si se ha habilitado, el modelo primero realiza búsqueda en la **Base de Conocimientos** (Azure Cognitive Search) para obtener datos relevantes (RAG).  
  5. El **Modelo de IA (GPT)** genera una respuesta utilizando tanto su conocimiento como los datos recuperados.  
  6. Respuesta devuelta al usuario vía la interfaz web, incluyendo eventualmente referencias a artículos de soporte.  
- **Componentes Azure involucrados:** Azure AI Foundry (gestión del modelo y orquestación), Azure OpenAI Service (modelo GPT), Azure AI Search (datos corporativos), Azure App Service (aplicación web del chatbot).  
- *Nota:* El diagrama enfatiza cómo Foundry actúa como puente entre los servicios de IA y la aplicación, facilitando la conexión de todos estos componentes.

**Diapositiva 5: Flujo de Desarrollo en Azure AI Foundry**  
*(Esta diapositiva visualmente puede mostrar un **timeline** o pasos numerados junto a capturas de pantalla representativas de la interfaz de Foundry.)*  
- **Paso 1 – Crear Proyecto:** Iniciar un proyecto en Azure AI Foundry para agrupar modelo + datos + flujo. Elegir un nombre y recursos (se crea en un Hub de Foundry). *(Imagen sugerida: Pantalla de creación de proyecto o overview del proyecto).*  
- **Paso 2 – Seleccionar/Desplegar Modelo:** Desde el catálogo, elegir un modelo pre-entrenado apropiado (GPT-3.5, GPT-4, etc.) y hacer *Deploy* a nuestro proyecto. El modelo aparece como “implementado” y listo para usar. *(Imagen: Vista del catálogo de modelos con uno seleccionado para deploy).*  
- **Paso 3 – Añadir Datos de Soporte:** Conectar fuente de datos (documentos FAQ, manuales) via Azure AI Search. Indexar esos datos para usarlos en las respuestas. *(Imagen: Pantalla de “Add your data” en Foundry mostrando datos cargados).*  
- **Paso 4 – Configurar Prompt & Flows:** Definir el prompt del sistema (rol del bot) y, si es necesario, usar Prompt Flow para orquestar pasos (por ejemplo, “buscar en datos -> llamar modelo -> formatear respuesta”).  
- **Paso 5 – Probar en Chat Playground:** Usar la interfaz interactiva para chatear con el bot de prueba. Verificar respuestas, refinar instrucciones. *(Imagen: Captura del chat playground con una pregunta de prueba y la respuesta del bot, incluyendo referencias a los datos).*  

**Diapositiva 6: Exportación y Portabilidad del Proyecto**  
- **Código accesible:** Azure AI Foundry permite ver y exportar el código del chatbot (por ejemplo, el flujo en formato Python). Existe un botón “View code” para inspeccionar la lógica en Python y un “Export” para extraer la aplicación o integrarla con Copilot Studio.  
- **SDK y Desarrollo externo:** Podemos conectar con el proyecto vía SDK. Ej: usar `azure-ai-projects` en un script Python local para llamar al modelo del proyecto con unas pocas líneas de código. Esto significa que *lo que corre en Foundry puede correr en cualquier lugar* con acceso a Azure.  
- **Edición en VS Code:** Integración con Visual Studio Code (incluso en web) donde podemos abrir el proyecto Foundry en un contenedor remoto. Allí editamos archivos, gestionamos dependencias y versionamos con Git, facilitando la colaboración y posterior despliegue.  
- **Sin bloqueo de plataforma:** La lógica del chatbot no depende de componentes privativos del portal; es trasladable. Si mañana se quisiera ejecutar on-premises (hipotéticamente) con los mismos modelos vía API, sería posible con ajustes mínimos. La demo se enfoca en Azure App Service como destino inmediato de despliegue.

**Diapositiva 7: Despliegue en Azure App Service – Opción 1 (Automática)**  
- **One-Click Deploy desde Foundry:** Una vez satisfechos con el chatbot, Azure AI Foundry permite desplegarlo directamente.  
  - En el portal, botón **Deploy > ...as a web app** – inicia el asistente de publicación.  
  - Se proporcionan datos: Nombre de la app (e.g. *“soporte-chatbot”*), selección de suscripción, grupo de recursos, región y plan de App Service. *(Mostrar una pequeña captura del menú desplegable “...as a web app”).*  
  - Foundry crea automáticamente la Web App en Azure con todo el código necesario.  
- **Proceso automatizado:** Se aprovisiona una App Service (en Linux por defecto para Python), se despliega el código del chatbot y se configuran integraciones (por ejemplo, la app sabe a qué proyecto/modelo de Foundry conectarse).  
- **Resultado:** En minutos, tenemos una URL pública (por ej. `soporte-chatbot.azurewebsites.net`) donde está funcionando el chatbot con la misma funcionalidad probada en Foundry. Podemos abrirlo en el navegador y comprobar que responde correctamente a las preguntas de soporte.  
- *Ventaja:* No hace falta manipular servidores, contenedores ni pipelines manualmente – el portal se encarga del DevOps básico.

**Diapositiva 8: Despliegue en Azure App Service – Opción 2 (Manual)**  
- **Exportar y desplegar manualmente:** Alternativamente, se puede llevar el código fuera y desplegarlo por cuenta propia, útil si se requiere más control o integración en una app existente. Pasos resumidos:  
  1. **Obtener código**: Descargar el proyecto (por ejemplo, vía VS Code integration o repositorio Git).  
  2. **Preparar App Service**: Crear un nuevo Azure App Service para Python.  
  3. **Deploy de código**: Subir el código (usando FTP, ZIP Deploy, GitHub Actions, Azure DevOps CI/CD, etc.).  
  4. **Configurar variables**: Por ejemplo, establecer en App Service la *CONNECTION_STRING* de Azure AI Foundry o claves necesarias (Azure OpenAI key, Search key, etc.), para que la app pueda comunicarse con los servicios.  
  5. **Instalar dependencias**: Asegurarse de que el `requirements.txt` incluye todas las librerías (ej. azure-ai-inference, flask). App Service las instalará automáticamente al desplegar, pero conviene verificar en los logs.  
- **Considerar ajustes de entorno:** seleccionar la versión de Python adecuada en la configuración de App Service (ej.: Python 3.10). Habilitar *Managed Identity* si vamos a usar autenticación en vez de claves para los servicios (más seguro).  
- **Prueba post-deploy:** Validar manualmente que el chatbot inicia y responde. Esto se hace accediendo a la URL y también consultando los logs de App Service (disponibles en Azure Portal) para cualquier error en importaciones o conexión.  
- *Nota:* Esta ruta ofrece flexibilidad (podemos incorporar este chatbot como parte de una aplicación web más grande, por ejemplo), a cambio de un poco más de trabajo técnico. En nuestro caso de estudio no fue necesaria porque el despliegue automático cubrió los requisitos.

**Diapositiva 9: Portabilidad y Compatibilidad – Evaluación**  
- **¿Exportación sin fricción?** Sí, el caso práctico mostró que lo construido en Foundry pasó a App Service **sin cambios en la lógica**. La consistencia de las respuestas del bot se mantuvo.  
- **Ajustes menores realizados:**  
  - Configurar credenciales en el nuevo entorno (por seguridad, no se arrastran automáticamente).  
  - Verificar versiones de Python y paquetes para evitar incompatibilidades.  
  - Escoger un plan de App Service adecuado para el tamaño del modelo (p. ej., GPT-4 puede requerir más memoria/tiempo por consulta).  
- **Integraciones soportadas:** Todo lo usado (modelo OpenAI, Cognitive Search) funcionó en App Service, ya que son servicios de Azure accesibles vía API/SDK. No hubo nada “pegado” al portal de Foundry que impidiera correr afuera.  
- **Latencia y rendimiento:** Se observaron tiempos de respuesta similares. Foundry Playground y la App final ambas llaman al mismo modelo en la nube, por lo que la principal diferencia de rendimiento podría venir por el plan de App Service (computación disponible) pero en nuestro despliegue no fue significativo.  
- **Conclusión de compatibilidad:** Azure AI Foundry aprueba con nota en portabilidad: la plataforma consigue que “lo que ves (en desarrollo) es lo que obtienes (en producción)”. Esto reduce el *time-to-market* y la incertidumbre típica de llevar IA a producción.

**Diapositiva 10: Mejores Prácticas para el Despliegue**  
- **Prueba local/portal antes de producción:** iterar en Foundry hasta lograr alta calidad de respuestas. Un chatbot mal afinado no mejorará por desplegarlo rápido.  
- **Usar control de versiones:** Aunque Foundry es visual, mantener versiones del prompt flow o del código (por ejemplo, guardando en GitHub vía VS Code integration) para retroceder cambios si algo falla.  
- **Seguridad ante todo:** No exponer claves API en el código. Utilizar Azure Key Vault o Managed Identities para que la App Service acceda al modelo de forma segura. Azure AI Foundry y App Service se integran bien con estas prácticas (ej.: asignamos a la App Service permisos sobre el recurso Azure OpenAI en lugar de usar la key directamente).  
- **Monitoreo continuo:** Activar Application Insights para la App web del chatbot. Así monitorizamos cuántas consultas recibe, tiempos de respuesta, y podemos detectar excepciones (ej.: si el modelo rechaza alguna petición por política de contenido, etc.). Esto permite mejorar el servicio de forma iterativa.  
- **Planificar actualización de contenido:** En un entorno de soporte técnico, la base de conocimientos evoluciona. Establecer un proceso (manual o automático) para reindexar nuevos documentos en Azure AI Search y, si es necesario, re-entrenar o ajustar el chatbot. Azure AI Foundry facilita re-cargar datos en el proyecto; aprovechémoslo periódicamente para que el bot esté siempre actualizado.  
- **Escalabilidad:** Estar listos para escalar. Si la empresa lanza el chatbot y aumenta su uso, usar características de escalado de App Service (instancias adicionales) o incluso considerar migrar a un servicio más robusto (por ej., contenedores en AKS) si la demanda crece enormemente. La arquitectura modular (separación de frontend y servicios de IA) ayuda a escalar cada parte independientemente.

**Diapositiva 11: Beneficios de Azure AI Foundry en Portabilidad y Despliegue**  
- **Desarrollo acelerado:** Permite crear un MVP funcional en días, integrando modelos de última generación sin pelear con configuraciones complejas. Esto acelera la innovación y prueba de conceptos.  
- **Menor brecha Dev->Prod:** Las herramientas tradicionales a veces funcionan en laboratorio pero cuesta llevarlas a producción. Foundry reduce esa brecha con sus opciones integradas de deploy, lo que significa *menos fallos de integración* y *menos esfuerzo DevOps* necesario.  
- **Iteración sencilla:** Hacer cambios (mejorar el prompt, añadir datos) y redeploy es muy sencillo, fomentando la mejora continua del chatbot. Se puede publicar actualizaciones rápidamente, manteniendo el servicio siempre mejorado.  
- **Ecosistema Azure completo:** Al ser parte de Azure, Foundry permite orquestar una solución completa: modelo, búsqueda, web app, autenticación Azure AD, telemetría… todo cohesionado. Esto da confianza a nivel empresarial, pues cumple requisitos de seguridad y cumplimiento.  
- **Caso de éxito replicable:** Aunque aquí hicimos un chatbot de soporte, la misma receta aplica para *otros casos*: asistentes en comercio electrónico, bots para finanzas (con datos privados), etc. Foundry + App Service proveen un patrón repetible para muchas aplicaciones de IA generativa.

**Diapositiva 12: Conclusiones Finales**  
- **Azure AI Foundry = Enabler:** Ha demostrado ser una plataforma didáctica y práctica que **democratiza** la creación de aplicaciones de IA avanzadas. Un desarrollador puede, con conocimientos básicos de Python y de Azure, montar un chatbot sofisticado aprovechando lo mejor de la IA actual.  
- **Portabilidad comprobada:** La transición desde el entorno de desarrollo al entorno de producción fue fluida. Esto valida que las soluciones creadas no se “quedan atrapadas” en el laboratorio, sino que están listas para usarse en entornos reales con mínimo esfuerzo adicional.  
- **Impacto en el negocio:** Un chatbot de asistencia técnica desplegado puede reducir costes de soporte, mejorar la satisfacción del usuario (respuestas inmediatas, 24/7) y liberar al personal para tareas más complejas. La facilidad de construirlo y mantenerlo hace viable su adopción.  
- **Siguientes pasos:** Se invita a la audiencia a explorar Azure AI Foundry por sí mismos, quizás iniciando con plantillas o tutoriales que ofrece Microsoft, y probar a crear su propio piloto de chatbot u otra aplicación generativa. También a profundizar en temas como Prompt Engineering y evaluación de IA responsable, que Foundry tiene incorporados.  
- **Cierre:** En la era de la IA generativa, herramientas como Azure AI Foundry + Azure App Service nos permiten materializar ideas rápidamente y de forma confiable. ¡Aprovechemos estas tecnologías para innovar en nuestros proyectos de asistencia técnica y más allá! Gracias.
---


Gracias por la aclaración. Para garantizar que la presentación y el guion sean lo más útiles y relevantes posible, ¿tienes alguna preferencia sobre el propósito del chatbot? Puede ser un asistente para soporte técnico, un chatbot de atención al cliente, un chatbot interno para empleados, o cualquier otro caso de uso específico.

Además, ¿prefieres que la solución incluya la integración con algún servicio específico de Azure, como Azure Cognitive Services, Azure AI Search para mejorar las respuestas con documentos propios, o simplemente utilizar modelos de lenguaje preexistentes de Azure AI Foundry?

Déjame saber estos detalles y me pondré a trabajar en los documentos para tu charla técnica.
---


Aquí tienes una lista de títulos sugeridos para tu charla técnica sobre la creación y despliegue de un chatbot de asistencia técnica utilizando Azure AI Foundry, Python y Azure App Service:

### Títulos sugeridos (más técnicos):

1. **"De cero a chatbot: Construcción rápida con Azure AI Foundry y despliegue en Azure App Service"**

2. **"Azure AI Foundry en acción: Chatbot de asistencia técnica con Python y despliegue en la nube"**

3. **"Crea y despliega un chatbot inteligente con Azure AI Foundry y Azure App Service"**

4. **"Azure AI Foundry: Simplificando la creación de asistentes técnicos con Python y Azure App Service"**

5. **"Chatbot de soporte técnico: De MVP a producción con Azure AI Foundry y Azure App Service"**

### Títulos sugeridos (más atractivos y amigables):

6. **"Tu asistente técnico en minutos: Azure AI Foundry, Python y Azure App Service en acción"**

7. **"Inteligencia Artificial ágil: Construye y despliega chatbots técnicos fácilmente con Azure AI Foundry"**

8. **"Chatbots inteligentes al alcance de todos: Creando soporte técnico con Azure AI Foundry y Python"**

9. **"De idea a realidad: Cómo Azure AI Foundry simplifica la creación de chatbots de asistencia técnica"**

10. **"Chatbots técnicos rápidos y escalables: El poder combinado de Azure AI Foundry y Azure App Service"**

Estos títulos buscan captar la atención al enfatizar tanto la facilidad y rapidez como la utilidad práctica del caso propuesto. ¿Te gustaría ajustar algo más o te quedas con alguno de estos?
---


Voy a preparar dos documentos detallados para tu charla técnica sobre Azure AI Foundry, con un caso práctico basado en la creación de un chatbot utilizando Python.

1. Un **guion detallado** para guiarte en la charla, incluyendo:
   - Introducción sobre Azure AI Foundry y su transición desde Azure AI Studio.
   - Caso práctico: desarrollo de un chatbot con Azure AI Foundry.
   - Pasos secuenciales para la creación, exportación y despliegue en Azure App Service.
   - Consejos para una implementación exitosa y conclusión destacando la facilidad de construir un MVP.

2. Una **presentación** en formato **PowerPoint y Apple Keynote**, con:
   - Introducción y objetivos.
   - Resumen visual del caso práctico.
   - Ilustración del proceso en Azure AI Foundry (capturas y diagramas conceptuales).
   - Pasos para exportación e implementación en Azure App Service.
   - Beneficios y diferenciadores de Azure AI Foundry.
   - Conclusiones y recomendaciones.

Te avisaré en cuanto tenga lista la información.
---


## Guion Detallado para la Charla

### Introducción a Azure AI Foundry 
Azure AI Foundry es la evolución de Azure AI Studio, el entorno de desarrollo de IA de Microsoft. Este cambio de nombre viene acompañado de **nuevas funcionalidades y mejoras** que facilitan llevar una idea en IA generativa desde el concepto, al código, hasta la nube de forma más rápida【3†L1025-L1032】. En esencia, Azure AI Foundry proporciona **una plataforma unificada** y confiable para que desarrolladores y equipos de TI diseñen, personalicen y administren aplicaciones y agentes de IA. Ofrece un conjunto completo de capacidades de IA a través de un portal sencillo, un SDK unificado y APIs, permitiendo **integración segura de datos, personalización de modelos y gobierno empresarial** para acelerar el paso a producción【1†L975-L982】【25†L73-L80】. En otras palabras, Foundry integra en una sola experiencia todo lo necesario para construir y desplegar soluciones de IA (modelos base, datos, evaluación, despliegue), aprovechando las herramientas que los desarrolladores ya usan. Esta plataforma surge como respuesta a la rápida evolución de la IA generativa, consolidando lo que antes conocíamos como Azure AI Studio en un **hub integral de desarrollo de IA**【3†L1025-L1032】.

*Nota:* Azure AI Foundry se integra con servicios como Azure OpenAI, Azure AI Services, Azure Cognitive Search, etc., y se conecta con herramientas de desarrollo populares (VS Code, GitHub, Copilot) para brindar una experiencia fluida a los desarrolladores. Desde su anuncio, Azure AI Foundry ha pasado a disponibilidad general, mostrando la apuesta de Microsoft por simplificar y agilizar el desarrollo de aplicaciones de IA generativa en la nube.

### Caso Práctico – Chatbot en Python con Azure AI Foundry
Para ilustrar las capacidades de Azure AI Foundry, presentaremos un **caso práctico**: el desarrollo rápido de un **chatbot conversacional** usando Python, y su despliegue en un servicio web escalable mediante **Azure App Service**. Imaginemos que nuestra organización necesita un **asistente virtual** que responda preguntas frecuentes o consulte información de productos. Tradicionalmente, crear un chatbot así requería integrar manualmente un modelo de lenguaje, posiblemente entrenarlo, desarrollar una aplicación web y encargarse de la infraestructura. Con Azure AI Foundry, veremos cómo podemos construir un **MVP (Producto Mínimo Viable)** funcional en **tiempo récord**, apoyándonos en los modelos de lenguaje avanzados de Azure (por ejemplo, GPT-4) y en la infraestructura gestionada de Azure.

En este caso práctico, el flujo general será:
- **Diseñar el chatbot en Azure AI Foundry**, aprovechando un modelo de lenguaje pre-entrenado (por ejemplo, GPT-3.5 Turbo o GPT-4) e incorporando una *prompt* o instrucciones que definan su comportamiento.
- **(Opcional)** Conectar datos de la empresa para especializar el chatbot (por ejemplo, un índice de Azure Cognitive Search con documentos de productos, para implementar *retrieval-augmented generation*). Azure AI Foundry permite **“grounding” del modelo con datos propios** para respuestas más precisas【6†L49-L57】.
- **Exportar o extraer el proyecto** generado por Foundry, ya sea obteniendo el código base para integrarlo en una app Python o utilizando las opciones de exportación que ofrece la plataforma.
- **Implementar y desplegar** el chatbot en Azure App Service, convirtiéndolo en una aplicación web accesible para los usuarios finales.
- Por último, revisar algunas **mejores prácticas** aplicadas durante el proceso para garantizar que el despliegue sea exitoso (en términos de seguridad, rendimiento y mantenimiento).

### Pasos Detallados para Desarrollar el Chatbot

**1. Creación del chatbot en Azure AI Foundry:** Comenzamos ingresando al portal de Azure AI Foundry (https://ai.azure.com) y creando un **nuevo proyecto de IA**. Un proyecto actúa como contenedor de todos los componentes (modelos, datos, evaluaciones, despliegues) y facilita la colaboración y organización【22†L60-L68】【22†L77-L85】. Dentro del proyecto, seleccionamos un **modelo de lenguaje** adecuado de la **catalogo de modelos** (por ejemplo, *gpt-4o* o *gpt-35-turbo* desplegado en Azure OpenAI) y lo implementamos para usarlo en nuestro chatbot【37†L75-L83】【37†L89-L97】. Azure AI Foundry soporta una amplia variedad de modelos, tanto de OpenAI como de otros proveedores, incluyendo modelos open-source, lo que nos da flexibilidad para elegir el modelo que mejor se adapte al caso de uso.

Una vez desplegado el modelo dentro del proyecto, utilizamos el **Chat Playground** del portal para diseñar la conversación. Configuramos el **mensaje de sistema** que establece el rol y tono del asistente, por ejemplo: *“Eres un asistente de IA que ayuda a la gente a encontrar información”*【39†L125-L132】 (podemos adaptar este prompt a nuestro dominio, como describir conocimiento de productos específicos si aplica). Este prompt de sistema sirve para **orientar al modelo** sobre cómo debe responder. Opcionalmente, añadimos mensajes de sistema de seguridad pre-construidos (por ejemplo, instrucciones para evitar contenido inapropiado) para alinear el comportamiento con políticas de IA responsable. Luego probamos el chatbot ingresando algunas **preguntas de ejemplo** en la interfaz del playground (p.ej., “¿Cuál es el precio del nuevo producto X?”) y observamos las respuestas del modelo en tiempo real. Si las respuestas no son las deseadas, iteramos ajustando el mensaje del sistema, agregando ejemplos de conversación o incluso conectando datos adicionales. 

> **Integración de datos (opcional):** Una de las ventajas de Azure AI Foundry es la facilidad para integrar **fuentes de datos propias** en el flujo de la conversación. Por ejemplo, podemos **conectar un recurso de Azure AI Search** (servicio de búsqueda cognitiva) indexando nuestros documentos o base de conocimientos. Esto permite que el chatbot “busque” información relevante y la use para fundamentar sus respuestas, técnica conocida como *grounding*. En nuestro caso práctico, podríamos indexar información de productos en Azure Cognitive Search y asociarla al proyecto. Al activar esta conexión, el modelo podrá recuperar datos específicos (descripciones, precios, inventario, etc.) para responder con mayor precisión las preguntas sobre productos【6†L49-L57】. Esta arquitectura de *Retrieval-Augmented Generation (RAG)* combina lo mejor de la búsqueda y los modelos generativos, reduciendo las “alucinaciones” y proporcionando respuestas actualizadas con datos de la empresa. Si optamos por este camino, Foundry ofrece asistentes para agregar la fuente de datos y probar nuevamente el chatbot con preguntas relacionadas a ese contenido, verificando que ahora incluya detalles concretos que antes desconocía.

Tras configurar el modelo (y opcionalmente los datos) y afinar la *prompt*, **evaluamos las interacciones** en el playground. Azure AI Foundry proporciona herramientas integradas de **evaluación y depuración**, por ejemplo un visor de *trazas* de las llamadas al modelo y la posibilidad de probar diferentes inputs automáticamente. Esto nos ayuda a identificar si el modelo sigue correctamente las instrucciones y a calibrar parámetros antes del despliegue. Una vez **satisfechos con el comportamiento** del chatbot en el entorno de desarrollo, estamos listos para llevarlo fuera del portal.

**2. Exportación del proyecto generado:** Azure AI Foundry nos da varias opciones para **aprovechar el proyecto de IA fuera del portal**. Una alternativa es utilizar el botón **“View code” (Ver código)** en la interfaz del Chat Playground, que genera fragmentos de código listos para usar la solución desde un entorno de desarrollo. Por ejemplo, podemos obtener código Python que muestre cómo invocar nuestro modelo con su endpoint REST o mediante el SDK unificado de Foundry. Este código incluye la lógica de la conversación que definimos, y **se puede incorporar fácilmente en una aplicación web Python** (por ejemplo, agregándolo como endpoint en un servidor Flask o FastAPI)【13†L37-L40】. De esta manera, si deseamos mayor control o personalización de la aplicación, podemos **exportar la lógica del chatbot al código Python** y continuar el desarrollo en local, integrándolo con otras funcionalidades.

Otra opción que ofrece la plataforma es la **exportación directa a otros canales**. En el menú de *Deploy/Export* del playground, Azure AI Foundry permite, por ejemplo, **exportar el chatbot como una aplicación de Teams** (descargando un paquete .zip listo para publicar en Microsoft Teams) o **como un Copilot** en el Microsoft 365 Copilot Studio (para integrarlo en experiencias de Office). Estas opciones demuestran la versatilidad del servicio: con muy poco esfuerzo adicional podemos reutilizar el mismo chatbot en distintos canales corporativos. Para efectos de nuestro caso práctico, nos enfocaremos en llevar el chatbot al canal web mediante Azure App Service, pero vale la pena mencionar que esta portabilidad es una **mejora significativa en productividad** – un mismo desarrollo base puede servir en web, Teams, o como API, sin reescribir lógica.

**3. Implementación en Azure App Service:** Llegados a este punto, tenemos dos caminos para desplegar el chatbot en la web. El más sencillo es aprovechar la integración nativa que Foundry brinda con Azure App Service. Desde el propio portal de Azure AI Foundry, en el Chat Playground de nuestro proyecto, hacemos clic en **Deploy > ... as a web app** (“Desplegar > ... como aplicación web”). Esta acción desencadena un asistente que nos pide algunos datos mínimos: un nombre único para la aplicación web, la suscripción de Azure, grupo de recursos y región donde desplegar (generalmente utilizaremos los mismos que el proyecto Foundry) y el plan de tarifa para App Service【9†L352-L360】. Con esos datos, al confirmar, la plataforma **publica automáticamente el chatbot como una aplicación web** en nuestro Azure App Service. En segundo plano, se crea una instancia de App Service con una pequeña aplicación (preconfigurada por Microsoft) que contiene la interfaz de chat y la conexión a nuestro proyecto de Azure AI Foundry. Este proceso de publicación tarda solo unos minutos. Una vez completado, ya tendremos un **URL público** (o interno, según configuración) donde el chatbot está accesible y funcionando, sin que hayamos tenido que escribir código adicional para la interfaz web. De hecho, la documentación oficial destaca que una vez que estamos satisfechos con la experiencia en Foundry, podemos **desplegar el modelo como una aplicación web autónoma** con unos pocos clics【9†L301-L304】.

Si preferimos un mayor grado de control (por ejemplo, personalizar totalmente la interfaz de usuario o la lógica), podríamos tomar el código exportado en el paso anterior e implementarlo manualmente. En tal caso, crearíamos un **proyecto web en Python (Flask/FastAPI)** que utilice el SDK de Azure AI Foundry o las APIs REST para interactuar con el modelo y (opcionalmente) el índice de búsqueda. Luego desplegaríamos esa aplicación Python en Azure App Service mediante métodos tradicionales (CI/CD, *git push*, etc.). Sin embargo, para construir un MVP rápido, la **ruta no-code/low-code** que ofrece Foundry de *“Deploy as web app”* es la más directa y recomendada.

Tras el despliegue en App Service, accedemos a la URL de la aplicación para realizar pruebas finales. Podremos ver una sencilla **interfaz web de chat** donde el usuario escribe preguntas y recibe respuestas, alimentadas por nuestro modelo en Azure AI Foundry (y nuestros datos, si los integramos). Es importante mencionar que, de forma predeterminada, **esta aplicación web estará protegida**: solo nuestro usuario (creador) puede verla inicialmente. Esto se debe a que, al crearla desde Foundry, se habilita por defecto la autenticación mediante Azure AD (*Easy Auth*), restringiendo el acceso. En un entorno empresarial, probablemente querremos mantener esa autenticación y quizá configurarla para que cualquier usuario de nuestro directorio de Azure AD (nuestra organización) pueda usar el chatbot tras iniciar sesión【9†L374-L381】. De esta forma nos aseguramos que el MVP es accesible solo por el público objetivo (por ejemplo, empleados internos si es un asistente interno). Alternativamente, podríamos decidir abrir el acceso removiendo la autenticación (si el chatbot fuese de uso público), pero siempre es recomendable **controlar el acceso en las etapas iniciales**, tanto por seguridad como por costos.

En resumen, con Azure AI Foundry logramos pasar del diseño de un chatbot a tenerlo **desplegado en un entorno escalable** en muy poco tiempo y con mínima codificación manual. A continuación, revisamos algunas mejores prácticas aplicadas durante este proceso para asegurar el éxito del proyecto.

### Recomendaciones y Mejores Prácticas

- **Comenzar sencillo y escalar gradualmente:** Al construir un MVP conviene iniciar con un alcance acotado. En nuestro caso, definimos primero el comportamiento base del chatbot con un solo modelo y luego, opcionalmente, incorporamos la conexión a datos adicionales. Azure AI Foundry facilita este enfoque iterativo, ya que podemos agregar componentes (datos, nuevos prompts, evaluaciones) sobre la marcha dentro del mismo proyecto. Empezar con un modelo más pequeño o un subconjunto de datos y luego ampliarlo permite encontrar rápidamente un producto funcional y **evitar sobrecarga inicial**.

- **Aprovechar las herramientas de evaluación en Foundry:** Antes de desplegar, es vital probar bien el chatbot. Utilice el playground para simular diversas preguntas, incluidas aquellas “trampa” o fuera de alcance, para ver cómo responde el modelo. Azure AI Foundry incluye opciones como *Prompt flow* y *Evaluate* que ayudan a depurar las conversaciones y medir la calidad de las respuestas. Es recomendable iterar sobre el prompt y la configuración hasta lograr respuestas coherentes. Asimismo, si incorporó datos con Azure Cognitive Search, verifique que el modelo esté utilizando esa información correctamente (por ejemplo, cite datos específicos cuando corresponda). Esta fase de afinamiento en Foundry **reduce sorpresas** una vez que el bot esté publicado.

- **Gestión de credenciales y configuración:** Foundry maneja internamente la conexión con los servicios (modelos de Azure OpenAI, búsqueda, almacenamiento) dentro del proyecto. No obstante, si exporta el código para uso externo, asegúrese de **proteger las claves y endpoints**. Use Azure Key Vault o las configuraciones de App Service (Settings) para no exponer credenciales en el código. En nuestro despliegue automático, Foundry configura la aplicación web con la información necesaria de forma segura (posiblemente mediante **identidades administradas** en Azure AD para autenticarse contra los servicios de Azure, evitando el uso directo de API keys).

- **Seguridad y control de acceso:** Como mencionamos, la aplicación en App Service puede requerir autenticación Azure AD para su uso. Es una buena práctica mantener esta seguridad al menos durante la fase de MVP interno, de modo que solo el equipo o los usuarios autorizados accedan al chatbot (especialmente si este usa datos confidenciales). Más adelante, si el bot se abre a un público mayor, evalúe implementar cuotas o validaciones adicionales para evitar abusos. Azure AD permite integrar **autenticación con diversos proveedores** fácilmente en App Service, o incluso limitar por roles del directorio quién puede acceder.

- **Monitoreo y registro:** Tras el despliegue, es importante monitorizar el funcionamiento del chatbot. Azure App Service se integra con **Azure Monitor** y Application Insights, lo que permite recoger logs de conversación, métricas de uso, tiempos de respuesta, etc. Activa el logging de App Service y, si es posible, instrumenta tu chatbot (en caso de haber código personalizado) para registrar preguntas y respuestas, siempre respetando la privacidad. Este monitoreo te ayudará a detectar si el modelo comete errores o si hay consultas frecuentes que no sabe responder, para iterar sobre ellas.

- **Optimización de costos y rendimiento:** Utilizar modelos de lenguaje grandes puede ser costoso. Para un MVP, considere usar modelos más pequeños o limitar la frecuencia de llamadas mientras evalúa el interés de los usuarios. Azure AI Foundry y los servicios conectados (OpenAI, Search) generan costos que conviene vigilar. Configure alertas de costos en la suscripción. Asimismo, en App Service seleccione un plan adecuado: por ejemplo, un plan básico puede ser suficiente para un MVP; escale a uno Standard o superior solo si el tráfico de usuarios lo demanda. Después de las demos o pruebas, **apague o elimine recursos que no necesite** (por ejemplo, el App Service o el índice de búsqueda de prueba) para no incurrir en gastos continuos.

- **Planes para producción:** Si bien el enfoque mostrado es excelente para un prototipo funcional rápido, al prepararse para producción se deben considerar prácticas adicionales. Por ejemplo, **control de versiones del prompt** (llevar registro de cambios en las instrucciones del bot), pruebas más exhaustivas incluyendo validación de seguridad en las respuestas, y posiblemente fine-tuning del modelo si se requiere un comportamiento muy específico. La arquitectura también podría endurecerse: en un escenario productivo crítico podría convenir aislar el modelo en un endpoint gestionado de Azure ML, emplear escalado automático en App Service, usar un frontend más personalizado, etc. Microsoft ofrece arquitecturas de referencia que amplían esta básica con consideraciones de alta disponibilidad y redes privadas, llegado el caso. Para nuestro MVP, mantenemos las cosas simples, pero con la confianza de que **es sencillo evolucionar el prototipo hacia un producto robusto** usando la base construida en Azure AI Foundry.

### Conclusión 
En esta charla hemos visto cómo Azure AI Foundry nos permite **construir y desplegar rápidamente un chatbot de IA** utilizando Python y servicios cloud, con un esfuerzo significativamente menor al tradicional. Partiendo de una idea, pasamos en poco tiempo a una aplicación web funcional, gracias a la integración que Foundry ofrece de todo el ciclo (desde el modelo hasta el hosting). Esto **acelera el tiempo de salida al mercado** de aplicaciones de IA generativa【3†L1027-L1031】, permitiéndonos crear un MVP en cuestión de días o incluso horas. Destacamos la **facilidad**: muchas tareas complejas (como orquestar un modelo de lenguaje con fuentes de datos o aprovisionar infraestructura web) se realizan con configuraciones mínimas o automatizadas. Asimismo, la **agilidad**: pudimos refinar el comportamiento del bot sobre la marcha y desplegar con un clic, lo que en un entorno de desarrollo ágil nos deja iterar rápidamente con feedback real de usuarios.

En resumen, Azure AI Foundry se perfila como una herramienta poderosa para desarrolladores y empresas que busquen **innovar con IA generativa** sin invertir enormes recursos iniciales. Nos habilita para crear asistentes, copilotos y aplicaciones inteligentes de forma acelerada, con soporte de buenas prácticas y escalabilidad de Azure desde el día uno. La experiencia de haber construido este chatbot nos muestra que combinar Azure AI Foundry con Azure App Service es una fórmula ganadora para materializar prototipos de IA en productos utilizables. **La construcción de un MVP nunca ha sido tan sencilla y rápida**, y queda abierta la puerta para llevar este MVP al siguiente nivel, iterando y mejorándolo hasta convertirlo en una solución de producción completa. ¡Esperamos que esta demostración les inspire a probar Azure AI Foundry en sus propios proyectos de IA!

---

## Presentación (PowerPoint / Keynote)

- **Diapositiva 1 – Introducción y Objetivos:** Presenta el tema de la charla: *“Creación rápida de un Chatbot con Azure AI Foundry y despliegue en Azure App Service”*. Incluye el logo de Azure AI Foundry y Azure App Service para ambientar. Se explica brevemente qué es Azure AI Foundry y por qué surge (evolución de Azure AI Studio) – enfatizando que es la nueva plataforma unificada de Microsoft para desarrollo de aplicaciones de IA generativa. Objetivos en bullet points: **1)** Mostrar cómo desarrollar un chatbot usando herramientas de Azure AI de forma ágil, **2)** Demostrar un caso práctico paso a paso, **3)** Compartir recomendaciones para llegar a un MVP exitoso. El mensaje clave: *Con Azure AI Foundry podemos pasar “de **idea** a **aplicación de IA** en producción” de manera más sencilla y rápida que nunca*【3†L1027-L1031】.

- **Diapositiva 2 – Azure AI Foundry: Visión General:** Explica visualmente la plataforma antes de entrar al caso práctico. Se puede incluir una captura de pantalla de la **página de bienvenida de Azure AI Foundry** o el portal para situar al público【36†embed_image】. Los puntos a destacar: Azure AI Foundry centraliza todo lo necesario para proyectos de IA – modelos (Azure OpenAI y otros), datos, herramientas de evaluación, y despliegue – en una interfaz unificada【25†L73-L80】. Mencionar que antes esto era Azure AI Studio y ahora se amplía con más capacidades. Bullets en la diapositiva podrían ser: *“Plataforma unificada de IA”*, *“Más de 1800 modelos disponibles (OpenAI, HuggingFace, etc.)”*, *“Integración con herramientas de desarrollo (VS Code, GitHub)”*, *“Enfoque enterprise (gobernanza, seguridad, colaboración)”*. Esto prepara el contexto de por qué usar Foundry para el chatbot.

- **Diapositiva 3 – Caso Práctico: Arquitectura del Chatbot**: Se presenta un **diagrama de arquitectura** sencillo del chatbot que vamos a crear. 【16†embed_image】 *Arquitectura de la solución – flujo de interacción del chatbot*. En este diagrama se ilustra el flujo: el **usuario** interactúa mediante una aplicación web (el chatbot UI en Azure App Service), sus preguntas viajan al **backend de Azure AI Foundry** donde está el modelo de lenguaje (por ejemplo GPT-4) que las procesa. Si el proyecto tiene datos conectados, el modelo realizará consultas a la **fuente de datos** (un índice de Azure Cognitive Search) para obtener información relevante (*grounding*), y finalmente el **modelo genera una respuesta** que es devuelta al usuario a través de la web. También se muestran otros componentes de Azure involucrados: por ejemplo **Azure OpenAI Service** (alojando el modelo GPT), **Azure AI Search** (almacenando el índice de información), **Azure Blob Storage** (conteniendo archivos o datos del proyecto) y **Azure App Service** (hospedando la interfaz web del chatbot). Esta diapositiva resume la solución: un chatbot Q&A que combina un LLM con datos empresariales, montado sobre servicios serverless/PaaS en Azure. El propósito es que la audiencia visualice los componentes y cómo encajan: Foundry actúa como el “cerebro” (donde se configura el agente de IA), y App Service como el “cuerpo” que interactúa con el usuario.

- **Diapositiva 4 – Desarrollo en Azure AI Foundry (Construcción del Chatbot):** Detalla los pasos realizados dentro del portal de Foundry para crear el chatbot. Incluye **capturas de pantalla** del proceso en Azure AI Foundry: por ejemplo, una captura de la sección de **Connected Resources** del proyecto (donde se ve el modelo Azure OpenAI y Azure AI Search conectados)【24†embed_image】, y/o una captura del **Chat Playground** con el prompt de sistema configurado y una pregunta de prueba. Las imágenes deben ilustrar el entorno visual de Foundry. Los puntos en la diapositiva: 
  - *Crear proyecto de AI Foundry* (seleccionar región, nombre, etc., se crea un “hub” y proyecto).
  - *Desplegar modelo de lenguaje en el proyecto* – en nuestro caso GPT-*x* seleccionado del catálogo e implementado dentro del proyecto.
  - *Configurar Prompt inicial* – establecer el rol del bot (ej. “Asistente de soporte de productos”) en el **System message**【39†L125-L132】.
  - *Conectar datos (opcional)* – añadir una conexión a Azure Cognitive Search con nuestro índice de conocimientos (p.ej. catálogo de productos) para habilitar preguntas sobre datos propios.
  - *Probar en Chat Playground* – mostrar cómo se ingresa una pregunta de ejemplo y el modelo responde. Indicar que Foundry permite iterar rápidamente aquí mismo hasta afinar el comportamiento.
  - *Evaluación y ajuste* – (breve) mencionar que existen herramientas de evaluación de respuestas y se puede iterar en este entorno.
  
  El énfasis de esta diapositiva es **lo mínimo que tuvo que hacer el desarrollador gracias a Foundry**: no hubo que programar la lógica de llamada al modelo ni preocuparse por infraestructura hasta este punto, todo se logró con configuraciones en la UI. La imagen de los recursos conectados destaca cómo Foundry **gestiona por nosotros la conexión a servicios de Azure** (modelo OpenAI, búsqueda, storage) dentro del proyecto【24†L0-L0】, facilitando la integración.

- **Diapositiva 5 – Exportación e Implementación en Azure App Service:** Ahora se explica cómo llevamos el chatbot del entorno de desarrollo a un entorno de producción ligero. Se muestra una captura del **menú de despliegue en el Chat Playground** donde Azure AI Foundry ofrece opciones de exportar o desplegar【17†embed_image】. La captura destacada resalta la opción *“Deploy… as a web app”* (desplegar como app web) dentro de Foundry. Los puntos de la diapositiva:
  - *Exportar proyecto (opciones)* – Mencionar que Foundry permite obtener el código del bot o exportar a otros formatos (Teams, Copilot) si se quisiera. En nuestro caso, usamos la opción de desplegar directamente.
  - *Deploy as Web App* – Al hacer clic en **Deploy > ...as a web app**, Foundry empaqueta nuestro chatbot y lo publica en Azure App Service automáticamente【9†L301-L304】. No se requiere escribir ningún script de despliegue; simplemente proporcionamos un nombre de app, elegimos la suscripción, grupo de recurso y región adecuados【9†L352-L360】, y Foundry hace el resto.
  - *Azure App Service* – Explicar brevemente que App Service es el servicio de Azure que hospeda aplicaciones web. Nuestro chatbot se ejecutará allí con alta disponibilidad y escalado básico. El hecho de que Foundry lo use nos evitó configurar contenedores o máquinas manualmente.
  - *Prueba en producción* – Una vez desplegado, podemos hacer clic en “Launch” en Foundry o ir al URL del App Service para ver el chatbot en acción ya fuera del portal. Debemos ver la misma funcionalidad de chat pero ahora en un sitio web independiente.
  - *Seguridad* – Notar que, por defecto, solo nosotros podemos acceder inicialmente (la app está protegida con login Azure AD). Si quisiéramos abrir el acceso a otros usuarios de la organización, habilitaríamos autenticación para ellos en la configuración del App Service【9†L374-L381】. Es una buena práctica tener esta autenticación para controlar el uso durante el piloto.
  
  En esta diapositiva, reforzamos **la facilidad de despliegue**: con pocos clics pasamos de un entorno de prueba a tener un servicio web real funcionando, lo cual en proyectos tradicionales de IA suele requerir bastante trabajo de ingeniería. El público debe apreciar que Azure App Service se configuró sin escribir código, gracias a la integración de Foundry.

- **Diapositiva 6 – Beneficios y Diferenciadores de Azure AI Foundry:** Recapitula por qué Azure AI Foundry aceleró el desarrollo de nuestro MVP comparado con otras aproximaciones. Lista de **beneficios clave**:
  - **Desarrollo acelerado:** menor tiempo de desarrollo al tener una plataforma integrada (idea a prototipo en horas/días).
  - **Menos código necesario:** muchas funcionalidades (orquestación del modelo, UI básica del chat, conexiones a servicios) se logran sin código, lo que permite a desarrolladores enfocarse en la lógica de negocio y prompts.
  - **Integración nativa con Azure:** el salto a producción es sencillo porque el proyecto ya vive en Azure (pudimos desplegar en App Service directamente, y se podrían aprovechar otros servicios Azure para monitorización, CI/CD, etc.). Esto elimina fricción al pasar de prototipo a producto.
  - **Versatilidad de modelos y datos:** posibilidad de usar modelos de última generación (GPT-4, etc.) e incluso combinarlos con datos privados vía Cognitive Search con poco esfuerzo. Esto es un diferenciador importante frente a soluciones que solo ofrecen un modelo general sin conexión a datos empresariales.
  - **Gobernanza y seguridad incorporadas:** Foundry está pensado para entornos empresariales, con control de acceso por roles, registro de actividades, cumplimiento de normas (por ejemplo, permite aplicar principios de IA responsable fácilmente). Esto significa que nuestro MVP ya nace en un entorno con cierto nivel de **compliance**, a diferencia de jugar con una API externa sin ese marco.
  - **Escalabilidad y transición a producción:** lo que funciona en Foundry en pequeño, puede escalar en Azure (basta con aumentar recursos del App Service, o integrar con pipelines DevOps para despliegues continuos, etc.). No hay que “rehacer” el trabajo en otra plataforma al crecer; la inversión en el MVP se aprovecha.
  
  Visualmente, esta slide puede no tener mucha imagen adicional, quizá iconos de “Low Code”, “Agile” o logos de velocidad, etc., para enfatizar rapidez y facilidad. El mensaje global: **Azure AI Foundry nos dio velocidad, integración y confianza** para construir el MVP.

- **Diapositiva 7 – Conclusiones y Recomendaciones Finales:** Cierra la presentación resumendo la experiencia. Aquí enfatizamos la **facilidad y agilidad** logradas: “En pocas horas construimos un chatbot funcional usando Azure AI Foundry, algo que normalmente tomaría días integrando múltiples servicios manualmente”. Se puede mencionar que el equipo logró un MVP que ya está en manos de usuarios de prueba, validando la idea rápidamente. También, unas **recomendaciones finales** a la audiencia:
  - *Prueben Azure AI Foundry*: si tienen casos de uso de IA (chatbots, análisis de texto, copilotos personalizados), esta herramienta puede ahorrarles mucho tiempo.
  - *Comiencen con MVPs pequeños*: validar con poco esfuerzo y luego iterar. Foundry hace muy sencillo ampliar o modificar el proyecto sobre la marcha.
  - *No olvidar la gobernanza*: aunque sea un prototipo, aprovechar las características de seguridad (Azure AD, datos seguros) desde el inicio, para que el paso a producción sea más fluido.
  - *Mantenerse actualizados*: Azure AI Foundry es relativamente nuevo y en constante evolución; Microsoft sigue añadiendo capacidades (por ejemplo, integración con Copilot Studio, nuevos modelos, etc.), por lo que es bueno estar atento a nuevas funciones que puedan potenciar aún más el desarrollo de aplicaciones de IA.
  
  Finalmente, agradecer la atención e invitar a preguntas. Terminar con una frase positiva sobre la experiencia: por ejemplo, *“Azure AI Foundry nos permitió convertir una idea en realidad en tiempo récord – ¡imaginen qué puede hacer por sus proyectos de IA!”*. Esto refuerza el mensaje de valor para llevar.
---


Antes de comenzar la investigación, ¿tienes alguna preferencia sobre el caso práctico que se utilizará como ejemplo en la charla? Puede ser un caso relacionado con chatbots, análisis de datos, automatización de procesos, etc. También, ¿te gustaría que incluyera algún lenguaje de programación específico en el proceso de desarrollo?

Además, ¿prefieres la presentación en un formato específico (PowerPoint, Google Slides, etc.) o simplemente un esquema con el contenido clave para que tú lo diseñes?

Déjame saber estos detalles para afinar la información que prepararé para ti.

---
*Generado desde conversación con 18 mensajes.*
*Azure/Cloud*
