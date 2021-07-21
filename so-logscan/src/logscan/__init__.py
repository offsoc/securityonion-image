import logging
import src.logscan as logscan
import configparser
from configparser import ConfigParser
from pytimeparse.timeparse import timeparse
import pathlib, os

def __read_config(file) -> ConfigParser:
    config = configparser.ConfigParser()
    config.read(file)
    return config


def __is_docker():
    path = '/proc/self/cgroup'
    return (
        os.path.exists('/.dockerenv') or
        os.path.isfile(path) and any('docker' in line for line in open(path))
    )


if __is_docker():
    BASE_DIR = '/logscan'
elif os.getenv('ENV') == 'testing':
    BASE_DIR = (pathlib.Path(logscan.__file__).parent.parent.parent).joinpath('tests')
else:
    BASE_DIR = pathlib.Path(logscan.__file__).parent.parent.parent


OUTPUT_DIR = f'{BASE_DIR}/output'
DATA_DIR = f'{BASE_DIR}/data'

if not pathlib.Path(OUTPUT_DIR).is_dir():
    os.mkdir(OUTPUT_DIR)

if not pathlib.Path(DATA_DIR).is_dir():
    os.mkdir(DATA_DIR)

ALERT_LOG = f'{OUTPUT_DIR}/alerts.log'
APP_LOG = f'{OUTPUT_DIR}/app.log'
HISTORY_LOG = f'{DATA_DIR}/history.log'

LOG_BASE_DIR = f'{BASE_DIR}/logs'

KRATOS_SUCCESS_STR = 'Identity authenticated successfully'

__CONFIG_FILE = f'{ "/logscan" if __is_docker() else pathlib.Path(logscan.__file__).parent.parent.parent }/logscan.conf'
CONFIG = __read_config(__CONFIG_FILE)

LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timeparse(CONFIG.get('global', 'scan_interval'))

KRATOS_LOG = f'{LOG_BASE_DIR}/{CONFIG.get("kratos", "log_path")}'

THREAD_EXPIRE_TIME = 1
    