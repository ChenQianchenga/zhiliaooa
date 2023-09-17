import random
import string

from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_mail import Message
from werkzeug.security import generate_password_hash

from blueprints.forms import RegisterForm
from exts import db, mail
from models import EmailCaptchaModel, UserModel

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login")
def login():
    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("regist.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(
                email=email,
                username=username,
                password=generate_password_hash(password),
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@auth_bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    source = string.digits * 4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    message = Message(subject="知了传课注册验证码", recipients=[email], body=f"您的验证码是：{captcha}")
    mail.send(message=message)
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({"code": 200, "message": "验证码获取成功", "data": None})
