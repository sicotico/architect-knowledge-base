---
title: Opciones de red en AKS
date: 2024-11-05
category: Azure/Cloud
slug: opciones-de-red-en-aks
tags: ['Azure/Cloud', 'azure']
---

# Opciones de red en AKS


> **Pregunta original:**
> 
en Azure defender topolgia
> Analiza este post y crea un comentario para ponerle en linkdin:

Antes de crear una instancia de AKS deberemos planificar la red que dará soporte a nuestro cluster de Kubernetes. Cuando creamos un cluster desde el portal, la opción por defecto asociada a la configuración de red es Azure CNI. Si bien es la opción más popular, es la que exige un mayor rango de direcciones disponible en nuestra VNet, por lo que puede no ser la mejor alternativa en el caso de que tengamos algún tipo de limitación con las direcciones disponibles, por ejemplo, un rango limitado en una conexión VPN Gateway.
Modelos de Red 

El modelo de red seleccionado determina cómo se comunican los nodos y los pods entre si y con los recursos externos al cluster. Cada modelo tiene sus ventajas y desventajas

Un vistazo rápido a la documentación ofrece una opción básica, Kubenet networking, y otra avanzada, Azure CNI. Existe una tercera opción añadida recientemente (GA, Abril 2023), Azure CNI Overlay, que en mi opinión es la mejor opción dado que aúna las ventajas de las 2 anteriores. Veamos cada opción en más detalle.
Kubenet Networking

Con Kubenet, únicamente los nodos reciben una dirección IP de la subnet. Los pods no pueden comunicarse directamente entre ellos. En su lugar UDRs y redirecciones IPs habilitan la comunicación entre pods distribuidos en diferentes nodos. Por defecto, el enrutamiento lo crea y mantiene el propio servicio de AKS, pero puede configurarse para escenarios complejos. En resumen:

    Sólo se permite la creación de un cluster AKS por subnet.
    Los nodos reciben una dirección IP del rango de direcciones de la subnet asociada.
    Los pods reciben una dirección IP interna de una subred lógica diferente a la subnet de los nodos (no consumen IPs del rango de direcciones de la subnet asociada).
    Se hace necesario NAT para habilitar la comunicación entre los pods y los recursos de la VNet. El uso de enrutado a medida puede complicar la implementación y la administración del cluster.

Azure Virtual Network

    Azure soporta un máximo de 400 UDRs, por lo que no será posible tener más de 400 nodos. Aunque raramente nos acerquemos a semejante número de nodos en un proyecto real, Microsoft desaconseja el uso de este modelo en entornos productivos debido a su “limitada” escalabilidad.

Azure CNI

En este modelo, cada pod recibe una dirección IP de la subnet asociada, por lo que son accesibles directamente desde la VNet. El espacio de direcciones debe ser único (no puede compartirse entre varias instancias de AKS) y planificado con anterioridad, ya que el número de IPs asignables a los pods son reservadas de antemano en función del máximo número de pods por nodo configurado. Resumiendo:

    Los pods reciben una dirección IP del rango de direcciones de la subnet asociada.
    Las IPs son reservadas de antemano.
    No es necesario NAT ni reglas de rutado.
    Requiere de una buena planificación. Si nos quedamos cortos será necesario recrear el cluster en una subnet con mayor rango de direcciones.

Azure CNI

La ventaja de CNI frente al modelo Kubenet es clara: al recibir cada pod una dirección de la subnet, son accesibles directamente desde recursos fuera del cluster sin necesidad de reglas de rutado o NATing. Por el contrario, exigen un espacio de direcciones mucho mayor.

La documentación de Microsoft establece unos criterios para seleccionar un modelo u otro:

Kubenet:

    Contamos con un espacio de direcciones IP limitado.
    La mayor parte del tráfico generado por los pods permanece en el cluster.
    No son necesarias funcionalidades avanzadas como Nodos virtuales o Azure Network policies.

Azure CNI:

    Disponemos de un espacio de direcciones sin limitaciones.
    La mayor parte del tráfico generado en los pods es hacia recursos fuera del cluster.
    Se hacen uso de las funcionalidades avanzadas descritas anteriormente.

Pero, ¿y que pasa si tenemos un espacio de direcciones limitado y nuestros pods generan la mayor parte del tráfico hacia recursos externos? Este es un escenario bastante frecuente, dicho sea de paso. En tal caso la opción más lógica entre las 2 opciones sería escoger el modelo Kubenet, ya que la limitación de direcciones IP disponibles es insalvable. Afortunadamente, desde la primavera del 2023, contamos con una tercera opción.
Azure CNI Overlay

Como ya hemos comentado, la desventaja del modelo CNI tradicional es que debemos estimar de antemano el espacio de direcciones que vamos a necesitar. A medida que las aplicaciones demandan más recursos, podemos llegar a agotar las direcciones IP disponibles haciendo imposible el escalado.

Con el modelo CNI Overlay, los nodos del cluster se despliegan en la subnet asociada, sin embargo, las direcciones IPs de los pods pertenecen a un segmento de red diferente al de la VNet que hospeda los nodos:

    El tráfico interno entre nodos y pods utilizan una red diferente (Overlay Network).
    NAT utiliza la dirección IP del nodo para acceder a recursos fuera del cluster.
    Nos ahorramos todas las direcciones reservadas para los pods, lo que permite un nivel de escalado mucho mayor, en tanto en cuanto podemos utilizar todas las direcciones disponibles para los nodos.
    Una ventaja adicional es que podemos reusar el CIDR de la red overlay en diferentes clusters.

Azure CNI Overlay

A efectos prácticos, la principal diferencia respecto al modelo CNI standard es que los recursos externos no pueden conectarse directamente con un pod. Esto no será mayor problema en la mayoría de los escenarios, ya que podremos exponer las aplicaciones de nuestros pods como un servicio Kubernetes Load Balancer, habilitando así el acceso desde la VNet.

Las ventajas de este modelo frente al modelo Kubenet quedan reflejadas en la tabla comparativa de la propia documentación de Microsoft:

    Ampliamos el límite de un máximo de 400 a 5000 nodos (250 pods/nodo).
    No es necesaria ningún tipo de configuración extra para el rutado.
    Mayor rendimiento en la conectividad intra pods.
    Soporte en Linux y Windows (Kubenet sólo es soportado en Linux)

Por el contrario, existen algunas limitaciones, la de mayor impacto desde mi punto de vista es que no se puede hacer uso de Azure Application Gateway como Ingress Controller. En base a mi experiencia Nginx sigue siendo el controlador preferido en la mayoría de los clientes, por lo que no debería ser un factor determinante en la mayoría de los escenarios.
Conclusión

Os animo a que optéis por este modelo de red en vuestras implementaciones de AKS, sobre todo si no disponéis de un rango de direcciones lo suficientemente grande y siempre y cuando las limitaciones no apliquen a vuestro cluster. 

Actualmente (marzo 2024) no veo la opción de implementar CNI Overlay desde el portal, pero la opción está incluida desde la versión CLI 2.48.0. También es posible actualizar un cluster con el modelo CNI a CNI Overlay siempre que se cumplan ciertos criterios (Kubernetes 1.22+ como punto de partida).
> Como pegar una imagen en un markdawn en Visula Studio Code

---


## Respuesta


Aquí tienes un comentario para LinkedIn que resume y destaca el contenido del post sobre las opciones de redes en AKS:

---

¡Excelente análisis sobre la configuración de red en AKS! 👏 La elección del modelo de red adecuado es crucial para asegurar una comunicación óptima entre los nodos y pods de un clúster, y es fascinante ver cómo ha evolucionado la oferta de Azure con el reciente CNI Overlay.

Me parece interesante cómo este modelo combina las ventajas de Kubenet y Azure CNI, especialmente para escenarios con limitaciones de direcciones IP. Las opciones de escalado hasta 5000 nodos y la simplificación del enrutamiento son, sin duda, beneficios significativos. Además, el soporte en Windows y Linux amplía las posibilidades para diversas implementaciones. 

Este artículo destaca muy bien cuándo cada modelo es adecuado, considerando tanto las necesidades internas como externas del clúster. Gracias por compartir esta guía práctica para aquellos que buscan optimizar sus configuraciones de AKS. Definitivamente, una lectura recomendada para todos los interesados en arquitecturas en la nube y Kubernetes. 💡
---


Para insertar una imagen en un archivo Markdown en Visual Studio Code, puedes hacerlo de las siguientes maneras:

### 1. Sintaxis de Markdown para imágenes

La forma más común es usar la sintaxis de Markdown para agregar una imagen. Asegúrate de que la imagen esté en la misma carpeta del archivo `.md` o en una ruta accesible. La sintaxis es:

```markdown
![Texto alternativo](ruta/imagen.jpg)
```

- `Texto alternativo`: Texto que se muestra si la imagen no carga (útil para accesibilidad).
- `ruta/imagen.jpg`: Ruta relativa o absoluta de la imagen.

Por ejemplo:

```markdown
![Logo de mi proyecto](./imagenes/logo.png)
```

### 2. Arrastrar y soltar la imagen

En Visual Studio Code, puedes **arrastrar y soltar** una imagen directamente en el archivo Markdown. Esto generará automáticamente el código de Markdown con la ruta de la imagen.

### 3. Ver la imagen en la previsualización de Markdown

Para ver la imagen, abre la **vista de previsualización** en Visual Studio Code. Puedes hacerlo de dos maneras:

- Usa el atajo `Ctrl + Shift + V` (Windows/Linux) o `Cmd + Shift + V` (Mac).
- Haz clic en el icono de "Abrir previsualización" en la esquina superior derecha de la ventana de edición.

Con esto, la imagen debería aparecer en la previsualización del archivo Markdown.

### 4. Opcional: Insertar una URL de imagen en línea

Si tienes una imagen en línea, también puedes usar su URL:

```markdown
![Texto alternativo](https://example.com/imagen.jpg)
```

Esto permite mostrar la imagen directamente desde internet sin necesidad de descargarla localmente.

Estos pasos te ayudarán a insertar imágenes en archivos Markdown en Visual Studio Code de manera efectiva.
---


Microsoft Defender for Cloud ofrece un **Mapa de red interactivo** que proporciona una vista gráfica de la topología de red de sus cargas de trabajo en Azure. Este mapa muestra las conexiones entre máquinas virtuales, subredes y redes virtuales, permitiendo explorar en profundidad cada recurso y visualizar recomendaciones de seguridad específicas. citeturn0search0

Para acceder al mapa de red:

1. En el portal de Azure, navegue a **Microsoft Defender for Cloud**.
2. En el menú lateral, seleccione **Protección de cargas de trabajo**.
3. Haga clic en **Mapa de red**.

El mapa de red le permite:

- **Visualizar la topología de su red**: Observe cómo están estructuradas sus redes virtuales, subredes y máquinas virtuales, y cómo se interconectan.
- **Identificar vulnerabilidades**: Los indicadores de gravedad resaltan recursos con recomendaciones de seguridad pendientes, facilitando la priorización de acciones correctivas.
- **Explorar detalles de recursos**: Al seleccionar un recurso específico, se muestra información detallada y recomendaciones relevantes para fortalecer su seguridad.

Esta herramienta es esencial para comprender y gestionar la seguridad de su infraestructura en la nube, proporcionando una visión clara de la configuración y posibles áreas de mejora en su red.

---
*Generado desde conversación con 6 mensajes.*
*Azure/Cloud*
