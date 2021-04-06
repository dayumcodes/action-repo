from flask import Blueprint
from flask import json
from flask import request
from flask import Flask

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/github', methods=["POST"])
def push():
    if request.headers['Content-Type']=='application/json':
        return json.dumps(request.json)
    return {}, 200


