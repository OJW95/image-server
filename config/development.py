from config.default import *

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'\
    .format(user='',
            pw='',
            url='',
            db='')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = ""
