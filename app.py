

pip install flask

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lihtne andmebaasina kasutatav list küsimuste ja vastuste salvestamiseks
questions_and_answers = []

@app.route('/')
def index():
    return render_template('index.html', questions=questions_and_answers)

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        question = request.form['question']
        # Lisatakse küsimus andmebaasi
        questions_and_answers.append({'question': question, 'answers': []})
        return redirect(url_for('index'))
    return render_template('ask.html')

@app.route('/answer/<int:question_id>', methods=['GET', 'POST'])
def answer(question_id):
    if request.method == 'POST':
        answer = request.form['answer']
        # Lisatakse vastus küsimusele
        questions_and_answers[question_id]['answers'].append(answer)
        return redirect(url_for('index'))
    return render_template('answer.html', question=questions_and_answers[question_id])

if __name__ == '__main__':
    app.run(debug=True)

