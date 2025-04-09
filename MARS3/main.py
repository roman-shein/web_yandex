import datetime

from flask import Flask, render_template
from data import db_session
from change_image import ChangeImage
import json
from random import choice
from data.users import User
from data.jobs import Jobs
from data.departments import Department

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')
    db_sess = db_session.create_session()
    # people = [
    #     {"surname": "Scott",
    #         "name": "Ridley",
    #         "age": 21,
    #         "position": "captain",
    #         "speciality": "research engineer",
    #         "address": "module_1",
    #         "email": "scott_chief@mars.org"},
    #     {"surname": "Иванов",
    #      "name": "Иван",
    #      "age": 16,
    #      "position": "подчиненный",
    #      "speciality": "трупроводчик линейный",
    #      "address": "module_2",
    #      "email": "qwert@email.org"},
    #     {"surname": "Петров",
    #      "name": "Петр",
    #      "age": 42,
    #      "position": "подчиненный",
    #      "speciality": "учитель",
    #      "address": "module_2",
    #      "email": "bsivisiv@email.org"},
    #     {"surname": "Николаев",
    #      "name": "Николай",
    #      "age": 25,
    #      "position": "руководитель",
    #      "speciality": "мойщик",
    #      "address": "module_1",
    #      "email": "fewnf@email.org"},
    #     {"surname": "Романов",
    #      "name": "Алексей",
    #      "age": 16,
    #      "position": "управляющий",
    #      "speciality": "просто крутой чувак",
    #      "address": "module_1",
    #      "email": "tsar@email.org"}
    # ]
    # for person in people:
    #     user = User()
    #     user.surname = person["surname"]
    #     user.name = person["name"]
    #     user.age = person["age"]
    #     user.position = person["position"]
    #     user.speciality = person["speciality"]
    #     user.address = person["address"]
    #     user.email = person["email"]
    #
    #     db_sess.add(user)
    #     db_sess.commit()
    #
    # jobs = Jobs()
    # jobs.team_leader = 1
    # jobs.job = "deployment of residential modules 1 and 2"
    # jobs.work_size = 15
    # jobs.collaborators = "2, 3"
    # jobs.start_date = datetime.datetime.now()
    # jobs.is_finished = False
    # db_sess.add(jobs)
    # db_sess.commit()
    #
    # department = Department()
    # department.title = "Геологическая разведка"
    # department.chief = 1
    # department.members = "2, 3, 4, 5"
    # department.email = "eovwuowb@email.org"
    # db_sess.add(department)
    # db_sess.commit()

    # people = {}
    # for person in list(map(int, db_sess.query(Department).filter(Department.id == 1).first().members.split(", "))):
    #     people[person] = 0
    #
    # jobs = db_sess.query(Jobs).all()
    # for job in jobs:
    #     for id in list(map(int, job.collaborators.split(", "))):
    #         if id in people:
    #             people[id] += job.work_size
    #
    # for key, val in people.items():
    #     if val > 25:
    #         res = db_sess.query(User).filter(User.id == key).first()
    #         print(res.surname, res.name)


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    params = {"title": "Что-то пишу",
              "surname": "Chill",
              "name": "Nick",
              "education": "high",
              "profession": "programmer",
              "sex": "man",
              "motivation": "+",
              "ready": True}
    return render_template("auto_answer.html", params=params)


@app.route("/distribution")
def distribution():
    names = ["Рома", "Гоша", "Ваня", "Никита", "Коля"]
    return render_template("distribution.html", params=names)


@app.route("/table/<gender>/<int:age>")
def table(gender, age):
    return render_template("table.html", gender=gender, age=age)


arr = ["mars.jpg", "mars1.jpg", "mars2.jpg"]


@app.route("/carousel", methods=["GET", "POST"])
def carousel():
    form = ChangeImage()
    if form.validate_on_submit():
        f = form.image.data
        f.save(f"static/image/{f.filename}")
        arr.append(f.filename)
    return render_template("carousel.html", form=form, arr=arr)


@app.route("/member")
def member():
    with open("templates/people.json", 'r', encoding="utf8") as fin:
        data = json.load(fin)
    people = choice(data["people"])
    prof = ', '.join(sorted(people["list_prof"]))
    return render_template("member.html", people=people, prof=prof)


@app.route("/")
def main_window():
    db_sess = db_session.create_session()
    works = db_sess.query(Jobs).all()
    return render_template("works.html", works=works)


if __name__ == '__main__':
    main()
