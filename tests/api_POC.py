import requests


def test_get_list_of_users():
    url = "https://reqres.in/api/users"
    response = requests.get(url)
    print(response)
    assert response.status_code == 201
