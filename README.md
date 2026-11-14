# Universal Media Hub

A free, self-hosted media system: organize, stream, and enjoy your movies, shows, and music on any device.

## Contact

Questions or feedback? Reach us on Telegram: [@johnconstantine570](https://t.me/johnconstantine570)

## Building

Requires .NET (see `global.json`):

```
dotnet build Jellyfin.slnx
```

## Sync

`.github/workflows/sync.yml` pulls upstream changes daily, re-applies the Universal Media Hub branding via `scripts/migrate.py`, and pushes.
