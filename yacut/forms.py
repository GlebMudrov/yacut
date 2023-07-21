from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .settings import SHORT_URL_PATTERN


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Оригинальная длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256),
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(SHORT_URL_PATTERN, message='Используйте только цифры и латинские буквы'),
        ]
    )
    submit = SubmitField('Создать')
