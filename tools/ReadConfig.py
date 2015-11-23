import configparser

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    return config