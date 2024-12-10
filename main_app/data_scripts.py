from . import models


def create_datas():
    staff_data = [{'first_name': 'Steve',
                   'last_name': 'Harrison',
                   'phone': '8(959)715-55-47',
                   'age': 30,
                   'address': 'Tokyo'},
                  {'first_name': 'Alex',
                   'last_name': 'Enderson',
                   'phone': '426(6094)855-93-25',
                   'age': 25,
                   'address': 'Sidney'},
                  {'first_name': 'Maria',
                   'last_name': 'Johnson',
                   'phone': '10(606)220-76-74',
                   'age': 28,
                   'address': 'Moscow'},
                  {'first_name': 'John',
                   'last_name': 'Black',
                   'phone': '71(23)637-89-87',
                   'age': 19,
                   'address': 'Paris'},
                  {'first_name': 'Lucy',
                   'last_name': 'Adamson',
                   'phone': '42(39)260-85-26',
                   'age': 41,
                   'address': 'Rome'},
                  ]

    staff_objects = [
        models.Staff.objects.create(
            **data) for data in staff_data]
