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

@auth.create_account("/create_account", methods=["POST", "GET"])
def create_account():
    if request.method=="POST":
        account_holder_name=request.form.get("account_holder_name")
        citizenship_number=request.form.get("citizenship_number")
        permanent_address=request.form.get("permanent_address")
        temporary_address=request.form.get("temporary_address")
        password_1=request.form.get("password_1")
        password_2=request.form.get("password_2")
        email=request.form.get("email")

@auth.logout("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))