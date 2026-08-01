---
title: PowerPoint Script Error Fix
date: 2025-03-20
category: General
slug: powerpoint-script-error-fix
tags: ['General']
---

# PowerPoint Script Error Fix


> **Pregunta original:**
> 
Dim objPPT
Dim objPresentation
Dim objSlide
Dim objShape

' Crear una instancia de PowerPoint
Set objPPT = CreateObject("PowerPoint.Application")
objPPT.Visible = True

' Crear una nueva presentación
Set objPresentation = objPPT.Presentations.Add

' Agregar una diapositiva de introducción
Set objSlide = objPresentation.Slides.Add(1, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Introducción"
objSlide.Shapes(2).TextFrame.TextRange.Text = "El documento tiene como objetivo establecer directrices de seguridad para entornos cloud, asegurando la protección de datos, la gestión eficiente de accesos y la minimización de riesgos de seguridad. Estas directrices buscan garantizar la integridad y disponibilidad de los recursos en la nube, lo cual es esencial para la continuidad del negocio."

' Agregar una diapositiva para la gestión de la postura de seguridad en la nube (CSPM)
Set objSlide = objPresentation.Slides.Add(2, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Gestión de la Postura de Seguridad en la Nube (CSPM)"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Evaluaciones Continuas:" & vbCrLf & "- Visibilidad Detallada: Proporciona una visión completa del estado de seguridad de los activos y cargas de trabajo en la nube, permitiendo identificar áreas de mejora." & vbCrLf & "- Puntuación de Seguridad: Utiliza herramientas como CSPM para evaluar y mejorar continuamente la postura de seguridad, asegurando que los estándares corporativos se mantengan."

' Agregar una diapositiva para la automatización de políticas de seguridad
Set objSlide = objPresentation.Slides.Add(3, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Automatización de Políticas de Seguridad"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Azure Policy: Permite crear y asignar políticas que imponen reglas sobre los recursos, asegurando el cumplimiento de estándares corporativos y normativos." & vbCrLf & "Corrección Automática: Configura acciones automáticas para corregir desviaciones de las políticas establecidas, reduciendo el riesgo de errores humanos."

' Agregar una diapositiva para la integración con herramientas de terceros
Set objSlide = objPresentation.Slides.Add(4, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Integración con Herramientas de Terceros"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Soluciones CSPM Avanzadas: Considera la integración de soluciones de terceros que ofrecen capacidades avanzadas de monitoreo, análisis y remediación para complementar las herramientas nativas de Azure."

' Agregar una diapositiva para la seguridad en el desarrollo de aplicaciones (DevSecOps)
Set objSlide = objPresentation.Slides.Add(5, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Seguridad en el Desarrollo de Aplicaciones (DevSecOps)"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Integración Continua de Análisis de Seguridad:" & vbCrLf & "- Normativa de FCC: Se debe seguir la normativa para el análisis de vulnerabilidades de código, asegurando que las aplicaciones sean seguras desde el inicio."

' Agregar una diapositiva de introducción a la gestión de dependencias
Set objSlide = objPresentation.Slides.Add(6, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Gestión de Dependencias"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- Inventario de Dependencias: Mantener un registro actualizado de todas las bibliotecas y paquetes utilizados en el proyecto, lo cual es crucial para identificar y mitigar vulnerabilidades." & vbCrLf & "- Actualizaciones Regulares: Establecer procesos para actualizar periódicamente las dependencias y parchear vulnerabilidades conocidas."

' Agregar una diapositiva para pruebas de seguridad automatizadas
Set objSlide = objPresentation.Slides.Add(7, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Pruebas de Seguridad Automatizadas"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- Integración en CI/CD: Incorporar pruebas de seguridad en las canalizaciones de integración y entrega continua para detectar y corregir vulnerabilidades de manera temprana."

' Agregar una diapositiva para seguridad en aplicaciones y redes
Set objSlide = objPresentation.Slides.Add(8, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Seguridad en Aplicaciones y Redes"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- Autenticación y Tráfico Seguro:" & vbCrLf & "  - Autenticación Obligatoria: Implementar autenticación en todas las aplicaciones para proteger la información y evitar accesos no autorizados." & vbCrLf & "  - Forzar HTTPS: Todo el tráfico debe ser forzado a HTTPS para garantizar la seguridad de las comunicaciones."

' Agregar una diapositiva para configuración de aplicaciones web
Set objSlide = objPresentation.Slides.Add(9, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Configuración de Aplicaciones Web"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- TLS y Certificados: Configurar la versión más reciente de TLS y habilitar certificados de cliente en aplicaciones web para asegurar las conexiones." & vbCrLf & "- Almacenamiento Seguro: Utilizar Azure Key Vault para almacenar variables sensibles, evitando que se expongan en configuraciones de la aplicación."

' Agregar una diapositiva para gestión de identidades y accesos (IAM)
Set objSlide = objPresentation.Slides.Add(10, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Gestión de Identidades y Accesos (IAM)"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- Acceso con Privilegios Mínimos:" & vbCrLf & "  - Just-In-Time (JIT) y Just-Enough-Access (JEA): Proporcionar acceso solo cuando sea necesario y con los privilegios mínimos requeridos, limitando la exposición de recursos críticos."

' Agregar una diapositiva para autenticación multifactor (MFA)
Set objSlide = objPresentation.Slides.Add(11, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Autenticación Multifactor (MFA)"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- Directrices de MFA: Habilitar MFA para todos los usuarios con privilegios administrativos y no administrativos, asegurando un acceso seguro a los recursos en la nube."

' Agregar una diapositiva para la aplicación en el negocio
Set objSlide = objPresentation.Slides.Add(12, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Aplicación en el Negocio"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Beneficios para el Negocio:" & vbCrLf & "- Protección de Datos: Al seguir estas directrices, se asegura la integridad y disponibilidad de los datos, lo cual es crucial para la continuidad del negocio." & vbCrLf & "- Eficiencia en la Gestión de Accesos: Facilita la administración de accesos, asegurando que solo los empleados necesarios tengan acceso a información crítica, lo que reduce el riesgo de fugas de información." & vbCrLf & "- Reducción de Riesgos: Implementar estas medidas reduce la probabilidad de incidentes de seguridad que podrían afectar la reputación y operaciones del negocio."

' Agregar una diapositiva para la conclusión
Set objSlide = objPresentation.Slides.Add(13, ppLayoutText)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Conclusión"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Recomendaciones:" & vbCrLf & "Para una audiencia no técnica, es importante destacar cómo estas medidas de seguridad no solo protegen la infraestructura tecnológica, sino que también salvaguardan los intereses del negocio al asegurar la continuidad operativa y proteger la información valiosa de la empresa. Este enfoque ayuda a comunicar la importancia de la seguridad en la nube de manera que resuene con los objetivos y preocupaciones del negocio."

' Guardar la presentación
objPresentation.SaveAs "C:\Users\lpuenteb\OneDrive - NTT DATA EMEAL\Documentos\FCC\Presentacion.pptx"

' Cerrar la presentación
objPresentation.Close

' Cerrar PowerPoint
objPPT.Quitls

Me falla con este mensaje:

PPTSecurity.vbs(14, 1) Microsoft PowerPoint: Slides.Add : Invalid enumeration value.

---


## Respuesta


El error "Invalid enumeration value" en el código VBA de PowerPoint generalmente indica que se está usando un valor no válido o incorrecto para uno de los parámetros esperados por una función, en este caso en la función `Slides.Add`.

El problema está en el segundo parámetro de `Slides.Add`, que especifica el diseño de la diapositiva. En tu código, estás utilizando `ppLayoutText` para definir el tipo de diapositiva, pero puede que no esté siendo reconocido correctamente.

### Posibles Soluciones:
1. **Asegúrate de que la constante `ppLayoutText` esté definida:**
   A veces, las constantes no se definen por defecto en entornos de VBA fuera de PowerPoint. En lugar de `ppLayoutText`, puedes usar su valor numérico correspondiente, que es `2`.

2. **Reemplazar `ppLayoutText` con el valor numérico**:
   El valor numérico de `ppLayoutText` es 2. Por lo tanto, cambia la línea:
   ```vb
   Set objSlide = objPresentation.Slides.Add(1, ppLayoutText)
   ```
   a:
   ```vb
   Set objSlide = objPresentation.Slides.Add(1, 2) ' Usar 2 en lugar de ppLayoutText
   ```

3. **Verificar que la versión de PowerPoint que estás usando sea compatible:**
   Si el problema persiste, podría ser útil revisar la versión de PowerPoint y las configuraciones del entorno VBA.

### Modificación de tu código:

Aquí está el código corregido:

```vb
Dim objPPT
Dim objPresentation
Dim objSlide
Dim objShape

' Crear una instancia de PowerPoint
Set objPPT = CreateObject("PowerPoint.Application")
objPPT.Visible = True

' Crear una nueva presentación
Set objPresentation = objPPT.Presentations.Add

' Agregar una diapositiva de introducción
Set objSlide = objPresentation.Slides.Add(1, 2) ' Usar 2 en lugar de ppLayoutText
objSlide.Shapes(1).TextFrame.TextRange.Text = "Introducción"
objSlide.Shapes(2).TextFrame.TextRange.Text = "El documento tiene como objetivo establecer directrices de seguridad para entornos cloud, asegurando la protección de datos, la gestión eficiente de accesos y la minimización de riesgos de seguridad. Estas directrices buscan garantizar la integridad y disponibilidad de los recursos en la nube, lo cual es esencial para la continuidad del negocio."

' Agregar una diapositiva para la gestión de la postura de seguridad en la nube (CSPM)
Set objSlide = objPresentation.Slides.Add(2, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Gestión de la Postura de Seguridad en la Nube (CSPM)"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Evaluaciones Continuas:" & vbCrLf & "- Visibilidad Detallada: Proporciona una visión completa del estado de seguridad de los activos y cargas de trabajo en la nube, permitiendo identificar áreas de mejora." & vbCrLf & "- Puntuación de Seguridad: Utiliza herramientas como CSPM para evaluar y mejorar continuamente la postura de seguridad, asegurando que los estándares corporativos se mantengan."

' Agregar una diapositiva para la automatización de políticas de seguridad
Set objSlide = objPresentation.Slides.Add(3, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Automatización de Políticas de Seguridad"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Azure Policy: Permite crear y asignar políticas que imponen reglas sobre los recursos, asegurando el cumplimiento de estándares corporativos y normativos." & vbCrLf & "Corrección Automática: Configura acciones automáticas para corregir desviaciones de las políticas establecidas, reduciendo el riesgo de errores humanos."

' Agregar una diapositiva para la integración con herramientas de terceros
Set objSlide = objPresentation.Slides.Add(4, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Integración con Herramientas de Terceros"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Soluciones CSPM Avanzadas: Considera la integración de soluciones de terceros que ofrecen capacidades avanzadas de monitoreo, análisis y remediación para complementar las herramientas nativas de Azure."

' Agregar una diapositiva para la seguridad en el desarrollo de aplicaciones (DevSecOps)
Set objSlide = objPresentation.Slides.Add(5, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Seguridad en el Desarrollo de Aplicaciones (DevSecOps)"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Integración Continua de Análisis de Seguridad:" & vbCrLf & "- Normativa de FCC: Se debe seguir la normativa para el análisis de vulnerabilidades de código, asegurando que las aplicaciones sean seguras desde el inicio."

' Agregar una diapositiva de introducción a la gestión de dependencias
Set objSlide = objPresentation.Slides.Add(6, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Gestión de Dependencias"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- Inventario de Dependencias: Mantener un registro actualizado de todas las bibliotecas y paquetes utilizados en el proyecto, lo cual es crucial para identificar y mitigar vulnerabilidades." & vbCrLf & "- Actualizaciones Regulares: Establecer procesos para actualizar periódicamente las dependencias y parchear vulnerabilidades conocidas."

' Agregar una diapositiva para pruebas de seguridad automatizadas
Set objSlide = objPresentation.Slides.Add(7, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Pruebas de Seguridad Automatizadas"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- Integración en CI/CD: Incorporar pruebas de seguridad en las canalizaciones de integración y entrega continua para detectar y corregir vulnerabilidades de manera temprana."

' Agregar una diapositiva para seguridad en aplicaciones y redes
Set objSlide = objPresentation.Slides.Add(8, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Seguridad en Aplicaciones y Redes"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- Autenticación y Tráfico Seguro:" & vbCrLf & "  - Autenticación Obligatoria: Implementar autenticación en todas las aplicaciones para proteger la información y evitar accesos no autorizados." & vbCrLf & "  - Forzar HTTPS: Todo el tráfico debe ser forzado a HTTPS para garantizar la seguridad de las comunicaciones."

' Agregar una diapositiva para configuración de aplicaciones web
Set objSlide = objPresentation.Slides.Add(9, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Configuración de Aplicaciones Web"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- TLS y Certificados: Configurar la versión más reciente de TLS y habilitar certificados de cliente en aplicaciones web para asegurar las conexiones." & vbCrLf & "- Almacenamiento Seguro: Utilizar Azure Key Vault para almacenar variables sensibles, evitando que se expongan en configuraciones de la aplicación."

' Agregar una diapositiva para gestión de identidades y accesos (IAM)
Set objSlide = objPresentation.Slides.Add(10, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Gestión de Identidades y Accesos (IAM)"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- Acceso con Privilegios Mínimos:" & vbCrLf & "  - Just-In-Time (JIT) y Just-Enough-Access (JEA): Proporcionar acceso solo cuando sea necesario y con los privilegios mínimos requeridos, limitando la exposición de recursos críticos."

' Agregar una diapositiva para autenticación multifactor (MFA)
Set objSlide = objPresentation.Slides.Add(11, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Autenticación Multifactor (MFA)"
objSlide.Shapes(2).TextFrame.TextRange.Text = "- Directrices de MFA: Habilitar MFA para todos los usuarios con privilegios administrativos y no administrativos, asegurando un acceso seguro a los recursos en la nube."

' Agregar una diapositiva para la aplicación en el negocio
Set objSlide = objPresentation.Slides.Add(12, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Aplicación en el Negocio"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Beneficios para el Negocio:" & vbCrLf & "- Protección de Datos: Al seguir estas directrices, se asegura la integridad y disponibilidad de los datos, lo cual es crucial para la continuidad del negocio." & vbCrLf & "- Eficiencia en la Gestión de Accesos: Facilita la administración de accesos, asegurando que solo los empleados necesarios tengan acceso a información crítica, lo que reduce el riesgo de fugas de información." & vbCrLf & "- Reducción de Riesgos: Implementar estas medidas reduce la probabilidad de incidentes de seguridad que podrían afectar la reputación y operaciones del negocio."

' Agregar una diapositiva para la conclusión
Set objSlide = objPresentation.Slides.Add(13, 2)
objSlide.Shapes(1).TextFrame.TextRange.Text = "Conclusión"
objSlide.Shapes(2).TextFrame.TextRange.Text = "Recomendaciones:" & vbCrLf & "Para una audiencia no técnica, es importante destacar cómo estas medidas de seguridad no solo protegen la infraestructura tecnológica, sino que también salvaguardan los intereses del negocio al asegurar la continuidad operativa y proteger la información valiosa de la empresa. Este enfoque ayuda a comunicar la importancia de la seguridad en la nube de manera que resuene con los objetivos y preocupaciones del negocio."

' Guardar la presentación
objPresentation.SaveAs "C:\Users\lpuenteb\OneDrive - NTT DATA EMEAL\Documentos\FCC\Presentacion.pptx"

' Cerrar la presentación
objPresentation.Close

' Cerrar PowerPoint
objPPT.Quit
```

Este cambio debería corregir el error de enumeración en tu código.
---


El error que mencionas:  
`PPTSecurity.vbs(14, 1) Microsoft PowerPoint: Slides.Add : Invalid enumeration value.`  
sugiere que el valor de `ppLayoutText` no está reconocido o válido en tu código.  

### Posibles Causas:
1. **Constante `ppLayoutText` no definida:**  
   En VBA/VBScript, `ppLayoutText` es una constante predefinida en PowerPoint, pero en VBScript, no está disponible por defecto. Si no está definida, PowerPoint no sabe qué tipo de diapositiva crear.
   
2. **Versión de PowerPoint incompatible:**  
   Algunas versiones de PowerPoint tienen diferencias en la numeración de los tipos de diseño de diapositivas.

### Solución:
Prueba reemplazar `ppLayoutText` con el valor numérico correspondiente. En PowerPoint, `ppLayoutText` suele corresponder al número `2`. Así que cambia esta línea:

```vb
Set objSlide = objPresentation.Slides.Add(1, ppLayoutText)
```
por:
```vb
Set objSlide = objPresentation.Slides.Add(1, 2) ' 2 = ppLayoutText
```

### Explicación:
- `Slides.Add(Index, Layout)`:  
  - `Index`: número de la diapositiva en la secuencia.
  - `Layout`: tipo de diseño de la diapositiva.  
    - `2` (equivalente a `ppLayoutText`) indica un diseño de título y contenido.

Si PowerPoint sigue sin reconocer el valor `2`, prueba `1` (`ppLayoutTitle`), `3` (`ppLayoutTextAndChart`), o revisa qué valores están disponibles en tu versión específica.

🔹 **Alternativa:**  
Si sigues teniendo problemas, intenta forzar la definición de la constante agregando al inicio del script:

```vb
Const ppLayoutText = 2
```

Prueba estos cambios y dime si sigues con el error. 🚀

---
*Generado desde conversación con 3 mensajes.*
*General*
