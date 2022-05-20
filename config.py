from distutils.log import DEBUG


class Config:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///base.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
