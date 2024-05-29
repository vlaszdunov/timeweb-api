import os
import dotenv


def config():
    dotenv.load_dotenv('.env')
    TIMEWEB_API_TOKEN = os.getenv('TIMEWEB_API_TOKEN')
    del os.environ['TIMEWEB_API_TOKEN']
    return TIMEWEB_API_TOKEN
