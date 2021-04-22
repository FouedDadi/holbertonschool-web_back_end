#!/usr/bin/env python3
"""[summary]"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def acceuil():
    """[summary]
    """
    return render_template('0-index.html')
