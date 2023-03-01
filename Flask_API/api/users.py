from flask import Blueprint, Response

users = Blueprint(
    "users",
    __name__,
    url_prefix="/users")

@users.route("/list")
def index():
    return Response(f"No Registered Users!")

