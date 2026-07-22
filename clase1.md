# Actividad de Clase: Analizando Agentes de IA con Hugging Face Spaces

## Objetivo

Explorar aplicaciones reales de Inteligencia Artificial en **Hugging
Face Spaces** y analizarlas desde la perspectiva de los **agentes
racionales**.

Al finalizar la actividad, los estudiantes deberán ser capaces de:

-   Identificar los componentes **PEAS** de un agente.
-   Clasificar las propiedades del entorno.
-   Proponer qué tipo de programa de agente podría implementarse detrás
    del sistema.
-   Justificar sus respuestas.

------------------------------------------------------------------------

## Instrucciones

1.  Ingresen a **https://huggingface.co/spaces**.
2.  Exploren diferentes Spaces.
3.  Seleccionen uno que les parezca interesante.
4.  Interactúen con el sistema durante algunos minutos.
5.  Completen la siguiente ficha de análisis.

------------------------------------------------------------------------

# Ficha de análisis

## 1. Nombre del Space

**Nombre:** Z Image Turbo

**Enlace:**https://huggingface.co/spaces/mrfakename/Z-Image-Turbo

------------------------------------------------------------------------

## 2. ¿Qué hace el agente?

Convierte texto en imágenes. Uno escribe una descripción, elige algunas opciones (tamaño, semilla, pasos) y el sistema genera una imagen que coincide con lo que se pidió. Es rápido porque usa una versión "turbo" del modelo.

------------------------------------------------------------------------

## 3. Análisis PEAS

  Elemento          Respuesta
  ----------------- ----------------------------------------------------
  **Performance**   Que la imagen se parezca a lo que el usuario pidió, se vea bien y se genere rápido.
  **Environment**   La página web del Space, el usuario que escribe el texto, y el modelo que corre detrás.
  **Actuators**     Muestra la imagen generada en pantalla.
  **Sensors**       El texto que escribe el usuario y las opciones que elige.

------------------------------------------------------------------------

## 4. Clasificación del entorno

Complete la siguiente tabla y justifique brevemente cada respuesta.

  Propiedad      Clasificación     Justificación
  -------------- ----------------- ---------------
  Observable     Parcial           Se ve el resultado, pero no lo que pasa dentro del modelo.
  Determinista   No                Con semilla al azar, el mismo texto puede dar imágenes distintas cada vez.
  Episódico      Sí                Cada imagen se genera sola, sin depender de las anteriores.          
  Estático       Sí                Nada cambia mientras el modelo está generando la imagen.          
  Discreto       Sí                En su mayoria las opciones son valores fijos, aunque el texto puede ser casi cualquier cosa.          
  Conocido       Sí                El modelo es público y de código abierto, así que se sabe cómo funciona en general.           

------------------------------------------------------------------------

## 5. ¿Qué tipo de programa de agente creen que es?

Agente de reflejo simple puesto que el sistema toma una entrada y produce una salida directamente, sin recordar lo que pasó antes ni aprender con el tiempo. No guarda memoria de prompts anteriores.

También se podría pensar como agente basado en objetivos, porque por dentro el modelo "intenta" lograr una imagen fiel al texto. Pero como eso pasa dentro de una caja negra que no vemos, la respuesta más simple de justificar es reflejo simple.

------------------------------------------------------------------------

# Discusión en clase

Después de las presentaciones, discutiremos preguntas como:

-   ¿Dos Spaces diferentes pueden compartir el mismo tipo de entorno?
-   ¿Es posible saber con certeza qué tipo de agente implementa un Space
    únicamente observándolo?
-   ¿Qué diferencia existe entre el comportamiento observable de un
    agente y su implementación interna?

------------------------------------------------------------------------

# Reto adicional

Encuentre un Space que pueda clasificarse como:

1.  **Totalmente observable, determinista y episódico.** Unlimited OCR: el texto de una imagen no cambia, se ve toda la entrada de una vez, y cada imagen se procesa aparte de las demás.
2.  **Parcialmente observable, estocástico y secuencial.** Small Talk: cada IA solo escucha lo que la otra dice (no su "pensamiento" interno), las respuestas varían aunque el input sea igual, y cada turno depende de los turnos anteriores.

------------------------------------------------------------------------

# Rúbrica (10 puntos)

| Criterio | Puntos |
|-----------|:------:|
| Descripción correcta del Space | 2 |
| Identificación de PEAS | 3 |
| Clasificación del entorno | 3 |
| Justificación del tipo de agente | 2 |
| **Total** | **10** |

------------------------------------------------------------------------


