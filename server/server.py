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


@app.route('/submit/<string:pageName>', methods=['POST'])
def submit(pageName):
    data = json.loads(request.data)
    print("courseName", data)
    if pageName == 'quiz':
        for i in data:
            question = i['question']
            answer = i['answer']
            with open('files/quiz.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([question, answer])

    if pageName == 'feedback':
        question = data['email']
        answer = data['feedback']
        with open('files/feedback.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([question, answer])

    return jsonify({'status': 'true', 'message': "Submission Successful"})


@app.route('/getData/<string:pageName>')
def get(pageName):
    data = []
    if pageName == 'students':
        with open('files/students.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append({'name': row[0]})

    if pageName == 'assignment':
        with open('files/assignment.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(row)
                data.append({'question': row[0], 'data': row[1]})

    if pageName == 'feedback':
        with open('files/feedback.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                data.append({'email': row[0], 'feedback': row[1]})
    return jsonify({'message': data})


if __name__ == '__main__':
    app.run(port=8000, debug=True)
