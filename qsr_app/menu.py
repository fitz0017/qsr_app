import json, os.path

from flask import Blueprint, render_template

bp = Blueprint("menu", __name__)
with open(os.path.join(bp.root_path, "assets", "sandwiches.json"), encoding="utf-8") as json_file:
    data = json.load(json_file)

@bp.route('/sayFood/<foodParam>')
def hello(foodParam):
    return render_template("menu/index.html", food=data)
