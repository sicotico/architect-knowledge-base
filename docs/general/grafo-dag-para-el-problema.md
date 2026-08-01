---
title: Grafo DAG para el problema.
date: 2024-05-13
category: General
slug: grafo-dag-para-el-problema
tags: ['General']
---

# Grafo DAG para el problema.


> **Pregunta original:**
> 
No soy muy de recursividad, lo puede hacer en iterativo
> Porque no usaríamos una red semántica ?
> Necesito que expliques este código como si fuera un niño pequeño:

for (const comb of combinaciones) {
            const nuevoEstado = new Estado(
                estadoActual.granjeroIzquierda + comb.granjero,
                estadoActual.loboIzquierda + comb.lobo,
                estadoActual.ovejaIzquierda + comb.oveja,
                estadoActual.colIzquierda + comb.col
            );

            const nuevasAcciones = [...accionesActuales, comb];

            if (nuevoEstado.esValido()) {
                estadosPorEvaluar.push(nuevoEstado);
                accionesPorEvaluar.push(nuevasAcciones);
            }
        }

> 
> *...y 5 preguntas de seguimiento*


---


## Respuesta


Para representar el problema del granjero que debe cruzar el río con el lobo, la oveja y la col, una técnica de representación del conocimiento adecuada sería la de los grafos, específicamente utilizando un grafo dirigido acíclico (DAG). Esta elección se justifica debido a que los grafos son una forma natural de representar relaciones entre entidades, y un grafo dirigido permite modelar las restricciones de movimiento en una dirección específica, como el río en este caso.

La representación del conocimiento para este juego se puede realizar de la siguiente manera:

Nodos:
- Los nodos representarán el estado actual de la situación, es decir, la ubicación del granjero, el lobo, la oveja y la col.
- Por ejemplo, un nodo podría ser (A, B, C, D), donde A representa la ubicación del granjero, B la del lobo, C la de la oveja y D la de la col.

Aristas:
- Las aristas representarán las acciones que el granjero puede realizar, es decir, cruzar el río solo o con un compañero.
- Por ejemplo, desde el nodo (A, B, C, D) se podría tener una arista hacia el nodo (A', B, C, D), donde A' representa la ubicación del granjero después de cruzar el río solo.

Restricciones:
- Se deben añadir restricciones adicionales para asegurar que no se violen las condiciones del problema, como el lobo no puede quedarse solo con la oveja ni la oveja sola con la col.

Conclusiones:
- Mediante la representación del problema mediante grafos dirigidos, se pueden explorar diferentes estados y acciones posibles para encontrar una solución sin violar las restricciones del problema.

Utilización en un sistema inteligente:
- Un sistema inteligente podría utilizar esta representación del problema junto con algoritmos de búsqueda como búsqueda en profundidad o búsqueda en anchura para encontrar una solución óptima o subóptima al problema del granjero y los animales. Además, se podría implementar una heurística para guiar la búsqueda hacia la solución más eficiente.
---


Claro, aquí tienes el pseudocódigo equivalente al fragmento de código JavaScript que proporcionaste:

```
Para cada combinación en combinaciones:
    // Para cada combinación de movimiento posible

    // Crear un nuevo estado después de aplicar el movimiento
    nuevoEstado = Nuevo Estado(
        estadoActual.granjeroIzquierda + comb.granjero,
        estadoActual.loboIzquierda + comb.lobo,
        estadoActual.ovejaIzquierda + comb.oveja,
        estadoActual.colIzquierda + comb.col
    )

    // Añadir la combinación actual a las acciones realizadas hasta ahora
    nuevasAcciones = accionesActuales + comb

    // Si el nuevo estado es válido:
    Si nuevoEstado.esValido() es verdadero:
        // Agregar el nuevo estado y las nuevas acciones a las listas para evaluar
        Agregar nuevoEstado a estadosPorEvaluar
        Agregar nuevasAcciones a accionesPorEvaluar
```

Este pseudocódigo representa la misma lógica que el fragmento de código JavaScript. Itera sobre cada combinación de movimientos posibles, crea un nuevo estado después de aplicar el movimiento, verifica si el nuevo estado es válido y, si lo es, lo agrega a las listas de estados y acciones por evaluar.
---


Claro, aquí tienes una explicación sencilla de ese fragmento de código:

```javascript
for (const comb of combinaciones) {
    const nuevoEstado = new Estado(
        estadoActual.granjeroIzquierda + comb.granjero,
        estadoActual.loboIzquierda + comb.lobo,
        estadoActual.ovejaIzquierda + comb.oveja,
        estadoActual.colIzquierda + comb.col
    );

    const nuevasAcciones = [...accionesActuales, comb];

    if (nuevoEstado.esValido()) {
        estadosPorEvaluar.push(nuevoEstado);
        accionesPorEvaluar.push(nuevasAcciones);
    }
}
```

Imagina que tienes una caja con cuatro peluches: un granjero, un lobo, una oveja y una col. Queremos ver cómo se pueden mover estos peluches de un lado del río al otro. Para hacerlo, vamos a probar diferentes combinaciones de movimientos.

- Para cada combinación que estamos probando (cada uno de los movimientos posibles):
  - Creamos un nuevo estado, que es como una foto de cómo se ve la caja después de hacer ese movimiento. Por ejemplo, si movemos al granjero a través del río, este nuevo estado nos mostrará dónde están el granjero y los otros peluches después de que él haya cruzado.
  - Luego, anotamos este nuevo movimiento que hicimos.
  - Después, revisamos si este nuevo estado es un movimiento válido, es decir, si los peluches siguen las reglas del juego (como no dejar al lobo solo con la oveja).
  - Si el movimiento es válido, lo guardamos en una lista de movimientos que tenemos que revisar más tarde.

Después de revisar todas las combinaciones posibles, tendremos una lista de nuevos movimientos válidos para seguir jugando. Es como si estuviéramos probando diferentes formas de mover los peluches, y anotando cada movimiento que sea seguro y correcto. ¡Espero que eso tenga sentido!
---


Por supuesto, aquí tienes un ejemplo de cómo podrías implementar una solución en JavaScript utilizando la lógica proposicional para el problema del granjero y los animales cruzando el río:

```javascript
class Estado {
    constructor(granjeroIzquierda, loboIzquierda, ovejaIzquierda, colIzquierda) {
        this.granjeroIzquierda = granjeroIzquierda;
        this.loboIzquierda = loboIzquierda;
        this.ovejaIzquierda = ovejaIzquierda;
        this.colIzquierda = colIzquierda;
    }

    esValido() {
        if ((this.ovejaIzquierda == this.loboIzquierda && this.ovejaIzquierda != this.granjeroIzquierda) ||
            (this.ovejaIzquierda == this.colIzquierda && this.ovejaIzquierda != this.granjeroIzquierda)) {
            return false;
        }
        return true;
    }

    esFinal() {
        return !this.granjeroIzquierda && !this.loboIzquierda && !this.ovejaIzquierda && !this.colIzquierda;
    }
}

function cruzarRio(estadoActual, acciones) {
    if (estadoActual.esFinal()) {
        return acciones;
    }

    if (!estadoActual.esValido()) {
        return null;
    }

    // Intentar cruzar con cada posible combinación de elementos
    const combinaciones = [
        { granjero: -1, lobo: 0, oveja: 0, col: 0 },
        { granjero: -1, lobo: -1, oveja: 0, col: 0 },
        { granjero: -1, lobo: 0, oveja: -1, col: 0 },
        { granjero: -1, lobo: 0, oveja: 0, col: -1 }
    ];

    for (const comb of combinaciones) {
        const nuevoEstado = new Estado(
            estadoActual.granjeroIzquierda + comb.granjero,
            estadoActual.loboIzquierda + comb.lobo,
            estadoActual.ovejaIzquierda + comb.oveja,
            estadoActual.colIzquierda + comb.col
        );

        const nuevaAcciones = [...acciones, comb];

        const solucion = cruzarRio(nuevoEstado, nuevaAcciones);
        if (solucion) {
            return solucion;
        }
    }

    return null;
}

// Ejemplo de uso
const estadoInicial = new Estado(true, true, true, true);
const solucion = cruzarRio(estadoInicial, []);

if (solucion) {
    console.log("Solución encontrada:");
    for (const accion of solucion) {
        console.log(accion);
    }
} else {
    console.log("No se encontró solución");
}
```

Este código implementa una solución recursiva utilizando lógica proposicional para encontrar una secuencia de acciones que permita al granjero y a los animales cruzar el río sin infringir las restricciones del problema.
---


Para este problema, una representación estructurada parece más adecuada. Podríamos usar un enfoque basado en lógica proposicional, donde representamos el estado del problema y las restricciones mediante proposiciones lógicas.

Por ejemplo, podríamos tener las siguientes proposiciones:

- \(G\) para denotar la posición del granjero.
- \(L\) para denotar la posición del lobo.
- \(O\) para denotar la posición de la oveja.
- \(C\) para denotar la posición de la col.

Además, podríamos usar proposiciones para representar las acciones que el granjero puede realizar, como \(M(X, Y)\) para denotar que el granjero se mueve de la posición \(X\) a la posición \(Y\), donde \(X\) e \(Y\) pueden ser cualquier combinación de \(G\), \(L\), \(O\), \(C\) para indicar el movimiento del granjero solo.

Por último, se añadirían proposiciones para representar las restricciones del problema, como \(L \rightarrow \neg O\) para indicar que el lobo no puede quedarse solo con la oveja.

Esta representación estructurada permite utilizar técnicas de inferencia lógica para encontrar soluciones al problema, garantizando que se cumplan todas las restricciones.
---


Para desarrollar un sistema inteligente que solucione este problema, podríamos utilizar la representación formal o estructurada del conocimiento, como la lógica proposicional que hemos discutido anteriormente. Aquí hay algunos pasos sobre cómo podríamos usar este enfoque:

1. **Codificación del problema**: Primero, necesitaríamos codificar el problema en términos de proposiciones lógicas que representen los estados iniciales, las acciones posibles y las restricciones del problema.

2. **Implementación de reglas**: Utilizando las reglas lógicas, definiríamos las restricciones del problema, como el lobo no puede estar solo con la oveja y la oveja no puede estar sola con la col.

3. **Desarrollo de un motor de inferencia**: Crearíamos un motor de inferencia que pueda realizar inferencias lógicas sobre el estado actual del problema y las acciones posibles para alcanzar una solución.

4. **Algoritmo de búsqueda**: Implementaríamos un algoritmo de búsqueda que utilice el motor de inferencia para explorar el espacio de estados y encontrar una secuencia de acciones que lleve a una solución válida.

5. **Heurísticas (opcional)**: Si es necesario, podríamos incorporar heurísticas para guiar la búsqueda hacia soluciones más eficientes, como la búsqueda en anchura o la búsqueda en profundidad.

6. **Interfaz de usuario (opcional)**: Si queremos que el sistema sea accesible para usuarios humanos, podríamos desarrollar una interfaz de usuario que permita ingresar el estado inicial del problema y visualizar la secuencia de acciones requeridas para resolverlo.

7. **Pruebas y refinamiento**: Una vez que el sistema esté implementado, realizaríamos pruebas exhaustivas para asegurarnos de que funcione correctamente en una variedad de casos de prueba. Luego, refinaremos el sistema según sea necesario para mejorar su rendimiento y eficiencia.

En resumen, utilizando la representación formal del conocimiento y técnicas de inferencia lógica, junto con algoritmos de búsqueda adecuados, podríamos desarrollar un sistema inteligente capaz de resolver el problema del granjero y los animales cruzando el río de manera efectiva y eficiente.
---


Una red semántica podría ser otra opción válida para representar este problema. Las redes semánticas son estructuras de datos que representan conocimiento en forma de nodos y enlaces, donde los nodos representan entidades y los enlaces representan relaciones entre ellas.

En el caso del problema del granjero y los animales cruzando el río, podríamos representar las entidades (el granjero, el lobo, la oveja y la col) como nodos, y las relaciones entre ellas como enlaces. Por ejemplo, podríamos tener enlaces que representen las relaciones "junto a", "en la misma orilla que", "en la barca con", etc.

Además, podríamos asignar atributos a los nodos para indicar la posición actual de cada entidad (en la orilla izquierda, en la orilla derecha, en la barca, etc.).

Una ventaja de utilizar una red semántica es su capacidad para representar relaciones complejas de manera intuitiva. Sin embargo, en este problema específico, donde las restricciones son bastante simples y bien definidas, una representación más estructurada como la lógica proposicional podría ser más directa y eficiente para encontrar soluciones.

En resumen, aunque una red semántica podría ser una opción viable, en este caso la representación estructurada mediante lógica proposicional parece más adecuada debido a la naturaleza clara y precisa de las restricciones del problema.
---


Por supuesto, aquí tienes una versión iterativa del código JavaScript que encuentra una solución para el problema del granjero y los animales cruzando el río:

```javascript
class Estado {
    constructor(granjeroIzquierda, loboIzquierda, ovejaIzquierda, colIzquierda) {
        this.granjeroIzquierda = granjeroIzquierda;
        this.loboIzquierda = loboIzquierda;
        this.ovejaIzquierda = ovejaIzquierda;
        this.colIzquierda = colIzquierda;
    }

    esValido() {
        if ((this.ovejaIzquierda == this.loboIzquierda && this.ovejaIzquierda != this.granjeroIzquierda) ||
            (this.ovejaIzquierda == this.colIzquierda && this.ovejaIzquierda != this.granjeroIzquierda)) {
            return false;
        }
        return true;
    }

    esFinal() {
        return !this.granjeroIzquierda && !this.loboIzquierda && !this.ovejaIzquierda && !this.colIzquierda;
    }
}

function cruzarRio() {
    const estadosPorEvaluar = [new Estado(true, true, true, true)];
    const accionesPorEvaluar = [[]];

    while (estadosPorEvaluar.length > 0) {
        const estadoActual = estadosPorEvaluar.shift();
        const accionesActuales = accionesPorEvaluar.shift();

        if (estadoActual.esFinal()) {
            return accionesActuales;
        }

        if (!estadoActual.esValido()) {
            continue;
        }

        const combinaciones = [
            { granjero: -1, lobo: 0, oveja: 0, col: 0 },
            { granjero: -1, lobo: -1, oveja: 0, col: 0 },
            { granjero: -1, lobo: 0, oveja: -1, col: 0 },
            { granjero: -1, lobo: 0, oveja: 0, col: -1 }
        ];

        for (const comb of combinaciones) {
            const nuevoEstado = new Estado(
                estadoActual.granjeroIzquierda + comb.granjero,
                estadoActual.loboIzquierda + comb.lobo,
                estadoActual.ovejaIzquierda + comb.oveja,
                estadoActual.colIzquierda + comb.col
            );

            const nuevasAcciones = [...accionesActuales, comb];

            if (nuevoEstado.esValido()) {
                estadosPorEvaluar.push(nuevoEstado);
                accionesPorEvaluar.push(nuevasAcciones);
            }
        }
    }

    return null;
}

// Ejemplo de uso
const solucion = cruzarRio();

if (solucion) {
    console.log("Solución encontrada:");
    for (const accion of solucion) {
        console.log(accion);
    }
} else {
    console.log("No se encontró solución");
}
```

Esta versión utiliza una cola para mantener los estados y las acciones a evaluar, realizando una búsqueda iterativa hasta encontrar una solución válida.

---
*Generado desde conversación con 16 mensajes.*
*General*
