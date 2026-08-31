from pathlib import Path

class DataBase:
    def __init__(self,path:str):
        self.path = Path(path)

        if not self.path.exists():
            self.path.mkdir(parents=True,exist_ok=True)
    