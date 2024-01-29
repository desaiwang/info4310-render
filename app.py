# controls flask server, listens to people's responses and sends back info
from flask import *
from whitenoise import WhiteNoise  # handles static files

# app object is the web server, it's implicitly running without doing anything
app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/",
                          prefix="static/", index_file="index.htm", autorefresh=True)


# string indicates routes that need to be handled, here we just do root dir
@app.route('/', methods=['GET'])
def hello():
    return make_response("Hello, world!!!!")


# have flask start server if calling from terminal
if __name__ == "__main__":
    app.run(threaded=True, port=5000)
