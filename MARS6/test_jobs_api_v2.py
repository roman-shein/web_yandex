from requests import get, post, delete

# print(get("http://127.0.0.1:8080/api/v2/jobs").json())
# print(get("http://127.0.0.1:8080/api/v2/jobs/1").json())
# print(get("http://127.0.0.1:8080/api/v2/jobs/999").json())
# print(post("http://127.0.0.1:8080/api/v2/jobs", json={
#     "team_leader_id": 1,
#     "job": "test",
#     "work_size": 1,
#     "collaborators": "2, 3",
#     "hazard_cat": 1,
#     "is_finished": True
# }).json())
# print(post("http://127.0.0.1:8080/api/v2/jobs", json={
#     "job": "test",
#     "work_size": 1,
#     "collaborators": "2, 3",
#     "hazard_cat": 1,
#     "is_finished": True
# }).json())
print(delete("http://127.0.0.1:8080/api/v2/jobs/3").json())
