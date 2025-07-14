from flask import Flask
from flask_cors import CORS
from .models import db
from .routes.case_routes import case_bp

app = Flask(__name__, template_folder='../templates', instance_relative_config=True)   
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(case_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
