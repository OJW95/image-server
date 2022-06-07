# 사용자에게 보여질 뷰를 따로 정의하는 곳. 따라서 객체 생성하는 곳 = 인잇이 뚱뚱해지지 않음.
from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_server():
    return 'Hello, Server!!'

@bp.route('/')
def index():
    return redirect(url_for('image._list'))