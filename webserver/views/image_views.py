from datetime import datetime

from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from .. import db
from ..models import ImageUpload
from ..views.auth_views import login_required

bp = Blueprint('image', __name__, url_prefix='/image')

@bp.route('/list')
def _list():
    page = request.args.get('page', type=int, default=1)
    image_list = ImageUpload.query.order_by(ImageUpload.create_date.desc())
    image_list = image_list.paginate(page, per_page=10)
    return render_template('image/image_list.html', image_list=image_list)

@bp.route('/upload/', methods=('POST', ))
def upload():
    if request.method == 'POST':
        _file = request.files['file']
        _file.save('C:\pythonProject1\webserver\static\\' + _file.filename)
        image = ImageUpload(filename=_file.filename, create_date=datetime.now(), user_id=1)
        if image != None:
            db.session.add(image)
            db.session.commit()
            return redirect(url_for('image._list'))

@bp.route('/detail/<int:image_id>/')
@login_required
def detail(image_id):
    image = ImageUpload.query.get_or_404(image_id)
    return render_template('image/image_detail.html', image = image)

@bp.route('/delete/<int:image_id>')
@login_required
def delete(image_id):
    image = ImageUpload.query.get_or_404(image_id)
    if g.user != image.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('image.detail', image_id=image_id))
    db.session.delete(image)
    db.session.commit()
    return redirect(url_for('image._list'))