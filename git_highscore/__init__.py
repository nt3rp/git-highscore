from flask import Flask

app = Flask(__name__)
# Added to enable sessions; keep super secret!
app.secret = "\x021\x138'\xb2\x06\x89\xf0\x10\x07\xe7\x15\xd7\\\xc1N,\xc3\xc4$L\x07\x92"

import api
import views