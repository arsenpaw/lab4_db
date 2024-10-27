from http.client import responses
from typing import Type

from flask import Blueprint, make_response, Response
from werkzeug.exceptions import NotFound

simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/test1', methods=["GET"])
async def show() -> str:
    print('test')
    return 'test'
@simple_page.route('/test', methods=["GET"])
async def show1() -> Response:
    print('test')
    return make_response('Not Found', 404)