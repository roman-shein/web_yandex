import flask

from . import db_session
from .users import User

from flask import jsonify, make_response, request


blueprint = flask.Blueprint("users_api", __name__, template_folder="templates")


@blueprint.route("/api/users")
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            "users": [user.to_dict(
                only=["id", "surname", "name", "age", "email", "city_from"]
            ) for user in users]
        }
    )


@blueprint.route("/api/users/<int:user_id>", methods=["GET"])
def get_one_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return make_response(jsonify({"error": "Not Found"}), 404)
    return jsonify(
        {
            "user": user.to_dict(only=["id", "surname", "name", "age", "email", "city_from"])
        }
    )


@blueprint.route("/api/users", methods=["POST"])
def create_user():
    if not request.json:
        return make_response(jsonify({"error": "Empty Request"}), 400)
    elif not all(key in request.json for key in [
        "surname", "name", "age", "email", "hashed_password", "city_from"
    ]):
        return make_response(jsonify({"error": "Bad Request"}), 400)
    db_sess = db_session.create_session()
    user = User(
        name=request.json["name"],
        surname=request.json["surname"],
        age=request.json["age"],
        email=request.json["email"],
        city_from=request.json["city_from"]
    )
    user.set_password(request.json["hashed_password"])
    db_sess.add(user)
    db_sess.commit()
    return jsonify({"id": user.id})


@blueprint.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return make_response(jsonify({"error": "Not Found"}), 404)
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({"success": "OK"})


@blueprint.route("/api/users/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    keys = ["surname", "name", "age", "email", "hashed_password", "city_from"]
    if not user:
        return make_response(jsonify({"error": "Not Found"}), 404)
    elif not all(key in keys for key in request.json.keys()):
        return make_response(jsonify({"error": "Bad Request"}), 400)
    for key, val in request.json.items():
        if key != "hashed_password":
            exec(f"user.{key} = \"{val}\"")
        else:
            user.set_password(val)
    db_sess.commit()
    return jsonify({"id": user.id})
