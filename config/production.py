from config.default import *

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'\
    .format(user='jw',
            pw='1234',
            url='54.157.12.31',
            db='postgres')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'ctm \xd7h\xb0\xc4\x06C\xb4\\\x82]\x14)'