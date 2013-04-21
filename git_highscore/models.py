"""
It appears that there is nothing special about a resource: it is merely an
intermediary layer between the client and that database. Therefore,
it is necessary to implement a data model separately. Hence `models.py`
"""

# TODO:
# - Git repo wrapper, to handle either github or ordinary git repo
#     - Unless there is a library to do it already...

class Repo(object):
    def __init__(self, *args, **kwargs):
        # Set path to repo
        pass

    def log(self, branch=None):
        pass

    def show(self, commit):
        pass