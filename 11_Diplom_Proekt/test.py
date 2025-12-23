import requests

BASE_URL = "https://84a8ce50-3ba4-4cbe-91d6-99c8223fa5fa.serverhub.praktikum-services.ru"

r = requests.post(f"{BASE_URL}/api/v1/orders", json={"firstName":"Тест","lastName":"Тестов","address":"ул. Тест","metroStation":4,"phone":"+79990000000","rentTime":1,"deliveryDate":"2024-12-31","comment":"тест","color":["BLACK"]})
print(r.status_code, r.text)

if r.status_code == 201:
    track = r.json()["track"]
    print(track)
    
    r2 = requests.get(f"{BASE_URL}/api/v1/orders/track?t={track}")
    print(r2.status_code, r2.text)