from flask import Flask, url_for, request

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


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
