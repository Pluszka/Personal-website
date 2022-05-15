from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    if request.args.get('language') == 'pl':
        return render_template('PLindex.html', lanuage='pl')
    return render_template('index.html', lanuage='ang')

if __name__ == "__main__":
    app.run(debug=True)
