#!/usr/bin/env python3
"""Re-apply the Universal Media Hub rebrand after each upstream sync."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REPL = [
    ('https://github.com/jellyfin/jellyfin','https://github.com/yashhasan570/UniversalMediaHub'),
    ('github.com/jellyfin/jellyfin','github.com/yashhasan570/UniversalMediaHub'),
    ('opencollective.com/jellyfin','github.com/yashhasan570/UniversalMediaHub'),
    ('[assembly: AssemblyProduct("Jellyfin Server")]','[assembly: AssemblyProduct("Universal Media Hub Server")]'),
]
EXTS = {'.cs','.csproj','.json','.md','.yml','.yaml','.txt','.props','.targets','.slnx','.sh','.py','.js','.html'}
SKIP = {'.git','node_modules','scripts'}

def main():
    wf = ROOT/'.github'/'workflows'
    for p in wf.glob('*.y*ml'):
        if p.name != 'sync.yml':
            p.unlink()
    changed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for fn in filenames:
            if fn == 'sync.yml': continue
            p = Path(dirpath)/fn
            if p.suffix.lower() not in EXTS: continue
            try: s = p.read_text(encoding='utf-8')
            except Exception: continue
            o = s
            for a,b in REPL: s = s.replace(a,b)
            if s != o:
                p.write_text(s, encoding='utf-8'); changed += 1
    print(f'migrate: {changed} files updated')

if __name__ == '__main__':
    main()
