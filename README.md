# Universal Media Hub

A free, self-hosted media system: organize, stream, and enjoy your movies, shows, and music on any device.

Universal Media Hub is a fork of the Jellyfin server codebase, maintained as a private build. Clients connect through the standard Jellyfin-compatible API, so existing apps keep working.

## Contact

Questions or feedback? Reach us on Telegram: [@johnconstantine570](https://t.me/johnconstantine570)

## Building

Requires .NET (see `global.json`):

```
dotnet build Jellyfin.slnx
```

## Sync

`.github/workflows/sync.yml` pulls upstream changes from the Jellyfin project daily, re-applies the Universal Media Hub branding via `scripts/migrate.py`, and pushes.
