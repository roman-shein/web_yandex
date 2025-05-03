from flask import jsonify
from flask_restful import Resource, abort
from . import db_session
from .jobs import Jobs
from .jobs_parser import parser


def abort_if_user_not_found(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found!")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_user_not_found(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        print(job)
        return jsonify({"jobs": job.to_dict(
            only=("id", "user.name", "user.surname", "job",
                  "work_size", "collaborators", "start_date", "end_date",
                  "category.title", "is_finished")
        )})

    def delete(self, job_id):
        abort_if_user_not_found(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        db_sess.delete(job)
        db_sess.commit()
        return jsonify({"success": "OK"})


class JobsListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        return jsonify({
            "jobs": [job.to_dict(
                only=("id", "user.name", "user.surname", "job",
                      "work_size", "collaborators", "start_date", "end_date",
                      "category.title", "is_finished")) for job in jobs]
        })

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        job = Jobs(
            team_leader=args["team_leader_id"],
            job=args["job"],
            work_size=args["work_size"],
            collaborators=args["collaborators"],
            hazard_cat=args["hazard_cat"],
            is_finished=args["is_finished"]
        )
        db_sess.add(job)
        db_sess.commit()
        return jsonify({"id": job.id})

