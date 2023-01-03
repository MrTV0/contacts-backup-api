import requests
import json

def test_get_user():
    response = requests.get('http://127.0.0.1:8000/user/1')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["full_name"]) == str
    assert type(response_dictionary["email"]) == str

def test_get_user_non_existing():
    response = requests.get('http://127.0.0.1:8000/user/2')
    assert response.status_code == 404
    response_dictionary = json.loads(response.text)
    assert 'User not found' in response_dictionary.values()

def test_get_all_users():
    response = requests.get('http://127.0.0.1:8000/users/')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    for user in response_dictionary:
        assert type(user["full_name"]) == str
        assert type(user["email"]) == str
        assert type(user["id"]) == int

def test_get_limited_users():
    response = requests.get('http://127.0.0.1:8000/users/?skip=10&limit=500')
    assert response.status_code == 200





def test_get_all_contacts():
    response = requests.get('http://127.0.0.1:8000/contacts/')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    for contact in response_dictionary:
        assert type(contact["full_name"]) == str
        assert type(contact["email"]) == str
        assert type(contact["id"]) == int
        assert type(contact["users_id"]) == int

def test_get_limited_contacts():
    response = requests.get('http://127.0.0.1:8000/contacts/?skip=5&limit=200')
    assert response.status_code == 200




def test_get_all_numbers_of_a_contact():
    response = requests.get('http://127.0.0.1:8000/numbers/?user=1&contact=1')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    for number in response_dictionary:
        assert type(number["phonenumber"]) == str
        assert type(number["relation"]) == str

def test_get_all_numbers_of_a_contact():
    response = requests.get('http://127.0.0.1:8000/numbers/?user=3&contact=5')
    assert response.status_code == 404
    response_dictionary = json.loads(response.text)
    assert 'Number not found' in response_dictionary.values()