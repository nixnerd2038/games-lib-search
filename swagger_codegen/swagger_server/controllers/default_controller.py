import connexion
import six

from swagger_server import util


def get_hello_world(param1=None):  # noqa: E501
    """Hello world operation

    A demonstration of a GET call on a sample resource. # noqa: E501

    :param param1: A sample parameter that is optional and has a default value of \&quot;sample\&quot;.
    :type param1: str

    :rtype: None
    """
    return 'do some magic!'
