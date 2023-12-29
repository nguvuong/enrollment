# look for any initialization of the file 
from flask import Flask

# __name__ is a special variable name to identify the current module that is being rendered
app = Flask(__name__)

from application import routes