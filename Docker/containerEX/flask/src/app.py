from flask import Flask

app = Flask('/')

@app.route('/')
def hello_flask():
    return 'Hello Flask!'