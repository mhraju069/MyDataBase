from pathlib import Path

class Storage:
    def __init__(self, path: str):
        self.path = Path(path)

    def write(self, filename: str, data: bytes):

        file_path = self.path / filename
        
        with open(file_path, "wb") as file:
            file.write(data)

    def read(self, filename: str) -> bytes :
        
        file_path = self.path / filename
        
        with open(file_path, "rb") as file:
            return file.read()
