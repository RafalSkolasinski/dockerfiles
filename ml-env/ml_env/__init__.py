try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata


try:
    # This will read version from pyproject.toml
    __version__ = importlib_metadata.version(__name__)
except Exception:
    __version__ = "unknown"


def example():
    import sys

    print(f"Python executable: {sys.executable}")
    print(f"Code version: {__version__}")
