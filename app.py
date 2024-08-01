from flask import Flask, render_template
from models import db, Employee

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hrm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# @app.before_first_request
def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employees')
def employee_list():
    employees = Employee.query.all()
    return render_template('employee_list.html', employees=employees)

@app.route('/employee/<int:id>')
def employee_detail(id):
    employee = Employee.query.get_or_404(id)
    return render_template('employee_detail.html', employee=employee)

@app.route('/salary')
def salary():
    return render_template('salary.html')

@app.route('/holidays')
def holidays():
    return render_template('holidays.html')

if __name__ == '__main__':
    app.run(debug=True)
