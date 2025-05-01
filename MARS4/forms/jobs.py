from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField("description", validators=[DataRequired()])
    team_leader_id = IntegerField("team leader id", validators=[DataRequired()])
    work_size = IntegerField("work size", validators=[DataRequired()])
    collaborators = StringField("collaborators", validators=[DataRequired()])
    is_finished = BooleanField("is finished")
    submit = SubmitField("Add")
