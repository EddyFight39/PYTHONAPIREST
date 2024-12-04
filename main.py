from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello, welcome to the REST API!"})

@app.route('/api/greet', methods=['POST'])
def personalized_greet():
    data = request.get_json()
    name = data.get("name", "Guest")
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
