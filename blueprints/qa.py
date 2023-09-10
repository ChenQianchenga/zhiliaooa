from flask import Blueprint

qa_bp = Blueprint("qa", __name__, url_prefix="/")


# http://127.0.0.1:5000/
@qa_bp.route("/")
def index():
    return "hello!!!"
