#!/usr/bin/env python3
"""[summary]"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:

    def __init__(self):
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """[summary]

        Args:
            email ([type]): [description]
            hashed_password (bool): [description]
        """
        session = self._session
        user = User(email=email, hashed_password=hashed_password)
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """[summary]

        Raises:
            InvalidRequestError: [description]
            NoResultFound: [description]

        Returns:
            User: [description]
        """
        if not kwargs:
            raise InvalidRequestError
        usr = self._session.query(User).filter_by(**kwargs).first()
        if not usr:
            raise NoResultFound
        else:
            return usr

    def update_user(self, user_id: int, **kwargs) -> None:
        """[summary]

        Args:
            user_id (int): [description]
        """
        for k, v in kwargs.items():
            if hasattr(self.find_user_by(id=user_id), k):
                setattr(self.find_user_by(id=user_id), k, v)
            else:
                raise ValueError
        self._session.commit()
