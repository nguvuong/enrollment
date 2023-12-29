import os 

class Config(object):
    # SPECIAL KEY USED AS SIGNATURE TO MAKE SURE THAT EVERYTHING U SEND 
    # ACROSS THE SERVER IS NOT BEEN ALTERED, HACKED
    SECRET_KY = os.environ.get('SECRET_KEY') or "secret_string"
    