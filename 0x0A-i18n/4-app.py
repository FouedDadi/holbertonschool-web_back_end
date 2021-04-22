#!/usr/bin/env python3
"""[flask app to render a template]"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """[summary]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('4-app.Config')


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


@app.route('/')
def acceuil():
    """[summary]
    """
    return render_template('4-index.html')
