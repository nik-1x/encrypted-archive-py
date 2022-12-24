from pt2.FileManager import File
from pt2.ContainerManager import Container
from pt2.HashManager import Hash

match(input('Action: ')):
    case 'compile':
        File(input("Enter path to output file: ")).write_bytes(Hash(input("Enter password: ")).encrypt(Container.compiler(input("Enter path to folder: ")).data))
    case 'decompile':
        Container.decompiler(Hash(input("Enter password: ")).decrypt(File(input("Enter path to file: ")).read_bytes()))