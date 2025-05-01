from requests import get, post, delete, put


# task 3 (тестирование обработчиков для получения работ)
# print(get("http://localhost:8080/api/jobs").json())
# print(get("http://localhost:8080/api/jobs/1").json())
# print(get("http://localhost:8080/api/jobs/999").json())
# print(get("http://localhost:8080/api/jobs/q").json())

# task 5 (добавление работы)
# print(post("http://localhost:8080/api/jobs", json={}).json())  # пустой параметр
# print(post("http://localhost:8080/api/jobs", json={"team_leader": 1}).json())  # неполный параметр
# print(post("http://localhost:8080/api/jobs", json={"team_leader": 1,
#                                                    "job": "test3",
#                                                    "work_size": 1,
#                                                    "collaborators": 1,
#                                                    "hazard_cat": 1,
#                                                    "is_finished": True}).json())  # корректный запрос
# print(get("http://localhost:8080/api/jobs").json())

# task 7 (тестирование удаления)
# print(delete("http://localhost:8080/api/jobs/111").json())  # некорректный запрос
# print(delete("http://localhost:8080/api/jobs/4").json())  # корректный запрос
# print(get("http://localhost:8080/api/jobs").json())

# task 9 (тестирование редактирования)
print(put("http://localhost:8080/api/jobs/999", json={}).json())  # некорректный запрос
print(put("http://localhost:8080/api/jobs/3", json={"ccc": "fsii"}).json())  # некорректный запрос (несуществующее поле)
print(put("http://localhost:8080/api/jobs/3", json={"job": "test 3"}).json())  # корректный запрос
