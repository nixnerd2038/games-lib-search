# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Error(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, detail: str=None, status: int=None, title: str=None, type: str=None):  # noqa: E501
        """Error - a model defined in Swagger

        :param detail: The detail of this Error.  # noqa: E501
        :type detail: str
        :param status: The status of this Error.  # noqa: E501
        :type status: int
        :param title: The title of this Error.  # noqa: E501
        :type title: str
        :param type: The type of this Error.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'detail': str,
            'status': int,
            'title': str,
            'type': str
        }

        self.attribute_map = {
            'detail': 'detail',
            'status': 'status',
            'title': 'title',
            'type': 'type'
        }
        self._detail = detail
        self._status = status
        self._title = title
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Error':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Error of this Error.  # noqa: E501
        :rtype: Error
        """
        return util.deserialize_model(dikt, cls)

    @property
    def detail(self) -> str:
        """Gets the detail of this Error.


        :return: The detail of this Error.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail: str):
        """Sets the detail of this Error.


        :param detail: The detail of this Error.
        :type detail: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

    @property
    def status(self) -> int:
        """Gets the status of this Error.


        :return: The status of this Error.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this Error.


        :param status: The status of this Error.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def title(self) -> str:
        """Gets the title of this Error.


        :return: The title of this Error.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Error.


        :param title: The title of this Error.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def type(self) -> str:
        """Gets the type of this Error.


        :return: The type of this Error.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Error.


        :param type: The type of this Error.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type
