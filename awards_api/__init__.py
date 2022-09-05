import pkgutil
import importlib
from pathlib import Path

importlib.find_loader("*.models")


def load_models():
    """Load all models from this folder."""
    package_dir = Path(__file__).resolve().parent.parent.joinpath("awards_api", "api")
    modules = pkgutil.walk_packages(
        path=[str(package_dir)],
        prefix="awards_api.api.",
    )
    for module in modules:
        if module.name.split(".")[-1] == "models":
            __import__(module.name)
