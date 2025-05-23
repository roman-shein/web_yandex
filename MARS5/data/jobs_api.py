import flask

from . import db_session
from .jobs import Jobs

from flask import jsonify, make_response, request

blueprint = flask.Blueprint("jobs_api", __name__, template_folder="templates")


@blueprint.route("/api/jobs")
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            "jobs": [job.to_dict(only=["id", "user.name", "user.surname", "job",
                                       "work_size", "collaborators", "start_date", "end_date",
                                       "category.title", "is_finished"]) for job in jobs]
        }
    )


@blueprint.route("/api/jobs/<int:job_id>", methods=["GET"])
def get_one_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return make_response(jsonify({"error": "Not Found"}), 404)
    return jsonify(
        {
            "jobs": job.to_dict(only=["id", "user.name", "user.surname", "job",
                                      "work_size", "collaborators", "start_date", "end_date",
                                      "category.title", "is_finished"])
        }
    )


@blueprint.route("/api/jobs", methods=["POST"])
def create_job():
    if not request.json:
        return make_response(jsonify({"error": "Empty request"}), 400)
    elif not all(key in request.json for key in ["team_leader", "job", "work_size",
                                                 "collaborators", "hazard_cat", "is_finished"]):
        return make_response(jsonify({"error": "Bad request"}), 400)
    db_sess = db_session.create_session()
    job = Jobs(
        team_leader=request.json["team_leader"],
        job=request.json["job"],
        work_size=request.json["work_size"],
        collaborators=request.json["collaborators"],
        hazard_cat=request.json["hazard_cat"],
        is_finished=request.json["is_finished"]
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({"id": job.id})


@blueprint.route("/api/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return make_response(jsonify({"error": "Not Found"}), 404)
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({"success": "OK"})


@blueprint.route("/api/jobs/<int:job_id>", methods=["PUT"])
def edit_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
    keys = ["team_leader", "job", "work_size", "collaborators", "hazard_cat", "is_finished"]
    if not job:
        return make_response(jsonify({"error": "Not Found"}), 404)
    elif not all(key in keys for key in request.json.keys()):
        return make_response(jsonify({"error": "Bad Request"}), 400)
    job: "Jobs"
    for key, val in request.json.items():
        exec(f"job.{key} = \"{val}\"")
    db_sess.commit()
    return jsonify({"id": job_id})
