# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной


# 1. Создание файла. ++++
# ---------------------------
# 2. Добавление новой записи. ++++
#   * забрать ввод пользователя
#   * открытие файла на дозапись
#   * записать в файл
# ------------------------------
# 3 Вывод на экран ++++
# * открыть файл на чтение
#   * считывание данных
#   * вывод на экран
# ------------------------------
# 4 Поиск контакта
#   * выбрать вариант поиска
#   * забрать ввод пользователя
#   * открытие файла на чтение
#   * считать данные
#   * осуществить поиск
#   * вывести результат поиска
# ------------------------------
# 5 Создание интерфейса ++++


def name_input():
    return input('Введите имя: ').title()


def surname_input():
    return input('Введите фамилию: ').title()


def patronymic_input():
    return input('Введите отчество: ').title()


def phone_input():
    return input('Введите номер: ')


def address_input():
    return input('Введите адрес: ').title()


def create_contact():
    '''Add an entry'''
    surname = surname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    address = address_input()

    return f'{surname} {name} {patronymic} {phone} {address}\n\n'


def write_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
        print('\nКонтакт записан!\n')


def print_contacts():
    '''List all entries'''
    # with open('phonebook.txt', 'r', encoding='utf-8') as file:
    #     print('-----------------------')
    #     print(file.read())
    #     print('-----------------------')

    # 2
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for nn, contact in enumerate(contacts_list, 1):
            print(f'{nn}. {contact}\n')


def search_contact(field=''):
    ''''''
    print(
        'Возможные варианты поиска:\n'
        '1. по фамилии\n'
        '2. по имени\n'
        '3. по отчеству\n'
        '4. по номеру\n'
        '5. по городу\n'
    )

    index_var = int(input('Введите вариант поиска: '))-1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    # print([data_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    # print(contacts_list)

    for contact_str in contacts_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'\n{contact_str}\n')

def copy_contact():
  
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for nn, contact in enumerate(contacts_list, 1):
            print(f'{nn}. {contact}\n')
    line_number = int(input('Введите номер строки: '))
        
    if line_number < 1 or line_number > len(contacts_list):
        print('Некорректный номер строки')
        return
    
    with open('simbook.txt', 'a') as file:
        file.write((contacts_list[line_number - 1]) + '\n')
    print('Копирование выполнено!\n')
    
def update_contact():
    
    with open('simbook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read()
    print(contacts_list)
    print('')
    index_delete_file = int(input('Введите номер строки для редактирования: ')) - 1
    contacts_list_lines = contacts_list.split('\n')
    edit_contacts_list_lines = contacts_list_lines[index_delete_file]
    elements = edit_contacts_list_lines.split(' ')
    surname = input('Введите фамилию: ').title()
    name = input('Введите имя: ').title()
    patronymic = input('Введите отчество: ').title()
    phone = input('Введите номер: ')
    address = input('Введите адрес: ').title()
    if len(surname) == 0:
        surname = elements[0]
    if len(name) == 0:
        name = elements[1]
    if len(patronymic) == 0:
        patronymic = elements[2]
    if len(phone) == 0:
        phone = elements[3]
    if len(address) == 0:
        address = elements[4]
    edited_line = f'{surname} {name} {patronymic} {phone} {address}\n\n'
    contacts_list_lines[index_delete_file] = edited_line
    print(f'Запись — {edit_contacts_list_lines}, изменена на — {edited_line}\n')
    
    with open('simbook.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(contacts_list_lines))

def interface():
    with open('phonebook.txt', 'a'):
        pass

    user_input = None
    while user_input != '7':
        print(
            'Возможные варианты действия:\n'
            '1. Добавить контакт\n'
            '2. Вывод списка контактов\n'
            '3. Поиск контакта\n'
            '4. Копировать контакт\n'
            '5. Удаление контакта\n'
            '6. Изменение контакта\n'
            '7. Выход из программы\n'
        )

        user_input = input('Введите вариант: ')

        while user_input not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Некорректный ввод.')
            user_input = input('Введите вариант: ')

        print()

        match user_input:
            case '1':
                write_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_contact()
            case '5':
                del_contact()
            case '6':
                update_contact()


if __name__ == '__main__':
    interface()