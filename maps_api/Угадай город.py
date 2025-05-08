import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QPixmap
import sys
from random import choice

cities = [
    ("москва", 0.03),
    ("санкт-петербург", 0.01),
    ("мурманск", 0.01),
    ("лондон", 0.03),
    ("париж", 0.03),
    ("берлин", 0.03)
]

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_api_key = "cf79098a-155e-47b7-9b49-b55b4461472d"

static_api_server = "https://static-maps.yandex.ru/v1?"
static_api_key = "318965a9-b51c-41fb-a672-2acad73bc050"

geocode_params = {
    "apikey": geocoder_api_key,
    "geocode": "",
    "format": "json"
}

static_params = {
    "apikey": static_api_key,
    "ll": '',
    "spn": ''
}


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 600, 600)

        self.btn = QPushButton(self)
        self.btn.resize(100, 30)
        self.btn.move(450, 500)
        self.btn.setText("Проверить")
        self.btn.clicked.connect(self.get_image)

        self.image = QLabel(self)
        self.image.resize(600, 450)
        self.image.move(0, 0)

        self.line_edit = QLineEdit(self)
        self.line_edit.resize(400, 30)
        self.line_edit.move(10, 500)

        self.info_label = QLabel(self)
        self.info_label.resize(100, 30)
        self.info_label.move(10, 550)

        self.prev_city = (None, None)
        self.cur_city = (None, None)
        self.first = True
        self.get_image()

    def get_image(self):
        if self.line_edit.text().lower() == self.cur_city[0] or self.first:
            self.first = False
            self.info_label.setText("")
            self.line_edit.setText("")
            self.prev_city, self.cur_city = self.cur_city, choice(cities)
            while self.prev_city == self.cur_city:
                self.cur_city = choice(cities)

            geocode_params["geocode"] = self.cur_city[0]
            response = requests.get(geocoder_api_server, params=geocode_params).json()
            if not response["response"]["GeoObjectCollection"]["featureMember"]:
                self.info_label.setText("Ошибка")
                return
            ll = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()
            ll = ','.join(ll)
            static_params["ll"] = ll
            static_params["spn"] = ','.join([str(self.cur_city[1]), str(self.cur_city[1])])

            response = requests.get(static_api_server, params=static_params)

            if not response:
                self.info_label.setText("Ошибка")
                return

            with open("map.png", 'wb') as f:
                f.write(response.content)

            self.pixmap = QPixmap("map.png")
            self.image.setPixmap(self.pixmap)
        else:
            self.info_label.setText("Неверный ответ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec())
