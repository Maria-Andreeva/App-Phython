from data_create import input_user_data
import os

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\n В каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    index = 1
    if len(get_sorted_data(var)) > 0:
        index =  int(list(get_sorted_data(var).keys())[-1]) + 1

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:

            file.write( f'{index}\n'
                        f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{index};{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 Файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 Файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
def get_sorted_data(type):
    
    if type == 1:

        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()       
            particular_value = '\n'
            result = []
            temp_list = []
            sorted_list = {}
            last_index = 0
            
            for i in data:
                if i == particular_value:
                    if len(temp_list) == 5:
                        result.append(temp_list)
                        last_index = int(temp_list[0])
                        sorted_list[last_index] = temp_list
                    temp_list = []
                        
                else:
                    temp_list.append(i.replace('\n', ''))
    else:
        
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()       
            particular_value = '\n'
            result = []
            temp_list = []
            sorted_list = {}
            last_index = 0
            
            for i in data:
                if i == particular_value:
                    if len(temp_list) == 1:
                        result.append(temp_list)
                        last_index = int(str(temp_list[0]).split(';')[0])
                        sorted_list[last_index] = temp_list
                    temp_list = []
                        
                else:
                    temp_list.append(i.replace('\n', ''))
                    
    return sorted_list

def copy_data_to_file2():
    var = int(input(f'\nВведите номер данных \n'))
    
    index = int(list(get_sorted_data(2).keys())[-1]) + 1

    sorted_data = get_sorted_data(1)
    
    copy_element = sorted_data.get(var)
    
    with open('data_second_variant.csv', 'a', encoding='utf-8') as file:

            file.write(f'{index};{copy_element[1]};{copy_element[2]};{copy_element[3]};{copy_element[4]}\n\n')

def copy_data_to_file1():
    var = int(input(f'\nВведите номер данных \n'))
    
    index = int(list(get_sorted_data(1).keys())[-1]) + 1

    sorted_data = get_sorted_data(2)
    
    copy_element = sorted_data.get(var)
    
    with open('data_first_variant.csv', 'a', encoding='utf-8') as file:

            file.write( f'{index}\n'
                        f'{copy_element[0].split(';')[1]}\n'
                        f'{copy_element[0].split(';')[2]}\n'
                        f'{copy_element[0].split(';')[3]}\n'
                        f'{copy_element[0].split(';')[4]}\n\n')
    

def delete_data_from_file1():
    var = int(input(f'\nВведите номер данных \n'))
    
    sorted_data = get_sorted_data(1)

    del sorted_data[var]
    
    os.remove('data_first_variant.csv')
    
    with open('data_first_variant.csv', 'a', encoding='utf-8') as file:

            for element in sorted_data.values():
                 file.write(f'{element[0]}\n'
                            f'{element[1]}\n'
                            f'{element[2]}\n'
                            f'{element[3]}\n'
                            f'{element[4]}\n\n')
                 
def delete_data_from_file2():
    var = int(input(f'\nВведите номер данных \n'))
    
    sorted_data = get_sorted_data(2)

    del sorted_data[var]
    
    os.remove('data_second_variant.csv')

    with open('data_second_variant.csv', 'a', encoding='utf-8') as file:

            for element in sorted_data.values():
               file.write(f'{str(element).replace('[', '').replace(']', '').replace("'", '')}\n\n')
                          
def change_data_from_file1():
    var = int(input(f'\nВведите номер данных \n'))
    
    name, surname, phone, adress = input_user_data()
    
    sorted_data = get_sorted_data(1)
    
    element = sorted_data[var]
    
    if name != "":
       element[1] = name
       
    if surname != "":
        element[2] = surname
    
    if phone != "":
        element[3] = phone
        
    if adress != "":
        element[4] = adress
    
    os.remove('data_first_variant.csv')
    
    with open('data_first_variant.csv', 'a', encoding='utf-8') as file:

           for element in sorted_data.values():
                 file.write(f'{element[0]}\n'
                            f'{element[1]}\n'
                            f'{element[2]}\n'
                            f'{element[3]}\n'
                            f'{element[4]}\n\n')
    
def change_data_from_file2():
    var = int(input(f'\nВведите номер данных \n'))
    
    name, surname, phone, adress = input_user_data()
    
    sorted_data = get_sorted_data(2)
    
    element = str(sorted_data[var])
    
    new_data = str(var) + ";"
    
    if name != "":
       new_data += name + ";"
    else:
       new_data += element.split(';')[1] + ";"
       
    if surname != "":
       new_data += surname + ";"
    else:
       new_data += element.split(';')[2] + ";"
    
    if phone != "":
       new_data += phone + ";"
    else:
       new_data += element.split(';')[3] + ";"
        
    if adress != "":
       new_data += adress
    else:
       new_data += element.split(';')[4]
    
    sorted_data[var] = new_data
  
    os.remove('data_second_variant.csv')
    
    with open('data_second_variant.csv', 'a', encoding='utf-8') as file:

           for element in sorted_data.values():
               file.write(f'{str(element).replace('[', '').replace(']', '').replace("'", '')}\n\n')
               
    
    
    

                          

            
           
    
 
 
   
        