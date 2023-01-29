def get_type():
    type = int(input("1 - записать контакт / 2 - показать контакты: "))
    return type


def get_contact():
    id = input("Введите id работника: ")
    first_name = input("Введите имя работника: ")
    last_name = input("Введите фамилию работника: ")
    tel = input("Введите номер телефон работника: ")
    comment = input("Введите комментарии: ")
    return (f" {id} {first_name} {last_name} {tel} {comment}")


def get_view():
    out = int(input(
        "Как вы хотите вывести данные: "
        "1-Отсортировать по id / 2-Отсортировать по имени / 3-показать только имя и фамилию / 4 - показать весь список "))
    return out
