def custom_write(file_name, strings):
    strings_positions = {}

    f = open(file_name, 'w', encoding='utf-8')

    line_number = 1
    for string in strings:
        position = f.tell()
        f.write(string + '\n')
        strings_positions[(line_number, position)] = string
        line_number += 1

    f.close()

    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
