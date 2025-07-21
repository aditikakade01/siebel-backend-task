import os
import logging
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .models import db
from .routes.case_routes import case_bp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Starting the Flask application...")


app = Flask(__name__, template_folder='../templates', instance_relative_config=True)   
CORS(app)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    logger.info("Database tables created successfully.")

app.register_blueprint(case_bp)

if __name__ == '__main__':
    logger.info("Flask app running at http://0.0.0.0:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
