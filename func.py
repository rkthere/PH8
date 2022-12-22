def timetable(file):
    """
    показать рассписание
    """
    with open(file, "r") as f:
        text = f.read()
        return text


def list_less(file):
    """
    Показать список предметов
    """
    with open(file, "r") as f:
        text = f.readlines()
        return '\n'.join([i.split()[0] for i in text[1:]])


def list_less_task(file):
    """
    Показать список предметов и домашнее задние
    """
    with open(file, "r") as f:
        text = f.readlines()
        return '\n'.join([i.split('  ')[0].strip() + ' ' + i.split('  ')[1].strip() for i in text[1:]])


def progress(file):
    """
    Оценка предмет загрузка задания
    """
    with open(file, "r") as f:
        text = f.read()
        return text


def check_less(file):
    """
    Оценить работу
    """
    less = input('Введите название предмета, который был проверен ')
    grade = input('Введите оценку ')
    num = []
    with open(file, "r") as f:
        text = f.readlines()
        for i in text:
            if less in i:
                print(i)
                num.append(i.strip() + ' ' + grade + '\n')
            else:
                num.append(i)
    with open(file, "w") as f:
        f.writelines(num)


def load_less(file):
    """
    Загрузить работу
    """
    less = input('Введите название предмета, который готов к проверке ')
    num = []
    with open(file, "r") as f:
        text = f.readlines()
        for i in text:
            if less in i:
                num.append(i.strip() + '  ' + 'Загружено' '\n')
            else:
                num.append(i)
    with open(file, "w") as f:
        f.writelines(num)
