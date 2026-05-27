from flask import Blueprint, render_template, url_for, redirect, request, flash
from . import Db
from werkzeug.security import check_password_hash, generate_password_hash
from .model import Account
from flask_login import login_user, login_required, logout_user

auth=Blueprint("auth", __name__)

@auth.login("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        account_holder_name=request.form.get("account_holder_name")
        account_number=request.form.get("account_number")
        password=request.form.get("password")

        account=Account.query.filter_by(account_number=account_number).first()
        if account:
            if check_password_hash(account.password, password):
                flash("Welcome back customer!!!", category="success")
                login_user(account, remember=True)
            else:
                flash("Please check the Password!!!", category="error")
        else:
            flash("Account doesn't exist!!!", category="error")

    return render_template("login.html")
