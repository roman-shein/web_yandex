import datetime

import requests
from flask import Flask, render_template, redirect, request, abort, make_response, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from loginform import LoginForm
from data import db_session, jobs_api, users_api
from change_image import ChangeImage
import json
from random import choice
from data.users import User
from data.jobs import Jobs
from data.departments import Department
from data.categories import Categories
from forms.user import RegisterForm
from forms.jobs import JobsForm
from forms.departments import DepartmentsForm
from requests import get
from flask_restful import reqparse, abort, Api, Resource
from data.users_resource import UsersResource, UsersListResource
from data.jobs_resource import JobsResource, JobsListResource

app = Flask(__name__)
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)
    api.add_resource(UsersResource, "/api/v2/users/<int:user_id>")
    api.add_resource(UsersListResource, "/api/v2/users")
    api.add_resource(JobsResource, "/api/v2/jobs/<int:job_id>")
    api.add_resource(JobsListResource, "/api/v2/jobs")
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
    # cat = Categories()
    # cat.title = "test1"
    # db_sess.add(cat)
    # db_sess.commit()
    #
    # jobs = Jobs()
    # jobs.team_leader = 1
    # jobs.job = "deployment of residential modules 1 and 2"
    # jobs.work_size = 15
    # jobs.collaborators = "2, 3"
    # jobs.start_date = datetime.datetime.now()
    # jobs.hazard_cat = 1
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


@app.route('/login', methods=['GET', 'POST'])
def login():  # qwerty@email.com password: qwerty12345, для капитана пароль 123!!!
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/departments")
@login_required
def show_departments():
    db_sess = db_session.create_session()
    departments = db_sess.query(Department).all()
    return render_template("departments.html", departments=departments)


@app.route("/add_departments", methods=["GET", "POST"])
@login_required
def add_departments():
    form = DepartmentsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        dep = Department()
        dep.title = form.title.data
        surname, name = form.chief.data.split()
        chief = db_sess.query(User).filter(User.surname == surname, User.name == name).first()
        if not chief:
            err = "Начальник не зарегистрирован в системе!"
            return render_template("add_departments.html", form=form, err=err)
        dep.chief = chief.id
        dep.members = form.members.data
        dep.email = form.email.data
        db_sess.add(dep)
        db_sess.commit()
        return redirect("/departments")
    return render_template("add_departments.html", form=form, err="")


@app.route("/edit_department/<int:id>", methods=["GET", "POST"])
@login_required
def edit_departments(id):
    form = DepartmentsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        dep = db_sess.query(Department).filter(Department.id == id).first()
        if dep:
            form.title.data = dep.title
            form.chief.data = dep.user.surname + " " + dep.user.name
            form.members.data = dep.members
            form.email.data = dep.email
        else:
            abort(404)

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        dep = db_sess.query(Department).filter(Department.id == id).first()
        if dep:
            dep.title = form.title.data
            surname, name = form.chief.data.split()
            chief = db_sess.query(User).filter(User.surname == surname, User.name == name).first()
            if not chief:
                err = "Начальник не зарегистрирован в системе!"
                return render_template("add_departments.html", form=form, err=err)
            dep.chief = chief.id
            dep.members = form.members.data
            dep.email = form.email.data
            db_sess.commit()
            return redirect("/departments")
    return render_template('add_departments.html',
                           title='Редактирование департамента',
                           form=form, err="")


@app.route("/delete_department/<int:id>", methods=["GET", "POST"])
@login_required
def delete_departments(id):
    db_sess = db_session.create_session()
    dep = db_sess.query(Department).filter(Department.id == id).first()
    if dep:
        db_sess.delete(dep)
        db_sess.commit()
    else:
        abort(404)
    return redirect("/departments")


@app.route('/addjob',  methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.team_leader = form.team_leader_id.data
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.hazard_cat = form.hazard_cat.data
        job.is_finished = form.is_finished.data
        db_sess.add(job)
        db_sess.commit()
        return redirect("/")
    return render_template("add_jobs.html", title="Добавление работы", form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.team_leader == current_user.id
                                          ).first()
        if jobs:
            form.team_leader_id.data = jobs.team_leader
            form.job.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.hazard_cat.data = jobs.hazard_cat
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.user == current_user
                                          ).first()
        if jobs:
            jobs.team_leader = form.team_leader_id.data
            jobs.job = form.job.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.hazard_cat = form.hazard_cat.data
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('add_jobs.html',
                           title='Редактирование новости',
                           form=form
                           )


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def job_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id
                                      ).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            modified_date=datetime.datetime.now(),
            city_from=form.city_from.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template("register.html", form=form, title="Регистрация")


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not Found"}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({"error": "Bad Request"}), 400)


@app.route("/users_show/<int:user_id>")
@login_required
def get_city(user_id):
    user = get(f"http://localhost:8080/api/users/{user_id}").json()
    if "error" in user:
        return """<h1>404</h1>
<h2>Not Found</h2>"""
    elif user["user"]["city_from"] is None:
        return render_template("users_show.html", user=user["user"], err="City is not specify")
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    static_api_server = "https://static-maps.yandex.ru/v1"
    geocoder_params = {
        "apikey": "cf79098a-155e-47b7-9b49-b55b4461472d",
        "geocode": user["user"]["city_from"],
        "format": "json"
    }
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        return """<h1>404</h1>
<h2>Not Found</h2>"""
    # print(response.json(), file=open("res.json", 'w', encoding="utf8"))
    json_response = response.json()
    ll = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()
    ll = ",".join(ll)
    delta = "0.075"
    static_api_params = {
        "ll": ll,
        "spn": ','.join([delta, delta]),
        "apikey": "318965a9-b51c-41fb-a672-2acad73bc050"
    }
    response = requests.get(static_api_server, params=static_api_params)
    map_file = "static/image/map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    return render_template("users_show.html", user=user["user"], err='')


if __name__ == '__main__':
    main()
