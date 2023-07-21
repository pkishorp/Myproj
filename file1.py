import os
import json
import yaml
from configparser import ConfigParser

# config = {}
def read_config(file_path):

    _, file_extension = os.path.splitext(file_path)
    if file_extension == '.yml':
        with open(file_path, 'r') as yaml_file:
            config_data = yaml.load(yaml_file, Loader=yaml.SafeLoader)
    elif file_extension == '.cfg' or file_extension == '.conf':
            global config
            config = ConfigParser()
            config.read(file_path)
            config_data = {}
            for section in config.sections():
                 config_data[section] = {key: config.get(section, key) for key in config.options(section)}
    else:
        raise ValueError("Unsupported file format")

    flat_config = {}

    for section, options in config_data.items():
        for key, value in options.items():
         flat_config[section.upper() + '_' + key.upper()] = value
    return flat_config


def write_config(file_path, config, format, ext):

    if format == 'json':
        with open(file_path, 'w') as json_file:
             json.dump(config, json_file, indent=4)
    elif format == 'env':
        with open(file_path, 'w') as env_file:
            for key, value in config.items():
                env_file.write(f"{key}={value}\n")
    else:
        raise ValueError("Unsupported file format")


def set_config_env(config):

    for key, value in config.items():
        os.environ[key] = value

if __name__ == "__main__":
    a = read_config("checks.cfg")
    print(a)
    b = write_config("checks.cfg", a, "env",".env")
    print(b)
    c = set_config_env(a)
    print(c)

