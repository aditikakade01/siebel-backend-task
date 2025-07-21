from flask import Blueprint, render_template, request, jsonify
from ..models import db, CaseSubmission

case_bp = Blueprint('case_bp', __name__)

@case_bp.route('/')
def index():
    return render_template('index.html')   

@case_bp.route('/submit', methods=['POST'])
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

