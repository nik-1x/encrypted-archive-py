import pathlib
import json

class File:

    def __init__(self, path, on_empty = ""):
        self.path = pathlib.Path(path)

        self.path.absolute().parent.mkdir(parents=True, exist_ok=True)
        
        if not self.path.exists():
            self.path.write_text("")

    def read(self):
        with self.path.open("r") as f:
            data = f.read()
            f.close()
        return data

    def read_json(self):
        try:
            with self.path.open("r") as f:
                data = json.loads(f.read())
                f.close()
            return data
        except:
            return False

    def read_bytes(self):
        with self.path.open("rb") as f:
            data = f.read()
            f.close()
        return data

    def write(self, data):
        with self.path.open("w") as f:
            f.write(data)
            f.close()
    
    def write_json(self, data: dict):
        with self.path.open("w") as f:
            f.write(json.dumps(data, indent=4))
            f.close()

    def write_bytes(self, data):
        with self.path.open("wb") as f:
            f.write(data)
            f.close()

