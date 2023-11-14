# pages/employee.py

from flask import render_template, Blueprint

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employee')
def employee():
    return render_template('employee.html')

