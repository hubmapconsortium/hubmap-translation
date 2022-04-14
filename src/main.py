import importlib
import logging
import os
import sys
from pathlib import Path

from flask import Flask
from yaml import safe_load

# Set logging format and level (default is warning)
# All the API logging is forwarded to the uWSGI server and gets written into the log file `uwsgo-entity-api.log`
# Log rotation is handled via logrotate on the host system with a configuration file
# Do NOT handle log file and rotation via the Python logging to avoid issues with multi-worker processes

logging.basicConfig(format='[%(asctime)s] %(levelname)s in %(module)s:%(lineno)d: %(message)s', level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

config = {}
app = Flask(__name__, instance_path=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance'),
            instance_relative_config=True)
app.config.from_pyfile('app.cfg')

# load the index configurations and set the default
config['INDICES'] = safe_load((Path(__file__).absolute().parent / 'instance/search-config.yaml').read_text())
config['DEFAULT_INDEX_WITHOUT_PREFIX'] = config['INDICES']['default_index']

logger.debug("############ INDICES config LOADED")
logger.debug(config['INDICES'])

# Remove trailing slash / from URL base to avoid "//" caused by config with trailing slash
config['DEFAULT_ELASTICSEARCH_URL'] = config['INDICES']['indices'][config['DEFAULT_INDEX_WITHOUT_PREFIX']]['elasticsearch']['url'].strip('/')
config['DEFAULT_ENTITY_API_URL'] = config['INDICES']['indices'][config['DEFAULT_INDEX_WITHOUT_PREFIX']]['document_source_endpoint'].strip('/')

config['SECURE_GROUP'] = app.config['SECURE_GROUP']
config['GROUP_ID'] = 'group_membership_ids'

config['APP_CLIENT_ID'] = app.config['APP_CLIENT_ID']
config['APP_CLIENT_SECRET'] = app.config['APP_CLIENT_SECRET']

sys.path.append("search_api/src")

translator_module = importlib.import_module("hubmap_translator")

from src import app as search_api

# For local development/testing
if __name__ == "__main__":
    try:
        search = search_api.SearchAPI(config, translator_module)
        search.app.run(host='0.0.0.0', port="5005")
    except Exception as e:
        print("Error during starting debug server.")
        print(str(e))
        search_api.logger.error(e, exc_info=True)
        print("Error during startup check the log file for further information")
