import importlib
import sys

sys.path.append("search_api/src")

translator_module = importlib.import_module("hubmap_translator")

from src import app as search_api

# For local development/testing
if __name__ == "__main__":
    try:
        search_api.translator_module = translator_module
        search_api.app.run(host='0.0.0.0', port="5005")
    except Exception as e:
        print("Error during starting debug server.")
        print(str(e))
        search_api.logger.error(e, exc_info=True)
        print("Error during startup check the log file for further information")
