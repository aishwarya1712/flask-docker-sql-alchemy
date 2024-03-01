
from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint("health", __name__, description="Health Check APIs")

@blp.route("/health")
class Health(MethodView):
    def get(self):
        return {"message": "Up and running!"}