import requests

BASE_URL = "https://f8e40f7b-2cd9-43ac-976b-8241fa016f9a.serverhub.praktikum-services.ru/"
data = {
    "firstName": "Тест",
    "lastName": "Тестов",
    "address": "ул. Тест, 1",
    "metroStation": 4,
    "phone": "+79990000000",
    "rentTime": 1,
    "deliveryDate": "2024-12-31",
    "comment": "тест",
    "color": ["BLACK"]
}

def test():
    r = requests.post(f"{BASE_URL}/api/v1/orders", json=data)
    print("Статус:", r.status_code)
    print("Текст ответа:", r.text[:200])
    
    if r.status_code == 201:
        track = r.json()["track"]
        r2 = requests.get(f"{BASE_URL}/api/v1/orders/track?t={track}")
        print("Статус получения:", r2.status_code)
        if r2.status_code == 200:
            print("Успех")
    else:
        print("Ошибка создания")

if __name__ == "__main__":
    test()