import importlib
from collections import defaultdict
from pathlib import Path
from typing import Any

from discord.ext import commands


class Loader:
    """
    Cargador dinámico de módulos (Comandos, Eventos y Tareas) para el cliente.
    """

    def __init__(self, client: commands.Bot) -> None:
        """
        Inicializa el cargador dinámico usando la instancia del cliente.
        :param client: Instancia principal del cliente
        :type client: commands.Bot
        """
        self.client: commands.Bot = client

    async def load_cogs(self) -> None:
        """
        Escanea e importa de forma dinámica los módulos de la aplicación.

        Recorre las carpetas 'commands', 'events', 'tasks', construye la ruta
        e importa las clases 'commands.Cog' que encuentre.
        :return: None
        """
        base_path = Path(__file__).parent.parent
        categories = defaultdict[Any, dict[str, Any]] (
            lambda: {"total": 0, "loaded": 0, "failed": []}
        )

        for cog_type in ("commands", "events", "tasks"):
            cog_path = base_path / "app" / cog_type

            for file in cog_path.rglob("*.py"):
                if file.name == "__init__.py":
                    continue

                category = file.parent.name
                key = (cog_type, category)
                categories[key]["total"] += 1

                module_path = ".".join(
                    file.relative_to(base_path.parent)
                    .with_suffix("")
                    .parts
                )

                try:
                    module = importlib.import_module(module_path)

                    for attribute in vars(module).values():
                        if not isinstance(attribute, type):
                            continue

                        if not issubclass(attribute, commands.Cog):
                            continue

                        if attribute is commands.Cog:
                            continue

                        if attribute.__module__ != module.__name__:
                            continue

                        await self.client.add_cog(attribute(self.client))
                        categories[key]["loaded"] += 1

                except (ImportError, AttributeError, TypeError) as error:
                    categories[key]["failed"].append((file.name, error))

        self._summary(categories)

    @staticmethod
    def _summary(categories: dict) -> None:
        """
        Muestra el resultado detallado de la carga de módulos.
        :param categories: Diccionario de modulos, dividido por categorías
        :return: None
        """
        for (cog_type, category), data in categories.items():
            if data["failed"]:
                for filename, error in data["failed"]:
                    print(f'{category} | {filename} | {type(error).__name__}: {error}')
                continue
            print(f'{cog_type} | {category} | Modules loaded {data["loaded"]}.')
