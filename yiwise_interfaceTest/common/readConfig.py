import os
import configparser
from conf import getPathInfo

path = getPathInfo.get_Path()
config_path = os.path.join(path, 'config.ini')
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')


class ReadConfig():
    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('Email', name)
        return value


if __name__ == '__main__':
    print(config_path)
    r = ReadConfig()
    print(r.get_http('baseurl'))
