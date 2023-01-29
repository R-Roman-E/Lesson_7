def input_contact(contact):
    with open("PhoneBook.txt", "a") as file:
        file.write(f"{contact}\n")
