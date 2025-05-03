from flask import jsonify
from flask_restful import Resource, abort
from . import db_session
from .users import User
from .users_parser import parser


def abort_if_user_not_found(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found!")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        return jsonify({"user": user.to_dict(
            only=("id", "surname", "name", "age", "email", "city_from")
        )})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        db_sess.delete(user)
        db_sess.commit()
        return jsonify({"success": "OK"})


class UsersListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return jsonify({
            "users": [user.to_dict(
                only=("id", "surname", "name", "age", "email", "city_from")
            ) for user in users]
        })

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        user = User(
            surname=args["surname"],
            name=args["name"],
            age=args["age"],
            email=args["email"],
            city_from=args["city_from"]
        )
        user.set_password(args["password"])
        db_sess.add(user)
        db_sess.commit()
        return jsonify({"id": user.id})

