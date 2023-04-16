import json
import csv
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/login/<string:userType>', methods=['POST'])
def login(userType):
    data = json.loads(request.data)
    email = data['email']
    password = data['password']

    if userType == 'student':

        if email == 'student' and password == '123456':
            return jsonify({'status': 'true', 'message': "Login Successful"})

        else:
            return jsonify({'status': 'false', 'error': "Invalid Credentials"})

    if userType == 'lecturer':

        if email == 'lecturer' and password == '123456':
            return jsonify({'status': 'true', 'message': "Login Successful"})

        else:
            return jsonify({'status': 'false', 'error': "Invalid Credentials"})


@app.route('/enrollCourse/<string:courseName>', methods=['POST'])
def enrollCourse(courseName):
    print("courseName", courseName)
    with open('files/courses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([courseName])

    return jsonify({'status': 'true', 'message': "Enroll Successful"})


@app.route('/submit/<string:quiz>', methods=['POST'])
def submit(quiz):
    data = json.loads(request.data)
    print("courseName", data)
    for i in data:
        question = i['question']
        answer = i['answer']
        with open('files/quiz.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([question, answer])

    return jsonify({'status': 'true', 'message': "Submission Successful"})


if __name__ == '__main__':
    app.run(port=8000, debug=True)
