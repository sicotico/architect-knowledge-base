---
title: Código vs Mantenimiento
date: 2026-07-06
category: Comparativas
slug: codigo-vs-mantenimiento
tags: ['Comparativas']
---

# Código vs Mantenimiento


> **Pregunta original:**
> 
he visto este articulo y quiero comentarlo, pero no me queda clarosi es uan descripción de la situación actual y justificación de nuevos trabajos  aumento de carga en otros trabajos. Mi comentario tiene que ir en que se nos esta olvidando hacer las cosas bien desde el principio. Asi que generamos código y luego lo revisamos , no creo que sea el camino correcto.

 El código nunca fue el activo
Alberto Diaz Martin
Alberto Diaz Martin
Cloud & AI Whisperer | Chief Technology & Innovation Officer | Microsoft Regional Director | Microsoft Foundry & Microsoft 365 Copilot MVP | Profesor de IA ESIC | Transformando Cloud, IA y Agentes en valor para negocio
6 de julio de 2026

El coste de escribir código está colapsando. El coste de responder por él, no. Ese desequilibrio es el tema. No la IA.
El 80% del coste siempre estuvo después del commit

Así funciona el desarrollo hoy: un backlog, sprints, PRs, CI, despliegue. Escribir el código es la parte visible. No es la parte cara.

La parte cara empieza después. Mantenimiento. Parches de seguridad. Dependencias que se rompen. Estándares que cambian. Integraciones con sistemas que nadie documentó. Un repositorio de cinco años acumula más coste en operarlo que en haberlo escrito.

Este sistema ya estaba al límite antes de la IA. Los cuellos de botella no eran de tecleo: eran de contexto, coordinación y verificación. Cualquier equipo con un pipeline de CI lento y una cola de PRs sin revisar lo sabe.
La tesis bajista confunde código con producto

Con el coste de escribir código cayendo, aparece la pregunta obvia: ¿por qué pagar por software si puedes pedirle a la IA tu propia aplicación a medida?

    La pregunta asume que el código es el producto pero no lo es. 

Una empresa que genera su propio CRM con IA no ha comprado software. Ha adoptado un pasivo. Ahora es dueña del mantenimiento, de los parches, del cumplimiento normativo, de cada integración futura. Un viaje sin fin que no tiene nada que ver con su negocio.

Por eso las empresas no operan sobre puro open source aunque el código sea gratis. No quieren código. Quieren un producto: soporte, garantías, alguien que responda cuando falla.

El código generado no cambia esa ecuación. La expone.
La IA encaja en el código porque el código se puede verificar

Hay una razón técnica por la que la generación de código funciona mejor que otros usos de la IA: el encaje entre salidas probabilísticas y un entorno determinista. El código tiene que compilar. Tiene que pasar tests. Tiene que ejecutarse.

Eso convierte cada generación en una hipótesis falsable. Un modelo puede equivocarse y el sistema puede detectarlo. Esa propiedad no existe en un informe o en una estrategia.

Pero la propiedad tiene una condición: alguien tiene que haber construido el arnés de verificación. Tests que signifiquen algo. CI que falle cuando debe. Contratos de API explícitos. Sin eso, el código generado compila, se despliega y falla en producción.

El problema no es el modelo, el problema está en el sistema que lo recibe.
Se ve en el patrón de los que critican y luego adoptan

El patrón se repite: un ingeniero senior critica públicamente las herramientas de codificación con agentes. Semanas después admite que construyó algo que no habría hecho, o que habría tardado meses.

Las dos cosas son ciertas a la vez. Las herramientas fallan de formas visibles y producen valor de formas medibles. La crítica apunta a la fricción; la adopción apunta al resultado.

Lo que no se mide en ese ciclo es el coste desplazado. Más código generado significa más PRs. Más PRs significa más carga de revisión. La velocidad de escritura sube; la capacidad de verificación no. Velocidad sin gobierno es ruido.
El contexto es infraestructura, no documentación

Si el código es barato y la verificación es cara, el trabajo de ingeniería se desplaza: de escribir a diseñar las condiciones en las que un agente puede escribir sin romper nada.

Eso es Context Engineering. Convenciones del repositorio explícitas. Restricciones de arquitectura codificadas. Criterios de aceptación que un agente pueda ejecutar, no interpretar. El contexto deja de ser documentación que envejece y pasa a ser infraestructura que se mantiene.

El PR es el plano de control de este modelo. Ya no contiene solo código: contiene comportamiento propuesto por un agente, con su contexto y su evidencia de verificación. Revisar deja de ser leer diffs y pasa a ser auditar decisiones.
Ganan los que absorben verificación, no los que escriben software

La conclusión cómoda sería: las compañías de software ganan, porque escribirán más código, más rápido y más barato.

La ventaja pasa a las organizaciones que pueden verificar y mantener más código del que generan. Eso exige roles nuevos. Alguien tiene que diseñar el contexto, fijar los límites de los agentes y responder por su salida. Ese rol ya tiene nombre: Agent Boss. No escribe el código, gobierna el sistema que lo produce.

Una compañía de software sin esa capacidad tiene el mismo problema que su cliente: más código del que puede sostener. La etiqueta del sector no protege a nadie.
El activo es el sistema que sostiene el código

El futuro no es escribir menos código. Es operar sistemas capaces de absorber más decisiones de las que un humano puede escribir.

El código nunca fue el activo. El sistema que lo verifica, lo mantiene y responde por él, sí. La IA no ha cambiado eso. Ha hecho imposible seguir ignorándolo.

---


## Respuesta


Sí: el artículo es más una descripción de la situación actual y una justificación de que el trabajo se desplaza hacia verificación, contexto, gobierno y mantenimiento. Lo bueno es que acierta al decir que generar código no elimina responsabilidad. Lo discutible es que puede normalizar una dinámica peligrosa: producir más primero y revisar después, como si el problema se resolviera solo con mejores filtros al final.

Te propongo este comentario:

:::writing{variant="social_post" id="48291"}
Muy de acuerdo con la idea de que el código no es el activo principal y que el verdadero coste está en mantener, verificar y responder por lo que se pone en producción.

Pero creo que hay un riesgo importante: asumir que el nuevo modelo consiste en generar más código y reforzar después la revisión, el gobierno y la verificación. Eso puede acabar desplazando el problema, no resolviéndolo.

Para mí, la clave no debería ser “generamos y luego revisamos mejor”, sino diseñar desde el principio las condiciones para hacer las cosas bien: requisitos claros, arquitectura explícita, criterios de aceptación verificables, tests con sentido y límites técnicos antes de producir código.

Si la IA acelera la escritura pero no mejora la intención, el diseño y la calidad de partida, solo estaremos fabricando más trabajo aguas abajo. La verificación es imprescindible, sí, pero no debería convertirse en la coartada para olvidarnos de construir bien desde el inicio.
:::
---


Voy a tratarlo como un comentario para publicar: primero separo qué dice realmente el artículo, y luego te propongo una respuesta que conserve tu punto sin sonar simplemente en contra.

---
*Generado desde conversación con 3 mensajes.*
*Comparativas*
