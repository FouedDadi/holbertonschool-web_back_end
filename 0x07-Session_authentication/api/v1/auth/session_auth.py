#!/usr/bin/env python3
"""[summary]"""

from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """[summary]

    Args:
        Auth ([type]): [description]
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """[summary]

        Args:
            user_id (str, optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        if user_id is None or type(user_id) is not str:
            return None
        else:
            sess_id = str(uuid.uuid4())
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """[summary]

        Args:
            session_id (str, optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.
        """
        id = self.user_id_for_session_id(self.session_cookie(request))
        user = User.get(id)
        return user

    def destroy_session(self, request=None):
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.
        """
        if request is None:
            return False
        cook = self.session_cookie(request)
        if not cook:
            return False
        usr_id = self.user_id_by_session_id(cook)
        if not usr_id:
            return False
        del self.user_id_by_session_id[cook]
        return True
