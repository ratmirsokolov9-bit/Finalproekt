import requests

BASE_URL = "https://75e400af-eab2-4f7a-84c5-2ed036230b08.serverhub.praktikum-services.ru/"

def create_order(data):
    return requests.post(f"{BASE_URL}/api/v1/orders", json=data)

def get_order_by_track(track):
    return requests.get(f"{BASE_URL}/api/v1/orders/track?t={track}")

def update_order(order_id, data):
    return requests.put(f"{BASE_URL}/api/v1/orders/{order_id}", json=data)

def delete_order(order_id):
    return requests.delete(f"{BASE_URL}/api/v1/orders/{order_id}")

def get_all_orders():

    return requests.get(f"{BASE_URL}/api/v1/orders")
