from faker import Faker

fake = Faker('ru_RU')

def generate_order_data(color=None):
    """Генерация данных заказа"""
    data = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.random_int(min=1, max=10),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=10),
        "deliveryDate": fake.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d'),
        "comment": fake.text(max_nb_chars=50),
        "color": color or []
    }
    return data