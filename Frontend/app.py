from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def load_page():
    return render_template('index.html')


@app.route('/processdata', methods=["POST"])
def processData():
    data = request.form.get('getText')
    # function that takes in data and returns suggestions
    return data

@app.route('/suggestionsdata', methods=["POST"])
def suggestionsData():
    return "hello world testing 123" #function that returns suggestions

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)