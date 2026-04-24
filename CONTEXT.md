# CONTEXT — OmniSync_Standard

> Formato compatible con Claude y Antigravity AI  
> Última actualización: 2026-04-19  
> Ver también: [OmniSync/CONTEXT.md](file:///home/erk/OmniSync/CONTEXT.md) para contexto completo del ecosistema.

## Resumen Ejecutivo

**OmniSync_Standard** es la distribución standalone del motor de sincronización delta SHA-256 de `@erk`. Es la variante **gratuita** y es la que se integra como plugin en proyectos externos como **FReeClaude**.

- **Versión publicada**: v1.0.4
- **Repo**: `https://github.com/ErkRodCS/OmniSync_Standard`

## Skills MCP Expuestas

| Skill | Precio | Descripción |
|---|---|---|
| `sync_standard` | 0 sats (FREE) | Sincronización segura SHA-256 para agentes |

## Interrelaciones

| Proyecto | Detalle |
|---|---|
| **FReeClaude** | Montado como plugin en `/app/plugins/omnisync` via Docker volume |
| **carbonioClaw/skills/omnisync** | Copia registrada como skill del ecosistema |

## Comandos

```bash
python3 /home/erk/OmniSync_Standard/omnisync_engine.py
```
