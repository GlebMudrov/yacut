from flask import flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data

        if URLMap.query.filter_by(short=custom_id).first():
            flash(f'Имя {custom_id} уже занято!')
            return render_template('index.html', form=form)

        if not custom_id:
            custom_id = get_unique_short_id()

        url = URLMap(
            original=form.original_link.data,
            short=custom_id
        )

        db.session.add(url)
        db.session.commit()
        return render_template('index.html', form=form, url=url)

    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirect_view(short):
    original_url = URLMap.query.filter_by(short=short).first_or_404().original
    return redirect(original_url)
