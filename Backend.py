from flask import Flask
from flask import request

app = Flask(__name__)

board = '''
<html>
<head>
    <title>message board</title>
</head>
<body>
    <form action="/" method="post">
        Message: <input type="text" name="message"> <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        message = request.form['message']
        with open('message.txt', 'a') as f:
            f.write(message + '\n')
            print(message)
    return board


if __name__ == '__main__':
    app.run(debug=True)