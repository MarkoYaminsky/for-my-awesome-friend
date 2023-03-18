def get_parts_of_file(file_name: str):
    with open(f'instructions/{file_name}.hints') as file:
        return map(lambda x: '\n' + x, file.read().split('\n\n\n'))
