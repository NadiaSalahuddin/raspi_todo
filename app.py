from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def todo():
    return render_template('index.html')

@app.route('/submit')
def submitted():
    return render_template('submitted.html')


if __name__ == "__main__":
    app.debug = True
    app.run()