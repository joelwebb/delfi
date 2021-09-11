class Development(object):
    """ development config object - can be used to specify prod/non-prod/sint/testing"""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    #changeme

app_config = {
    'development': Development,
}
