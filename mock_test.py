import requests

BASE_URL = "https://68db5b3323ebc87faa32b209.mockapi.io/api/v1/users"

def test_create_user():
    response = requests.post(f"{BASE_URL}", json={'name': 'Naruapon'})
    assert response.status_code == 201
    response_data = response.json()
    assert 'id' in response_data
    assert response_data['id'] == '53'
    assert response_data['name'] == 'Naruapon'

def test_get_user():
    # Get the created user
    response = requests.get(f"{BASE_URL}")
    assert response.status_code == 200
   
    # Now process the response
    response_data = response.json()
   
    assert response_data[0]['name'] == "Clyde O'Kon"
    assert response_data[0]['id'] == '1'

def test_delete_user():
    user_id = 53
    # Delete the created user
    response = requests.delete(f"{BASE_URL}/{user_id}")
    assert response.status_code == 200

    # Try to get the deleted user
    # response = requests.get(f"{BASE_URL}/users/{user_id}")
    # assert response.status_code == 404
    # assert response.json()['error'] == 'User not found'