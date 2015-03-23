__author__ = 'Pedro Sernadela sernadela@ua.pt'

from file_utils import *


class Boot:
    def __init__(self, config_location):
        self.config_file = get_config_file(config_location)
        self.namespace = self.config_file['namespace']
        self.prefix = self.config_file['prefix']
        self.service = self.config_file['normalization']['service']
        self.query = self.config_file['normalization']['query']




