import git
from gitdb.exc import BadObject
from flask.ext import restful

# TODO (Resources):
# - Title (held by some for some measurable feat, one user)
# - Rank (similar to title, but for less prestigious things, multiple users)
# - Achievements (not restricted to one user)
# - Users

# For now, just use a really dumb model
# Can obtain active branch via model.active_branch
# getattr(model.heads, 'branch_name') to try to get other branches

model = git.Repo('.')

# TODO: What format do we want results to be?
# TODO: How to do pagination with flask-restful?

class Commit(restful.Resource):
    def get(self, id):
        try:
            commit = model.commit(id)
        except BadObject:
            # TODO: Error
            pass
        else:
            return {
                'commit': {
                    'author': commit.author.email,
                    'message': commit.message
                }
            }


class CommitList(restful.Resource):
    def get(self):
        return {'commits': []}