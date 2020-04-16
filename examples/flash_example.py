from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    if(request.method == 'GET'):
        json_string = request.get_json()
        return jsonify({'request': json_string}), 201
    else:
        return jsonify({'request': "none"}), 201

if __name__ == '__main__':
    app.run(debug=True)