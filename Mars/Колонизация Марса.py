from flask import Flask, url_for, request
import os

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promorion():
    return """Человечество вырастает из детства.<br>
Человечеству мала одна планета.<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
И начнем с Марса!<br>
Присоединяйся!"""


@app.route('/image_mars')
def image_mars():
    return f"""
<h1>Жди нас, Марс!</h1>
<img src="{url_for('static', filename='image/mars.jpg')}"
    alt="здесь должна была быть картинка, но не нашлась" title="Красиво!">
<p>Вот она какая, красная планета.</p>
"""


@app.route('/promotion_image')
def promation_image():
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
    crossorigin="anonymous">
    <title>Привет, Яндекс!</title>
  </head>
  <body>
    <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='image/mars.jpg')}"
            alt="здесь должна была быть картинка, но не нашлась" title="Красиво!">
        <p>Вот она какая, красная планета.</p>
    <div class="alert alert-primary" role="alert">
        Человечество вырастает из детства.
    </div>
    <div class="alert alert-secondary" role="alert">
        Человечеству мала одна планета.
    </div>
    <div class="alert alert-success" role="alert">
        Мы сделаем обитаемыми безжизненные пока планеты.
    </div>
    <div class="alert alert-danger" role="alert">
        И начнем с Марса!
    </div>
    <div class="alert alert-warning" role="alert">
        Присоединяйся!
    </div>
  </body>
</html>"""


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
    crossorigin="anonymous">
    <title>Привет, Яндекс!</title>
  </head>
  <body>
    <h1>Мое предложение: {planet_name}</h1>
    <div class="alert alert-primary" role="alert">
        Эта планета близко к земле;
    </div>
    <div class="alert alert-secondary" role="alert">
        На ней много необходимых ресурсов;
    </div>
    <div class="alert alert-success" role="alert">
        На ней есть вода и атмосфера;
    </div>
    <div class="alert alert-danger" role="alert">
        На ней есть небольшое магнитное поле;
    </div>
    <div class="alert alert-warning" role="alert">
        Наконец, она просто красива!
    </div>
  </body>
</html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
    crossorigin="anonymous">
    <title>Привет, Яндекс!</title>
  </head>
  <body>
    <h1>Результаты отбора</h1>
    <h2>Претенденты на участие в миссии {nickname}</h2>
    <div class="alert alert-secondary" role="alert">
        Поздравляем! Ваш рейтинг после {level} этапа отбора
    </div>
    <div class="alert alert-success" role="alert">
        составляет {rating}!
    </div>
    <div class="alert alert-danger" role="alert">
        Желаем удачи!
    </div>
  </body>
</html>"""


@app.route("/load_photo", methods=['GET', 'POST'])
def load_photo():
    if request.method == "GET":
        return f'''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
            crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Пример формы</title>
          </head>
          <body>
            <h1>Загрузим файл</h1>
            <h2>для участия в миссии</h2>
            <div>
            <form class="login_form" method="post" enctype="multipart/form-data">
               <div class="form-group">
                    <label for="photo">Выберите файл</label>
                    <input type="file" class="form-control-file" id="photo" name="file">
                </div>
                <div>
                <img src='static\image\input.jpg' alt="Ничего не выбрано">
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
            </div>
          </body>
        </html>'''
    elif request.method == "POST":
        f = request.files['file']
        f.save(r"static\image\input.jpg")
        return f'''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
            crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Пример формы</title>
          </head>
          <body>
            <h1>Загрузим файл</h1>
            <h2>для участия в миссии</h2>
            <div>
            <form class="login_form" method="post" enctype="multipart/form-data">
               <div class="form-group">
                    <label for="photo">Выберите файл</label>
                    <input type="file" class="form-control-file" id="photo" name="file">
                </div>
                <div>
                <img src='static\image\input.jpg' alt="Ничего не выбрано">
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
            </div>
          </body>
        </html>'''


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    <title>Пример формы</title>
  </head>
  <body>
    <h1>Анкета претендента</h1>
    <h2>на участие в миссии</h2>
    <div>
        <form class="login_form" method="post">
            <input type="surname" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
            <input type="name" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите имя" name="name">
            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
            <div class="form-group">
                <label for="classSelect">Какое у вас образование?</label>
                <select class="form-control" id="classSelect" name="class">
                  <option>Начальное</option>
                  <option>Среднее</option>
                  <option>Высшее</option>
                </select>
             </div>
         <div class="form-group form-check">
            <label class="form-check-label" for="acceptRules">Какие у вас профессии?</label>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
            </div>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
            </div>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Пилот</label>
            </div>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Метеоролог</label>
            </div>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечиванию</label>
            </div>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
            </div>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Врач</label>
            </div>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Экзобиолог</label>
            </div>
        </div>
            
        <div class="form-group">
            <label for="form-check">Укажите пол</label>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
              <label class="form-check-label" for="male">
                Мужской
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
              <label class="form-check-label" for="female">
                Женский
              </label>
            </div>
        </div>
        
        <div class="form-group">
            <label for="about">Почему вы ходите принять участие в миссии?</label>
            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
        </div>
                                
        <div class="form-group" enctype="multipart/form-data">
            <label for="photo">Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>
        
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
            <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
        </div>
        <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
    </div>
  </body>
</html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route("/carousel")
def carousel():
    return f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" 
          integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" 
          crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.min.js" 
          integrity="sha384-Atwg2Pkwv9vp0ygtn1JAojH0nYbwNJLPhwyoVbhoPwBhjQPR5VtM2+xf0Uwh9KtT" 
          crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    <title>Пример формы</title>
</head>
<body>
    <h1 align="center">Пейзажи Марса</h1>
    <div id="carouselExampleDark" class="carousel carousel-dark slide">
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="10000">
          <img src="{url_for('static', filename='image/mars.jpg')}" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item" data-bs-interval="2000">
          <img src="{url_for('static', filename='image/mars1.jpg')}" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="{url_for('static', filename='image/mars2.jpg')}" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" 
              data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" 
              data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
