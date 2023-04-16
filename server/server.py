import json
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


if __name__ == '__main__':
    app.run(port=8000, debug=True)
