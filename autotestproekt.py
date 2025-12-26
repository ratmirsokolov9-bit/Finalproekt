from test_data import generate_order_data
from queries import create_order, get_order_by_track

def test_create_order():
    data = generate_order_data()
    response = create_order(data)
    assert response.status_code == 201
    assert "track" in response.json()

def test_get_order_by_track():
    data = generate_order_data()
    create_response = create_order(data)
    track = create_response.json()["track"]
    
    get_response = get_order_by_track(track)
    assert get_response.status_code == 200
    assert get_response.json()["order"]["track"] == track

if __name__ == "__main__":
    test_create_order()
    test_get_order_by_track()