""" the settings module
"""
import os
from jinja2 import Environment, FileSystemLoader
import yaml

#pylint: disable=C0103


class SettingsObject(): # pylint: disable=R0903
    """ Generic object for storing a setting
    """

    def __init__(self, d):
        for a, b in d.items():  # pylint: disable=C0103
            if isinstance(b, (list, tuple)):
                setattr(self, a, [SettingsObject(x)
                                  if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, SettingsObject(b)
                        if isinstance(b, dict) else b)


class Settings:  # pylint: disable=R0903
    """ The settings class
    """

    def __init__(self, fname):
        template_loader = FileSystemLoader(searchpath="./")
        j2_env = Environment(loader=template_loader,
                             trim_blocks=True)
        j2_env.filters['env_override'] = self.env_override
        d = yaml.full_load(j2_env.get_template(fname).render())
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [SettingsObject(x)
                                  if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, SettingsObject(b)
                        if isinstance(b, dict) else b)

    @staticmethod
    def env_override(value, key):
        """ A simple jinja filter to get a val from env
        """
        return os.getenv(key, value)