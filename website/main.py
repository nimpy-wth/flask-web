from website import create_app
from flask import Flask

app = Flask(__name__, static_folder='static', template_folder='templates')
app = create_app()

if __name__ == '__main__':
    app.run(debug = True)