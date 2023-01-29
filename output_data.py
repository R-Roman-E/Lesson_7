def out_contact():
    with open("PhoneBook.txt", "r") as file:
        array = []
        for i in file.read().splitlines():
            array.append(i)
        return array


def sort_id():
    array = out_contact()
    return list(sorted(array, key=lambda x: x[3]))


def sort_first_name():
    array = out_contact()
    return list(sorted(array, key=lambda x: x[5]))

    
def out_first_name_last_name():
    array = []
    for i in out_contact():
        a = i.split(" ")
        array.append(f"{a[2]}-{a[3]}")
    return array

