from pathlib import Path

from .storage import Storage


class Database:
    def __init__(self, path: str):
        self.path = Path(path)

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.storage = Storage(path)

    def close(self):
        self.storage.close()