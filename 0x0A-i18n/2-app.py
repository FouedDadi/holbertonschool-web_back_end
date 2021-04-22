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


app.config.from_object('2-app.Config')


@babel.localeselector
def get_locale():
    """[summary]

    Returns:
        [type]: [description]
    """
    return request.accept_languages.best_match(app.config.LANGUAGES)


@app.route('/')
def acceuil():
    """[summary]
    """
    return render_template('2-index.html')
