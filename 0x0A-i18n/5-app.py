#!/usr/bin/env python3
"""[flask app to render a template]"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """[summary]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('5-app.Config')


@babel.localeselector
def get_locale():
    """[summary]

    Returns:
        [type]: [description]
    """
    local = request.args.get('locale')
    if local is None:
        return request.accept_languages.best_match(Config.LANGUAGES)
    else:
        if local in Config.LANGUAGES:
            return local


def get_user():
    """[summary]

    Returns:
        [type]: [description]
    """
    Id = request.args.get('login_as')
    if int(Id) in users:
        return users[int(Id)]
    return None


@app.before_request
def before_request():
    """[summary]
    """
    try:
        g.user = get_user()
    except Exception:
        return None


@app.route('/')
def acceuil():
    """[summary]
    """
    return render_template('5-index.html')
