import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Department(SqlAlchemyBase):
    __tablename__ = "departments"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    members = sqlalchemy.Column(sqlalchemy.Integer)
    email = sqlalchemy.Column(sqlalchemy.String)

    user = orm.relationship("User")

    def __repr__(self):
        return f"<Department> {self.title}"
