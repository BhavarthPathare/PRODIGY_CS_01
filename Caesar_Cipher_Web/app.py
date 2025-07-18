from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        message = request.form['message']
        shift = int(request.form['shift'])
        mode = request.form['mode']
        result = caesar_cipher(message, shift, mode)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
