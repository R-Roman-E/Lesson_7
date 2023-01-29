import view
import input_data
import output_data


def buttom():
    type = view.get_type()
    if type == 1:
        contact = view.get_contact()
        input_data.input_contact(contact)
    elif type == 2:
        out = view.get_view()
        if out == 1:
            print(output_data.sort_id())
        elif out == 2:
            print(output_data.sort_first_name())
        elif out == 3:
            print(output_data.out_first_name_last_name())
        elif out == 4:
            print(output_data.out_contact)
        else:
            print(output_data.out_contact)
