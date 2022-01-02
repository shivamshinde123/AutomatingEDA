from flask import Flask, render_template, request
from eda_methods import EDA

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results',methods=['POST'])
def results():
    if request.method == 'POST':
        url = request.form['dataset_url']
        obj = EDA(url)
        obj.report_creation()
        return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)

