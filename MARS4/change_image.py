from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired


class ChangeImage(FlaskForm):
    image = FileField("Выберите изображение", validators=[FileRequired()])
    submit = SubmitField("Отправить")
