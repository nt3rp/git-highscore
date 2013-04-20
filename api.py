from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

# TODO (Resources):
# - Title (held by some for some measurable feat, one user)
# - Rank (similar to title, but for less prestigious things, multiple users)
# - Achievements (not restricted to one user)
# - Users

class Commit(restful.Resource):
    def get(self, id):

        return {'hello': 'world'}


class CommitList(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(CommitList, '/commits')
api.add_resource(Commit, '/commits/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)