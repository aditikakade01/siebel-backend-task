from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class CaseSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    case_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        errors = {}

        if not data.get('name', '').strip():
            errors['name'] = 'Name is required'
        elif len(data.get('name', '')) > 100:
            errors['name'] = 'Name cannot exceed 100 characters'

        if not data.get('caseName', '').strip():
            errors['caseName'] = 'Case Name is required'
        elif len(data.get('caseName', '')) > 100:
            errors['caseName'] = 'Case Name cannot exceed 100 characters'

        if not data.get('description', '').strip():
            errors['description'] = 'Description is required'
        elif len(data.get('description', '')) > 250:
            errors['description'] = 'Description cannot exceed 250 characters'

        if errors:
            return jsonify({'success': False, 'errors': errors}), 400

        new_case = CaseSubmission(
            name=data['name'],
            case_name=data['caseName'],
            description=data['description']
        )
        db.session.add(new_case)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Form submitted and saved to database!',
            'data': data
        })

    except Exception as e:
        return jsonify({'success': False, 'errors': {'general': str(e)}}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
