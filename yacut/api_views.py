import re
from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id
from .settings import SHORT_URL_PATTERN


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_url(short_id: str):
    original_url = URLMap.query.filter_by(short=short_id).first()
    if not original_url:
        raise InvalidAPIUsage('Данный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': original_url.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_id():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса', HTTPStatus.BAD_REQUEST)
    if not data.get('url'):
        raise InvalidAPIUsage('"url" является обязательным полем')

    short_id = data.get('custom_id')
    if not short_id:
        short_id = get_unique_short_id()
    if not re.search(SHORT_URL_PATTERN, short_id) or len(short_id) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=short_id).first():
        raise InvalidAPIUsage(f'Имя "{short_id}" уже занято.')

    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(urlmap.to_dict()), HTTPStatus.CREATED
