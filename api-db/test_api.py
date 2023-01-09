import requests
import json

headers = {
"accept": "application/json",
"Content-Type": "application/x-www-form-urlencoded"
}

# Account 'test@test.be' with password 'test' has already been pre-made, either manually or with another requests.post
request_data = {
    "client_id": "",
    "client_secret": "",
    "scope": "",
    "grant_type": "",
    "refresh_token": "",
    "username": "test@test.com",
    "password": "test"
}

tokenrequest = requests.post("http://127.0.0.1:8000/token", data=request_data, headers=headers)

# Printing the information for debugging and illustration purposes
print(tokenrequest.text)
# Extracting the token that came with the response
token = json.loads(tokenrequest.text)['access_token']

# Using the token in the headers of a secured endpoint
headerswithtoken = {
"accept" : "application/json",
"Authorization": f'Bearer {token}'
}

getrequest = requests.get("http://localhost:8000/users/me", headers=headerswithtoken)

# Printing the information for debugging and illustration purposes
print(getrequest .text)


create_new_user = {
    "full_name": "test testerone",
    "email": "test@testipers.com",
    "password": "testerates"
}

def test_create_new_user():
    response = requests.post('http://127.0.0.1:8000/user/', json=create_new_user)
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert response_dictionary["full_name"] == "test testerone"
    assert response_dictionary["email"] == "test@testipers.com"

create_user_same_name = {
    "full_name": "test testerone",
    "email": "test@nottestipers.com",
    "password": "testerates"
}

def test_create_user_same_name():
    response = requests.post('http://127.0.0.1:8000/user/', json=create_user_same_name)
    assert response.status_code == 400
    response_dictionary = json.loads(response.text)
    assert "Name already registered" in response_dictionary.values()

create_user_same_email = {
    "full_name": "test nottesterone",
    "email": "test@testipers.com",
    "password": "testerates"
}

def test_create_user_same_email():
    response = requests.post('http://127.0.0.1:8000/user/', json=create_user_same_email)
    assert response.status_code == 400
    response_dictionary = json.loads(response.text)
    assert "Email already registered" in response_dictionary.values()

def test_get_user():
    response = requests.get('http://127.0.0.1:8000/user/2')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["full_name"]) == str
    assert type(response_dictionary["email"]) == str

def test_get_user_non_existing():
    response = requests.get('http://127.0.0.1:8000/user/500')
    assert response.status_code == 404
    response_dictionary = json.loads(response.text)
    assert "User not found" in response_dictionary.values()

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


create_new_contact = {
    "full_name": "cousin test",
    "email": "cousin@testipers.com"
}

def test_create_new_contact():
    response = requests.post('http://127.0.0.1:8000/user/2/contact/', json=create_new_contact)
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert response_dictionary["full_name"] == "cousin test"
    assert response_dictionary["email"] == "cousin@testipers.com"

create_contact_same_name = {
    "full_name": "cousin test",
    "email": "cousin@nottestipers.com",
    "password": "testerates"
}

def test_create_contact_same_name():
    response = requests.post('http://127.0.0.1:8000/user/2/contact/', json=create_contact_same_name)
    assert response.status_code == 400
    response_dictionary = json.loads(response.text)
    assert "Contact already registered" in response_dictionary.values()

create_contact_same_email = {
    "full_name": "cousin nottest",
    "email": "cousin@testipers.com",
    "password": "testerates"
}

def test_create_contact_same_email():
    response = requests.post('http://127.0.0.1:8000/user/2/contact/', json=create_contact_same_email)
    assert response.status_code == 400
    response_dictionary = json.loads(response.text)
    assert "Email already registered" in response_dictionary.values()

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


create_new_number = {
    "phonenumber": "0452 36 14 79",
    "relation": "home"
}

def test_create_new_number():
    response = requests.post('http://127.0.0.1:8000/user/2/contact/1', json=create_new_number)
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert response_dictionary["phonenumber"] == "0452 36 14 79"
    assert response_dictionary["relation"] == "home"

create_same_number = {
    "phonenumber": "0452 36 14 79",
    "relation": "home"
}

def test_create_number_already_existing():
    response = requests.post('http://127.0.0.1:8000/user/2/contact/1', json=create_same_number)
    assert response.status_code == 400
    response_dictionary = json.loads(response.text)
    assert "Number already registered" in response_dictionary.values()

def test_get_all_numbers_of_a_contact():
    response = requests.get('http://127.0.0.1:8000/numbers/?user=2&contact=1')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    for number in response_dictionary:
        assert type(number["phonenumber"]) == str
        assert type(number["relation"]) == str

def test_get_all_numbers_of_a_contact_non_existing():
    response = requests.get('http://127.0.0.1:8000/numbers/?user=30&contact=50')
    assert response.status_code == 404
    response_dictionary = json.loads(response.text)
    assert "Number not found" in response_dictionary.values()

update_number = {
    "phonenumber": "0431 52 68 37",
    "relation": "work"
}

def test_update_number():
    response = requests.put('http://127.0.0.1:8000/number/1', json=update_number)
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert response_dictionary["phonenumber"] == "0431 52 68 37"
    assert response_dictionary["relation"] == "work"

def test_update_number_non_existing():
    response = requests.put('http://127.0.0.1:8000/number/100', json=update_number)
    assert response.status_code == 400
    response_dictionary = json.loads(response.text)
    assert "Number doesn't exist" in response_dictionary.values()


def test_delete_user():
    response = requests.delete('http://127.0.0.1:8000/user/2')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert "Successful" in response_dictionary.values()

def test_delete_user_non_existing():
    response = requests.delete('http://127.0.0.1:8000/user/300')
    assert response.status_code == 404
    response_dictionary = json.loads(response.text)
    assert "User not found" in response_dictionary.values()
