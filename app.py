from flask import Flask
from user_input.views import user_input_bp

app = Flask(__name__)
app.register_blueprint(user_input_bp, url_prefix='/user_input')

if __name__ == '__main__':
    app.run(debug=True)
