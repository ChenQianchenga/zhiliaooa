from functools import wraps

from flask import Flask, session, g
from flask_migrate import Migrate
import config
from blueprints.auth import auth_bp
from blueprints.qa import qa_bp
from exts import db, mail
from models import UserModel

app = Flask(__name__)
app.app_context().push()
# 绑定配置文件
app.config.from_object(config)
# 先创建再绑定
db.init_app(app)
mail.init_app(app)

# 注册蓝本
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

migrate = Migrate(app, db)


@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)


@app.context_processor
def my_context_processor():
    return {"user": g.user}


if __name__ == "__main__":
    app.run(debug=True)
