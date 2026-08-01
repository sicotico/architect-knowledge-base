---
title: API Key ScreenScraper
date: 2026-05-08
category: Programación
slug: api-key-screenscraper
tags: ['Programación']
---

# API Key ScreenScraper


> **Pregunta original:**
> 
no encuentro la APi Key en SCREEN SCRAPER
> es necesari aun api key para este servicio dentro de la app de RomM ?

---


## Respuesta


No. Para integrar [RomM](https://romm.app) con [ScreenScraper](https://www.screenscraper.fr), normalmente **no necesitas API key**.

RomM usa:

- usuario de ScreenScraper
- contraseña de ScreenScraper

Variables típicas:

```env
SCREENSCRAPER_USER=tu_usuario
SCREENSCRAPER_PASSWORD=tu_password
```

No existe una “API key pública” visible en el panel estándar de ScreenScraper para este uso.

## Lo bueno
- configuración simple
- compatibilidad directa con RomM
- evita gestionar tokens OAuth/API

## Lo malo
- ScreenScraper tiene límites de rate limit bastante agresivos
- si muchos usuarios usan scraping masivo, puede ralentizarse
- la disponibilidad del servicio a veces es irregular

## Error frecuente en RomM

Mucha gente confunde:

- IGDB → sí requiere credenciales API/Twitch
- SteamGridDB → API key
- ScreenScraper → usuario/contraseña

Son sistemas distintos.

## Qué revisar en RomM

En tu `.env` o docker compose:

```env
SCREENSCRAPER_USER=
SCREENSCRAPER_PASSWORD=
```

y nada más relacionado con API key.

Si quieres, puedo ayudarte a verificar:
- variables exactas de RomM
- docker compose
- conexión ScreenScraper
- errores de scraping/logs
- configuración recomendada para evitar rate limits.
---


En urlScreenScraperhttps://www.screenscraper.fr normalmente **no necesitas una API Key** como tal.  
La mayoría de scrapers (Batocera, EmulationStation, Skyscraper, RetroBat, RomM, etc.) usan:

- usuario
- contraseña

directamente de tu cuenta de ScreenScraper. citeturn0search1turn0search8

## Dónde se suele configurar

### Batocera / EmulationStation
Solo introduces:

- `ScreenScraperUser`
- `ScreenScraperPass`

No hay API key visible en la web. citeturn0search8

### RomM
Igual:

- `SCREENSCRAPER_USER`
- `SCREENSCRAPER_PASSWORD`

citeturn0search1

### Skyscraper
Se configura así:

```ini
[screenscraper]
userCreds="usuario:password"
```

citeturn0search3

---

## Entonces, ¿por qué algunos hablan de “API key”?

Hay dos casos:

1. **Confusión con IGDB o TheGamesDB**
   - esos sí usan Client ID / Secret / API Key

2. **Developer key privada**
   - ScreenScraper puede dar claves especiales para desarrolladores
   - no aparecen automáticamente en la cuenta
   - normalmente se solicitan en foros/Discord citeturn0search4

---

## Conclusión

Si estás configurando:

- Batocera
- RetroBat
- EmulationStation
- RomM
- Skyscraper

lo normal es que SOLO necesites:

```text
usuario ScreenScraper
contraseña ScreenScraper
```

y no una API key.

Si me dices exactamente qué programa estás intentando conectar con ScreenScraper, te digo el campo correcto y dónde ponerlo.

---
*Generado desde conversación con 4 mensajes.*
*Programación*
