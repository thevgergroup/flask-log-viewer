
from flask import Flask, render_template
from flask_log_viewer.viewer import log_viewer_blueprint
import os

app = Flask(__name__)
cwd = os.getcwd()
logs_path = os.path.join(cwd, 'tmp')



log_viewer = log_viewer_blueprint(base_path=logs_path, allowed_directories=[logs_path])

app.register_blueprint(log_viewer, url_prefix='/logs')

@app.route('/')
def hello():
    return "<html><body><a href='/logs/view/foo.log'>View Logs</a></body></html>"


if __name__ == '__main__':
    app.run( port=3001) #debug=True,