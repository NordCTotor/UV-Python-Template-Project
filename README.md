# UV Python Template Project

Template de projet Python basé sur [uv](https://docs.astral.sh/uv/), avec une structure `src` layout,
configuration de logging pilotée par YAML et gestion des variables d'environnement.

## Structure

```
.
├── pyproject.toml        # Métadonnées, dépendances et outillage (PEP 621)
├── src/application/     # Code source (src layout)
│   ├── __main__.py      # Point d'entrée (`runapp`)
│   └── utils/
│       ├── logs_manager/       # Configuration du logging (YAML → dictConfig)
│       │   └── logging_conf_files/
│       └── system_info/        # Gestion du .env et des informations système
└── tests/               # Tests pytest
```

## Prérequis

- Python ≥ 3.13
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Démarrage

```bash
uv sync --all-groups        # Installer toutes les dépendances (dev + test)
uv run runapp               # Lancer l'application
```

Un fichier `.env` optionnel à la racine permet de définir des variables d’environnement locales (secrets, URLs, flags). Il est **en lecture seule** pour l’application : `load_dotenv` le charge s’il existe, sans jamais le modifier.

Les informations système et les chemins ne sont plus stockés dans `.env` : l’application construit un **contexte global** typé et immuable (`src/application/context.py`) contenant :

- `project_root` : racine du projet
- `system` / `node` : informations système capturées au runtime
- `log_file` : chemin du fichier de log

Accès : `init_context()` au démarrage, `get_context()` ensuite.

## Outillage

```bash
uv run ruff check .        # Lint
uv run pytest              # Tests
uv build                   # Construire le paquet
```

## Logging

La configuration est divisée en trois fichiers YAML dans
`src/application/utils/logs_manager/logging_conf_files/` :

- `formatters.yaml` : formats des messages
- `handlers.yaml` : handlers (console + fichier rotatif à minuit, 7 backups)
- `loggers.yaml` : loggers et niveaux

Les logs sont écrits dans `Logs/application.log` (créé automatiquement).

## Licence

MIT
