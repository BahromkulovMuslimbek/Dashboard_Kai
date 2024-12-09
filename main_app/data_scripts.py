from . import models


def create_datas():
    staff_1 = models.Staff.objects.create(
        first_name='Ali',
        last_name='Azamatov',
        phone='998907772233',
        age=30,
        address='Tokyo')
    staff_2 = models.Staff.objects.create(
        first_name='Alex',
        last_name='Davlatov',
        phone='998903337711',
        age=25,
        address='Sidney')
    staff_3 = models.Staff.objects.create(
        first_name='Maria',
        last_name='Rahimov',
        phone='998906661122',
        age=28,
        address='Moscow')
    staff_4 = models.Staff.objects.create(
        first_name='John',
        last_name='Dadajonov',
        phone='998337772233',
        age=19,
        address='Paris')
    staff_5 = models.Staff.objects.create(
        first_name='Lucy',
        last_name='Ibragimov',
        phone='998911112233',
        age=32,
        address='Rome')

    print(f"Created: {staff_1}, {staff_2}, {staff_3}, {staff_4, {staff_5}}")
