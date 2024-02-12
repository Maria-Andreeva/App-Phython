from logger import input_data, print_data, copy_data_to_file2, copy_data_to_file1, delete_data_from_file1, delete_data_from_file2, change_data_from_file1, change_data_from_file2


def interface():
    print('Добрый день! Это бот-поиощник.\n'
          'Что вы хотите сделать? \n'
          '1 - Ввести данные \n'
          '2 - Записать данные \n' 
          '3 - Копировать данные из файла first_variant в second_variant \n'
          '4 - Копировать данные из файла second_variant в first_variant \n'
          '5 - Удалить данные из файла first_variant \n'
          '6 - Удалить данные из файла second_variant \n'
          '7 - Изменить данные в файле first_variant \n'
          '8 - Изменить данные в файле second_variant')
    
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 8:
        command = int(input('Ошибка! Ваш выбор: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        copy_data_to_file2()
    elif command == 4:
        copy_data_to_file1()
    elif command == 5:
        delete_data_from_file1()
    elif command == 6:
        delete_data_from_file2()
    elif command == 7:
        change_data_from_file1()
    elif command == 8:
        change_data_from_file2()
        
interface()