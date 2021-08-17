from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/sign-in")
def sign_in():
    return "Sign In"


@auth.route("/sign-up")
def sign_up():
    return "Sign Up"


@auth.route("/sign-out")
def sign_out():
    return "Sign Out"
