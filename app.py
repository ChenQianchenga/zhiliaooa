from flask import Flask
from flask_migrate import Migrate
import config
from blueprints.auth import auth_bp
from blueprints.qa import qa_bp
from exts import db, mail
from models import UserModel

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)
# 先创建再绑定
db.init_app(app)
mail.init_app(app)

# 注册蓝本
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(debug=True)
