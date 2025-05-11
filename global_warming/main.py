from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GW.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(30), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        login = request.form['email']
        password = request.form['password']
        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/quiz')
    else:
        return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']

        users_db = User.query.all()
        for user in users_db:
            if form_login == user.login and form_password == user.password:
                return redirect('/quiz')
        else:
            error = 'Неправильно указан пользователь или пароль'
            return render_template('login.html', error=error)

    else:
        return render_template('login.html')

@app.route('/' or '/info')
def info():
    return render_template('info.html')

@app.route('/quiz', methods =["GET"])
def quiz():
  return render_template('quiz.html', result = None)

@app.route('/quiz_result', methods=['POST'])
def quiz_result():
    answers = {
        'q1': request.form.get('q1'),
        'q2': request.form.get('q2'),
        'q3': request.form.get('q3'),
        'q4': request.form.get('q4'),
        'q5': request.form.get('q5'),
        'q6': request.form.get('q6'),
        'q7': request.form.get('q7'),
        'q8': request.form.get('q8'),
        'q9': request.form.get('q9'),
        'q10': request.form.get('q10'),
        'q11': request.form.get('q11'),
        'q12': request.form.get('q12')
    }

    correct_answers = 0
    if answers['q1'] == 'C':
        correct_answers += 1
    if answers['q2'] == 'C':
        correct_answers += 1
    if answers['q3'] == 'C':
        correct_answers += 1
    if answers['q4'] == 'C':
        correct_answers += 1
    if answers['q5'] == 'C':
        correct_answers += 1
    if answers['q6'] == 'C':
        correct_answers += 1
    if answers['q7'] == 'B':
        correct_answers += 1
    if answers['q8'] == 'D':
        correct_answers += 1
    if answers['q9'] == 'B':
        correct_answers += 1
    if answers['q10'] == 'B':
        correct_answers += 1
    if answers['q11'] == 'C':
        correct_answers += 1
    if answers['q12'] == 'C':
        correct_answers += 1

    return render_template('quiz_result.html', result=correct_answers)


if __name__ == '__main__':
    app.run(debug=True)
