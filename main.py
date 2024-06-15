from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/item/<string:item>', methods=['GET'])
def get_item(item):
    html_template = """
    <h1>You searched for: "{}"</h1>
    """
    return render_template_string(html_template.format(item))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)