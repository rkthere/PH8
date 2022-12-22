from func import timetable, list_less, list_less_task, load_less, check_less, progress

user = input('Введите вашу роль Учитель/Ученик ')

while user == 'Ученик':
    print('====================================='
          'Доступные функции\n'
          '1 - Просмотр рассписания\n'
          '2 - Просмотр списка предметов\n'
          '3 - Просмотр задания по предметам\n'
          '4 - Загрузить выполненное задание\n'
          '5 - Общее состояние учебы\n'
          '0 - Выход'
          '=====================================')
    func = int(input('Введите номер функции '))
    if func == 1:
        print(timetable('рассписание.txt'))
    elif func == 2:
        print(list_less('cписок_предметов_дз.txt'))
    elif func == 3:
        print(list_less_task('cписок_предметов_дз.txt'))
    elif func == 4:
        print(load_less('cписок_предметов_дз.txt'))
    elif func == 5:
        print(progress('cписок_предметов_дз.txt'))
    elif func == 0:
        break
while user == 'Учитель':
    print('====================================='
          'Доступные функции\n'
          '1 - Просмотр рассписания\n'
          '2 - Просмотр списка предметов\n'
          '3 - Просмотр задания по предметам\n'
          '4 - Оценить задание\n'
          '5 - Общее состояние учебы\n'
          '0 - Выход'
          '=====================================')
    func = int(input('Введите номер функции '))
    if func == 1:
        print(timetable('рассписание.txt'))
    elif func == 2:
        print(list_less('cписок_предметов_дз.txt'))
    elif func == 3:
        print(list_less_task('cписок_предметов_дз.txt'))
    elif func == 4:
        print(check_less('cписок_предметов_дз.txt'))
    elif func == 5:
        print(progress('cписок_предметов_дз.txt'))
    elif func == 0:
        break
