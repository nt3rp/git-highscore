from flask.ext import restful

# TODO (Resources):
# - Title (held by some for some measurable feat, one user)
# - Rank (similar to title, but for less prestigious things, multiple users)
# - Achievements (not restricted to one user)
# - Users

class Commit(restful.Resource):
    def get(self, id):
        return {'commit': 'blah'}


class CommitList(restful.Resource):
    def get(self):
        return {'commits': []}