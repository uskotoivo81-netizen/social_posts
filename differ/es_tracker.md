---
title: SpeedyIndex: rastreador de posiciones de Google y AI Overview
seo_title: El rastreador de posiciones de Google con SpeedyIndex
meta_description: El rastreador de posiciones de SpeedyIndex controla rankings en Google de escritorio, citas en AI Overview y paga solo por las comprobaciones que ejecutas.
keyword: rastreador de posiciones (170/KD14 (es))
tags: SEO, Artificial Intelligence, Marketing
cover: /home/claude/differ/es_tracker_cover.png
video: 8T4g4q-0knY
---

# SpeedyIndex: rastreador de posiciones de Google y AI Overview

Un rastreador de posiciones sirve para comprobar en qué puesto aparece tu sitio en los resultados de Google para cada palabra clave. SpeedyIndex Rank Tracker cumple esa función con resultados de Google de escritorio, segmentados por país o ciudad. Puedes elegir una profundidad Top-10, Top-30, Top-50 o Top-100; solo se cargan las páginas más profundas mientras tu sitio o un competidor no aparezcan, y pagas por las páginas realmente cargadas.

La configuración del proyecto se hace en la [página de seguimiento de posiciones de Google de SpeedyIndex](https://es.speedyindex.com/seguimiento-posiciones-google/). El informe incluye también datos de AI Overview: si Google muestra un resumen generado por IA para una palabra clave, verás si cita tu sitio, qué dice sobre ti y cómo cambia esa mención entre una comprobación y la siguiente. En este breve vídeo se muestra cómo conectar SpeedyIndex a Claude.
![SpeedyIndex + Claude — video](https://img.youtube.com/vi/8T4g4q-0knY/hqdefault.jpg)

## Qué mide el rastreador de posiciones

El rastreador de posiciones de SpeedyIndex analiza únicamente los resultados de escritorio de Google. Para cada proyecto eliges un país o una ciudad y una profundidad de búsqueda: Top-10, Top-30, Top-50 o Top-100. Las páginas de resultados más allá del Top-10 solo se cargan mientras tu sitio o un competidor no haya aparecido todavía; esto reduce el consumo de tokens a las páginas que realmente se consultan.

Puedes añadir hasta 10 dominios de competidores por proyecto. El informe muestra todos los sitios que llegan al Top-10 para tus palabras clave y tu posición entre ellos.

## Informe tras cada comprobación

Después de cada comprobación, el informe se organiza en cuatro bloques:

- **Resumen**: visibilidad, posición media, recuento de Top-3 y Top-10, citas en AI Overview y cambio respecto a la comprobación anterior.
- **Posiciones**: cada palabra clave con su puesto, funciones SERP, URL de posicionamiento y tendencia.
- **Competidores en SERP**: qué dominios ocupan los primeros puestos.
- **AI Overview**: si hay resumen generado por IA, si cita tu sitio y qué dice.

La visibilidad representa tu cuota de clics posibles sobre el total de palabras clave del proyecto; tiene en cuenta las posiciones y cuántas palabras clave se han encontrado.

## Historial y configuración

Puedes comparar una comprobación con la anterior: palabras clave que entran o salen del Top-10, movimiento de visibilidad y de posición media. El proyecto admite etiquetas, URL objetivo, comprobaciones manuales o programadas y exportación de resultados.

Para crear un proyecto nuevo hay tres pasos. Primero, indica el dominio y las palabras clave (una por línea, con etiquetas y URL objetivo opcionales), el país o la ciudad y la profundidad. Segundo, añade hasta 10 competidores y elige programación o comprobación manual. Tercero, lee el informe.

## Precios y tokens

No hay suscripción: pagas solo por las comprobaciones que ejecutas con tokens. El precio habitual es de 4 tokens por palabra clave con profundidad Top-10. Desde el 2 de noviembre hasta el 2 de diciembre de 2026, el precio de lanzamiento es de 2 tokens por palabra clave. Al registrarte recibes 100 tokens gratuitos, sin tarjeta. Los tokens no caducan.

El mismo saldo de tokens se utiliza en [SpeedyIndex](https://es.speedyindex.com/) para tareas de indexación de enlaces, comprobaciones de indexación (Google, Bing, Yandex) y verificación de backlinks.

## Uso desde Claude con MCP

SpeedyIndex ofrece un conector MCP para Claude. Puedes leer posiciones, tendencia de hasta 90 comprobaciones y datos de AI Overview. Crear un proyecto y añadir palabras clave es gratuito; ejecutar una comprobación consume tokens. El coste se muestra antes de lanzar la comprobación con la herramienta `rank_tracker_get_check_cost`.

El servidor remoto se encuentra en `mcp.speedyindex.com/mcp`. La conexión se hace mediante OAuth con una clave de API que no se introduce en el chat.

## FAQ

### ¿El rastreador de posiciones comprueba resultados en móvil?

No. Solo analiza los resultados de escritorio de Google. No cubre resultados móviles ni otros buscadores.

### ¿Qué profundidad de resultados puedo elegir?

Puedes elegir Top-10, Top-30, Top-50 o Top-100. Las páginas más profundas se cargan solo si tu sitio o un competidor aún no ha aparecido, y pagas por las páginas realmente cargadas.

### ¿Cómo muestra las citas de AI Overview?

Para las palabras clave donde Google muestra un AI Overview, el informe indica si cita tu sitio, qué dice sobre ti y cómo cambia esa mención entre comprobaciones.