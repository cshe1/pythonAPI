import requests
import url as u


def test_get_list_of_users():
    response = requests.get(u.users_url)
    assert response.status_code == 200


def test_get_user_three():
    response = requests.get(u.user_three_url)
    assert response.status_code == 200


def test_create_new_user():
    response = requests.post(u.users_url, data=u.user_create_pl)
    assert response.status_code == 201


def test_update_user():
    response = requests.put(u.user_three_url, data=u.user_update_pl)
    assert response.status_code == 200


def test_patch_user():
    response = requests.patch(u.user_three_url, data=u.user_patch_pl)
    assert response.status_code == 200


def test_delete_user():
    response = requests.delete(u.user_three_url)
    assert response.status_code == 204


def test_register_user():
    response = requests.post(u.register_url, data=u.user_register_pl)
    assert response.status_code == 200
