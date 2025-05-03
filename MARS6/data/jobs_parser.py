from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument("team_leader_id", required=True)
parser.add_argument("job", required=True)
parser.add_argument("work_size", required=True)
parser.add_argument("collaborators", required=True)
parser.add_argument("hazard_cat", required=True)
parser.add_argument("is_finished", required=True, type=bool)
