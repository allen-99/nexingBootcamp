from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/healthcheck")
def api():
    json_out = [{'status': 'started'}]
    return jsonify(json_out), 200


@app.route("/")
def index():
    text = 'Привет мир!!!!!!!!'
    return render_template('index.html', txt=text)


@app.route('/users/<page>', methods=['GET'])
def get_run_requests_page(page):
    response = requests.get('https://reqres.in/api/users?page=' + page)
    txt = response.json()
    pages = int(txt['total_pages'])
    txt = txt['data']
    return render_template('get.html', out_json=txt, pages=pages)


@app.route('/form', methods=['GET', 'POST'])
def form():
    text = ''
    if request.method == 'POST':
        text = request.form.get('input_text')
    return render_template('form.html', text=text)


if __name__ == "__main__":
    app.run(debug=True)