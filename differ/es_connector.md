---
title: Cómo configurar el conector MCP de SpeedyIndex en Claude
seo_title: Conector MCP de SpeedyIndex para Claude
meta_description: Aprende a configurar el conector MCP de SpeedyIndex en Claude: URL del servidor, clave API, herramientas de indexación y comprobación de Google.
keyword: conector mcp (20/KD0 (es))
tags: SEO, Artificial Intelligence, Marketing
cover: /home/claude/differ/es_connector_cover.png
video: 8T4g4q-0knY
---

# Cómo configurar el conector MCP de SpeedyIndex en Claude

El conector MCP de SpeedyIndex permite que Claude acceda a tu cuenta de SpeedyIndex mediante Model Context Protocol (MCP). Para conectarlo, añade la URL `mcp.speedyindex.com/mcp` como conector personalizado en `claude.ai/plugins` y pega la clave API en la página de acceso de SpeedyIndex; la clave no se escribe en el chat. Una vez conectado, Claude puede consultar saldo, listar tareas, obtener informes, lanzar tareas de indexación y comprobar posiciones.

Claude pide aprobación antes de cada llamada a herramienta; las 7 herramientas que modifican la cuenta (incluidas las 5 que gastan tokens) siempre preguntan salvo que las marques como «Permitir siempre». Un vídeo breve muestra la conexión en Claude web y de escritorio.
![SpeedyIndex + Claude — video](https://img.youtube.com/vi/8T4g4q-0knY/hqdefault.jpg)

## Conexión en Claude

En Claude web y de escritorio, abre Plugins (`claude.ai/plugins`), elige Añadir conector personalizado, ponle el nombre «SpeedyIndex» y la URL `mcp.speedyindex.com/mcp`. Después de pulsar Continuar y Conectar, pega la clave API en la página de acceso de SpeedyIndex. Luego activa SpeedyIndex en el chat con el botón «+» → Conectores. Para comprobar que funciona, pregunta «¿Cuál es mi saldo de SpeedyIndex?». Los pasos completos para cada cliente están en la [guía de configuración del conector MCP de SpeedyIndex](https://es.speedyindex.com/mcp/). En Claude Code, ejecuta `claude mcp add` y luego `/mcp` → speedyindex → Authenticate. Cursor usa el archivo `.cursor/mcp.json` o `~/.cursor/mcp.json` con la URL del servidor; VS Code permite añadirlo con el comando «MCP: Add Server» (HTTP) o con `.mcp.json` del espacio de trabajo. En planes Team y Enterprise, un propietario añade el conector en Ajustes de organización → Conectores y cada miembro lo conecta individualmente. Los conectores personalizados funcionan en todos los planes de Claude; el plan Free permite un conector personalizado.

```bash
claude mcp add --transport http --scope user speedyindex https://mcp.speedyindex.com/mcp
```

## Herramientas del conector

Las 22 herramientas del servidor remoto se dividen en 15 de solo lectura (gratuitas) y 7 que modifican la cuenta; de estas últimas, 5 gastan tokens. Las más relevantes para SEO:

- Indexación: Google y Yandex, hasta 10.000 URL por tarea; las tareas de Google son de pago por indexada, con devolución automática de tokens para URL no indexadas y un goteo de 2 a 30 días.
- Comprobación de índice: Google, Yandex y Bing, hasta 10.000 URL por tarea; devuelve listas de indexadas y no indexadas.
- Comprobador de backlinks: verifica que las páginas donantes que indiques sigan enlazando a tus dominios; muestra estado HTTP, ancla, nofollow, Domain Authority de Moz y spam score; hasta 50 dominios objetivo.
- Seguimiento de posiciones: Google escritorio, hasta 5 regiones y 10 competidores, historial de tendencia y si AI Overview cita tu sitio.
- Herramientas gratuitas de solo lectura: saldo, listas de tareas, estado e informes de tareas, posiciones y tendencias.

Las 5 herramientas que gastan tokens (crear tarea de indexación, enviar URL única, crear tarea de comprobación de índice, crear tarea de comprobación de backlinks y lanzar comprobación de seguimiento de posiciones) piden confirmación salvo que las marques como «Permitir siempre». Crear un proyecto de seguimiento de posiciones y añadir palabras clave es gratuito; lanzar una comprobación no lo es y el coste se muestra antes con rank_tracker_get_check_cost. Para comprobar si tus páginas están en el índice de Google, el [comprobador masivo de índice de Google](https://es.speedyindex.com/comprobador-indice-google/) permite subir hasta 10.000 URL por tarea.

## Seguridad y tokens

El conector no almacena la clave API en una base de datos; la clave se guarda solo dentro de un token cifrado. El token de acceso dura 1 hora y el inicio de sesión se renueva hasta 90 días; si cambias la clave en tu cuenta, se revocan todos los inicios de sesión. El conector no realiza pagos, no crea facturas y no elimina proyectos ni tareas. El conector en sí es gratuito; las tareas se pagan con tokens de SpeedyIndex y no requieren suscripción. Las cuentas nuevas reciben 100 tokens gratuitos.

## FAQ

### ¿Qué es el conector MCP de SpeedyIndex?

Es un servidor MCP remoto que permite a Claude usar las herramientas de SpeedyIndex. La URL del servidor es `mcp.speedyindex.com/mcp`.

### ¿Cuánto cuesta usar el conector MCP de SpeedyIndex?

El conector es gratuito. Las tareas se pagan con tokens de SpeedyIndex, sin suscripción. Las cuentas nuevas reciben 100 tokens gratuitos.

### ¿En qué clientes funciona el conector MCP de SpeedyIndex?

Funciona en Claude web y de escritorio, Claude Code, Cursor y VS Code. También hay una opción local con el paquete npm `speedyindex-mcp` para Node.js 18+.