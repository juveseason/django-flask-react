import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AMQP_URI = os.getenv('AMQP_URI')

    # https://stackoverflow.com/questions/62002249/docker-container-sending-request-to-http
    # M1 Mac use linux answer
    DOCKER_LOCALHOST = os.getenv('DOCKER_LOCALHOST')
