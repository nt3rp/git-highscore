from flask.ext import restful
from git_highscore import app
from resources import *

api = restful.Api(app)

api.add_resource(CommitList, '/commits')
api.add_resource(Commit, '/commits/<string:id>')