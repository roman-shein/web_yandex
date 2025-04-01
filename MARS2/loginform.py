from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astronaut = StringField('Id астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_capitan = StringField('Id капитана', validators=[DataRequired()])
    password_capitan = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')
