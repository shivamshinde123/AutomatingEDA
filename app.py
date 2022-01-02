from flask import Flask, render_template, request
from eda_methods import EDA

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results',methods=['POST'])
def results():
    data = request.form['dataset']
    obj = EDA(data)
    return render_template('results.html',obj=obj)


if __name__ == '__main__':
    app.run(debug=True)

