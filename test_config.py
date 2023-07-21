import os
import pytest
from config_reader import read_config, write_config

def test_read_config():
    config = read_config('test_config.yml')
    assert config == {'DATABASE_HOST': 'localhost', 'DATABASE_PORT': '3306', 'DATABASE_USER': 'root', 'DATABASE_PASSWORD': 'Pooja@1992'}

def test_write_config():
    config = {'DATABASE_HOST': 'localhost', 'DATABASE_PORT': '3306', 'DATABASE_USER': 'root', 'DATABASE_PASSWORD': 'Pooja@1992'}
    write_config('test_config.json', config, 'json')
    assert os.path.exists('test_config.json')

def test_set_config_env():
    config = {'DATABASE_HOST': 'localhost', 'DATABASE_PORT': '3306', 'DATABASE_USER': 'root', 'DATABASE_PASSWORD': 'Pooja@1992'}
    set_config_env(config)
    assert os.environ.get('DATABASE_HOST') == 'localhost'
    assert os.environ.get('DATABASE_PORT') == '3306'
    assert os.environ.get('DATABASE_USER') == 'root'
    assert os.environ.get('DATABASE_PASSWORD') == 'Pooja@1992'
