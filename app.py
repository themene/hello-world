from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/post', methods=['POST'])
def post_message():
    username = request.form.get('username', 'Anonymous')
    text = request.form.get('message', '')
    if text:
        messages.append({'user': username, 'text': text})
    return redirect('/')

@app.route('/messages')
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)
