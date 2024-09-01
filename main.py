from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

key = Fernet.generate_key()


def encryp(message):
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    return encMessage


def decryp(encMessage):
    fernet = Fernet(key)
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        message = request.form.get('pass', '')  # Get the 'pass' value from the form or set an empty string if not provided
        encMessage = encryp(message)
        decMessage = decryp(encMessage)
    else:
        message = ""
        encMessage = ""
        decMessage = ""
    return render_template('index.html', message=message, encMessage=encMessage, decMessage=decMessage)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encMessage = request.form.get('encPass', '')
    decMessage = decryp(encMessage)
    return render_template('index.html', message="", encMessage="", decMessage=decMessage)



if __name__ == "__main__":
    app.run(debug=True)
