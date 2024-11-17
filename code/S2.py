def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip() 
            if not content:
                raise ValueError("Файл пустой")
            print(content)
    except ValueError as ve:
        print(ve)
    except FileNotFoundError:
        print("Файл не найден.")
read_file("file2.txt")
read_file("file1.txt")