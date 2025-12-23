import requests

BASE_URL = "https://84a8ce50-3ba4-4cbe-91d6-99c8223fa5fa.serverhub.praktikum-services.ru"

def test_create_order_and_get_by_track():
    create_order_url = f"{BASE_URL}/api/v1/orders"
    
    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "ул. Тестовая, 10",
        "metroStation": 4,
        "phone": "+79991234567",
        "rentTime": 3,
        "deliveryDate": "2024-12-31",
        "comment": "тестовый заказ",
        "color": ["BLACK"]
    }
    
    try:
        create_response = requests.post(create_order_url, json=order_data, timeout=10)
        create_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка создания заказа: {e}")
        return
    
    assert create_response.status_code == 201, f"Ожидался 201, получен {create_response.status_code}"
    
    response_json = create_response.json()
    track_number = response_json.get("track")
    assert track_number is not None, "Трек-номер отсутствует"
    
    get_order_url = f"{BASE_URL}/api/v1/orders/track?t={track_number}"
    
    try:
        get_response = requests.get(get_order_url, timeout=10)
        get_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка получения заказа: {e}")
        return
    
    assert get_response.status_code == 200, f"Ожидался 200, получен {get_response.status_code}"
    
    print("Тест пройден успешно")
    print(f"Трек-номер: {track_number}")

if __name__ == "__main__":
    test_create_order_and_get_by_track()