import pathlib
from .FileManager import File
from base64 import b64encode, b64decode

class Container:

    CONTAINER_DEFAULT_SEPARATOR = str(0x4293865AE2789EEBB9501279857).encode('utf-8')
    CONTAINER_FILE_SEPARATOR = str(0x55120A258892B928682f248427289).encode('utf-8')

    class compiler:

        def __init__(self, path):

            self.data = b64encode(Container.CONTAINER_FILE_SEPARATOR.join([
                file["name"].encode('utf-8') + Container.CONTAINER_DEFAULT_SEPARATOR + file["data"] 
                for file in [{
                    "name": str(file.absolute()),
                    "data": file.read_bytes()
                } for file in [
                    file
                    for file in pathlib.Path(path).iterdir() if file.is_file()
                ]]
            ])) if pathlib.Path(path).is_dir() else None

    class decompiler:

        def __init__(self, data):

            data = b64decode(data)
            files = data.split(Container.CONTAINER_FILE_SEPARATOR)

            for file in files:
                file = file.split(Container.CONTAINER_DEFAULT_SEPARATOR)
                File(file[0].decode('utf-8')).write_bytes(file[1])

