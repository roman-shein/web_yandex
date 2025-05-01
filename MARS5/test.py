from requests import get, post, delete


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
