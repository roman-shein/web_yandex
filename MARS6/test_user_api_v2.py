from requests import get, post, delete

print(get("http://127.0.0.1:8080/api/v2/users").json())
print(delete("http://127.0.0.1:8080/api/v2/users/8").json())
print(post("http://127.0.0.1:8080/api/v2/users", json={
    "name": "test1",
    "surname": "test",
    "age": 1,
    "email": "test@test.com",
    "city_from": "test",
    "password": "123"
}).json())
print(get("http://127.0.0.1:8080/api/v2/users/8").json())
print(get("http://127.0.0.1:8080/api/v2/users/999").json())
print(get("http://127.0.0.1:8080/api/v3/users").json())
print(delete("http://127.0.0.1:8080/api/v2/users/999").json())
