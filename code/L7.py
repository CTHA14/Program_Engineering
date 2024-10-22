import os

def print_docs(directory):
    all_files=os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы {", ".join([files for files in catalog[2]])}')
    print('-'*48)

print_docs('/SuperPK/code/__pycache__')