from flask import Flask, render_template

app = Flask(__name__)


@app.route('/nucarnival/calculator')
def index():
    return render_template('calculatorIndex.html')


if __name__ == '__main__':
    app.run(port=8090)
