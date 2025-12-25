import requests

BASE_URL = "https://f4d80519-59eb-44cc-b9cd-74758965ee0c.serverhub.praktikum-services.ru/"
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
    assert r.status_code == 201, f"Создание: ожидался 201, получен {r.status_code}"
    
    track = r.json()["track"]
    assert track is not None, "Трек-номер отсутствует"
    
    r2 = requests.get(f"{BASE_URL}/api/v1/orders/track?t={track}")
    assert r2.status_code == 200, f"Получение: ожидался 200, получен {r2.status_code}"
    
    print("Тест пройден")

if __name__ == "__main__":
    test()