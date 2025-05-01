from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, SubmitField
from wtforms.validators import DataRequired


class DepartmentsForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    chief = StringField("Начальник (фамилия, имя)", validators=[DataRequired()])
    members = StringField("Участники", validators=[DataRequired()])
    email = EmailField("Почта", validators=[DataRequired()])
    submit = SubmitField("Добавить")
