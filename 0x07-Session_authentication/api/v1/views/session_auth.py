#!/usr/bin/env python3
"""[summary]"""
from flask import request, jsonify
from models.user import User
import os
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def log():
    """[summary]
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        sess_user_id = auth.create_session(user[0].id)
        final = jsonify(user[0].to_json())
        final.set_cookie(os.getenv("SESSION_NAME"), sess_user_id)
        return final
